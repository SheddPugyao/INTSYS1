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
