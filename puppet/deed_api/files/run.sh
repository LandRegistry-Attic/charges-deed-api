#! /usr/bin/bash

virtualenv ./.service_env

source ./.service_env/bin/activate

pip3 install -r requirements.txt

port="${DEED_API_GUNICORN_PORT:-8000}"
host="${DEED_API_GUNICORN_HOST:-0.0.0.0}"


gunicorn -b $host:$port --pid /var/run/deed_api/deed_api.pid "app:create_manager().app"
