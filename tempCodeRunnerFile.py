from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from enrollment_data import enrollment_queries
# Create a new instance of a ChatBot
bot = ChatBot('EnrollmentBot')

# Train the chatbot using list trainer
trainer = ListTrainer(bot)
trainer.train(enrollment_queries)

# Now, let's chat with the bot
while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)
    print("Bot: \n", response)
