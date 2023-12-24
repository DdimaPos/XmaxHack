import json
import csv

group = json.load(open("group_table_sem1.json", "r"))
teacher = json.load(open("teacher_table_sem1.json", "r"))
rooms = json.load(open("rooms.json", "r"))

audit_rooms = ["5-1", "6-2"]
course_rooms = ["3-101", "3-104"]

for key, value in rooms.items():
    if value["capacity"] is None:
        if key in audit_rooms:
            value["capacity"] = 180
        elif key in course_rooms:
            value["capacity"] = 90
        else:
            value["capacity"] = 30


# print(teacher)

for day, lessons in teacher.items():
    if not any(lessons.values()):
        continue
    else:
        for lesson_name, details in lessons.items():
            if details:
                print(details)
                lesson_type = details["type"]
                print(f"{lesson_name} is a {lesson_type} lesson.")
                if lesson_type == "course":
                    # check capacity of room
                    for room, room_details in rooms.items():
                        if room_details["capacity"] >= 70:
                            details["room"] = room
                            break
                    # print(details["room"])

                elif lesson_type == "seminar":
                    # check capacity of room
                    for room, room_details in rooms.items():
                        # print(room_details["capacity"])
                        if 30 <= room_details["capacity"] < 50:
                            details["room"] = room
                            break
                elif lesson_type == "laboratory":
                    # check capacity of room
                    for room, room_details in rooms.items():
                        if room_details["capacity"] < 30:
                            details["room"] = room
                            break

print(teacher)

# save teacher to json
with open("teacher_table_sem1_rooms.json", "w") as f:
    json.dump(teacher, f, indent=4)


for gr, entries in group.items():
    for entry in entries:
        course_name = entry["course"]
        if course_name in teacher.get("1", {}):
            room = teacher["1"][course_name]["room"]
            entry["room"] = room
        else:
            # Handle the case when the course name is not found in data1
            entry["room"] = None

print(group)

# save group to json
with open("group_table_sem1_rooms.json", "w") as f:
    json.dump(group, f, indent=4)
