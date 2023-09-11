from abc import ABC, abstractmethod

class DataSaver(ABC):
    @abstractmethod
    def load_data():
        pass
    
    @abstractmethod
    def save_data():
        pass