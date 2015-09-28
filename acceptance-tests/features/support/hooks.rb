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
After ('@delete_test_data') do
  if @created_deed_id
    puts "Deleting test deed #{@created_deed_id}"
    delete_deed_data(@created_deed_id)
  end
  if @created_case_id
    puts "Deleting test case #{@created_case_id}"
    delete_case_data(@created_case_id)
  end
end
