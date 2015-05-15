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

coverage run --source=app tests.py --xml

test_pass=$?

coverage xml
coverage -rm

exit $test_pass
