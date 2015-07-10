from random import randint
from app.deed.model import Deed


class DeedHelper:
    _id = randint(1, 999999)
    _json_doc = {
        'operative-deed': {
            'provisions': [

            ],
            'borrowers': [
                {
                    'name': 'John Smith',
                    'address': {
                        'street-address': 'test street',
                        'postal-code': 'RG1 1DP',
                        'locality': 'London',
                        'extended-address': 'test-extended address'
                    }
                }
            ],
            'restrictions': [

            ],
            "signatures": [],
            'effective-clause': 'const',
            'lender': {
                'name': 'Bank Test',
                'address': {
                    'street-address': 'test street',
                    'postal-code': 'RG1 1DP',
                    'locality': 'London',
                    'extended-address': 'test-extended address'
                },
                'company-number': '1233123ADF'
            },
            'title': {
                'address': {
                    'street-address': 'test street',
                    'postal-code': 'RG1 1DP',
                    'locality': 'London',
                    'extended-address': 'test-extended address'
                },
                'title-number': '123ABC'
            },
            'charging-clause': 'const',
            'mdref': 2
        }
    }

    @staticmethod
    def _create_deed_db():
        DeedHelper._id = randint(1, 999999)

        deed = Deed()
        deed.id = DeedHelper._id
        deed.json_doc = DeedHelper._json_doc

        deed.save()

        return deed.id

    @staticmethod
    def _create_deed():
        DeedHelper._id = randint(1, 999999)

        deed = Deed()
        deed.id = DeedHelper._id
        deed.json_doc = DeedHelper._json_doc

        return deed

    @staticmethod
    def _delete_deed(_id):
        Deed.delete(_id)
