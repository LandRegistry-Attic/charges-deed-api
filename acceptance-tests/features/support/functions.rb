def create_deed_data(deed_json)
  deed_json = JSON.parse(deed_json)
  response = HTTP.post(Env.domain + '/deed/', json: deed_json)
  if response.code == 200
    JSON.parse(response.body)['id']
  else
    fail "Error: Couldn't create deed #{deed_json}, "\
            "Received response #{response.code}"
  end
end

def get_deed_data(deed_id)
  response = HTTP.get(Env.domain + '/deed/' + deed_id.to_s)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't retrieve deed #{deed_id}, "\
            "Received response #{response.code}"
  end
end

def delete_deed_data(deed_id)
  response = HTTP.delete(Env.domain + '/deed/' + deed_id.to_s)
  if response.code == 200
    puts "Deed #{deed_id} has been deleted."
  else
    fail "Error: Couldn't delete deed #{deed_id}, "\
            "received response #{response.code}."
  end
end

def sign_the_deed(deed_id, signature, borrower_id)
  signature_json = {
    'signature' => signature
  }
  response = HTTP.post(Env.domain + '/deed/' + deed_id.to_s +
                       '/' + borrower_id + '/signature/',
                       json: signature_json)

  if response.code == 200
    puts "Deed #{deed_id} has been signed."
  else
    fail "Error: Couldn't sign deed #{deed_id}, "\
            "received response #{response.code}."
  end
end

def make_deed_effective(deed_id)
  signature_json = {
    'registrars-signature' => 'SIGNATURE'
  }
  response = HTTP.post(Env.domain + '/deed/' + deed_id.to_s + '/completion',
                       json: signature_json)

  if response.code == 200
    puts "Deed #{deed_id} has been made effective."
  else
    fail "Error: Couldn't make deed #{deed_id} effective, "\
            "received response #{response.code}."
  end
end

def create_case_data
  payload = {
    'conveyancer_id' => '1'
  }
  response = HTTP.post(Env.case_api + '/case', json: payload)
  if response.code == 201
    JSON.parse(response.body)['id']
  else
    fail "Error: Couldn't create case #{payload}, "\
            "Received response #{response.code}"
  end
end

def update_case_deed
  payload = {
    'deed_id' => @deed_id
  }
  response = HTTP.post(Env.case_api + '/case/' + @case_id.to_s + '/deed',
                       json: payload)
  if response.code == 200
    JSON.parse(response.body)['id']
  else
    fail "Error: Couldn't update case with deed_id #{payload}, "\
            "Received response #{response.code}"
  end
end

def delete_case_data(case_id)
  response = HTTP.delete(Env.case_api + '/case/' + case_id.to_s)
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't delete deed #{case_id}, "\
            "received response #{response.code}."
  end
end