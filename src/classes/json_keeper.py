from src.classes.data_keeper import DataKeeper
import json


class JSONKeeper(DataKeeper):
    """
    Клаасс для сохранения информации о вакансиях в JSON-файл
    """
    def __init__(self, file_name):
        super().__init__(file_name)

    def load_data(self, vacancies):
        """
        Метод для записи информации в JSON-файл
        :param vacancies: экземпляры класса
        :return: JSON-файл
        """
        with open(self.file_name, "w", encoding='utf-8') as file:
            file.write(json.dumps(vacancies, indent=2, ensure_ascii=False))

    def get_data(self):
        with open(self.file_name, encoding='utf-8') as file:
            return json.load(file)

    def delete_data(self, vacancies):
        with open(self.file_name, "w", encoding='utf-8') as file:
            file.truncate()
