import time
import requests
import os
import pandas as pd
import pprint


class LanguageTranslator:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._base_url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        self._api_key = "trnsl.1.1.20191123T042847Z.9cbe09e68450f11a.6a453d0246373470816ee73d70fa34bb7ae9d0fc"
        self.languages = pd.read_csv(
            self.path + "/dataset/language_standart.csv")

    def translate(self, text="", src_lang="", target_lang="en"):
        lang = target_lang

        if src_lang != "":
            selected_lang = self.languages.loc[self.languages['tripadvisor'] ==
                                               src_lang]
            if not selected_lang.empty:
                src_lang = selected_lang['yandex']
            lang = src_lang + "-" + target_lang

        params = {
            'key': self._api_key,
            'lang': lang,
            'text': text
        }

        res = requests.post(self._base_url, params=params)
        res_obj = res.json()

        pprint.pprint(res_obj)

        text_translated = res_obj['text'][0]
        return text_translated
