When(/^I get the effective deed from the api$/) do
  @effective_deed = get_deed_data(@created_deed_id)
end

Then(/^the registrars signature is applied to the deed$/) do
  assert_equal('SIGNATURE', @effective_deed['registrars-signature'])
end

Then(/^the effective date is applied to the deed$/) do
  date_effective = @effective_deed['date-effective']
  assert_match(Time.now.strftime('%Y-%m-%d'), date_effective)
end

When(/^I try to sign the deed again$/) do
  @response = HTTP.post(Env.deed_api + '/deed/' + @created_deed_id.to_s +
                             '/1/signature/')
end

Then(/^I should get a (\d+) response$/) do |response_code|
  assert_equal(response_code, @response.code.to_s)
end
