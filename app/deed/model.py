from app.db import db, json_type
from sqlalchemy.sql import text
import string
import random


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
    def matches(deed_id, borrower_id):
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
    def generate_token():
        size = 6
        return ''.join(random.choice(string.ascii_uppercase + string.digits)
                       for _ in range(size))
