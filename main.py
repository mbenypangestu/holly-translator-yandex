from translator.translator import LanguageTranslator
from database.mongo_service import MongoService
from database.solr_service import SolrService
from services.location_service import LocationService
from services.hotel_service import HotelService
from services.review_service import ReviewService
from services.sentiment_review_service import SentimentReviewService
from services.review_translated_service import ReviewTranslatedService
from sentiment.sentiment import SentimentAnalyzer

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
        language_translator = LanguageTranslator()
        reviewtranslate_service = ReviewTranslatedService()

        hotel_service = HotelService()
        review_service = ReviewService()
        location_service = LocationService()
        locations = location_service.get_all_locations()

        for i, location in enumerate(locations):
            hotels = hotel_service.get_hotels_by_locationid(
                location['location_id'])

            for j, hotel in enumerate(hotels):
                reviews = review_service.get_review_by_hotel_locationid(
                    hotel['location_id'])
                reviewtranslate_on_hotel = reviewtranslate_service.get_review_by_hotel_locid(
                    hotel['location_id'])

                for r, review in enumerate(reviews):
                    text_to_translate = review['text']

                    try:
                        gTranslator = Translator()
                        text_translated = gTranslator.translate(
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

                        isexist_review = any(x['review_id'] == review['id']
                                             for x in reviewtranslate_on_hotel)
                        if not isexist_review:
                            reviewtranslate_service.create(data)
                        else:
                            print("---> Review (",
                                  review['id'], ") on table Translated Review is already exist")

                        # review_service.update_review_byid(
                        #     review['id'], {'gtrans_translated': 1})

                    except Exception as e:
                        print(str("Err : ", e))
                        continue

                # solrService = SolrService()
                # count = solrService.getCollection("test_review", "test")
                # print("Count : ", count)


if __name__ == "__main__":
    Main()
    # time.sleep(10000)
