from app.deed.model import Deed
from app.db import db
from sqlalchemy.sql import text


def all():
    return Deed.query.all()


def get(id_):
    return Deed.query.filter_by(id=id_).first()


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


def delete(id_):
    deed = Deed.query.filter_by(id=id_).first()

    if deed is None:
        return deed

    db.session.delete(deed)
    db.session.commit()

    return deed


def borrower_on(deed_id, borrower_id):
    deed = get(deed_id)
    borrowers = deed.json_doc['deed']['operative-deed']['borrowers']

    for borrower in borrowers:
        if int(borrower['id']) == int(borrower_id):
            return True

    return False


def borrower_has_signed(deed_id, borrower_id):
    deed = get(deed_id)
    signatures = deed.json_doc['deed']['signatures']

    for signature in signatures:
        if int(signature['borrower_id']) == int(borrower_id):
            return True

    return False


def all_borrowers_signed(deed):
    deed_ = deed.json_doc['deed']
    operative_deed = deed_['operative-deed']
    borrowers_length = len(operative_deed['borrowers'])
    signature_len = len(deed_['signatures'])

    return borrowers_length == signature_len


def names_of_all_borrowers_not_signed(deed_id):
    deed = get(deed_id)
    signatures = deed.json_doc['deed']['signatures']
    borrower_ids_signed = [int(sgn['borrower_id']) for sgn in signatures]
    borrowers = deed.json_doc['deed']['operative-deed']['borrowers']

    result = list()

    for borrower in borrowers:
        if int(borrower['id']) not in borrower_ids_signed:

            if borrower["middle_names"] != "":
                middlename = borrower["middle_names"] + " "
            else:
                middlename = ""

            fullborrowername = borrower["first_name"] + " " + middlename + \
                borrower["last_name"]

            result.append(fullborrowername)

    return result


def names_of_all_borrowers_signed(deed_id):
    deed = get(deed_id)
    signatures = deed.json_doc['deed']['signatures']

    return [signature['borrower_name'] for signature in signatures]


def registrars_signature_exists(deed_id):
    deed = Deed.query.filter_by(id=deed_id).first()

    return 'registrars-signature' in deed.json_doc


def sign_deed(self, borrower_id, signature):
    deed_json = self.get_json_doc()
    operative_deed = deed_json['deed']['operative-deed']
    signatures = deed_json['deed']['signatures']
    names = ""
    borrowers = operative_deed["borrowers"]
    for borrower in borrowers:
        if borrower["id"] == int(borrower_id):
            names = [borrower["first_name"], borrower["middle_names"],
                     borrower["last_name"]]

    # strings return false if they are empty or null,
    # this lambda strips out those
    names_list = list(filter(lambda name: bool(name), names))

    # whats left gets joined together
    full_borrower_name = ' '.join(names_list)

    user_signature = {
        "borrower_id": borrower_id,
        "borrower_name": full_borrower_name,
        "signature": signature
    }
    signatures.append(user_signature)
    self.json_doc = deed_json
