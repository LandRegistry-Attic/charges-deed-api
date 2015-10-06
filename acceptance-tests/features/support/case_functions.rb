def create_case_data
  case_json = {
    'conveyancer_id' => '1'
  }
  response = HTTP.post(Env.case_api + '/case', json: case_json)
  if response.code == 201
    JSON.parse(response.body)['id']
  else
    fail "Error: Couldn't create case #{case_json}, "\
            "Received response #{response.code}"
  end
end

def delete_case_data(case_id)
  response = HTTP.delete(Env.case_api + '/case/' + case_id.to_s)
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't delete case #{case_id}, "\
            "received response #{response.code}."
  end
end

def add_borrowers_to_case(case_id, borrower_json)
  borrower_json = JSON.parse(borrower_json)
  response = HTTP.post(Env.case_api + '/case/' + case_id.to_s +
                      '/borrowers', json: borrower_json)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't add borrowers to case #{borrower_json}, "\
            "received response #{response.code}"
  end
end

def add_property_to_case(case_id, property_json)
  property_json = JSON.parse(property_json)
  response = HTTP.post(Env.case_api + '/case/' + case_id.to_s +
                      '/property', json: property_json)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't add property to case #{property_json}, "\
            "received response #{response.code}"
  end
end

def update_case_deed(deed_id, case_id)
  payload = {
    'deed_id' => deed_id
  }
  response = HTTP.post(Env.case_api + '/case/' + case_id.to_s +
   '/deed', json: payload)
  if response.code == 200
    JSON.parse(response.body)['id']
  else
    fail "Error: Couldn't update case with deed_id #{payload}, "\
            "Received response #{response.code}"
  end
end
