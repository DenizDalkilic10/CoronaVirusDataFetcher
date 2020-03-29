import json

from Models import Country
from Services import FirestoreService, CollectAPIService
from Controllers import ModelController


class ServerApplication(object):

    def __init__(self, firestore_credentials_resource, api_url, api_key):
        self.collectAPI_service = CollectAPIService.CollectAPIService(api_url, api_key)
        self.firestore_service = FirestoreService.FireStoreServices(firestore_credentials_resource)
        self.model_controller = ModelController.ModelController()

    def run(self):
        self.download_country_info()
        self.upload_country_info()

    def download_country_info(self):
        response = json.loads(self.collectAPI_service.get_country_data())
        country_list = response["result"]
        for country in country_list:
            country_model = Country.Country(country["country"],
                                            int(country["totalCases"].replace(",", "")) if country[
                                                                                               "totalCases"] != "" else 0,
                                            int(country["newCases"].replace(",", "")) if country[
                                                                                             "newCases"] != "" else 0,
                                            int(country["totalDeaths"].replace(",", "")) if country[
                                                                                                "totalDeaths"] != "" else 0,
                                            int(country["newDeaths"].replace(",", "")) if country[
                                                                                              "newDeaths"] != "" else 0,
                                            int(country["totalRecovered"].replace(",", "")) if country[
                                                                                                   "totalRecovered"] != "" else 0,
                                            int(country["activeCases"].replace(",", "")) if country[
                                                                                                "activeCases"] != "" else 0)

            self.model_controller.add_or_update_country(country_model)
            print("country info for " + country["country"] + " fetched")

    def upload_country_info(self):
        for country in self.model_controller.get_countries():
            self.firestore_service.add_country(country)
            print("country info uploaded for " + country.name + " fetched")
