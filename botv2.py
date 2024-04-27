from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from enrollment_data import enrollment_queries, process_one, process_two, process_three, question, programs

bot = ChatBot('EnrollmentBot')

trainer = ListTrainer(bot)
trainer.train(enrollment_queries)
trainer.train(process_one)
trainer.train(process_two)
trainer.train(process_three)
trainer.train(question)
trainer.train(programs)


while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)
    
    response_str = str(response)
    
    response_lines = response_str.split("newline")
    print("EnrollmentBot: ", end="")
    for line in response_lines:
        print(line)

#possible queries: (from enrollment_data.py)
#Hi, I'm interested in enrolling for a program. What options do you have?
# What's the deadline for enrollment?
# Can you tell me about the reservation procedures for incoming freshmen?
# What are the admission requirements for incoming freshmen?
# Hi, I'm a new student. How do I enroll for courses?
# What are the subjects for Associate in Computer Technology in the first semester of the first year?
# What are the subjects for Multimedia and Web Design in the first semester of the first year?
# What are the subjects for Information Technology in the first semester of the first year?
# What are the subjects for Computer Engineering in the first semester of the first year?
# What are the subjects for Computer Science in the first semester of the first year?