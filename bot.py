from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import SpecificResponseAdapter
from rich.console import Console
from rich.table import Table
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

    if any(keyword in user_input_lower for keyword in ["cs", "computer science", "compsci", "comsci", "bscs"]):
        program = "CS"
    elif any(keyword in user_input_lower for keyword in ["coe", "computer engineering", "comeng", "compeng", "comp eng", "bscoe"]):
        program = "COE"
    elif any(keyword in user_input_lower for keyword in ["it", "information technology", "info tech", "information tech", "bsit"]):
        program = "IT"
    elif any(keyword in user_input_lower for keyword in ["act-mwd", "associate in computer technology with specialization in multimedia", "associate in comp tech w specialization in multimedia", "mwd", "multimedia"]):
        program = "ACT-MWD"
    elif any(keyword in user_input_lower for keyword in ["act", "associate in computer technology", "associate in comp tech"]):
        program = "ACT"

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
    elif program == "ACT":
        if semester == "all" and year == "all":
            return ACT_info["courses"]["ACT"]
        elif semester == "all":
            return (
                ACT_info["courses"]["ACT"][year]["first_sem"]
                + ACT_info["courses"]["ACT"][year]["second_sem"]
            )
        else:
            return ACT_info["courses"]["ACT"][year][semester]
    elif program == "ACT-MWD":
        if semester == "all" and year == "all":
            return ACT_MWD_info["courses"]["ACT-MWD"]
        elif semester == "all":
            return (
                ACT_MWD_info["courses"]["ACT-MWD"][year]["first_sem"]
                + ACT_MWD_info["courses"]["ACT-MWD"][year]["second_sem"]
            )
        else:
            return ACT_MWD_info["courses"]["ACT-MWD"][year][semester]
    else:
        return ACT_MWD_info["courses"]["ACT-MWD"][year][semester]

# Function to generate response containing subject names
def get_subject_names(subjects, program, year, semester):
    console = Console()
    if subjects:
        # response = f"Here are the {year} {semester} courses in {program}:\n"
        intro_message = f"EnrollmentBot: Here are the {year} {semester} courses in {program}:\n"
        console.print(intro_message)
        console = Console()
        table = Table()
        table.add_column("Subject", style="bold")
        table.add_column("Description", style="bold")

        for course in subjects:
            table.add_row(course['subject'], course['desc'])

        console.print(table)
    else:
        response = f"No courses found for {year} {semester} in {program}."

    return ""


def get_subject_names_all(subjects, program, semester, title):
    console = Console()
    
    # Print the introductory message
    intro_message = f"EnrollmentBot: Here are all the courses in {program}:"
    console.print(intro_message)
    
    # Display the table
    table = Table(title=title)  # Set the table title dynamically
    table.add_column("Year", style="bold")
    table.add_column("Semester", style="bold")
    table.add_column("Subject", style="bold")
    table.add_column("Description", style="bold")
    
    previous_year = None
    previous_semester = None
    
    for year, semesters in subjects.items():
        year = year.replace("first", "1ST").replace("second", "2ND").replace("third", "3RD").replace("fourth", "4TH")
        for semester, courses in semesters.items():
            semester = semester.replace("first_sem", "1ST SEM").replace("second_sem", "2ND SEM")
            for i, course in enumerate(courses):
                year_cell = year if year != previous_year else ""
                semester_cell = semester if semester != previous_semester else ""
                if i == 0:
                    table.add_row(year_cell, semester_cell, course['subject'], course['desc'])
                else:
                    table.add_row("", "", course['subject'], course['desc'])
                previous_year = year
                previous_semester = semester
        
        # Add row separator after each semester
        table.add_row("", "", "", "")
    
    # Add row separator after each year
    table.add_row("", "", "", "")
    
    console.print(table)
    
    return ""

