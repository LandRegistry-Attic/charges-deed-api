from flask import request, jsonify, abort
from flask.ext.api import exceptions, status

from app.deed.model import Deed


def register_routes(blueprint):
    @blueprint.route('/deed/<id_>', methods=['GET'])
    def get(id_):
        deed = Deed.get(id_)

        if deed is None:
            abort(404)
        else:
            return jsonify(id=deed.id, deed=deed.json_doc), status.HTTP_200_OK

    @blueprint.route('/deed/', methods=['POST'])
    def create():
        deed = Deed()
        deed_json = request.get_json()
        json_doc = {
            "operative-deed": {
                "mdref": deed_json['mdref'],
                "title": deed_json['title'],
                "lender": deed_json['lender'],
                "borrowers": deed_json['borrowers'],
                "charging-clause": "You, the borrower, with full title "
                                   "guarantee, charge property to the "
                                   "lender by way of legal mortgage with "
                                   "the payment of all money secured by this"
                                   " charge.",
                "effective-clause": "This charge takes effect when the "
                                    "registrar receives notification from "
                                    "Bailey & Co Solicitors, who prepared "
                                    "this charge. The effective date and time "
                                    "is applied by the registrar on "
                                    "completion.",
                "restrictions": [],
                "provisions": []
            }}
        deed.json_doc = json_doc
        try:
            deed.save()
            return jsonify({"id": deed.id}), status.HTTP_200_OK
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            raise exceptions.NotAcceptable()

    @blueprint.route('/deed/<id_>', methods=['DELETE'])
    def delete(id_):
        try:
            deed = Deed.delete(id_)
        except Exception as inst:
            print(type(inst) + ":" + inst)

        if deed is None:
            abort(404)
        else:
            return jsonify(id=id_), status.HTTP_200_OK
