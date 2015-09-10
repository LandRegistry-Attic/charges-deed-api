from app.db import db, json_type
import copy
import uuid


class Deed(db.Model):
    __tablename__ = 'deed'

    id = db.Column(db.Integer, primary_key=True)
    json_doc = db.Column(json_type)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def all_borrowers_signed(self):
        operative_deed = self.json_doc['operative-deed']
        borrowers_length = len(operative_deed['borrowers'])
        signature_len = len(operative_deed['signatures'])

        return borrowers_length == signature_len

    @staticmethod
    def generate_token():
        return str(uuid.uuid4().hex[:6]).lower()

    def get_json_doc(self):
        return copy.deepcopy(self.json_doc)

    def sign_deed(self, borrower_id, signature):
        deed_json = self.get_json_doc()
        signatures = deed_json['operative-deed']['signatures']

        borrower_name = list(
            filter(lambda borrower:
                   borrower["id"] == str(borrower_id),
                   deed_json['operative-deed']["borrowers"]))[0]["name"]

        user_signature = {
            "borrower_id": borrower_id,
            "borrower_name": borrower_name,
            "signature": signature
        }
        signatures.append(user_signature)
        self.json_doc = deed_json
