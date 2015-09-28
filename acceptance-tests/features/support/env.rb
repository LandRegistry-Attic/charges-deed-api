
################################################################################
### This file contains the global variables for the various endpoints used   ###
### in acceptance tests, this abstracts the urls so that you will not        ###
### need to change every test when switching environments for example.       ###
################################################################################

class Env
  def self.borrower_frontend
    (ENV['BORROWER_FRONTEND_URL'] || 'http://borrower-frontend.dev.service.gov.uk')
  end

  def self.conveyancer_frontend
    (ENV['CONVEYANCER_FRONTEND_URL'] || 'http://conveyancer-frontend.dev.service.gov.uk')
  end

  def self.deed_api
    (ENV['DEED_API_URL'] || 'http://deedapi.dev.service.gov.uk')
  end

  def self.case_api
    (ENV['CASE_API_URL'] || 'http://case-api.dev.service.gov.uk')
  end
end
