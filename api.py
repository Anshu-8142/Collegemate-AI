import requests

API_URL = "http://127.0.0.1:5000"


def get_college_data():
    response = requests.get(f"{API_URL}/college")

    if response.status_code == 200:
        return response.json()

    return None


from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# ---------------- COLLEGE API ----------------

@app.route("/college")
def college():
    return jsonify(load_json("college.json"))


@app.route("/college/courses")
def courses():
    data = load_json("college.json")
    return jsonify(data["courses_and_branches"])


@app.route("/college/cse")
def cse_department():
    data = load_json("college.json")
    return jsonify(data["cse_department"])


@app.route("/college/facilities")
def facilities():
    data = load_json("college.json")
    return jsonify(data["facilities"])


@app.route("/college/academic")
def academic_information():
    data = load_json("college.json")
    return jsonify(data["academic_information"])


@app.route("/college/admission")
def admission_information():
    data = load_json("college.json")
    return jsonify(data["admission_information"])


@app.route("/college/faqs")
def faqs():
    data = load_json("college.json")
    return jsonify(data["faqs"])


# ---------------- SYLLABUS API ----------------

@app.route("/syllabus")
def syllabus():
    return jsonify(load_json("syllabus.json"))


@app.route("/syllabus/<semester>")
def semester_syllabus(semester):
    data = load_json("syllabus.json")

    semester_data = data["semesters"].get(semester)

    if semester_data is None:
        return jsonify({"error": "Semester not found"}), 404

    return jsonify(semester_data)


if __name__ == "__main__":
    app.run(debug=True)



