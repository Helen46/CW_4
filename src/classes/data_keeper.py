from abc import ABC, abstractmethod


class DataKeeper(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def load_data(self, vacancies):
        pass
