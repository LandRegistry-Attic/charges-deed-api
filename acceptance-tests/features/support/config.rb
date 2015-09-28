################################################################################
### This file contains details of any setup of libraries/gems and such that  ###
### will be needed for creating and running the acceptance tests.            ###
################################################################################

### Configure Capybara and Poltergeist for running tests against web apps
require 'capybara/cucumber'
require 'capybara/poltergeist'

include Capybara::DSL
Capybara.default_selector = :xpath
Capybara.default_wait_time = 10
Capybara.app_host = 'http://localhost:4567'

Capybara.default_driver = :poltergeist
Capybara.javascript_driver = :poltergeist

Capybara.register_driver :poltergeist do |app|
  Capybara::Poltergeist::Driver.new(app, inspector: true, js_errors: true)
end

### Configure Assertions so we can add assertions like assert_match() in tests
require 'test/unit'
include Test::Unit::Assertions

### Require gems such as httprb for interacting with the APIs
require 'http'

### Require pry gem for debugging purposes
require 'pry'
