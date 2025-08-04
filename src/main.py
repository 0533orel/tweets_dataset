from src.exploration import Exploration
from src.loader import LoadData

data = LoadData("../data/tweets_dataset.csv")

exploration = Exploration(data.dataset)
exploration.export_to_json_file()
