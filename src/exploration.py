class Exploration:
    """
    This department investigates the data from several different perspectives.
    Each investigation has its own methodology
    """
    def __init__(self, data):
        self.__dataset = data
        self.__total_tweets = {"antisemitic": 0,
                             "non_antisemitic": 0,
                             "total": 0,
                             "unspecified": 0
                               }
        self.__average_length = {"antisemitic": 0,
                                 "non_antisemitic": 0,
                                 "total": 0
                                 }
        self.__common_words = {"total": []}
        self.__longest_3_tweets = {"antisemitic": [],
                                   "non_antisemitic": []
                                   }
        self.__uppercase_words = {"antisemitic": 0,
                                  "non_antisemitic": 0,
                                  "total": 0
                                  }

    def total_tweets(self):
        """
        Count how many tweets there are from each category.
        """
        if self.__dataset is None:
            raise ValueError("\nThe dataset is empty")
        for idx, row in self.__dataset.iterrows():
            if row["Biased"] == 1:
                self.__total_tweets["antisemitic"] += 1
            elif row["Biased"] == 0:
                self.__total_tweets["non_antisemitic"] += 1
            else:
                self.__total_tweets["unspecified"] += 1
            self.__total_tweets["total"] += 1

    def average_length(self):
        """
        Counts how many words and tweets there are in each category and calculates their average
        """
        if self.__dataset is None:
            raise ValueError("\nThe dataset is empty")

        if self.__total_tweets["total"] == 0:
            self.total_tweets()

        antisemitic_words = []
        non_antisemitic_words = []
        for idx, row in self.__dataset.iterrows():
            words = row["Text"].split(" ")
            if row["Biased"] == 1:
                for word in words:
                    antisemitic_words.append(word)
            elif row["Biased"] == 0:
                for word in words:
                    non_antisemitic_words.append(word)

        if self.__total_tweets["antisemitic"] > 0:
            self.__average_length["antisemitic"] = len(antisemitic_words) / self.__total_tweets["antisemitic"]
        else:
            raise ValueError("\nCannot divide by zero (no tweets in category antisemitic)")

        if self.__total_tweets["non_antisemitic"] > 0:
            self.__average_length["non_antisemitic"] = len(non_antisemitic_words) / self.__total_tweets["non_antisemitic"]
        else:
            raise ValueError("\nCannot divide by zero (no tweets in category non_antisemitic)")

        if self.__total_tweets["antisemitic"] > 0 or self.__total_tweets["non_antisemitic"] > 0:
            self.__average_length["total"] = (len(antisemitic_words) + len(non_antisemitic_words)) / (self.__total_tweets["antisemitic"] + self.__total_tweets["non_antisemitic"])
        else:
            raise ValueError("\nCannot divide by zero (No tweets)")


