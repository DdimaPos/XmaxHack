import random as rnd

import pandas as pd
from prettytable import PrettyTable

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1


class Data:
    cabinete = pd.read_csv("classrooms.csv")
    cabinete_lab = cabinete[cabinete['Sum of IS_LAB'] == 1]
    cabinete_lab = cabinete_lab.drop(['Sum of IS_LAB'], axis=1)
    cabinete_lab = cabinete_lab.values.tolist()

    cabinete_no_lab = cabinete[cabinete['Sum of IS_LAB'] == 0]
    cabinete_no_lab = cabinete_no_lab.drop(['Sum of IS_LAB'], axis=1)
    cabinete_curs = cabinete_no_lab[cabinete_no_lab['NO_PERSONS'] >= 70]
    cabinete_no_lab = cabinete_no_lab.values.tolist()
    cabinete_curs = cabinete_curs.values.tolist()

    #del later
    cabinete = cabinete.drop(['Sum of IS_LAB'], axis=1)
    cabinete = cabinete.values.tolist()
    #del later

    ROOMS = cabinete
    MeetingTimes = [
        ["M1", "Luni 08:00 - 9:30"],
        ["M2", "Luni 9:45 - 11:15"],
        ["M3", "Luni 11:30 - 13:00"],
        ["M4", "Luni 13:30 - 15:00"],
        ["M5", "Luni 15:15 - 16:45"],
        ["M6", "Luni 17:00 - 18:30"],
        ["M7", "Luni 18:45 - 20:15"]#,
        # ["M8", "Marti 08:00 - 9:30"],
        # ["M9", "Marti 9:45 - 11:15"],
        # ["M10", "Marti 11:30 - 13:00"],
        # ["M11", "Marti 13:30 - 15:00"],
        # ["M12", "Marti 15:15 - 16:45"],
        # ["M13", "Marti 17:00 - 18:30"],
        # ["M14", "Marti 18:45 - 20:15"],
        # ["M15", "Miercuri 08:00 - 9:30"],
        # ["M16", "Miercuri 9:45 - 11:15"],
        # ["M17", "Miercuri 11:30 - 13:00"],
        # ["M18", "Miercuri 13:30 - 15:00"],
        # ["M19", "Miercuri 15:15 - 16:45"],
        # ["M20", "Miercuri 17:00 - 18:30"],
        # ["M21", "Miercuri 18:45 - 20:15"],
        # ["M22", "Joi 08:00 - 9:30"],
        # ["M23", "Joi 9:45 - 11:15"],
        # ["M24", "Joi 11:30 - 13:00"],
        # ["M25", "Joi 13:30 - 15:00"],
        # ["M26", "Joi 15:15 - 16:45"],
        # ["M27", "Joi 17:00 - 18:30"],
        # ["M28", "Joi 18:45 - 20:15"],
        # ["M29", "Vineri 08:00 - 9:30"],
        # ["M30", "Vineri 9:45 - 11:15"],
        # ["M31", "Vineri 11:30 - 13:00"],
        # ["M32", "Vineri 13:30 - 15:00"],
        # ["M33", "Vineri 15:15 - 16:45"],
        # ["M34", "Vineri 17:00 - 18:30"],
        # ["M35", "Vineri 18:45 - 20:15"],
        # ["M36", "Sambata 08:00 - 9:30"],
        # ["M37", "Sambata 9:45 - 11:15"],
        # ["M38", "Sambata 11:30 - 13:00"],
        # ["M39", "Sambata 13:30 - 15:00"],
        # ["M40", "Sambata 15:15 - 16:45"],
        # ["M41", "Sambata 17:00 - 18:30"],
        # ["M42", "Sambata 18:45 - 20:15"]

        # "LMMJVS 9:45 - 11:15",
        # "LMMJVS 11:30 - 13:00",
        # "LMMJVS 13:30 - 15:00",
        # "LMMJVS 15:15 - 16:45",
        # "LMMJVS 17:00 - 18:30",
        # "LMMJVS 18:45 - 20:15"#,

        # "Marti 08:00 - 9:30",
        # "Marti 9:45 - 11:15",
        # "Marti 11:30 - 13:00",
        # "Marti 13:30 - 15:00",
        # "Marti 15:15 - 16:45",
        # "Marti 17:00 - 18:30",
        # "Marti 18:45 - 20:15",
        # "Miercuri 08:00 - 9:30",
        # "Miercuri 9:45 - 11:15",
        # "Miercuri 11:30 - 13:00",
        # "Miercuri 13:30 - 15:00",
        # "Miercuri 15:15 - 16:45",
        # "Miercuri 17:00 - 18:30",
        # "Miercuri 18:45 - 20:15",
        # "Joi 08:00 - 9:30",
        # "Joi 9:45 - 11:15",
        # "Joi 11:30 - 13:00",
        # "Joi 13:30 - 15:00",
        # "Joi 15:15 - 16:45",
        # "Joi 17:00 - 18:30",
        # "Joi 18:45 - 20:15",
        # "Vineri 08:00 - 9:30",
        # "Vineri 9:45 - 11:15",
        # "Vineri 11:30 - 13:00",
        # "Vineri 13:30 - 15:00",
        # "Vineri 15:15 - 16:45",
        # "Vineri 17:00 - 18:30",
        # "Vineri 18:45 - 20:15"
    ]
    professors = pd.read_csv("exportedSEM1(1).csv")
    professors = professors[['Profesori.ID', 'Profesori.NAME']].drop_duplicates()
    # pd.unique(professors['Profesori.ID'])
    # professors = professors[professors['Profesori.ID'].unique()]
    professors = professors.values.tolist()

    Teachers = professors

    def __init__(self):
        self._rooms = []
        self._teachers = []
        self._meeting_times = []

        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MeetingTimes)):
            self._meeting_times.append(MeetingTime(self.MeetingTimes[i][0], self.MeetingTimes[i][1]))
        for i in range(0, len(self.Teachers)):
            self._teachers.append(Teacher(self.Teachers[i][0], self.Teachers[i][1]))
        cursuri = pd.read_csv("exportedSEM1(1).csv")
        cursuri = cursuri[['ID', 'SUBJECT', 'TYPE', 'Profesori.NAME', 'Grupe.nr_persoane']]
        print(cursuri['TYPE'].unique())
        # if grupe.nr_persoane is null then if type is lab grupe.nr_persoane = 30
        cursuri.loc[cursuri['TYPE'] == 'teorie', 'Grupe.nr_persoane'] = cursuri['Grupe.nr_persoane'].fillna(70)
        cursuri['Grupe.nr_persoane'] = cursuri['Grupe.nr_persoane'].fillna(30)
        curs = {"number": [cursuri['ID']], "name": [cursuri['SUBJECT'] + " " + cursuri['TYPE']], "teachers": [cursuri["Profesori.NAME"]], "max_students": [cursuri['Grupe.nr_persoane']]}
        print("\n Curs")
        print(curs)
        course1 = Course("C1", "325K", [self._teachers[0], self._teachers[1]], 25)
        course2 = Course("C2", "319K", [self._teachers[0], self._teachers[1], self._teachers[2]], 35)
        course3 = Course("C3", "462K", [self._teachers[0], self._teachers[1]], 25)
        self._courses = [course1, course2]
        dept1 = Department("MATH", [course1, course2])
        dept2 = Department("EE", [course2, course3])
        self._depts = [dept1,dept2]
        self._number_of_classes = 0
        for i in range(0, len(self._depts)):
            self._number_of_classes += len(self._depts[i].get_courses())

    def get_rooms(self):
        return self._rooms

    def get_teachers(self):
        return self._teachers

    def get_meeting_times(self):
        return self._meeting_times

    def get_courses(self):
        return self._courses

    def get_depts(self):
        return self._depts

    def get_number_of_classes(self):
        return self._number_of_classes


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numb_of_conflicts = 0
        self._fitness = -1
        self._class_numb = 0
        self._is_fitness_changed = True

    def get_classes(self):
        self._is_fitness_changed = True
        return self._classes

    def get_numb_of_conflicts(self):
        return self._numb_of_conflicts

    def get_fitness(self):
        if self._is_fitness_changed == True:
            self._fitness = self.calculate_fitness()
            self._is_fitness_changed = False
        return self._fitness

    # add constraints
    def calculate_fitness(self):
        self._numb_of_conflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if classes[i].get_room().get_seating_capacity() < classes[i].get_course().get_max_students():
                self._numb_of_conflicts += 1
            for j in range(0, len(classes)):
                if j >= i:
                    if (
                        classes[i].get_meeting_time() == classes[j].get_meeting_time()
                        and classes[i].get_id() != classes[j].get_id()
                    ):
                        if classes[i].get_room() == classes[j].get_room():
                            self._numb_of_conflicts += 1
                        if classes[i].get_teacher() == classes[j].get_teacher():
                            self._numb_of_conflicts += 1
        return 1 / ((1.0 * self._numb_of_conflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ","
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                new_class = Class(self._class_numb, depts[i], courses[j])
                self._class_numb += 1
                new_class.set_meeting_time(
                    self._data.get_meeting_times()[rnd.randrange(0, len(self._data.get_meeting_times()))])
                new_class.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))])
                new_class.set_teacher(courses[j].get_teachers()[rnd.randrange(0, len(courses[j].get_teachers()))])
                self._classes.append(new_class)
        return self


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())

    def get_schedules(self):
        return self._schedules


