from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from test_data import enrollment_data, enrollment_process_data

bot = ChatBot('EnrollmentBot')

trainer = ListTrainer(bot)

for course in enrollment_data:
    for semester, subjects in course["subjects"].items():
        trainer.train(subjects)

for process in enrollment_process_data:
    trainer.train(process["steps"])

while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        break
    response = None

    # subjects
    for course_data in enrollment_data:
        for course in course_data["course"]:
            if course.lower() in user_input:
                for semester, subjects in course_data["subjects"].items():
                    if semester.lower() in user_input:
                        response = subjects
    #process
    if not response:
        for process_data in enrollment_process_data:
            for process in process_data["process"]:
                if process.lower() in user_input:
                    response = process_data["steps"]

    if response:
        for item in response:
            print("Bot:", item)
    else:
        print("Bot: I'm sorry, I couldn't find information for that query. Please clarify.")

#note
# query must only have this structure for year and sem: {first/second/third/fourth} year {first/seond} semester
# query must only have this structure for course: CS/IT/COE/ or yung full
# sample query: give me {first/second/third/fourth} year {first/seond} semester of IT

