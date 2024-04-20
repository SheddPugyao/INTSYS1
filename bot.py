from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import json


def load_enrollment_info(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


CS_info_file = r"cs.json"
CS_info = load_enrollment_info(CS_info_file)

IT_info_file = r"it.json"
IT_info = load_enrollment_info(IT_info_file)

COE_info_file = r"coe.json"
COE_info = load_enrollment_info(COE_info_file)


bot = ChatBot('SIT Enrollment Bot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


def extract_enrollment_query(input_text, CS_info, IT_info, COE_info):
    input_text_lower = input_text.lower()

    program_keywords = {
        "CS": CS_info,
        "IT": IT_info,
        "COE": COE_info
    }

    for program, program_info in program_keywords.items():
        for year, year_info in program_info["keywords"].items():
            for semester, semester_keywords in year_info.items():
                # Check if all words in input_text_lower are in semester_keywords
                if any(keyword.lower() in input_text_lower for keyword in semester_keywords):
                    return program, year, semester

    return None, None, None

def get_courses(program, year, semester, CS_info, IT_info, COE_info):
    info = None
    if program == "CS":
        info = CS_info
    elif program == "IT":
        info = IT_info
    elif program == "COE":
        info = COE_info

    if not info:
        return []

    if year not in info["courses"].get(program, {}):
        return []

    if semester not in info["courses"][program].get(year, {}):
        return []

    return info["courses"][program][year][semester]


print("Type something to begin...")

while True:
    user_input = input("You: ")
    program, year, semester = extract_enrollment_query(user_input, CS_info, IT_info, COE_info)

    if program and year and semester:
        courses_info = get_courses(program, year, semester, CS_info, IT_info, COE_info)

        if courses_info:
            response = f"Here are the {year} {semester} courses in {program}:\n"
            for course in courses_info:
                response += f"{course['subject']} {course['desc']}\n"
        else:
            response = f"No courses found for {year} {semester} in {program}."
    else:
        response = bot.get_response(user_input)

    print("Bot:", response)
