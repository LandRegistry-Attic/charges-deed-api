from flask import Flask, make_response, Response, jsonify
import json

def register_routes(blueprint):
    @blueprint.route('/helloworld', methods=['GET'])
    def get_title():

        result = {
            "Hello": "World",
        }

        return jsonify(result)
