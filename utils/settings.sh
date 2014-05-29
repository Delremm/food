#! /bin/bash

production () {
    echo "Setting production DJANGO_SETTINGS_MODULE"
    export DJANGO_SETTINGS_MODULE=food.settings.production
}

dev () {
    echo "Setting dev DJANGO_SETTINGS_MODULE"
    export DJANGO_SETTINGS_MODULE=food.settings.dev
}

