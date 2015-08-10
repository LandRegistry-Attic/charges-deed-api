from app.db import db, json_type
from sqlalchemy.sql import text
import uuid
import copy


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
                   "json_doc -> 'operative-deed' -> 'borrowers') ->> 'token' "
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
        conn = db.session.connection()

        sql = text("select "
                   "count(*) as count "
                   "from (select "
                   "jsonb_array_elements(json_doc -> 'operative-deed' -> "
                   "'borrowers') "
                   "as borrower from deed where id = :deed_id) "
                   "as borrowers "
                   "where borrower ->> 'id' = :borrower_id")

        result = conn.execute(sql, deed_id=deed_id, borrower_id=borrower_id) \
            .fetchall()

        for row in result:
            return int(row['count']) > 0

    @staticmethod
    def borrower_has_signed(deed_id, borrower_id):
        conn = db.session.connection()

        sql = text("select count(signatures) as count "
                   "from (select "
                   "jsonb_array_elements(json_doc -> "
                   "'operative-deed' -> 'signatures') as signature "
                   "from deed where id = :deed_id) "
                   "as signatures "
                   "where signature ->> 'borrower_id' = :borrower_id ")

        result = conn.execute(sql, deed_id=deed_id, borrower_id=borrower_id) \
            .fetchall()

        for row in result:
            return int(row['count']) > 0

    @staticmethod
    def names_of_all_borrowers_signed(deed_id):
        conn = db.session.connection()

        sql = text("select jsonb_array_elements(json_doc -> "
                   "'operative-deed' -> 'signatures') "
                   "->> 'borrower_name' as borrower_name "
                   "from deed where id = :deed_id")

        result = conn.execute(sql, deed_id=deed_id) \
            .fetchall()
        borrower_names = list(map(lambda borrower_name: str(borrower_name[0]), result))
        return borrower_names

    @staticmethod
    def names_of_all_borrowers_not_signed(deed_id):
        conn = db.session.connection()

        sql = text("select jsonb_array_elements(borrowers) ->> 'name'"
                   "from (select jsonb_array_elements(json_doc -> "
                   "'operative-deed' -> 'borrowers') "
                   "from deed where id = :deed_id) as borrowers "
                   "where jsonb_array_elements(borrowers) "
                   "->> 'id' not in (select "
                   "jsonb_array_elements(json_doc -> "
                   "'operative-deed' -> 'signatures') ->> "
                   "'borrower_id' from deed where id = :deed_id) ")

        result = conn.execute(sql, deed_id=deed_id) \
            .fetchall()

        borrower_names = list(map(lambda borrower_name: str(borrower_name[0]), result))
        return borrower_names

    def all_borrowers_signed(self):
        operative_deed = self.json_doc['operative-deed']
        borrowers_length = len(operative_deed['borrowers'])
        signature_len = len(operative_deed['signatures'])

        return borrowers_length == signature_len

    @staticmethod
    def registrars_signature_exists(deed_id):
        deed = Deed.query.filter_by(id=deed_id).first()
        operative_deed_dct = deed.json_doc['operative-deed']

        return 'registrars-signature' in operative_deed_dct

    @staticmethod
    def generate_token():
        return str(uuid.uuid4().hex[:6]).lower()

    def get_json_doc(self):
        return copy.deepcopy(self.json_doc)
