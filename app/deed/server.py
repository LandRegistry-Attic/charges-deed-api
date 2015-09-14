from flask import request, abort
from flask.ext.api import status
from app.deed import service as deed_service
from app.deed.model import Deed
from datetime import datetime


def register_routes(blueprint, case_api):
    @blueprint.route('/deed/<id_>', methods=['GET'])
    def get(id_):
        deed = deed_service.get(id_)

        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)
        else:
            return {'id': deed.id, 'deed': deed.json_doc}, status.HTTP_200_OK

    @blueprint.route('/deed/borrower/<token_>', methods=['GET'])
    def get_with_token(token_):
        deed = deed_service.get_deed_by_token(token_)

        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)
        else:
            return {'id': deed.id, 'deed': deed.json_doc}, status.HTTP_200_OK

    @blueprint.route('/deed/<id_>/signed/name', methods=['GET'])
    def get_names_signed(id_):
        deed_names = deed_service.names_of_all_borrowers_signed(id_)

        return {'names': deed_names}, status.HTTP_200_OK

    @blueprint.route('/deed/<id_>/signed_status', methods=['GET'])
    def get__signed_status(id_):
        all_signed = deed_service.get(id_).all_borrowers_signed()
        deed_names = deed_service.names_of_all_borrowers_not_signed(id_)

        return {
            'all_signed': all_signed,
            'names': deed_names
        }, status.HTTP_200_OK

    @blueprint.route('/deed/', methods=['POST'])
    def create():
        deed = Deed()
        deed_json = request.get_json()

        for borrower in deed_json['borrowers']:
            borrower["token"] = Deed.generate_token()

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
            return {'id': deed.id}, status.HTTP_200_OK
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

    @blueprint.route('/deed/<id_>', methods=['DELETE'])
    def delete(id_):
        try:
            deed = deed_service.delete(id_)
        except Exception as inst:
            print(str(type(inst)) + ":" + str(inst))

        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)
        else:
            return {'id': id_}, status.HTTP_200_OK

    @blueprint.route('/deed/<deed_id>/<borrower_id>/signature/',
                     methods=['POST'])
    def sign(deed_id, borrower_id):

        deed = deed_service.get(deed_id)
        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)

        if deed_service.borrower_on(deed_id, borrower_id) and \
                not deed_service.borrower_has_signed(deed_id, borrower_id):

            signature = request.json['signature']
            deed_service.sign_deed(deed, borrower_id, signature)
            try:
                deed.save()
            except Exception as inst:
                print(str(type(inst)) + ":" + str(inst))
                abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

            if deed.all_borrowers_signed():
                case_api.update_status(deed_id, 'Deed signed')
        else:
            abort(status.HTTP_403_FORBIDDEN)

        return {'signature': signature}, status.HTTP_200_OK

    @blueprint.route('/deed/<deed_id>/completion', methods=['POST'])
    def confirm_completion(deed_id):
        def update_case_status():
            response = case_api.update_status(deed.id, "Completion confirmed")
            if response.status_code != status.HTTP_200_OK:
                abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        def update_deed():
            try:
                deed_json = deed.get_json_doc()
                operative_deed = deed_json['operative-deed']
                operative_deed['registrars-signature'] = registrars_signature
                operative_deed['date-effective'] = str(datetime.now())
                deed.json_doc = deed_json
                deed.save()
            except Exception as exc:
                print(str(type(exc)) + ":" + str(exc))
                abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

        deed = deed_service.get(deed_id)
        if deed is None:
            abort(status.HTTP_404_NOT_FOUND)
        if not deed_service.registrars_signature_exists(deed.id):
            registrars_signature = request.data['registrars-signature']

            update_deed()
            update_case_status()

            return {'status_code': status.HTTP_200_OK}
        else:
            abort(status.HTTP_403_FORBIDDEN)
