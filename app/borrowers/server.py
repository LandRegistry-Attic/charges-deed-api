from flask import Flask, make_response, Response, jsonify
import json

def register_routes(blueprint):
    @blueprint.route('/get-borrower/<borrower_id>', methods=['GET'])
    def get_borrower(borrower_id):

        if int(borrower_id) == 1:
            result = {
                "borrower_forename" : "Peter",
                "borrower_middle" : "",
                "borrower_surname" : "Smith",
                "borrower_addr_1" : "Flat 16 Kingman Court",
                "borrower_addr_2" : "Verdant Road",
                "borrower_city" : "London",
                "borrower_postcode" : "SV19 9BT",
                    }

        if int(borrower_id) == 2:
            result = {
                "borrower_forename" : "Sarah",
                "borrower_middle" : "Jane",
                "borrower_surname" : "Spencer",
                "borrower_addr_1" : "Flat 16 Kingman Court",
                "borrower_addr_2" : "Verdant Road",
                "borrower_city" : "London",
                "borrower_postcode" : "SV19 9BT",
                    }
        return jsonify(result)
