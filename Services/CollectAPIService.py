import http.client


class CollectAPIService:

    def __init__(self, url, key):
        self.conn = http.client.HTTPSConnection(url)
        self.headers = {
            'content-type': "application/json",
            'authorization': key
        }

    def get_country_data(self):
        self.conn.request("GET", "/corona/countriesData", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        return data.decode("utf-8")

    def get_total_data(self):
        self.conn.request("GET", "/corona/totalData", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        return data.decode("utf-8")
