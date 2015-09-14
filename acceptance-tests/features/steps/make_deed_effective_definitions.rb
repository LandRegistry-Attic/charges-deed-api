Given(/^I have made the created deed effective$/) do
  sign_the_deed(@deed_id, 'SIGNATURE', '1')
  make_deed_effective(@deed_id)
end

Then(/^the signature is applied to the deed$/) do
  assert_equal(@deed['deed']['operative-deed']['registrars-signature'],
               'SIGNATURE')
end

Then(/^the date is applied to the deed$/) do
  date_effective = @deed['date-effective']
  assert_match(Time.now.strftime('%Y-%m-%d'), date_effective)
end

When(/^I try to sign the deed again$/) do
  @response = HTTP.post(Env.domain + '/deed/' + @deed_id.to_s +
                             '/1/signature/')
end

Then(/^I should get a (\d+) response$/) do |response_code|
  assert_equal(response_code, @response.code.to_s)
end