class Course:
    def __init__(self, number, name, teachers, max_students):
        self.name = name
        self.number = number
        self.teachers = teachers
        self.max_students = max_students

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_teachers(self):
        return self.teachers

    def get_max_students(self):
        return self.max_students

    def __str__(self):
        return self.name


class Department:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses

    def __str__(self):
        return self.name


class DisplayMgr:
    def print_available_data(self):
        print("<---All Available Data--->")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_teacher()
        self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        available_depts_table = PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            temp_str = "["
            for j in range(0, len(courses) - 1):
                temp_str += courses[j].__str__() + ", "
            temp_str += courses[len(courses) - 1].__str__() + "]"
            available_depts_table.add_row([depts.__getitem__(i).get_name(), temp_str])
        print(available_depts_table)

    def print_course(self):
        courses = data.get_courses()
        available_courses_table = PrettyTable(['id', 'course #', 'max # of students', 'teacher'])
        for i in range(0, len(courses)):
            available_courses_table.add_row(
                [courses[i].get_number(), courses[i].get_name(), courses[i].get_max_students(),
                 courses[i].get_teachers()])
        print(available_courses_table)

    def print_room(self):
        rooms = data.get_rooms()
        available_rooms_table = PrettyTable(['room #', 'max seating capacity'])
        for i in range(0, len(rooms)):
            available_rooms_table.add_row([rooms[i].get_number(), rooms[i].get_seating_capacity()])
        print(available_rooms_table)

    def print_teacher(self):
        teachers = data.get_teachers()
        available_teachers_table = PrettyTable(['id', 'teacher'])
        for i in range(0, len(teachers)):
            available_teachers_table.add_row([teachers[i].get_id(), teachers[i].get_name()])
        print(available_teachers_table)

    def print_meeting_times(self):
        meeting_times = data.get_meeting_times()
        available_meeting_times_table = PrettyTable(['id', 'meeting times'])
        for i in range(0, len(meeting_times)):
            available_meeting_times_table.add_row([meeting_times[i].get_id(), meeting_times[i].get_time()])
        print(available_meeting_times_table)

    def print_generation(self, population):
        table1 = PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [dept,class,room,instructor,meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_numb_of_conflicts(), schedules[i]])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = PrettyTable(['Class #', 'Dept', 'Course (number, max # of students)', 'Room (Capacity)', 'Instructor (Id)', 'Meeting Time (Id)'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" + classes[i].get_course().get_number() + ", " + str(classes[i].get_course().get_max_students()) + ")",
                           classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_seating_capacity()) + ")",
                           classes[i].get_teacher().get_name() + " (" + str(classes[i].get_teacher().get_id()) + ")",
                           classes[i].get_meeting_time().get_time() + " (" + str(classes[i].get_meeting_time().get_id()) + ")"])
        print(table)


