class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, name, description, salary_from, salary_to, salary_currency, link):
        self.name = name
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.link = link

    @classmethod
    def from_hh_dict(cls, data):
        """
        метод создает экземпляры вакансий с заданными атрибутами
        :param data: json файл
        :return: cls
        """
        name = data.get("name")
        description = data.get("snippet").get("requirement")
        salary = data.get("salary")
        salary_from = 0
        salary_to = 0
        salary_currency = None
        if salary:
            salary_from = salary.get("from", 0) if salary.get("from") is not None else 0
            salary_to = salary.get("to", 0) if salary.get("to") is not None else 0
            salary_currency = salary.get("currency")
        link = data.get("alternate_url")
        return cls(name, description, salary_from, salary_to, salary_currency, link)

    def to_dict(self):
        """
        метод для создания словаря вакансий в необходимом формате
        :return: dict
        """
        return {
            "name": self.name,
            "description": self.description,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "salary_currency": self.salary_currency,
            "link": self.link
        }
