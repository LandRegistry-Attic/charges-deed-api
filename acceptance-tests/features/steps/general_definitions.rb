Given(/^I have created the following deed:$/) do |deed_json|
  @@deed_id = create_deed_data(deed_json)
  @@TEST_DEEDS.push(@@deed_id)
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
