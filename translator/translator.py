import requests


class LanguageTranslator:
    def __init__(self):
        self._base_url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        self._api_key = "trnsl.1.1.20191123T042847Z.9cbe09e68450f11a.6a453d0246373470816ee73d70fa34bb7ae9d0fc"

    def translate(self, text="", from_lang="", target_lang="en"):
        lang = target_lang

        if from_lang != "":
            lang = from_lang + "-" + target_lang

        params = {
            'key': self._api_key,
            'lang': lang,
            'text': text
        }

        res = requests.post(self._base_url, params=params)
        res_obj = res.json()

        text_translated = res_obj['text'][0]
        return text_translated
