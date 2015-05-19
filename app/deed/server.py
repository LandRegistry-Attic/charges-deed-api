from flask import Flask, make_response, Response, jsonify
import json

def register_routes(blueprint):
    @blueprint.route('/view-deed', methods=['GET'])
    def get_deed():

        result = {
            "deed_id" : "123456",
            "property_addr_1" : "Flat 16 Kingman Court",
            "property_addr_2" : "Verdant Road",
            "property_city" : "London",
            "property_title_no" : "GHR67832",
            "lender_name" : "Bank of England Plc",
            "lender_addr_1" : "12 Trinity Place",
            "lender_addr_2" : "Regents Street",
            "lender_city" : "London",
            "lender_company_no" : "2347676",
            "provision_1" : "This Mortgage Deed incorporates the Lenders Mortgage Conditions and Explanation 2006, a copy of which has been received by the Borrower.",
            "provision_2" : "The lender is under an obligation to make further advances and applies for the obligation to be entered in the register.",
            "provision_3" : "No disposition of the registered estate by the proprietor of the registered estate is to be registered without a written consent signed by Bank of England Plc.",
        }

        return jsonify(result)
