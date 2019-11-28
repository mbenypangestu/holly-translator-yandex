from translator.translator import LanguageTranslator
from database.mongo_service import MongoService
from database.solr_service import SolrService
from services.review_service import ReviewService

import time


class Main(MongoService):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        revService = ReviewService()
        services = revService.get_all_reviews()

        solrService = SolrService()

        languageTranslator = LanguageTranslator()
        for i, service in enumerate(services):
            text_to_translate = service['text']
            print("\nReview : \n", text_to_translate)

            text_translated = languageTranslator.translate(text_to_translate)
            print("Review translated : \n", text_translated)

            time.sleep(1)


if __name__ == "__main__":
    Main()
    time.sleep(10000)
