# This class will handle the integration with firestore and uploading documents to it

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FireStoreServices(object):

    def __init__(self, credentials_resource):
        self.cred = credentials.Certificate(credentials_resource)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def add_country(self, country):
        country_data = {
            'name': country.name,
            'total_cases': country.total_cases,
            'new_cases': country.new_cases,
            'total_deaths': country.total_deaths,
            'new_deaths': country.new_deaths,
            'total_recovered': country.total_recovered,
            'active_cases': country.active_cases,
        }
        self.db.collection('countries').document(country.name).set(country_data)

    def add_total(self, total):
        total_data = {
            'total_cases': total.total_cases,
            'total_deaths': total.total_deaths,
            'total_recovered': total.total_recovered,
        }
        self.db.document("totaldata").set(total_data)
