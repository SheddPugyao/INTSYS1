from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

def load_enrollment_info(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

subjects_file = "subjects.json"
programs_file = "programs.json"

all_info = load_enrollment_info(subjects_file)
programs_info = load_enrollment_info(programs_file)

chatbot = ChatBot("MyChatBot")

trainer = ListTrainer(chatbot)

for course_info in all_info.values():
    for course, course_details in course_info.items():
        for year, year_info in course_details.items():
            for semester, subjects in year_info.items():
                subject_list = ", ".join(subject['desc'] for subject in subjects)
                trainer.train([f"What subjects are there for the {semester} semester of {course}?", subject_list])
                trainer.train([f"What are the subjects for {semester} semester of {year} year {course}?", subject_list])
                trainer.train([f"List the subjects for {semester} semester of {year} year {course}.", subject_list])

for program, description in programs_info.get('programs', {}).items():
    trainer.train([f"What is {program}?", description])
    trainer.train([f"What is the full name of {program}?", description])
    trainer.train([f"What does {program} stand for?", description])


def chat():
    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Bot:", response)

chat()
