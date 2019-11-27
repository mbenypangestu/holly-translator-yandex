from translator.translator import LanguageTranslator
from database.mongo_service import MongoService
from services.review_service import ReviewService


class Main(MongoService):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        revService = ReviewService()
        services = revService.get_all_reviews()

        text_to_translate = services[10000]['text']
        print(text_to_translate)

        languageTranslator = LanguageTranslator()
        text_translated = languageTranslator.translate(text_to_translate)

        print("Review translated : \n", text_translated)


if __name__ == "__main__":
    Main()
