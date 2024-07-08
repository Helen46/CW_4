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

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """
        метод для вывода топ ваканий
        :param vacancies: vacancies
        :param top_n: int
        :return: top vacancies
        """
        return vacancies[slice(top_n)]

    @staticmethod
    def filter_vacancies(vacancies, filter_words):
        """
        метод фильтрует вакансии по ключевым словам
        :param vacancies: list[dict]
        :param filter_words: str
        :return: list[dict]
        """
        vacancies_with_description = [
            vacancy
            for vacancy in vacancies
            if vacancy.get("description") is not None
        ]
        return [
            vacancy
            for vacancy in vacancies_with_description
            if filter_words in vacancy.get("description")
        ]

    @staticmethod
    def sort_vacancies(vacancies, min_salary, max_salary):
        return [
            vacancy
            for vacancy in vacancies
            if min_salary <= vacancy.get("salary_from", 0) <= max_salary
               and min_salary <= vacancy.get("salary_to", 0) <= max_salary
        ]

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from
