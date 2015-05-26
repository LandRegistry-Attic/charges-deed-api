from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/property', methods=['GET'])
    def get_property():

        result = {
            "address": {
                "street-address": "Flat 16 Kingman Court",
                "extended-address": "Verdant Road",
                "locality": "London",
                "postal-code": "",
                },
            "property-title-no": "GHR67832",
            }

        return jsonify(result)
