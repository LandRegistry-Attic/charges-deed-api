from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/lender', methods=['GET'])
    def get_lender():

        result = {
            "name": "Bank of England Plc",
            "address": {
                "street-address": "12 Trinity Place",
                "extended-address": "Regents Street",
                "locality": "London",
                "postal-code": "",
                },
            "company-no": "2347676",
            }

        return jsonify(result)
