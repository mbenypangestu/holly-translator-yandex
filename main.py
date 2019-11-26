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
        print(services)

        languageTranslator = LanguageTranslator()
        text_translated = languageTranslator.translate("Nama saya beny")

        print("Review translated : ", text_translated)


if __name__ == "__main__":
    Main()