class Teacher:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def __str__(self):
        return self.name


class MeetingTime:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time

    def __str__(self):
        return self.time


class Room:
    def __init__(self, number, seating_capacity):
        self.number = number
        self.seating_capacity = seating_capacity

    def get_number(self):
        return self.number

    def get_seating_capacity(self):
        return self.seating_capacity

    def __str__(self):
        return self.number


class Class:
    def __init__(self, id, dept, course):
        self.id = id
        self.dept = dept
        self.course = course
        self.teacher = None
        self.meeting_time = None
        self.room = None

    def get_id(self):
        return self.id

    def get_dept(self):
        return self.dept

    def get_course(self):
        return self.course

    def get_teacher(self):
        return self.teacher

    def get_meeting_time(self):
        return self.meeting_time

    def get_room(self):
        return self.room

    def set_teacher(self, teacher):
        self.teacher = teacher

    def set_meeting_time(self, meeting_time):
        self.meeting_time = meeting_time

    def set_room(self, room):
        self.room = room

    def __str__(self):
        return f"{self.dept.get_name()} {self.course.get_number()} {self.room.get_number()} {self.teacher.get_id()} {self.meeting_time.get_id()}"


class GeneticAlgorithm:
    def evolve(self, population):
        return self.mutate_population(self.crossover_population(population))

    def crossover_population(self, population):
        crossover_population = Population(0)
        for i in range(0, NUMB_OF_ELITE_SCHEDULES):
            crossover_population.get_schedules().append(population.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self.select_tournament_population(population).get_schedules()[0]
            schedule2 = self.select_tournament_population(population).get_schedules()[0]
            crossover_population.get_schedules().append(self.crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_population

    def mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self.mutate_schedule(population.get_schedules()[i])
        return population

    def crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def select_tournament_population(self, population):
        tournament_population = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_population.get_schedules().append(
                population.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_population


data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
print("\n")
generation_number = 0
print("Generation # " + str(generation_number))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm()
while population.get_schedules()[0].get_fitness() != 1.0:
    generation_number += 1
    print("\n")
    print("Generation # " + str(generation_number))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])

print("\n\n")
print(data.cabinete)
print("\n\n")
print(data.cabinete_lab)
print("\n\n")
print(data.cabinete_curs)
print("\n\n")
print(data.cabinete_no_lab)
print("\n\n")
print(data.professors)
print("\n\n")
print(len(data.professors))
print("\n\n")
print(data.ROOMS)
print("\n\n")
