from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/conveyancer', methods=['GET'])
    def get_conveyancer():

        result = {
            "name": "",
            "address": {
                "street-address": "",
                "extended-address": "",
                "locality": "",
                "postal-code": "",
                },
            }

        return jsonify(result)
