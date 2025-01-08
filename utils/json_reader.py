import json

class JsonReader:
    @staticmethod
    def read(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
