from rich.console import Console
from rich.table import Table

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from test_data import enrollment_data, enrollment_process_data

bot = ChatBot('EnrollmentBot')

trainer = ListTrainer(bot)

# Train the bot
for course in enrollment_data:
    for semester, subjects in course["subjects"].items():
        trainer.train(subjects)

for process in enrollment_process_data:
    trainer.train(process["steps"])

console = Console()

while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        break
    response = None

    # Check for subjects
    for course_data in enrollment_data:
        for course in course_data["course"]:
            if course.lower() in user_input:
                for semester, subjects in course_data["subjects"].items():
                    if semester.lower() in user_input:
                        response = subjects
    # Check for processes
    if not response:
        for process_data in enrollment_process_data:
            for process in process_data["process"]:
                if process.lower() in user_input:
                    response = process_data["steps"]

    if response:
        table = Table(title="Enrollment Bot")
        table.add_column("Response")

        for item in response:
            table.add_row(item)

        console.print(table)
    else:
        print("Bot: I'm sorry, I couldn't find information for that query. Please clarify.")


#note
# query must only have this structure for year and sem: {first/second/third/fourth} year {first/seond} semester
# query must only have this structure for course: CS/IT/COE/ or yung full
# sample query: give me {first/second/third/fourth} year {first/seond} semester of IT

