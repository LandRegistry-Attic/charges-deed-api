Then(/^the api response contains a token for each borrower$/) do
  @created_deed['deed']['operative-deed']['borrowers'].each do |borrower|
    assert(borrower['token'],
           "Error: Token doesn't exist for borrower #{borrower['id']}")
  end
end
