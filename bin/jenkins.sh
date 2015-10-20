#! /usr/bin/env bash

env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"

#create and activate a virtualenv
virtualenv $env_dir
. $env_dir/bin/activate

#install requirements
pip install -r requirements.txt

#install test only requirements
pip install -r requirements_test.txt

#ensure submodules are cloned
git submodule update --init

./acceptance-tests/run_linting.sh

rubocop=$?

createdb $JOB_NAME -h $ADDRESS -U $USERNAME

DATABASE_URI=postgres://$USERNAME:$PGPASSWORD@$ADDRESS/$JOB_NAME coverage run --source=app --omit=../*migrations* tests.py --xml

dropdb $JOB_NAME -h $ADDRESS -U $USERNAME

test_pass=$?

./run_linting.sh

python_linting=$?

coverage xml
coverage -rm

e_code=$((test_pass + rubocop + python_linting))

exit $e_code
