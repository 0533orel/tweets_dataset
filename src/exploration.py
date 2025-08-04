class Exploration:
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