from rich.console import Console
from rich.table import Table
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from test_data import specific_subjects, all_subjects, enrollment_queries, program_queries, other_data

# Initialize ChatBot instance
bot = ChatBot('EnrollEase')

# Initialize ListTrainer
trainer = ListTrainer(bot)

# Concatenate all subjects from specific_subjects and all_subjects into a single list
all_subject_list = []
for course_data in specific_subjects + all_subjects:
    for subjects in course_data["subjects"].values():
        all_subject_list.extend(subjects)

# Train the bot with all subjects
trainer.train(all_subject_list)

# Train the bot with enrollment process steps
for process in enrollment_queries:
    trainer.train(process["steps"])

# Train bot for course description
for program_data in program_queries:
    trainer.train(program_data["desc"])

# Train bot for other data
for other in other_data:
    trainer.train(other["steps"])


console = Console()

def handle_user_input(user_input, console):
    response = None
    response_all = None
    program_input = None  # Initialize program_input

    greetings = ["hi", "hello", "hey"]
    if user_input in greetings:
        bot_response = "EnrollEase: Hi, I'm EnrollEase! How may I help you with the SIT Enrollment?"
        console.print(bot_response)
        return
    
    # Check for specific user input related to enrollment process
    for process_data in enrollment_queries:
        for process in process_data["process"]:
            if process.lower() in user_input:
                response = process_data["steps"]
                header = "Enrollment Process"
                bot_response = f"EnrollEase: Here's the {header}:"
                break
    
    #Check for other queries in user input
    for others in other_data:
        for data in others["process"]:
            if data.lower() in user_input:
                other_response = others["steps"]
                
    #check for program description in user input 
    for course_data in program_queries:
        for desc in course_data["about"]:
            if desc.lower() in user_input:
                response = course_data["desc"]
    

    # Check for subjects
    if not response:
        for course_data in specific_subjects:
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
        for course_all_data in all_subjects:
            for course in course_all_data["course"]:
                if course.lower() in user_input:
                    program_input = course  # Set program_input to the matched course
                    response_all = course_all_data["subjects"]
                    header = f"{course}"
                    break

    # Display subjects, enrollment process, course description
    if response:
        if "programs offered" in user_input:
            header = "SIT Programs"
        elif "admission requirements" in user_input:
            header = "Admission Requirements"
        elif "reservation" in user_input:
            header = "Reservation for Freshmen"
        elif "enrollment" in user_input:
            header = "Enrollment Process"
        else:
            header = "Course Description"
        bot_response = f"EnrollEase:"
        console.print(bot_response)
        table = Table(show_header=True)
        table.add_column(header) 

        for item in response:
            table.add_row(item)

        console.print(table)
    
    elif other_response:
         for item in other_response:
            bot_response = f"EnrollEase: {item}"
            console.print(bot_response)

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
        print("EnrollEase: I'm sorry, I couldn't find information for that query. Please clarify.")

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
    > entrance exam 

FOR PROGRAMS:
    > programs offered (e.g., Give me programs offered under SIT)
    > program description (e.g., What is BSCS)

FOR TUITION FEE:
    > tuition fee (e.g., How much is the tuition fee for . . . )

"""
