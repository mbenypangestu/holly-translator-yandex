from translator.translator import LanguageTranslator
from database.mongo_service import MongoService
from database.solr_service import SolrService
from services.location_service import LocationService
from services.hotel_service import HotelService
from services.review_service import ReviewService
from services.sentiment_review_service import SentimentReviewService
from sentiment.sentiment import SentimentAnalyzer

import time
import datetime
import json
import pprint


class Main(MongoService):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        datenow = datetime.datetime.now()
        language_translator = LanguageTranslator()
        sentiment_service = SentimentReviewService()

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

                for r, review in enumerate(reviews):
                    text_to_translate = review['text']
                    text_translated = language_translator.translate_googletrans(
                        text_to_translate)

                    data = {
                        "hotel": hotel,
                        "review": review,
                        "text_to_translate": text_to_translate,
                        "text_translated": text_translated,
                        "created_at": datetime.datetime.now()
                    }

                    sentiment_service.create(data)
                    review_service.update_review_byid(
                        review['id'], {'gtrans_translated': 1})

        # solrService = SolrService()
        # count = solrService.getCollection("test_review", "test")
        # print("Count : ", count)


if __name__ == "__main__":
    Main()
    # time.sleep(10000)
