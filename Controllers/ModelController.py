# This class will be used as a gateway between the twitter and firestore services, and will perform filtering operations
# on tweet content as well as providing tojson methods for both the sources and news


class ModelController(object):

    def __init__(self):
        self.country_list = []

    def add_or_update_country(self, country):
        self.country_list.append(country)

    def get_countries(self):
        return list(self.country_list)

    def clear(self):
        self.country_list.clear()
        self.country_list = []
