from rich.console import Console
from rich.table import Table
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from test_data import enrollment_data, enrollment_process_data, all_course, course_description

bot = ChatBot('EnrollmentBot')

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


while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        break
    response = None
    response_all = None
    program_input = None  # Initialize program_input

    # Check for specific user input related to enrollment process
    for process_data in enrollment_process_data:
        for process in process_data["process"]:
            if process.lower() in user_input:
                response = process_data["steps"]
                header = "Enrollment Process"
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
        bot_response = f"EnrollmentBot: Here's the {header}:"
        console.print(bot_response)
        table = Table(show_header=True)
        table.add_column(header) 

        for item in response:
            table.add_row(item)

        console.print(table)

    elif response_all:
        bot_response = f"EnrollmentBot: Here are the subjects offered under {header}:"
        console.print(bot_response)
        console = Console()
        if program_input:  # Check if the user requested subjects for a specific program
            header = f"{program_input.upper()}"
        else:
            print("All Subjetcs:")
        
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

#note
# query must only have this structure for year and sem: {first/second/third/fourth} year {first/seond} semester
# query must only have this structure for course: CS/IT/COE/ or yung full
# sample query: give me {first/second/third/fourth} year {first/seond} semester of IT


# Is there a way to optimize test_data.py? Naulit kasi yung enrollment_data tapos all_course
# Pa add nga yung entrance exam tapos tuition fee query
# ayaw lumabas nung course description