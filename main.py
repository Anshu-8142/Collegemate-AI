import threading
import time

from api import app

from ai.ai_assistant import college_ai, study_ai

from college.college_info import (
    get_basic_details,
    get_courses,
    get_cse_department,
    get_facilities,
    get_academic_information,
    get_admission_information,
    get_faqs
)

from study.study import (
    get_semesters,
    get_subjects,
    get_units,
    get_topics,
    search_topic
)

def start_api():
    app.run(debug=False, use_reloader=False)


    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()

    time.sleep(1)


# ---------------- STUDY FUNCTIONS ----------------

def show_study_info():

    print("\n===== Study Assistant =====")

    semesters = get_semesters()

    print("\nAvailable Semesters:")

    for i, semester in enumerate(semesters, start=1):

        semester_number = semester.replace("semester_", "")

        print(f"{i}. Semester {semester_number}")


def select_semester():

    semesters = get_semesters()

    while True:

        print("\nAvailable Semesters:")

        for i, semester in enumerate(semesters, start=1):

            semester_number = semester.replace("semester_", "")

            print(f"{i}. Semester {semester_number}")

        choice = input("\nEnter semester number: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(semesters):

                return semesters[number - 1]

        print("\nInvalid semester number. Please enter again.")


def select_subject(semester):

    subjects = get_subjects(semester)

    if not subjects:
        print("\nNo subjects found.")
        return None

    while True:

        print(f"\n===== Subjects =====")

        for i, subject in enumerate(subjects, start=1):
            print(f"{i}. {subject}")

        choice = input("\nEnter subject number: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(subjects):

                return subjects[number - 1]

        print("\nInvalid subject number. Please enter again.")


def select_unit(semester, subject):

    units = get_units(semester, subject)

    if not units:

        print("\nNo theory units available for this subject.")
        return None

    while True:

        print(f"\n===== Units =====")

        for i, unit in enumerate(units, start=1):

            print(f"{i}. {unit['unit_title']}")

        choice = input("\nEnter unit number: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(units):

                return units[number - 1]

        print("\nInvalid unit number. Please enter again.")


def show_topics(unit):

    topics = unit["topics"]

    if not topics:

        print("\nNo topics available.")
        return

    print("\n===== Topics =====")

    for i, topic in enumerate(topics, start=1):

        print(f"{i}. {topic}")


def search_syllabus(keyword):

    results = search_topic(keyword)

    print(f"\nSearch results for: {keyword}")

    if not results:

        print("No topic found.")
        return

    for result in results:

        print("\nSemester:", result["semester"])
        print("Subject:", result["subject"])
        print("Unit:", result["unit_title"])
        print("Topic:", result["topic"])


# ---------------- MAIN MENU ----------------

while True:

    print("\n======= CollegeMate AI =======")
    print("1. College Information")
    print("2. Study Assistant")
    print("3. Search Syllabus")
    print("4. Ask AI")
    print("5. Exit")

    choice = input("\nEnter your choice: ")


    # -------- COLLEGE INFORMATION --------

    if choice == "1":

        print("\n===== College Information =====")

        print("1. Basic Details")
        print("2. Courses & Branches")
        print("3. CSE Department")
        print("4. Facilities")
        print("5. Academic Information")
        print("6. Admission Information")
        print("7. FAQs")

        sub_choice = input("\nEnter your choice: ")

        if sub_choice == "1":
            print(get_basic_details())

        elif sub_choice == "2":
            print(get_courses())

        elif sub_choice == "3":
            print(get_cse_department())

        elif sub_choice == "4":
            print(get_facilities())

        elif sub_choice == "5":
            print(get_academic_information())

        elif sub_choice == "6":
            print(get_admission_information())

        elif sub_choice == "7":
            print(get_faqs())

        else:
            print("Invalid choice.")


    # -------- STUDY ASSISTANT --------

    elif choice == "2":
        # Select semester
        semester = select_semester()

        # Select subject
        subject = select_subject(semester)

        if subject is None:
            continue

        # Select unit
        unit = select_unit(semester, subject)

        if unit is not None:

            print(f"\nSelected Unit: {unit['unit_title']}")

            # Show topics
            show_topics(unit)


        # -------- STUDY AI --------

        print("\n===== Study AI =====")

        question = input("Ask your question: ")

        if question.strip() == "":
            print("Question cannot be empty.")
            continue

        answer = study_ai(question, semester)

        print("\nCollegeMate AI:")
        print(answer)


    # -------- SEARCH SYLLABUS --------

    elif choice == "3":

        keyword = input("\nEnter topic to search: ")

        if keyword.strip() == "":
            print("Please enter a topic.")
            continue

        search_syllabus(keyword)


    # -------- ASK AI --------

    elif choice == "4":

        question = input("\nAsk CollegeMate AI: ")

        if question.strip() == "":
            print("Question cannot be empty.")
            continue

        answer = college_ai(question)

        print("\nCollegeMate AI:")
        print(answer)


    # -------- EXIT --------

    elif choice == "5":

        print("\nThank you for using CollegeMate AI!")

        break


    else:

        print("\nInvalid choice. Please try again.")