from time import sleep
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import sentiwordnet as swn, stopwords, wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk
import pandas as pd
import re

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


class SentimentAnalyzer:
    def __init__(self):
        self.sentimentAnalyzer = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos_tag(self, tag):
        tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV,
        }

        return tag_dict.get(tag, wordnet.NOUN)

    def get_vader(self, text):
        return self.sentimentAnalyzer.polarity_scores(text)

    def get_wordnet(self, text):
        pos_temp = 0
        neg_temp = 0
        obj_temp = 0

        new_text = " ".join(re.findall("[a-zA-Z]+", text))

        tokenized = nltk.pos_tag(word_tokenize(new_text))
        for word in tokenized:
            if word[0].lower() not in self.stop_words:
                pos_tag = self.get_wordnet_pos_tag(word[1][0])
                lemmatized = self.lemmatizer.lemmatize(word[0], pos_tag)
                try:
                    synset = swn.senti_synset('{0}.{1}.01'.format(
                        lemmatized, pos_tag))
                except:
                    continue

                pos_temp += synset.pos_score()
                neg_temp += synset.neg_score()
                obj_temp += synset.obj_score()

        pos_wordnet = 0
        neg_wordnet = 0

        total_wordnet = pos_temp + neg_temp + obj_temp

        if total_wordnet != 0:
            pos_wordnet = pos_temp / total_wordnet
            neg_wordnet = neg_temp / total_wordnet

        result = pos_wordnet - neg_wordnet

        return result
