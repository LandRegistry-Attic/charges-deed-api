################################################################################
### This file contains any code that should be executed before and after     ###
### the acceptance tests are run, this could include things like taking a    ###
### screenshot if a scenario fails or getting through any initial            ###
### authentication for the app before running the tests.                     ###
################################################################################

### Code that is executed before acceptance tests for each feature have run
Before do
end

### Code that is executed after acceptance tests for each feature have run
After do
end

### Code that is executed after all of the acceptance tests have run
After('@US65') do
  ### Delete any deed data that has been created
  puts 'Deleting deed test data...'
  binding.pry
  @@TEST_DEEDS.each do |deed_id|
    delete_deed_data(deed_id)
  end
end
