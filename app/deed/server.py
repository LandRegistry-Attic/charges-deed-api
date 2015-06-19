from flask import jsonify, abort, request


def register_routes(blueprint):
    @blueprint.route('/deed/<md_ref>', methods=['GET'])
    def get(md_ref):
        if int(md_ref) == 1:
            return jsonify({
                "deed-id": "12345",
                "borrowers": [{
                    "forename": "Peter",
                    "middle": "",
                    "surname": "Smith",
                    "address": {
                        "street-address": "Flat 16 Kingman Court",
                        "extended-address": "Verdant Road",
                        "locality": "London",
                        "postal-code": "SV19 9BT",
                    },
                }, {
                    "forename": "Sarah",
                    "middle": "Jane",
                    "surname": "Spencer",
                    "address": {
                        "street-address": "Flat 16 Kingman Court",
                        "extended-address": "Verdant Road",
                        "locality": "London",
                        "postal-code": "SV19 9BT",
                    },
                }],
                "property": {
                    "address": {
                        "street-address": "Flat 16 Kingman Court",
                        "extended-address": "Verdant Road",
                        "locality": "London",
                        "postal-code": "",
                    },
                    "property-title-no": "GHR67832",
                },
                "lender": {
                    "name": "Bank of England Plc",
                    "address": {
                        "street-address": "12 Trinity Place",
                        "extended-address": "Regents Street",
                        "locality": "London",
                        "postal-code": "",
                    },
                    "company-no": "2347676",
                }})
        else:
            abort(404)

    @blueprint.route('/deed/', methods=['POST'])
    def create():
        print("Deed " + str(request.get_json()) + " created!")
        return jsonify()

    @blueprint.route('/deed/<md_ref>', methods=['DELETE'])
    def delete(md_ref):
        print("Deed " + md_ref + " deleted!")
        return jsonify()
