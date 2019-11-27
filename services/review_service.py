
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

    def is_review_exist(self, reviewId):
        review = self.db.review.find({'id': reviewId})
        if review.count() > 0:
            return True
        else:
            return False