def parse_process(user_input):
    process=""
    user_input_lower = user_input.lower()

    if any(keyword in user_input_lower for keyword in ["current"]):
        process = "CURRENT"
    elif any(keyword in user_input_lower for keyword in ["incoming", "freshmen"]):
        process = "INCOMING"
    elif any(keyword in user_input_lower for keyword in ["returnee", "returning"]):
        process = "RETURNING"
    elif any(keyword in user_input_lower for keyword in ["transferee"]):
        process = "TRANSFEREE"

    return process

def get_process(process):
    if process == "CURRENT":
        return MISC_info["process"]["CURRENT"]
    elif process == "INCOMING":
        return MISC_info["process"]["INCOMING"]
    elif process == "RETURNING":
        return MISC_info["process"]["RETURNING"]
    elif process == "TRANSFEREE":
        return MISC_info["process"]["TRANSFEREE"]
    else:
        return ""

def get_process_steps(process, steps):
    console = Console()
    if steps:
        # response = f"Here are the {year} {semester} courses in {program}:\n"
        intro_message = f"EnrollmentBot: Here is the Enrollment Procedure for {process} STUDENTS:\n"
        console.print(intro_message)
        console = Console()
        table = Table()
        table.add_column(f"Enrollment Procedures for {process} STUDENTS", style="bold")

        for process in steps:
            table.add_row(process['steps'])

        console.print(table)
    else:
        response = f"No procedure found for {steps} STUDENTS."

    return ""

CS_info = load_enrollment_info("cs.json")
COE_info = load_enrollment_info("coe.json")
IT_info = load_enrollment_info("it.json")
ACT_info = load_enrollment_info("act.json")
ACT_MWD_info = load_enrollment_info("act-mwd.json")
MISC_info = load_enrollment_info("misc.json")
PROGRAMS_info = load_enrollment_info("programs.json")

bot = ChatBot("EnrollmentBot",
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'Sorry, I do not understand. Please clarify your questions about SIT enrollment.',
                      'maximum_similarity_threshold': 0.2
                  },
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
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': 'courses',
                      'output_text': 'For what major would you like to know courses offered?'
                  },
                  {
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': 'enrollment',
                      'output_text': 'For information about enrollment process, please specify the major.'
                  }
              ])


trainer = ChatterBotCorpusTrainer(bot)

console = Console()

print("EnrollmentBot: Hi! How may I help you?")

