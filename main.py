from translator.translator import LanguageTranslator
from database.mongo_service import MongoService
from database.solr_service import SolrService
from services.location_service import LocationService
from services.hotel_service import HotelService
from services.review_service import ReviewService
from services.sentiment_review_service import SentimentReviewService
from services.review_translated_service import ReviewTranslatedService

from mongoengine import connect
from pymongo import MongoClient
import time
import datetime
import json
import pprint
from googletrans import Translator


class Main(MongoService):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        datenow = datetime.datetime.now()
        reviewtranslate_service = ReviewTranslatedService()

        hotel_service = HotelService()
        review_service = ReviewService()
        location_service = LocationService()
        # locations = location_service.get_all_locations()
        locations = location_service.get_locations_indonesia()

        for i, location in enumerate(locations):
            hotels = hotel_service.get_hotels_by_locationid(
                location['location_id'])

            for j, hotel in enumerate(hotels):
                reviews = review_service.get_review_by_hotel_locationid(
                    hotel['location_id'])

                for r, review in enumerate(reviews):
                    text_to_translate = review['text']

                    try:
                        isexist_review = reviewtranslate_service.isexist_review_by_hotel_locid(
                            hotel['location_id'], review['id'])
                        # print(isexist_review)
                        if isexist_review.count() == 0:
                            print("[", datetime.datetime.now(), "] Review (",
                                  review['id'], ") on table Translated Review is not exist. Saving Review ...")

                            # gTranslator = Translator()
                            language_translator = LanguageTranslator()
                            text_translated = language_translator.translate_yandex(
                                text_to_translate)

                            data = {
                                "hotel": hotel,
                                "review": review,
                                "location_id": location['location_id'],
                                "hotel_id": hotel['location_id'],
                                "review_id": review['id'],
                                "text_to_translate": text_to_translate,
                                "text_translated": text_translated,
                                "created_at": datenow
                            }
                            if text_translated != None:
                                reviewtranslate_service.create(data)
                            else:
                                print(
                                    str("-----> Err : Failed to translate review !"))
                        else:
                            print("---> Review (",
                                  review['id'], ") on table Translated Review is already exist")

                    except Exception as err:
                        print(str("Err : ", err))
                        continue

                # solrService = SolrService()
                # count = solrService.getCollection("test_review", "test")
                # print("Count : ", count)

    def translate_reviews_onhotel(self, hotel):
        print()


if __name__ == "__main__":
    Main()
    # time.sleep(10000)
