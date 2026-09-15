import json
from pathlib import Path


# ---------------- LOAD SYLLABUS DATA ----------------

def load_syllabus_data():
    file_path = Path(__file__).resolve().parent.parent / "data" / "syllabus.json"

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


# ---------------- GET SEMESTERS ----------------

def get_semesters():
    data = load_syllabus_data()
    return list(data["semesters"].keys())


# ---------------- GET SUBJECTS ----------------

def get_subjects(semester_name):
    data = load_syllabus_data()

    semester = data["semesters"].get(semester_name)

    if not semester:
        return []

    subjects = []

    for subject in semester["subjects"]:
        subjects.append(subject["subject_name"])

    return subjects


# ---------------- GET UNITS ----------------

def get_units(semester_name, subject_name):
    data = load_syllabus_data()

    semester = data["semesters"].get(semester_name)

    if not semester:
        return []

    for subject in semester["subjects"]:

        if subject["subject_name"].lower() == subject_name.lower():

            units = []

            for unit in subject["units"]:

                # Skip non-dictionary entries
                if not isinstance(unit, dict):
                    continue

                for key, value in unit.items():

                    if key.startswith("unit_"):

                        units.append({
                            "unit_key": key,
                            "unit_title": value,
                            "topics": unit.get("Topics", [])
                        })

            return units

    return []


# ---------------- GET TOPICS ----------------

def get_topics(semester_name, subject_name, unit_key):

    units = get_units(semester_name, subject_name)

    for unit in units:

        if unit["unit_key"].lower() == unit_key.lower():
            return unit["topics"]

    return []


# ---------------- SEARCH TOPIC ----------------

def search_topic(keyword):

    data = load_syllabus_data()
    results = []

    for semester_name, semester in data["semesters"].items():

        for subject in semester["subjects"]:

            subject_name = subject["subject_name"]

            for unit in subject["units"]:

                if not isinstance(unit, dict):
                    continue

                unit_key = ""
                unit_title = ""

                for key, value in unit.items():

                    if key.startswith("unit_"):
                        unit_key = key
                        unit_title = value
                        break

                topics = unit.get("Topics", [])

                for topic in topics:

                    if keyword.lower() in topic.lower():

                        results.append({
                            "semester": semester_name,
                            "subject": subject_name,
                            "unit": unit_key,
                            "unit_title": unit_title,
                            "topic": topic
                        })

    return results