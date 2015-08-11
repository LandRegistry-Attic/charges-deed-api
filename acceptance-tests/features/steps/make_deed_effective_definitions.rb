Given(/^I have made the created deed effective$/) do
  sign_the_deed(@deed_id, 'SIGNATURE', '1')
  make_deed_effective(@deed_id)
end

When(/^I get the deed from the api$/) do
  @deed = get_deed_data(@deed_id)
end

Then(/^the signature is applied to the deed$/) do
  assert(@deed['deed']['operative-deed']['registrars-signature'],
         'Signature not applied')
end

Then(/^the date is applied to the deed$/) do
  assert(@deed['deed']['operative-deed']['date-effective'],
         'Date not applied')
end

Given(/^I have created a case$/) do
  @case_id = create_case_data
end

Given(/^I have linked the created deed and case$/) do
  update_case_deed
end

When(/^I try to sign the deed again$/) do
  @response = HTTP.post(Env.domain + '/deed/' + @deed_id.to_s +
                             '/1/signature/')
end

Then(/^I should get a (\d+) response$/) do |arg1|
  assert_equal(@response.code.to_s, arg1)
end
