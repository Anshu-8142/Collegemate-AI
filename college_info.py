import json

def load_college_data():
    with open("data\college.json", "r") as f:
        data = json.load(f)

    return data

def get_basic_details():
    data = load_college_data()

    return data["basic_details"]

def get_courses():
    data = load_college_data()

    return data["courses_and_branches"]

def get_cse_department():
    data = load_college_data()

    return data["cse_department"]

def get_facilities():
    data = load_college_data()

    return data["facilities"]

def get_academic_information():
    data = load_college_data()

    return data["academic_information"]

def get_admission_information():
    data = load_college_data()

    return data["admission_information"]

def get_faqs():
    data = load_college_data()

    return data["faqs"]