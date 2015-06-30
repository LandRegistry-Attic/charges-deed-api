#################################################################################################
### This script is used to run any acceptance tests in the repository. It saves time and      ###
### confusion of executing any setup before the tests are run by including it all in one      ###
### handy script.                                                                             ###
#################################################################################################

#!/bin/bash

### Retrieve the current location the script is running
currentLocation="$(cd "$(dirname "$0")"; pwd)"

### Set the location of the Gemfile based on the scripts current running location
gemfile=$currentLocation/Gemfile

set -e

### Remove any test failure screenshots from previous runs.
rm -f sshot*

### Installs any gems specified in the gemfile.
BUNDLE_GEMFILE=$gemfile bundle install

if [ -z "$1"]
  then
  ### If no arguments supplied when running this script then execute all tests other than those tagged as wip
  BUNDLE_GEMFILE=$gemfile bundle exec cucumber $currentLocation --tags ~@wip
else
  ### If arguments are supplied when running this script then execute th tests tagged with argument specified
  BUNDLE_GEMFILE=$gemfile bundle exec cucumber $currentLocation $1
fi
