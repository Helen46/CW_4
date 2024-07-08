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
