from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/borrower/<borrower_id>', methods=['GET'])
    def get_borrower(borrower_id):

        if int(borrower_id) == 1:
            result = {
                "forename": "Peter",
                "middle": "",
                "surname": "Smith",
                "address": {
                    "street-address": "Flat 16 Kingman Court",
                    "extended-address": "Verdant Road",
                    "locality": "London",
                    "postal-code": "SV19 9BT",
                    },
                }

        if int(borrower_id) == 2:
            result = {
                "forename": "Sarah",
                "middle": "Jane",
                "surname": "Spencer",
                "address": {
                    "stree-address": "Flat 16 Kingman Court",
                    "extended-address": "Verdant Road",
                    "locality": "London",
                    "postal-code": "SV19 9BT",
                    },
                }
        return jsonify(result)
