import json
from DataSaver import DataSaver

class JsonFileSaver(DataSaver):
    def __init__(self, path):
        self.path = path
    
    def load_data(self):
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except:
            return None

    def save_data(self, array_save_data):
        with open(self.path, 'w') as f:
            f.write(json.dumps([o.dump() for o in array_save_data], indent=4))