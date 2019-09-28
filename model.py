import pickle
import pandas as pd
import numpy as np
import re
import vk
import operator

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

from string import punctuation


class Model:

    def __init__(self):
        with open('vectorizer.pickle', 'rb') as f:
            self.vectorizer = pickle.load(f)

        with open('clf.pickle', 'rb') as f:
            self.clf = pickle.load(f)

        self.token = '25d8740525d8740525d874052425b486db225d825d87405785a18309e77a62887d0ffa8'
        
        self.session = vk.Session()
        self.api = vk.API(self.session, v=5.50)


    def clean_text(self, text):
        """Description.
        """
        text = text.lower()
        
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE) # Removing links
        text = re.sub(r'([@&#][\w_-]+\s)', '', text) # Remove hashtags 
        text = re.sub(r'\W+', ' ', text) # Remove special charecters
        
        text = ''.join([c for c in text if c not in self.punctuation])
        return text

    def predict_group(self, group, count):
        try:
            data = self.api.wall.get(owner_id=-group, access_token=self.token, count=count, v=5.50)

            counter = {i:0 for i in range(1, 7)}
            for i in range(len(data['items'])):
                text = data['items'][i]['text']
                text = self.vectorizer.transform([text])

                probs = list(self.clf.predict_proba(text)[0])
                predicted = self.clf.predict(text)[0]

                if probs[predicted-1] > 0.4:
                    counter[predicted] += 1
            return max(counter.items(), key=operator.itemgetter(1))[0]
        except:
            return None

    def classify(self, user, n_groups=50):
        try:
            groups = self.api.users.getSubscriptions(
                            user_id=user, access_token=self.token)['groups']['items']
            count = 10 if n_groups != 50 else 100

            cat = {i:0 for i in range(1, 7)}
            for group in range(min(n_groups, len(groups))):
                ans = self.predict_group(groups[group], count)
                if ans != None:
                    cat[ans] += 1
            print(cat)
            return max(cat.items(), key=operator.itemgetter(1))[0]
        except:
            return 3