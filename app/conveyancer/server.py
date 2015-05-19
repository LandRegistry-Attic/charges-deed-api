from flask import Flask, make_response, Response, jsonify
import json

def register_routes(blueprint):
    @blueprint.route('/get-conveyancer', methods=['GET'])
    def get_conveyancer():

        result = {
            "conveyancer_name": "",
            "conveyancer_addr_1": "",
            "conveyancer_addr_2": "",
            "conveyancer_city": "",
                }

        return jsonify(result)
