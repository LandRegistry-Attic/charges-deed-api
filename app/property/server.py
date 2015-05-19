from flask import Flask, make_response, Response, jsonify
import json

def register_routes(blueprint):
    @blueprint.route('/get-property', methods=['GET'])
    def get_property():

        result = {
            "deed_id" : "123456",
            "property_addr_1" : "Flat 16 Kingman Court",
            "property_addr_2" : "Verdant Road",
            "property_city" : "London",
            "property_title_no" : "GHR67832",
                }

        return jsonify(result)
