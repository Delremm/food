from fabric.api import run, local, prefix, shell_env
from fabric.api import env, cd
from fabric.contrib.files import upload_template, exists, append
import xmlrpclib
import sys

import string
import random

try:
    from fabsettings.fabsettings import WF_HOST, PROJECT_NAME, REPOSITORY, USER, PASSWORD, VIRTUALENVS, SETTINGS_SUBDIR, APP_PORT
except ImportError:
    print "ImportError: Couldn't find fabsettings.py, it either does not exist or giving import problems (missing settings)"
    sys.exit(1)

env.hosts          = [WF_HOST]
env.user = USER
#env.password = PASSWORD
env.use_ssh_config = True
env.home = "/home/%s" % USER
env.project = PROJECT_NAME
env.app_port = APP_PORT
env.repo = REPOSITORY
env.project_dir = env.home + '/webapps/' + PROJECT_NAME
#env.settings_dir = env.project_dir + '/' + SETTINGS_SUBDIR
env.supervisor_dir = env.home + '/webapps/supervisor'
env.virtualenv_dir = VIRTUALENVS
env.supervisor_ve_dir = env.virtualenv_dir + '/supervisor'
DJANGO_SETTINGS_MODULE = 'food.settings.production'
env.settings_mode = 'production'


def upload_gunicorn(settings_mode=env.settings_mode):
    # upload template to supervisor conf
    upload_template(
        'fabsettings/templates/gunicorn.conf',
        '%s/conf.d/%s.conf' % (env.supervisor_dir, env.project),
        {
            'project': env.project,
            'project_dir': env.project_dir,
            'virtualenv': '%s/%s' % (env.virtualenv_dir, env.project),
            'port': env.app_port,
            'user': env.user,
            'supervisor_dir': env.supervisor_dir,
        }
    )
    upload_template(
        'fabsettings/templates/gunicorn_start.bash',
        '%s/gunicorn_start_%s.bash' % (env.supervisor_dir, env.project),
        {
            'project': env.project,
            'project_dir': env.project_dir,
            'virtualenv': '%s/%s' % (env.virtualenv_dir, env.project),
            'port': env.app_port,
            'settings_mode': settings_mode,
        }
    )
    run("chmod u+x %s/gunicorn_start_%s.bash" %
        (env.supervisor_dir, env.project))


def install_app():
    """Installs the django project in its own wf app and virtualenv
    """
    if not exists(env.project_dir):
        response = _webfaction_create_app(env.project)
        env.app_port = response['port']

    clone_project()
    create_ve(env.project)
    reload_app()


def check():
    print(exists(env.project_dir))


def host_type():
    run('uname -s')


def clone_project():
    with cd(env.home + '/webapps'):
        if not exists(env.project_dir):
            run('git clone %s %s' % (env.repo, env.project_dir))
    create_ve(env.project)


def install_supervisor():
    """Installs supervisor in its wf app and own virtualenv
    """
    response = _webfaction_create_app("supervisor")
    env.supervisor_port = response['port']
    create_ve('supervisor')
    if not exists(env.supervisor_ve_dir + 'bin/supervisord'):
        _ve_run('supervisor','pip install supervisor')
    # uplaod supervisor.conf template
    upload_template('templates/supervisord.conf',
                     '%s/supervisord.conf' % env.supervisor_dir,
                    {
                        'user':     env.user,
                        'password': env.password,
                        'port': env.supervisor_port,
                        'dir':  env.supervisor_dir,
                    },
                    )

    # upload and install crontab
    upload_template('templates/start_supervisor.sh',
                    '%s/start_supervisor.sh' % env.supervisor_dir,
                     {
                        'user':     env.user,
                        'virtualenv': env.supervisor_ve_dir,
                    },
                    mode=0750,
                    )



    # add to crontab

    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(7))
    run('crontab -l > /tmp/%s' % filename)
    append('/tmp/%s' % filename, '*/10 * * * * %s/start_supervisor.sh start' % env.supervisor_dir)
    run('crontab /tmp/%s' % filename)


    # create supervisor/conf.d
    with cd(env.supervisor_dir):
        run('mkdir conf.d')

    with cd(env.supervisor_dir):
        with settings(warn_only=True):
            run('./start_supervisor.sh stop && ./start_supervisor.sh start')


def sync_app(settings_mode=env.settings_mode):
    with cd(env.project_dir), shell_env(DJANGO_SETTINGS_MODULE='food.settings.%s' % settings_mode):
        #_ve_run(env.project, "easy_install -i http://downloads.egenix.com/python/index/ucs4/ egenix-mx-base")
        _ve_run(env.project, "python3 manage.py syncdb")
        _ve_run(env.project, "python3 manage.py migrate")
        _ve_run(env.project, "python3 manage.py collectstatic")


def reload_app(arg=None):
    """Pulls app and refreshes requirements"""

    with cd(env.project_dir):
        #run('git stash')
        run('git pull origin master')

    if arg == "full":
        with cd(env.project_dir):
            _ve_run(env.project, "pip3 install -r requirements.txt")
            #_ve_run(env.project, "python manage.py createcachetable tecon_cache_table")
        sync_app()

    restart_app()


def restart_app():
    """Restarts the app using supervisorctl"""

    with cd(env.supervisor_dir):
        #_ve_run('supervisor','supervisorctl -c supervisord.conf')
        _ve_run('supervisor','supervisorctl reread && supervisorctl reload')
        _ve_run('supervisor','supervisorctl restart %s' % env.project)

def stop_app():
    with cd(env.supervisor_dir):
        #_ve_run('supervisor','supervisorctl -c supervisord.conf')
        _ve_run('supervisor','supervisorctl reread && supervisorctl reload')
        _ve_run('supervisor','supervisorctl stop %s' % env.project)

def start_app():
    with cd(env.supervisor_dir):
        #_ve_run('supervisor','supervisorctl -c supervisord.conf')
        _ve_run('supervisor','supervisorctl reread && supervisorctl reload')
        _ve_run('supervisor','supervisorctl start %s' % env.project)


### Helper functions

def create_ve(name):
    """creates virtualenv using virtualenvwrapper
    """
    if not exists('%s/%s' % (env.virtualenv_dir, name)):
        with cd(env.virtualenv_dir):
            run('mkdir %s' % name)
            run('pyvenv-3.4 %s' % name)
    else:
        print("Virtualenv with name %s already exists. Skipping." % name)


def _ve_run(ve, cmd):
    """virtualenv wrapper for fabric commands
    """
    run("""source %s/%s/bin/activate && %s""" % (env.virtualenv_dir, ve, cmd))


def _webfaction_create_app(app):
    """creates a "custom app with port" app on webfaction using the webfaction public API.
    """
    server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
    session_id, account = server.login(USER, PASSWORD)
    try:
        response = server.create_app(session_id, app, 'custom_app_with_port', False, '')
        print("App on webfaction created: %s" % response)
        return response

    except xmlrpclib.Fault:
        print("Could not create app on webfaction %s, app name maybe already in use" % app)
        sys.exit(1)
