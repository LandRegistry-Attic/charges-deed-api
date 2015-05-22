#! /usr/bin/bash

virtualenv ./.service_env

source ./.service_env/bin/activate

pip3 install -r requirements.txt

port="${API_SKELETON_GUNICORN_PORT:-8000}"
host="${API_SKELETON_GUNICORN_HOST:-0.0.0.0}"


gunicorn -b $host:$port --pid /var/run/api_skeleton.pid "app:create_manager().app"
