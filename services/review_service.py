
import requests
import json
from datetime import datetime
from time import sleep

from mongoengine import connect
from pymongo import MongoClient

from database.mongo_service import MongoService


class ReviewService(MongoService):
    def __init__(self):
        super().__init__()

    def get_all_reviews(self):
        reviews = self.db.review.find()
        return reviews

    def get_lessthan_datetime(self, datenow):
        reviews = self.db.review.aggregate([
            {
                '$lookup': {
                    "from": 'hotel',
                    "localField": 'hotel_locationID',
                    "foreignField": 'location_id',
                    "as": 'hotel_detail'
                }
            },
            {
                '$match': {
                    'created_at': {'$lt': datenow}
                }
            },
            {
                "$unwind": "$hotel_detail"
            }
        ])
        return reviews

    def is_review_exist(self, review_id):
        review = self.db.review.find({'id': review_id})
        if review.count() > 0:
            return True
        else:
            return False
