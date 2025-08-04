import pandas as pd

class Cleaner:
    def __init__(self, data):
        self.dataset = pd.read_csv(data)
        self.dataset.drop(['TweetID'])
        self.removing_punctuation_marks()

    def removing_punctuation_marks(self):
        self.dataset = self.dataset["Text"].replace("," " ")

