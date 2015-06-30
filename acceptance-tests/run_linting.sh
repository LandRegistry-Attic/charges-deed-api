#################################################################################################
### This shell script is used to run style guide checkers on code in the acceptance-tests     ###
### folder such as Rubocop.                                                                   ###
#################################################################################################

### Retrieve the current location the script is running
currentLocation="$(cd "$(dirname "$0")"; pwd)"

### Set the location of the Gemfile based on the scripts current running location
gemfile=$currentLocation/Gemfile

### Installs any gems specified in the gemfile.
BUNDLE_GEMFILE=$gemfile bundle install

### Run rubocop gem to check acceptance tests against the Ruby style guide.
BUNDLE_GEMFILE=$gemfile bundle exec rubocop -c $currentLocation/rubocop.yml

### Return from script with exit code
exit $?
