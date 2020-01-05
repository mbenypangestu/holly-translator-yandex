from translator.translator import LanguageTranslator
from database.mongo_service import MongoService
from database.solr_service import SolrService
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

        rev_service = ReviewService()
        reviews = rev_service.get_lessthan_datetime(datenow)
        self.store_sentiment(reviews)

        # solrService = SolrService()
        # count = solrService.getCollection("test_review", "test")
        # print("Count : ", count)

    def store_sentiment(self, reviews):
        language_translator = LanguageTranslator()
        sentiment_analyzer = SentimentAnalyzer()
        sentiment_service = SentimentReviewService()

        for i, review in enumerate(reviews):
            text_to_translate = review['text']
            text_translated = language_translator.translate(text_to_translate)
            vader = sentiment_analyzer.get_vader(text_translated)
            wordnet = sentiment_analyzer.get_wordnet(text_translated)

            data = {
                "location_id": review['hotel_detail']['locationID'],
                "location_object_id": review['hotel_detail']['locationObjectID'],
                "hotel_location_id": review['hotel_locationID'],
                "hotel_location_object_id": review['hotel_ObjectId'],
                "text_to_translate": text_to_translate,
                "text_translated": text_translated,
                "vader_sentiment": vader,
                "wordnet_sentiment": wordnet,
                "created_at": datetime.datetime.now()
            }
            sentiment_service.create(data)


if __name__ == "__main__":
    Main()
    time.sleep(10000)
