import csv
from prettytable import PrettyTable
from datetime import datetime


class StudentDatabase:
    """
    Klasa reprezentująca bazę danych studentów, umożliwiająca dodawanie,
    usuwanie studentów, zarządzanie ocenami, zapis i odczyt z pliku oraz
    śledzenie historii operacji.
    """

    def __init__(self):
        """
        Inicjalizacja bazy danych studentów.
        """
        self.students = []  # Lista studentów
        self.history = []  # Historia operacji

    def add_student(self, first_name, last_name, album_number):
        """
        Dodaje nowego studenta do bazy danych.

        :param first_name: Imię studenta.
        :param last_name: Nazwisko studenta.
        :param album_number: Numer albumu studenta.
        """
        self.students.append(
            {
                "Imię": first_name,
                "Nazwisko": last_name,
                "Numer albumu": album_number,
                "Oceny": {},
            }
        )
        self._log_history(f"Dodano studenta: {first_name} {last_name}")

    def remove_student(self, album_number):
        """
        Usuwa studenta z bazy danych na podstawie numeru albumu.

        :param album_number: Numer albumu studenta do usunięcia.
        """
        self.students = [
            s for s in self.students if s["Numer albumu"] != album_number]
        self._log_history(
            f"Usunięto studenta z numerem albumu: {album_number}")

    def display_students(self):
        """
        Wyświetla listę wszystkich studentów w bazie danych.
        """
        table = PrettyTable()
        table.field_names = ["Imię", "Nazwisko", "Numer albumu", "Oceny"]
        for student in self.students:
            grades = (
                ", ".join(
                    [f"{k}: {v}" for k, v in student["Oceny"].items()]) or "X"
            )
            table.add_row(
                [student["Imię"], student["Nazwisko"],
                    student["Numer albumu"], grades]
            )
        print(table)

    def add_grade(self, album_number, subject, grade):
        """
        Dodaje ocenę dla danego studenta.

        :param album_number: Numer albumu studenta.
        :param subject: Przedmiot, z którego dodawana jest ocena.
        :param grade: Ocena do dodania.
        """
        for student in self.students:
            if student["Numer albumu"] == album_number:
                student["Oceny"][subject] = grade
                self._log_history(
                    f"Dodano ocenę {grade} z {subject} dla {album_number}"
                )
                break

    # def save_to_file(self, filename):
    #     """
    #     Zapisuje bieżący stan bazy danych studentów do pliku CSV.

    #     :param filename: Nazwa pliku, do którego zostaną zapisani studenci.
    #     """
    #     with open(filename, "w", newline="") as file:
    #         writer = csv.DictWriter(
    #             file, fieldnames=["Imię", "Nazwisko", "Numer albumu", "Oceny"]
    #         )
    #         writer.writeheader()
    #         for student in self.students:
    #             student_copy = student.copy()
    #             student_copy["Oceny"] = ", ".join(
    #                 [f"{k}: {v}" for k, v in student["Oceny"].items()]
    #             )
    #             writer.writerow(student_copy)
    def save_to_file(self, filename):
        """
        Zapisuje bieżący stan bazy danych studentów do pliku CSV.
        :param filename: Nazwa pliku, do którego zostaną zapisani studenci.
        """
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["Imię", "Nazwisko", "Numer albumu", "Oceny"]
            )
            writer.writeheader()
            for student in self.students:
                student_copy = student.copy()
                student_copy["Oceny"] = ", ".join(
                    [f"{k}: {v}" for k, v in student["Oceny"].items()]
                )
                writer.writerow(student_copy)

    def load_from_file(self, filename):
        """
        Wczytuje stan bazy danych studentów z pliku CSV.

        :param filename: Nazwa pliku, z którego zostaną wczytani studenci.
        """
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            self.students = []
            for row in reader:
                row["Oceny"] = (
                    dict(item.split(": ") for item in row["Oceny"].split(", "))
                    if row["Oceny"]
                    else {}
                )
                self.students.append(row)

    def display_history(self):
        """
        Wyświetla historię ostatnich operacji wykonanych w bazie danych.
        """
        print("Ostatnie operacje:")
        for entry in self.history[-10:]:
            print(entry)

    def _log_history(self, action):
        """
        Loguje operację do historii operacji.

        :param action: Opis wykonanej operacji.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{timestamp}: {action}")


# Główna funkcja programu
def main():
    """
    Główna funkcja programu. Uruchamia interaktywne menu umożliwiające zarządzanie bazą danych studentów.
    """
    db = StudentDatabase()

    while True:
        print("\nMenu:")
        print("1. Dodaj studenta")
        print("2. Usuń studenta")
        print("3. Wyświetl studentów")
        print("4. Dodaj ocenę")
        print("5. Zapisz do pliku")
        print("6. Wczytaj z pliku")
        print("7. Wyświetl historię operacji")
        print("8. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            first_name = input("Podaj imię: ")
            last_name = input("Podaj nazwisko: ")
            album_number = input("Podaj numer albumu: ")
            db.add_student(first_name, last_name, album_number)
        elif choice == "2":
            album_number = input("Podaj numer albumu studenta do usunięcia: ")
            db.remove_student(album_number)
        elif choice == "3":
            db.display_students()
        elif choice == "4":
            album_number = input("Podaj numer albumu studenta: ")
            subject = input("Podaj nazwę przedmiotu: ")
            grade = input("Podaj ocenę: ")
            db.add_grade(album_number, subject, grade)
        elif choice == "5":
            filename = input("Podaj nazwę pliku do zapisu: ")
            db.save_to_file(filename)
        elif choice == "6":
            filename = input("Podaj nazwę pliku do wczytania: ")
            db.load_from_file(filename)
        elif choice == "7":
            db.display_history()
        elif choice == "8":
            print("Zakończenie programu.")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
