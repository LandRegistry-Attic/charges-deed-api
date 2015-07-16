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

def delete_deed_data(deed_id)
  response = HTTP.delete(Env.domain + '/deed/' + deed_id.to_s)
  if response.code == 200
    puts "Deed #{deed_id} has been deleted."
  else
    fail "Error: Couldn't delete deed #{deed_id}, "\
            "received response #{response.code}."
  end
end
