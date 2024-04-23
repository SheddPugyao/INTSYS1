from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import SpecificResponseAdapter
import json

# Function to load enrollment information from JSON files
def load_enrollment_info(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to parse user input and extract program, year, and semester
def parse_user_input(user_input):
    program = ""
    year = "all"
    semester = "all"

    # Convert user input to lowercase for case-insensitive comparison
    user_input_lower = user_input.lower()

    if "cs" in user_input_lower:
        program = "CS"
    elif "coe" in user_input_lower:
        program = "COE"
    elif "it" in user_input_lower:
        program = "IT"

    if "first year" in user_input_lower:
        year = "first year"
    elif "second year" in user_input_lower:
        year = "second year"
    elif "third year" in user_input_lower:
        year = "third year"
    elif "fourth year" in user_input_lower:
        year = "fourth year"

    if "first sem" in user_input_lower:
        semester = "first_sem"
    elif "second sem" in user_input_lower:
        semester = "second_sem"

    return program, year, semester


# Function to get subjects based on program, year, and semester
def get_subjects(program, year, semester):
    if program == "CS":
        if semester == "all" and year == "all":
            return CS_info["courses"]["CS"]
        elif semester == "all":
            return (
                CS_info["courses"]["CS"][year]["first_sem"]
                + CS_info["courses"]["CS"][year]["second_sem"]
            )
        else:
            return CS_info["courses"]["CS"][year][semester]
    elif program == "COE":
        if semester == "all" and year == "all":
            return COE_info["courses"]["COE"]
        elif semester == "all":
            return (
                COE_info["courses"]["COE"][year]["first_sem"]
                + COE_info["courses"]["COE"][year]["second_sem"]
            )
        else:
            return COE_info["courses"]["COE"][year][semester]
    elif program == "IT":
        if semester == "all" and year == "all":
            return IT_info["courses"]["IT"]
        elif semester == "all":
            return (
                IT_info["courses"]["IT"][year]["first_sem"]
                + IT_info["courses"]["IT"][year]["second_sem"]
            )
        else:
            return IT_info["courses"]["IT"][year][semester]
    else:
        return IT_info["courses"]["IT"][year][semester]

# Function to generate response containing subject names
def get_subject_names(subjects, program, year, semester):
    if subjects:
        if semester == "all":
            response = f"\nHere are all courses in {year} {program}:\n"
            # Use a set to keep track of subjects already included
            included_subjects = set()
            for course in subjects:
                # Check if the subject has already been included
                if course['subject'] not in included_subjects:
                    response += f"\t{course['subject']} {course['desc']}\n"
                    included_subjects.add(course['subject'])
        else:
            response = f"\nHere are the {year} {semester} courses in {program}:\n"
            for course in subjects:
                response += f"\t{course['subject']} {course['desc']}\n"
    else:
        if semester == "all":
            response = f"No courses found for {year} in {program}."
        else:
            response = f"No courses found for {year} {semester} in {program}."
    return response

def get_subject_names_all(subjects, program, semester):
    response = f"\nHere are all courses in {program}:\n"
    for year, semesters in subjects.items():
        response += f"{year}:\n"
        for semester, courses in semesters.items():
            response += f"\t{semester}:\n"
            for course in courses:
                response += f"\t\t{course['subject']} {course['desc']}\n"
    return response

CS_info = load_enrollment_info("cs.json")
COE_info = load_enrollment_info("coe.json")
IT_info = load_enrollment_info("it.json")


bot = ChatBot("EnrollmentBot",
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': 'hello',
                      'output_text': 'Hi, I\'m EnrollmentBot. How can I help you with the SIT Enrollment?'
                  },
                  {
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': 'hi',
                      'output_text': 'Hi, I\'m EnrollmentBot. How can I help you with the SIT Enrollment?'
                  },
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'Sorry, I do not understand. Please clarify your questions about SIT enrollment.',
                      'maximum_similarity_threshold': 0.4
                  },
                  {
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': 'courses',
                      'output_text': 'For what major would you like to know courses offered?'
                  }
              ])

trainer = ChatterBotCorpusTrainer(bot)

print("Type something to begin...")

while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)

    # program, year, semester = parse_user_input(user_input)
    # print("Parsed input - Program:", program, "Year:", year, "Semester:", semester)
    
    # NOT WORKING - Goal: If the user inputs incomplete prompts (e.g., 'courses'), bot shall respond with "For what major would you like to know courses offered?". User must specify (e.g., "IT"), after that, the bot must provide all the subjects offered for IT
    if "courses" in user_input.lower():
        prompt = f"For what major would you like to know courses offered? \nThe SIT department offers Information Technology (IT), Computer Science (CS), and Computer Engineering (CoE)"
        print("Bot:", prompt)  
        major = input("You: ") 
        if any(keyword in major.lower() for keyword in ["cs", "coe", "it"]):
            program, year, semester = parse_user_input(major)
            subjects = get_subjects(program, year, semester)
            response = get_subject_names_all(subjects, program, semester)
        else:
            print("Please specify what major.")

    elif any(keyword in user_input.lower() for keyword in ["cs", "coe", "it"]) and any(keyword in user_input.lower() for keyword in ["first", "second", "third", "fourth"]) or any(keyword in user_input.lower() for keyword in ["first sem", "second sem"]):
        program, year, semester = parse_user_input(user_input)
        subjects = get_subjects(program, year, semester)
        response = get_subject_names(subjects, program, year, semester)
    
    print("Bot:", response)


# CURRENT PROGRESS:
    # User can get subjects offered by specifying the course, year, and sem (e.g. "cs first year first sem") or by specifying the course and year (e.g., cs first year)