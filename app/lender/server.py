from flask import jsonify


def register_routes(blueprint):
    @blueprint.route('/get-lender', methods=['GET'])
    def get_lender():

        result = {
            "lender_name": "Bank of England Plc",
            "lender_addr_1": "12 Trinity Place",
            "lender_addr_2": "Regents Street",
            "lender_city": "London",
            "lender_company_no": "2347676", }

        return jsonify(result)
