from flask import Flask, jsonify
from main import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/get_groups", methods=["GET"])
def get_groups():
    return jsonify(groups)


@app.route("/group=<int:group_id>", methods=["GET"])
def get_group_schedule(group_id):
    return jsonify([group_schedule[0][group_id], group_schedule[1][group_id]])


def main():
    compute()
    app.run()


if __name__ == "__main__":
    main()
