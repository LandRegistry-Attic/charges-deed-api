Given(/^I visit \/([A-Za-z0-9\_\-]+)$/) do |url|
  response = Net::HTTP.get_response(URI("#{$DOMAIN}/#{url}"))
  $json = MultiJson.load(response.body)
end

Then(/^the json contains ([A-Za-z0-9\_\-]+):([A-Za-z0-9\_\-]+)$/) do |key, value|
  assert_match(value, $json[key], "Couldnt find #{value} in #{$json}")
end
