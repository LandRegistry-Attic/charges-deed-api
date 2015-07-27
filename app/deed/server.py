import copy
from flask import request, jsonify, abort
from flask.ext.api import status
from app.deed.model import Deed


def register_routes(blueprint, case_api):
    @blueprint.route('/deed/<id_>', methods=['GET'])
    def get(id_):
        deed = Deed.get(id_)

        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)
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
                "signatures": [],
                "restrictions": deed_json['restrictions'],
                "provisions": deed_json['provisions']
            }}
        deed.json_doc = json_doc
        try:
            deed.save()
            return jsonify(id=deed.id), status.HTTP_200_OK
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

    @blueprint.route('/deed/<id_>', methods=['DELETE'])
    def delete(id_):
        try:
            deed = Deed.delete(id_)
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))

        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)
        else:
            return jsonify(id=id_), status.HTTP_200_OK

    @blueprint.route('/deed/<deed_id>/<borrower_id>/signature/',
                     methods=['POST'])
    def sign(deed_id, borrower_id):
        def sign_allowed():
            return Deed.matches(deed_id, borrower_id)

        def sign_deed(deed_, signature_):
            deed_json = copy.deepcopy(deed_.json_doc)
            signatures = deed_json['operative-deed']['signatures']
            signatures.append(signature_)
            try:
                deed_.json_doc = deed_json
                deed_.save()
            except Exception as inst:
                print(str(type(inst)) + ":" + str(inst))
                abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        if sign_allowed():
            deed = Deed.get(deed_id)
            signature = request.form['signature']
            sign_deed(deed, signature)

            if deed.all_borrowers_signed():
                case_api.update_status(deed_id, 'Deed signed')
        else:
            abort(status.HTTP_403_FORBIDDEN)

        return jsonify(signature=signature), status.HTTP_200_OK
