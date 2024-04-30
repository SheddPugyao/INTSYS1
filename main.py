import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from rich.console import Console
from rich.table import Table

with open('subjects.json', 'r') as file:
    subjects_data = json.load(file)

with open('enrollment.json', 'r') as file:
    enrollment_info = json.load(file)

with open('programs.json', 'r') as file:
    programs_info = json.load(file)

chatbot = ChatBot(
    "EnrollmentBot",
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
            'input_text': 'subjects',
            'output_text': 'Sorry, I do not understand. Please clarify your questions about SIT enrollment.'
        }
    ]
)

# Functions to process enrollment procedure
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
        return enrollment_info["process"]["CURRENT"]
    elif process == "INCOMING":
        return enrollment_info["process"]["INCOMING"]
    elif process == "RETURNING":
        return enrollment_info["process"]["RETURNING"]
    elif process == "TRANSFEREE":
        return enrollment_info["process"]["TRANSFEREE"]
    else:
        return ""
    
def get_process_steps(process, steps):
    console = Console()
    if steps:
        intro_message = f"EnrollmentBot: Here is the Enrollment Procedure for {process} STUDENTS:\n"
        console.print(intro_message)
        console = Console()
        table = Table()
        table.add_column(f"Enrollment Procedures for {process} STUDENTS", style="bold")

        for process in steps:
            table.add_row(process['steps'])

<<<<<<< HEAD
        contact_table = Table(expand=True)
        contact_table.add_column("Contact US")
        contact_table.add_row(
            "For more information and for queries, please contact: \n\tUniversity of Baguio, General Luna Road, Baguio City \n\tsit@e.ubaguio.edu \n\t(074) 442-3036 \n\tOpen: 8:00 am - 5:00 pm")

        console.print(table)
        console.print(contact_table)
=======
        console.print(table)
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
    else:
        response = f"No procedure found for {steps} STUDENTS."

    return ""

# Function to handle enrollment schedule queries
def handle_enrollment_query(user_input):
    for keyword in ["schedule", "enrolment schedule", "enrollment schedule", "enrollment sched"]:
        if "summer" in user_input.lower():
                return enrollment_info["summer"]
        if keyword in user_input.lower():
            if "schedule" in user_input.lower():
                return enrollment_info["schedule"]
    return None

trainer = ListTrainer(chatbot)

console = Console()

programs_keywords = {
    "CS": ["cs", "computer science", "compsci", "comsci", "bscs"],
    "COE": ["coe", "computer engineering", "comeng", "compeng", "comp eng", "bscoe"],
    "IT": ["it", "information technology", "info tech", "information tech", "bsit"],
<<<<<<< HEAD
    "ASE": ["ase", "applied software engineering"],
=======
    "ACT": ["act", "associate in computer technology", "associate in comp tech"],
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
    "ACT-MWD": ["act-mwd", "associate in computer technology with specialization in multimedia", "associate in comp tech w specialization in multimedia", "mwd", "multimedia"]
}

print("EnrollmentBot: Hi! How can I help you with the SIT Enrollment?")
while True:
    user_input = input("You: ")

    if any(keyword in user_input.lower() for keyword in ["tuition", "tuition fee"]):
        print ("EnrollmentBot: For tuition fee information, please visit SIT Office, F Building, 2nd floor.")
    
    elif any(any(keyword in user_input.lower() for keyword in keywords) for keywords in programs_keywords.values()):
<<<<<<< HEAD
        subject = next((subj for subj in ["COE", "CS", "IT", "ACT-MWD", "ASE"] if any(keyword in user_input.lower() for keyword in programs_keywords[subj])), None)
=======
        subject = next((subj for subj in ["COE", "CS", "IT", "ACT-MWD", "ACT"] if any(keyword in user_input.lower() for keyword in programs_keywords[subj])), None)
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
        if subject:
            # Fetch subjects from the JSON data
            subjects = subjects_data["courses"][subject]
            
            intro_message = f"EnrollmentBot: Here are all the subjects in {subject}:"
            console.print(intro_message)
            
            # TABLE
            table = Table(title=f"{subject} Subjects\nEffective 2023-2024")
            table.add_column("Year", style="bold")
            table.add_column("Semester", style="bold")
            table.add_column("Course No.", style="bold")
            table.add_column("Description", style="bold")
            
            previous_year = None
            previous_semester = None
            
            for year, semesters in subjects.items():
                year = year.replace("first", "1st").replace("second", "2nd").replace("third", "3rd").replace("fourth", "4th")
                for semester, courses in semesters.items():
                    semester = semester.replace("first_sem", "1st Semester").replace("second_sem", "2nd Semester")
                    for i, course in enumerate(courses):
                        year_cell = year if year != previous_year else ""
                        semester_cell = semester if semester != previous_semester else ""
                        if i == 0:
                            table.add_row(year_cell, semester_cell, course['subject'], course['desc'])
                        else:
                            table.add_row("", "", course['subject'], course['desc'])
                        previous_year = year
                        previous_semester = semester
                
                # SEPARATOR
                table.add_row("", "", "", "")
