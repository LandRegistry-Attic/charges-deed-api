Given(/^I have created the following deed:$/) do |deed_json|
  @deed_id = create_deed_data(deed_json)
end

Given(%r{^I visit \/([A-Za-z0-9\_\-]+)$}) do |url|
  response = Net::HTTP.get_response(URI("#{Env.domain}/#{url}"))
  @json = MultiJson.load(response.body)
end

Then(
  /^the json contains ([A-Za-z0-9\_\-]+):([A-Za-z0-9\_\-]+)$/
) do |key, value|
  assert_match(value, @json[key], "Couldnt find #{value} in #{@json}")
end

When(/^I get the created deed from the api$/) do
  @deed = get_deed_data(@deed_id)
end

Then(/^the api response contains a token for each borrower$/) do
  @deed['deed']['operative-deed']['borrowers'].each do |borrower|
    assert(borrower['token'],
           "Error: Token doesn't exist for borrower #{borrower['id']}")
  end
end

Given(/^I have created a case$/) do
  @case_id = create_case_data
end

Given(/^I have linked the created deed and case$/) do
  update_case_deed
end
