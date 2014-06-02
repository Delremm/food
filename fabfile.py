from fabric.api import run, local, prefix

VIRTUALENV_NAME='food'

def host_type():
    run('uname -s')

def prepare_deploy(test=False):
    if test:
        with prefix('workon %s' % VIRTUALENV_NAME):
            local("./manage.py test")
    local("git add -u . && git commit")
    local("git push origin master")

def env_dev():
    local('export DJANGO_SETTINGS_MODULE=food.settings.dev')

def env_production():
    local('export DJANGO_SETTINGS_MODULE=food.settings.production')
