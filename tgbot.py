import openai
import telebot
from decouple import config

# Set up the ChatGPT API
openai.api_key = config('OPEN_AI_KEY')

# Create a new bot object
bot = telebot.TeleBot(config('TELEGRAM_API_KEY'))

# Define a function to handle messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message is a command
    if message.text.startswith('/'):
        handle_command(message)
    elif message.text.startswith('..'):
        handle_text(message)

# Define a function to handle commands
def handle_command(message):
    command = message.text[1:].lower()
    if command == 'start':
        bot.reply_to(message, "Hello! Welcome to the hive mind.")
    elif command == 'help':
        bot.reply_to(message, "Here are some commands you can use: /start, /help, /info, /status, /hello")
    elif command == 'info':
        bot.reply_to(message, "This bot was created by The Strangers.")
    elif command == 'status':
        bot.reply_to(message, "You are connected to the hive mind.")
    elif command == 'hello':
        bot.reply_to(message, "Hello there my dear puppet!")
    else:
        bot.reply_to(message, "The hive mind doesn't obey your pitty request.")

# Define a function to handle text messages
def handle_text(message):
    # Call the ChatGPT API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=250,
        n=1,
        stop=None,
        timeout=10,
    )

    # Send the response back to the user
    bot.reply_to(message, response.choices[0].text)

# Start the bot
bot.polling()