from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/view-deed', methods=['GET'])
    def get_deed():

        result = {
            "deed-id": "12345",
            "provisions": [
                "This Mortgage Deed incorporates the Lenders Mortgage\
                Conditions and Explanation 2006, a copy of which has been \
                received by the Borrower.",
                "The lender is under an obligation to make further\
                advances and applies for the obligation to be entered in the\
                register.",
                "No disposition of the registered estate by the\
                proprietor of the registered estate is to be registered\
                without a written consent signed by Bank of England Plc.",
            ]
        }

        return jsonify(result)
