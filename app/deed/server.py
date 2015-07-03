from flask import jsonify, abort, request


charge_clause = """You, the borrower, with full title
 guarantee, charge property to the lender by way of
 legal mortgage with the payment of all money
 secured by this charge."""

provision_1 = """This Mortgage Deed incorporates the Lenders Mortgage
 Conditions and Explanation 2006, a copy of which has been received by the
 Borrower."""
provision_2 = """No disposition of the registered estate by the proprietor of
 the registered estate is to be registered without a written consent signed by
 Bank of England Plc."""

effective_clause = """This charge takes effect when the registrar receives
 notification from Bailey & Co Solicitors, who prepared this charge. The
 effective date and time is applied by the registrar on completion."""


def register_routes(blueprint):
    @blueprint.route('/deed/<id_>', methods=['GET'])
    def get(id_):
        if int(id_) == 1:
            return jsonify({
                "id": "1",
                "deed": {
                    "operative-deed": {
                        "mdref": "1",
                        "title": {
                            "title-number": "GHR67832",
                            "description": "",
                            "address": {
                                "street-address": "Flat 16 Kingman Court",
                                "extended-address": "Verdant Road",
                                "locality": "London",
                                "postal-code": "",
                            },
                        },
                        "lender": {
                            "name": "Bank of England Plc",
                            "address": {
                                "street-address": "12 Trinity Place",
                                "extended-address": "Regents Street",
                                "locality": "London",
                                "postal-code": "2347676",
                            },
                            "company-number": "",
                        },
                        "borrowers": [{
                            "borrower-id": "1",
                            "name": "Peter Smith",
                            "address": {
                                "street-address": "Flat 16 Kingman Court",
                                "extended-address": "Verdant Road",
                                "locality": "London",
                                "postal-code": "SV19 9BT",
                            },
                        }, {
                            "borrower-id": "2",
                            "name": "Sarah Jane Smith",
                            "address": {
                                "street-address": "Flat 16 Kingman Court",
                                "extended-address": "Verdant Road",
                                "locality": "London",
                                "postal-code": "SV19 9BT",
                            },
                        }, ],
                        "charging-clause": charge_clause,
                        "provisions": [provision_1, provision_2],
                        "restrictions": [],
                        "effective-clause": effective_clause,
                    },
                    "signatures": [],
                    "effective-date": "",
                },
                "registrars-signature": {
                    "name": "",
                    "date": "",
                    "signature": "",
                },
            })
        else:
            abort(404)

    @blueprint.route('/deed/', methods=['POST'])
    def create():
        print("Deed " + str(request.get_json()) + " created!")
        return jsonify()

    @blueprint.route('/deed/<id_>', methods=['DELETE'])
    def delete(id_):
        print("Deed " + id_ + " deleted!")
        return jsonify()