<<<<<<< HEAD

            contact_table = Table(expand=True)
            contact_table.add_column("Contact US")
            contact_table.add_row(
                "For more information and for queries, please contact: \n\tUniversity of Baguio, General Luna Road, Baguio City \n\tsit@e.ubaguio.edu \n\t(074) 442-3036 \n\tOpen: 8:00 am - 5:00 pm")

            console.print(table)
            console.print(contact_table)
        else:
            print("EnrollmentBot: I'm sorry, I couldn't find information about that subject.")
    elif any(keyword in user_input.lower() for keyword in ["sit programs","program", "programs offered"]):
=======
            
            console.print(table)
        else:
            print("EnrollmentBot: I'm sorry, I couldn't find information about that subject.")
    elif any(keyword in user_input.lower() for keyword in ["sit programs","programs", "programs offered"]):
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
        response = "EnrollmentBot: Here are the programs offered by the SIT department:\n"
        table = Table()
        table.add_column("Program", style="bold")
        table.add_column("Description", style="bold")

        for program_code, description in programs_info["programs"].items():
            table.add_row(program_code, description)

        console.print(response)
<<<<<<< HEAD
        contact_table = Table(expand=True)
        contact_table.add_column("Contact US")
        contact_table.add_row(
            "For more information and for queries, please contact: \n\tUniversity of Baguio, General Luna Road, Baguio City \n\tsit@e.ubaguio.edu \n\t(074) 442-3036 \n\tOpen: 8:00 am - 5:00 pm")

        console.print(table)
        console.print(contact_table)
=======
        console.print(table)
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2

    elif "process" and any(keyword in user_input.lower() for keyword in ["procedure", "steps", "process"]):
        print("For which enrollment process would you like to know more?\n > Current Student\n > Incoming Student\n > Returning Student\n > Transferees")
        process_input = input("You: ")
        if any(keyword in process_input.lower() for keyword in ["current", "incoming", "freshmen", "returning", "transferees"]):
            process = parse_process(process_input)
            steps = get_process(process)
            response = get_process_steps(process, steps)
        else:
            print("EnrollmentBot: Please specify for which enrollment process you are looking for.")
            continue
    else:
        # Handle enrollment schedule queries
        enrollment_response = handle_enrollment_query(user_input)
        if enrollment_response:
            if isinstance(enrollment_response, list):
                print("EnrollmentBot:")
                table = Table(title="Enrollment Schedule")
                table.add_column("Year", style="bold")
                table.add_column("Schedule", style="bold")
                for item in enrollment_response:
                    for key, value in item.items():
                        table.add_row(key, value)
<<<<<<< HEAD
                contact_table = Table(expand=True)
                contact_table.add_column("Contact US")
                contact_table.add_row(
                    "For more information and for queries, please contact: \n\tUniversity of Baguio, General Luna Road, Baguio City \n\tsit@e.ubaguio.edu \n\t(074) 442-3036 \n\tOpen: 8:00 am - 5:00 pm")

                console.print(table)
                console.print(contact_table)
=======
                console.print(table)
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
            else:
                print("EnrollmentBot:", enrollment_response)
        else:
            response = chatbot.get_response(user_input)
            print("EnrollmentBot:", response)

<<<<<<< HEAD
=======


>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
#------------------------------------------------------------------------------------------
# SCOPE: 
    # Programs offered
    # Subjects offered per program
    # Enrollment process
    # Enrollment schedule

# LIMITATIONS:
    # Tuition fee inquiry
    # Unrelated SIT inquiries
    # Description for each subjects
<<<<<<< HEAD
    # Description for each programs(ADDED)

# TO FIX:
    # Change ACT to ASE; iba yung nakuha na data(DONE - except for the curriculum)
=======
    # Description for each programs

# TO FIX:
    # Change ACT to ASE; iba yung nakuha na data
>>>>>>> 23be54cda6d4ce0e84fddb3c3f93b547caeeb1a2
