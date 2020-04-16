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

    def get_locations_indonesia(self):
        locations = self.db.location.find({
            "name": {"$in": [
                'Surabaya',
                'Banda Aceh',
                'Medan',
                'Padang',
                'Pekanbaru',
                'Palembang',
                'Bengkulu',
                'Bandar Lampung',
                'Pangkal Pinang',
                'Tanjung Pinang',
                'Jakarta',
                'Bandung',
                'Semarang',
                'Yogyakarta',
                'Serang',
                'Denpasar',
                'Mataram',
                'Kupang',
                'Pontianak',
                'Banjarmasi',
                'Samarinda',
                'Manado',
                'Palu',
                'Makassar',
                'Kendari',
                'Gorontalo',
                'Mamuju',
                'Ambon',
                'Jayapura',
                'Manokwari',
                'Malang',
                'Sidoarjo'
            ]}
        })
        return locations