while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)


    if any(keyword in user_input.lower() for keyword in ["current", "current student", "incoming", "incoming student", "freshmen", "returnee", "returning", "returning studnet"]):
        process = parse_process(user_input)
        steps = get_process(process)
        response = get_process_steps(process, steps)

    elif "process" and any(keyword in user_input.lower() for keyword in ["procedure", "steps", "process"]):
        print("For what enrollment process would you like to know: \n\tCurrent Student \n\tIncoming Student \n\tReturning Student \n\tTransferees")
        process_input = input("You: ")
        if any(keyword in process_input.lower() for keyword in ["current", "incoming", "freshmen", "returnee", "returning"]):
            process = parse_process(process_input)
            steps = get_process(process)
            response = get_process_steps(process, steps)
        else:
            print("EnrollmentBot: Please specify what enrollment process you are looking for")
            continue

    elif "summer" in user_input.lower():
        response = MISC_info["summer"]
        console.print("EnrollmentBot: ",response)

    elif "schedule" in user_input.lower():
        info = MISC_info["schedule"]
        response = ""
        for item in info:
            for key, value in item.items():
                response += f"{key}: {value}\n"
        console.print("EnrollmentBot: \n", response)
    
    elif any(keyword in user_input.lower() for keyword in ["programs", "programs offered", "SIT programs"]):
        response = "EnrollmentBot: Here are the programs offered by the SIT department:\n"
        table = Table()
        table.add_column("Program", style="bold")
        table.add_column("Description", style="bold")

        for program_code, description in PROGRAMS_info["programs"].items():
            table.add_row(program_code, description)

        console.print(response)
        console.print(table)

    elif any(keyword in user_input.lower() for keyword in ["cs", "computer science", "compsci", "comsci", "bscs",
                                                           "coe", "computer engineering", "comeng", "compeng", "comp eng", "bscoe",
                                                           "it", "information technology", "info tech", "information tech", "bsit",
                                                           "act", "associate in computer technology", "associate in comp tech",
                                                           "act-mwd", "associate in computer technology with specialization in multimedia", "associate in comp tech w specialization in multimedia", "mwd", "multimedia"
                                                           ]) and any(keyword in user_input.lower() for keyword in ["first", "second", "third", "fourth"]) or any(keyword in user_input.lower() for keyword in ["first sem", "second sem"]):

        program, year, semester = parse_user_input(user_input)
        subjects = get_subjects(program, year, semester)
        response = get_subject_names(subjects, program, year, semester)

    elif "courses" and any(keyword in user_input.lower() for keyword in ["subject", "curriculum"]):
        print("EnrollmentBot: For which major would you like to know courses offered?\nThe SIT department offers Information Technology (IT), Computer Science (CS), and Computer Engineering (CoE)")
        major = input("You: ") 
        if any(keyword in major.lower() for keyword in ["cs", "computer science", "compsci", "comsci", "bscs",
                                                           "coe", "computer engineering", "comeng", "compeng", "comp eng", "bscoe",
                                                           "it", "information technology", "info tech", "information tech", "bsit",
                                                           "act", "associate in computer technology", "associate in comp tech",
                                                           "act-mwd", "associate in computer technology with specialization in multimedia", "associate in comp tech w specialization in multimedia", "mwd", "multimedia"]):
            if not any(keyword in user_input.lower() for keyword in ["cs", "it", "coe"]):
                print("EnrollmentBot: Please clarify your inquiry or specify the program (CS, IT, COE).")
                continue
            else:
                program, year, semester = parse_user_input(major)
                subjects = get_subjects(program, year, semester)
                response = get_subject_names_all(subjects, program, semester, f"{major.upper()} Subjects for Curriculum 2023-2024")
        else:
            print("EnrollmentBot: Please specify a major.")
            continue
    else:
        print("EnrollmentBot:", response)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # CURRENT PROGRESS:
    # User can retrieve subject info by specifying the course, year, and sem (e.g. "cs first year first sem") or by specifying the course and year (e.g., cs first year)
    # User can retrieve subject info of a specific major by prompting "courses", [specific major]
    # Remove "EnrollmentBot: " after displaying tables (FIXED)


    # Include data about the enrollment process
        # If the user asks for the enrollment process and requirements, the bot should refer them to SIT Office (e.g., Please go to SIT Office. . .) (ADDED)
    
    # Include data about the schedule of enrollments for SY 2024-2025 (include upcoming short term)
        # The bot should refer them to the office or to the UB pages (e.g., Please go to this site and wait for announcements . . .) (ADDED)

    # Include responses that gives info about the program offered by SIT (ADDED)
        # ex. User: What are the programs offered?
        #     EnrollmentBot:    
        #                       BSCS - Bachelor of Science in Computer Science
        #                       BSIT - Bachelor of Science in Information Technology
        #                       BSCOE - Bachelor of Science in Computer Engineering
        #                       ASE - Applied Software Engineering
        #                       ACT-MWD - Associate in Computer Technology with Specialization in Multimedia and Web Development


    # THINGS TO DO:
    # Fix conditions(ADDED)
        # Instead of "cs first year first sem", what if the user inputs "first year first sem"? 
            #Possible Solutions:
            # 1. Bot: Please clarify your inquiry
            # 2. Bot: For what program are you asking for? (CS, IT, COE)
    # Add related keywords dun sa mga condition na pwedeng i-mention ng user. For example, instead of 'courses', they might input 'subjects' but still want to see the courses offered for a specific course
    

    # EXTRA THINGS TO DO:
    # Find a way to optimize the code since it's taking too long to retrieve the info. Tried asyncio pero parang ang hirap intindihin

    # TERMS:
        # COURSES/SUBJECTS - pertains to subjects (MATHMW1, CMARCH1, etc)
        # PROGRAM - BSCS, BSIT, BSCOE, ASE, ACT-MWD