from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

def load_enrollment_info(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def parse_user_input(user_input):
    program = ""
    year = ""
    semester = "all"

    if "cs" in user_input.lower():
        program = "CS"
    elif "coe" in user_input.lower():
        program = "COE"
    elif "it" in user_input.lower():
        program = "IT"

    if "first year" in user_input.lower():
        year = "first year"
    elif "second year" in user_input.lower():
        year = "second year"
    elif "third year" in user_input.lower():
        year = "third year"
    elif "fourth year" in user_input.lower():
        year = "fourth year"

    if "first sem" in user_input.lower():
        semester = "first_sem"
    elif "second sem" in user_input.lower():
        semester = "second_sem"

    return program, year, semester

def get_subjects(program, year, semester):
    if program == "CS":
        if semester == "all":
            return CS_info["courses"]["CS"]["first_sem"] + CS_info["courses"]["CS"][year]["second_sem"]
        else:
            return CS_info["courses"]["CS"][year][semester]
    elif program == "COE":
        if semester == "all":
            return COE_info["courses"]["COE"][year]["first_sem"] + COE_info["courses"]["COE"][year]["second_sem"]
        else:
            return COE_info["courses"]["COE"][year][semester]
    elif program == "IT":
        if semester == "all":
            return IT_info["courses"]["IT"][year]["first_sem"] + IT_info["courses"]["IT"][year]["second_sem"]
        else:
            return IT_info["courses"]["IT"][year][semester]



def get_subject_names(subjects):
    response =  f"\nHere are the {year} {semester} courses in {program}:\n"
    for course in subjects:
                response += f"\t{course['subject']} {course['desc']}\n"
    return response


CS_info = load_enrollment_info("cs.json")
COE_info = load_enrollment_info("coe.json")
IT_info = load_enrollment_info("it.json")

bot = ChatBot("EnrollmentBot")

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

print("Type something to begin...")

while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)

    if any(keyword in user_input.lower() for keyword in ["cs", "coe", "it"]) and any(keyword in user_input.lower() for keyword in ["first", "second", "third", "fourth"]) or any(keyword in user_input.lower() for keyword in ["first sem", "second sem"]):
        program, year, semester = parse_user_input(user_input)
        subjects = get_subjects(program, year, semester)
        subject_names = get_subject_names(subjects)
        # response = ", ".join(subject_names)

    print("Bot:", subject_names)