import os, sys
from platform import system
from datetime import datetime as dt


if system() == 'Windows':
    from msvcrt import getch
else:
    sys.path.insert(0, './lib')
    from getch import getch


class Grades():
    def __init__(self):
        self.data: dict[ str, float | None ] = {
                'Programming': None,
                'Algorithms': None,
                'Math': None,
                'Phisics': None,
                }


class Student():
    def __init__(self, id, name, surname, grades: Grades | None = None):
        self.id = id
        self.name = name
        self.surname = surname
        self.grades = grades if grades is not None else Grades()

    def __str__(self):
        return f'{self.id}, {self.name} {self.surname}'

    def setGrades(self, grades: Grades):
        self.grades = grades

    def getGrades(self) -> Grades:
        return self.grades


class History():
    def __init__(self):
        self.path = 'history.txt'
        # self.limit = 10
        if not os.path.exists(self.path):
            with open(self.path, 'w') as _:
                pass

    def getHistory(self) -> list[str]:
        with open(self.path, 'r') as f:
            return [l for l in f.readlines() if l != '\n']

    def saveAction(self, s: str):
        time = dt.now().strftime("%H:%M:%S")
        action = f'{time}: {s}\n'
        with open(self.path, 'a') as f:
            f.write(action)


class Database():
    def __init__(self):
        self.records = []
        self.path = '   '
        if not os.path.exists(self.path):
            with open(self.path, 'w') as _:
                pass

    def getStudents(self):
        return self.records;

    def getStudentIdx(self, st: Student):
        return self.records.index(st)

    def getStudent(self, arg: Student | int) -> Student:
        if isinstance(arg, Student):
            return self.records[self.getStudentIdx(arg)]
        elif isinstance(arg, int):
            return self.records[arg]

    def addStudent(self, st: Student):
        self.records.append(st)

    def updateStudentGrades(self, arg: Student | int, grades: Grades):
        idx = -1
        if isinstance(arg, Student):
            idx = self.getStudentIdx(arg)
        elif isinstance(arg, int):
            idx = arg
        self.records[idx].setGrades(grades)

    def removeStudent(self, index: int):
        if index in range(len(self.records)):
            self.records.pop(index)

    def importFromCSV(self) -> bool:
        with open(self.path, 'r') as f:
            lines = f.read().splitlines()
            if len(lines) <= 1 or lines == None:
                return False

        new_records = []
        for l in lines[1::]:
            cells = l.split(',')

            grades = Grades()
            for i, subj in enumerate(grades.data.keys()):
                grade = cells[i+3]
                grades.data[subj] = float(grade) if grade != 'x' else None

            new_records.append(Student(cells[0], cells[1], cells[2], grades))
        self.records = new_records
        return True

    def exportToCSV(self):
        lines = []
        headers = f'id,name,surname,{",".join(list(Grades().data.keys()))}'
        lines.append(headers)

        for student in self.records:
            grades = [str(g) if g is not None else 'x' for g in student.getGrades().data.values()]
            line = f'{student.id},{student.name},{student.surname},{",".join(grades)}'
            lines.append(line)

        with open(self.path, 'w') as f:
            for line in lines:
                f.write(f'{line}\n')


class App():
    def __init__(self):
        self.CLEAR = 'cls' if system() == 'Windows' else 'clear'
        self.db = Database()
        self.hist = History()
        self.main_menu = {
                'Import CSV':     lambda: self.__importFromCSV(),
                'Export CSV':     lambda: self.__exportToCSV(),
                'History':        lambda: self.__showHistory(),
                'Show Students':  lambda: self.__showStudents(),
                'Add Student':    lambda: self.__addStudent(),
                'Remove Student': lambda: self.__removeStudent(),
                'Grade Student':  lambda: self.__gradeStudent(),
                'Exit':           lambda: self.__exit(),
                }

    def run(self):
        while True:
            keys = list(self.main_menu.keys())
            i = self.__menu(keys, 'Main Menu', True)
            self.main_menu[keys[i]]()

    def __menu(self, items: list, prompt = None, interactive = False):
        controlls = { 'j': 1, 'k': -1 }
        index = 0
        if not interactive:
            os.system(self.CLEAR)
            for i, item in enumerate(items):
                print(f'{item}')
            print()
            print('Press Enter..')
            while True:
                key = getch()
                if key == '\n':
                    break

        while (interactive):
            os.system(self.CLEAR)

            print("Move Down - 'j'\tMove Up - k\nSelect - Enter\n")
            if prompt is not None:
                print(prompt)

            for i, item in enumerate(items):
                prefix = '*' if i == index else ''
                print(f'{prefix} {item}')
            print()

            print('Press Enter..')
            key = getch()
            if key == '\n':
                break
            offset = 0
            if (n:=controlls.get(key)) is not None:
                offset = n

            index += offset
            index = 0 if index < 0 else index
            index = len(items) - 1 if index > len(items) - 1 else index
        return index

    def __showHistory(self):
        lines = self.hist.getHistory()
        self.__menu(lines)

    def __importFromCSV(self):
        if not self.db.importFromCSV():
            os.system(self.CLEAR)
            print('Database Empty\n')
            input('Press Enter..')
        self.hist.saveAction('Imported Data From CSV')

    def __exportToCSV(self):
        self.db.exportToCSV()
        self.hist.saveAction('Exported Data To CSV')

    def __showStudents(self):
        for student in self.db.getStudents():
            print(f'{student} - ', end='')
            for subject, grade in student.grades.data.items():
                print(f'{subject}: {"x" if grade is None else grade}', end=' ')
            print()
        input('\nPress Enter..')

    def __addStudent(self):
        print('Adding a student...\n')
        id = input('Album number:')
        name = input('Name:')
        surname = input('Surname:')

        new_student = Student(id, name, surname)
        self.db.addStudent(new_student)
        self.hist.saveAction(f'Added {name} {surname} To The Student List')

    def __removeStudent(self):
        s_idx = self.__selectStudent()
        if s_idx == -1:
            return
        s = self.db.getStudent(s_idx)
        self.db.removeStudent(s_idx)
        self.hist.saveAction(f'Removed {s.name} {s.surname} From The Student List')

    def __selectStudent(self) -> int:
        students = self.db.getStudents()
        if len(students) <= 0:
            print('No Students..')
            return -1
        i = self.__menu(students, 'Select Student', True)
        return i

    def __gradeStudent(self, st: Student | None = None):
        idx = -1
        if st is None:
            idx = self.__selectStudent()
        else:
            idx = self.db.getStudentIdx(st)

        if idx == -1:
            return

        grades = self.db.getStudent(idx).getGrades()

        for sub, grade in grades.data.items():
            os.system(self.CLEAR)
            print(f'Subject - {sub}')
            print(f'Current Grade - {grade if grade is not None else "x"}\n')
            print('-- Leave blank to skip the subject --')

            new_grade = None
            while True:
                grade = input('Input a grade: ').lstrip().rstrip()
                if grade.isnumeric():
                    new_grade = float(grade)
                    break
                elif grade == '':
                    break
            if new_grade is not None:
                grades.data[sub] = new_grade

        self.db.updateStudentGrades(idx, grades)
        st = self.db.getStudent(idx)
        self.hist.saveAction(f'Updated Grades Of a Student: {st.name} {st.surname} From The Student List')
        input('\nPress Enter..')

    def __exit(self):
        exit(0)


if __name__ == "__main__":
    App().run()
