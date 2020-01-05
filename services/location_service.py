import requests
import json
from datetime import datetime
from time import sleep

from mongoengine import connect
from pymongo import MongoClient

from database.mongo_service import MongoService


class LocationService(MongoService):
    def __init__(self):
        super().__init__()

    def get_all_locations(self):
        locations = self.db.location.find()
        return locations
