from flask import Flask, jsonify
from main import *
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
teachers_sheet = pd.read_csv("py/HackathonScrathDir-main/DataSheets/teachers.csv")
subjects_sheet = pd.read_csv("py/HackathonScrathDir-main/DataSheets/subjects.csv")
CORS(app)
@app.route("/get_groups", methods=["GET"])
def get_groups():
    return jsonify(groups)


@app.route("/group=<int:group_id>", methods=["GET"])
def get_group_schedule(group_id):
    print([group_schedule[0][group_id], group_schedule[1][group_id]])
    return jsonify([group_schedule[0][group_id], group_schedule[1][group_id]])

@app.route("/teachers", methods=["GET"])
def get_teachers():
    teachers = {}
    for i in range(len(teachers_sheet)):
        teachers[str(teachers_sheet["id"][i])] = str(teachers_sheet["name"][i])
    return jsonify(teachers)

@app.route("/subjects", methods=["GET"])
def get_subjects():
    subjects = {}
    for i in range(len(subjects_sheet)):
        subjects[str(subjects_sheet["id"][i])] = str(subjects_sheet["unitate_curs"][i])
    return jsonify(subjects)

def main():
    compute()
    app.run()


if __name__ == "__main__":
    main()