from rich.console import Console
from rich.table import Table
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from test_data import enrollment_data, enrollment_process_data, all_course, course_description

# Initialize ChatBot instance
bot = ChatBot('EnrollEase')

# Initialize ListTrainer
trainer = ListTrainer(bot)

# Concatenate all subjects from enrollment_data and all_course into a single list
all_subjects = []
for course_data in enrollment_data + all_course:
    for subjects in course_data["subjects"].values():
        all_subjects.extend(subjects)

# Concatenate all course descriptions into a single list
all_descriptions = [desc["desc"] for desc in course_description]

# Train the bot with all subjects
trainer.train(all_subjects)

# Train the bot with all course descriptions
trainer.train(all_descriptions)

# Train the bot with enrollment process steps
for process in enrollment_process_data:
    trainer.train(process["steps"])

console = Console()

def handle_user_input(user_input, console):
    response = None
    response_all = None
    program_input = None  # Initialize program_input

    # Check for greetings
    greetings = ["hi", "hello", "hey"]
    if user_input in greetings:
        bot_response = "EnrollEase: Hi, I'm EnrollEase! How may I help you with the SIT Enrollment?"
        console.print(bot_response)
        return

    # Check for specific user input related to enrollment process
    for process_data in enrollment_process_data:
        for process in process_data["process"]:
            if process.lower() in user_input:
                response = process_data["steps"]
                header = "Enrollment Process"
                bot_response = f"EnrollEase: Here's the {header}:"
                break

    # Check for subjects
    if not response:
        for course_data in enrollment_data:
            for course in course_data["course"]:
                if course.lower() in user_input:
                    program_input = course  # Set program_input to the matched course
                    for semester, subjects in course_data["subjects"].items():
                        if semester.lower() in user_input:
                            response = subjects
                            program_name = course_data["course"][0].upper() 
                            semester_name = semester.upper() 
                            header = f"{program_name} - {semester_name} SUBJECTS"
                            break

    # Check for all subjects
    if not response:
        for course_all_data in all_course:
            for course in course_all_data["course"]:
                if course.lower() in user_input:
                    program_input = course  # Set program_input to the matched course
                    response_all = course_all_data["subjects"]
                    header = f"{course}"
                    break

    # Display subjects or enrollment process
    if response:
        if "programs offered" in user_input:
            header = "SIT Programs"
        elif "admission requirements" in user_input:
            header = "Admission Requirements"
        bot_response = f"EnrollEase:"
        console.print(bot_response)
        table = Table(show_header=True)
        table.add_column(header) 

        for item in response:
            table.add_row(item)

        console.print(table)

    elif response_all:
        bot_response = f"EnrollEase: Here are the subjects offered under {header}:"
        console.print(bot_response)
        if program_input:  # Check if the user requested subjects for a specific program
            header = f"{program_input.upper()}"
        else:
            print("All Subjects:")
        
        table = Table(show_header=True)
        table.add_column("Semester", style="cyan")
        table.add_column("Subjects")

        last_year = None  
        for semester, subjects in response_all.items():
            year, sem = semester.split()[:2]
            # Check if the year is different from the last one, add space if so
            if year != last_year:
                table.add_row("") 
                last_year = year
            table.add_row(semester, "\n".join(subjects))
        
        console.print(table)

    else:
        print("Bot: I'm sorry, I couldn't find information for that query. Please clarify.")

def main():
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("EnrollEase: Feel free to reach out for any further inquiries. Goodbye!")
            break
        handle_user_input(user_input, console)

if __name__ == "__main__":
    main()

# Queries:
"""
FOR SPECIFIC SUBJECTS:
    > [program] [year] [semester] subjects|courses (e.g., Give me cs first year first semester subjects)

FOR ALL SUBJECTS UNDER A SPECIFIC PROGRAM:
    > [program] (e.g., All subjects for cs)

FOR ENROLLMENT QUERIES: 
- This can handle questions about 
    > enrollment process|procedures|process
    > enrollment process for returning student|transferee|current students
    > admission requirements
    > admission requirements for incoming freshmen|transferee 
    > reservation for incoming freshmen
    > enrollment deadline|date
    > entrance exam (NOT YET ADDED)

FOR PROGRAMS:
    > programs offered (e.g., Give me programs offered under SIT)

FOR TUITION FEE: (NOT YET ADDED)
    > tuition fee (e.g., How much is the tuition fee for . . . )

"""
# Add entrance exam and tuition fee query
# Update ASE info
# Fix course description (it's not showing)
# Can the greetings be added to the training set?
