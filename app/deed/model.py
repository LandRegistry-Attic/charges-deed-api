from app.db import db, json_type
from sqlalchemy.sql import text
import copy
import uuid


class Deed(db.Model):
    __tablename__ = 'deed'

    id = db.Column(db.Integer, primary_key=True)
    json_doc = db.Column(json_type)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def all():
        return Deed.query.all()

    @staticmethod
    def get(id_):
        return Deed.query.filter_by(id=id_).first()

    @staticmethod
    def get_deed_by_token(token_):
        conn = db.session.connection()

        sql = text("SELECT * "
                   "FROM deed AS the_deed "
                   "WHERE :token in "
                   "(SELECT jsonb_array_elements("
                   "json_doc -> 'deed' -> 'operative-deed' -> "
                   "'borrowers') ->> 'token' "
                   "FROM deed WHERE id = the_deed.id)")

        result = conn.execute(sql, token=token_) \
            .fetchall()

        if len(result) > 1:
            raise ValueError(
                'Tokens should be unique however several deeds were found')

        if len(result) == 0:
            return None

        deed = Deed()
        deed.id = result[0]['id']
        deed.json_doc = result[0]['json_doc']

        return deed

    @staticmethod
    def delete(id_):
        deed = Deed.query.filter_by(id=id_).first()

        if deed is None:
            return deed

        db.session.delete(deed)
        db.session.commit()

        return deed

    @staticmethod
    def borrower_on(deed_id, borrower_id):
        deed = Deed.get(deed_id)
        borrowers = deed.json_doc['deed']['operative-deed']['borrowers']

        for borrower in borrowers:
            if int(borrower['id']) == int(borrower_id):
                return True

        return False

    @staticmethod
    def borrower_has_signed(deed_id, borrower_id):
        deed = Deed.get(deed_id)
        signatures = deed.json_doc['deed']['signatures']

        for signature in signatures:
            if int(signature['borrower_id']) == int(borrower_id):
                return True

        return False

    @staticmethod
    def names_of_all_borrowers_signed(deed_id):
        deed = Deed.get(deed_id)
        signatures = deed.json_doc['deed']['signatures']

        return [signature['borrower_name'] for signature in signatures]

    @staticmethod
    def names_of_all_borrowers_not_signed(deed_id):
        deed = Deed.get(deed_id)
        signatures = deed.json_doc['deed']['signatures']
        borrower_ids_signed = [int(sgn['borrower_id']) for sgn in signatures]
        borrowers = deed.json_doc['deed']['operative-deed']['borrowers']

        result = list()

        for borrower in borrowers:
            if int(borrower['id']) not in borrower_ids_signed:
                result.append(borrower['name'])

        return result

    def all_borrowers_signed(self):
        deed_ = self.json_doc['deed']
        operative_deed = deed_['operative-deed']
        borrowers_length = len(operative_deed['borrowers'])
        signature_len = len(deed_['signatures'])

        return borrowers_length == signature_len

    @staticmethod
    def registrars_signature_exists(deed_id):
        deed = Deed.query.filter_by(id=deed_id).first()

        return 'registrars-signature' in deed.json_doc

    @staticmethod
    def generate_token():
        return str(uuid.uuid4().hex[:6]).lower()

    def get_json_doc(self):
        return copy.deepcopy(self.json_doc)

    def sign_deed(self, borrower_id, signature):
        deed_json = self.get_json_doc()
        operative_deed = deed_json['deed']['operative-deed']
        signatures = deed_json['deed']['signatures']

        borrower_name = list(
            filter(lambda borrower:
                   borrower["id"] == str(borrower_id),
                   operative_deed["borrowers"]))[0]["name"]

        user_signature = {
            "borrower_id": borrower_id,
            "borrower_name": borrower_name,
            "signature": signature
        }
        signatures.append(user_signature)
        self.json_doc = deed_json
