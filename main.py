from src.classes.hh_api import HH
from src.classes.vacancy import Vacancy
from src.classes.json_keeper import JSONKeeper


def main():

    hh_api = HH()

    def user_interaction():
        # platforms = ["HeadHunter"]
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
        min_salary, max_salary = input("Введите диапазон зарплат: ").split("-")  # Пример: 100000 - 150000

        vacancies = hh_api.load_vacancies(search_query)
        vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
        vacancies = [vacancy.to_dict() for vacancy in vacancies]

        filtered_vacancies = Vacancy.filter_vacancies(vacancies, filter_words)
        ranged_vacancies = Vacancy.sort_vacancies(filtered_vacancies, int(min_salary), int(max_salary))
        top_vacancies = Vacancy.get_top_vacancies(ranged_vacancies, top_n)

        json_file = JSONKeeper("vacancies.json")
        json_file.load_data(top_vacancies)

    if __name__ == "__main__":
        user_interaction()


if __name__ == "__main__":
    main()
