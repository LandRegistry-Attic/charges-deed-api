# Deed API

This application provides provides API for borrowers and conveyancers to operate on mortgage deeds.

## Contents
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Changing the migration](#changing-the-migration)
- [Current Model](#current-model)
- [Testing](#testing)

## Usage
```

GET     /deed/<id>                                  # get mortgage deed by id
POST    /deed/                                      # create a mortgage deed
DELETE  /deed/<id>                                  # delete a mortgage deed
GET     /deed/borrower/<token>                      # get mortgage deed by borrower token
GET     /deed/<id>/signed/name                      # get names of all borrowers who have signed the mortgage deed
GET     /deed/<id>/signed_status                    # check if all borrowers have signed the deed and return names of
                                                    # those who haven't
POST    /deed/<deed_id>/<borrower_id>/signature/    # sign the mortgage deed
POST    /deed/<deed_id>/completion                  # confirm mortgage deed completion (add registrars signature)
```

## Getting started

Get the git submodules
```
git submodule init
git submodule update
```

Install the requirements
```
pip install -r requirements.txt
pip install -r requirements_test.txt
```

Export your database URI
```
export DEED_DATABASE_URI=postgres:///deed_api
```

To run the migration run the command
```
python run.py db upgrade head
```

To run the application run the command
```
python run.py runserver
```

## Changing the migration
All you have to do is change/create the related model and run the command

```
python run.py db revision --autogenerate
```

> For some helpful documentation on using alembic go [here](alembic.md)


## Current model
```
### Deed

{
    "id": 37,
    "deed": {
        "operative-deed": {
            "mdref": "MD0149A",
            "borrowers": [
                {
                    "id": "1",
                    "address": {
                        "postal-code": "N16 5UP",
                        "locality": "London",
                        "extended-address": "",
                        "street-address": "83 Lordship Park"
                    },
                    "token": "162fe8",
                    "name": "Peter Smith"
                },
                {
                    "id": "2",
                    "address": {
                        "postal-code": "N16 5UP",
                        "locality": "London",
                        "extended-address": "",
                        "street-address": "83 Lordship Park"
                    },
                    "token": "4945fb",
                    "name": "John Smith"
                }
            ],
            "provisions": [
                "I am a provision"
            ],
            "restrictions": [
                "This is my restriction"
            ],
            "effective-clause": "This charge takes effect when the registrar receives notification
                                 from Bailey & Co Solicitors, who prepared this charge. The effective
                                 date and time is applied by the registrar on completion.",
            "title": {
                "address": {
                    "postal-code": "N12 5TN",
                    "locality": "London",
                    "extended-address": "",
                    "street-address": "18 Lordly Place"
                },
                "title-number": "GHR67832"
            },
            "lender": {
                "address": {
                    "postal-code": "NW10 6TQ",
                    "locality": "London",
                    "extended-address": "Regents Street",
                    "street-address": "12 Trinity Place"
                },
                "company-number": "24071987",
                "name": "Bank of England PLC"
            },
            "charging-clause": "You, the borrower, with full title guarantee, charge property to the
                                lender by way of legal mortgage with the payment of all money secured by
                                this charge."
        },
        "signatures": [
            {
                "signature": "Peter Smith_16/09/2015_11:16:01",
                "borrower_id": "1",
                "borrower_name": "Peter Smith"
            },
            {
                "signature": "John Smith_16/09/2015_11:16:18",
                "borrower_id": "2",
                "borrower_name": "John Smith"
            }
        ]
    },
    "registrars-signature": "THE_SIGNATURE",
    "date-effective": "2015-09-16 11:16:25.659042"
}
```
## Testing

### Unit tests

Run the unit tests
```
python tests.py
```

### Acceptance tests

All of the acceptance tests are contained within the acceptance-tests folder with the feature files under the features folder and the step-definitions under the steps folder.

If you would like to run all of the acceptance tests then navigate into the acceptance-tests folder and run the following command:

```
./run_tests.sh
```

You can also pass arguments to this command as you would if you were just running cucumber on it's own.

For example you can use the following command to display a cut down version of cucumbers progress when it is running:

```
./run_tests.sh --format progress
```

Or you can use the following to run only the scenarios that have been tagged with whatever tags you specify:

```
/run_tests.sh --tags @USXX
```

### Running Rubocop

Rubocop is ruby gem that will check any ruby code in the repository against the ruby style guide and then provide a report of any offenses.

In order to run Rubocop on the acceptance test code then navigate into the acceptance test folder and run the command:

```
./run_linting.sh
```

If you wish to amend what cops are used, what files are ignored when running Rubocop then you will need to put this in the rubocop.yml file.
