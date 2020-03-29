# This is the model class of a news
import re


class Country(object):

    # instance attributes
    def __init__(self, name, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases):
        self.name = name
        self.total_cases = total_cases
        self.new_cases = new_cases
        self.total_deaths = total_deaths
        self.new_deaths = new_deaths
        self.total_recovered = total_recovered
        self.active_cases = active_cases
