import telebot
import pyjokes

TELEBOT_TOKEN = '166480857:AAGTJBWhXvjgvjmCWtxN8ZjjgVBwwKC-atY'

def start_telebot():
    tb = telebot.TeleBot(TELEBOT_TOKEN)

    @tb.message_handler(commands=["hello",])
    def hello_handler(message):
        tb.send_message(message.chat.id, "Hello %s!" % (message.from_user.first_name))
    
    @tb.message_handler(commands=["joke",])
    def joke_handler(message):
        joke = pyjokes.get_joke(language='en', category='neutral')
        tb.send_message(message.chat.id, joke)

    @tb.message_handler(commands=["chuckjoke",])
    def chuck_joke_handler(message):
        joke = pyjokes.get_joke(language='en', category='chuck')
        tb.send_message(message.chat.id, joke)

    @tb.message_handler(commands=["dir",])
    def dir_handler(message):
        items = ["{} -> {}".format(attr, getattr(message, attr)) for attr in dir(message)]
        tb.send_message(message.chat.id, '\n'.join(items)) 
    #Use none_stop flag let polling will not stop when get new message occur error.
    tb.polling()
    # Interval setup. Sleep 3 secs between request new message.
    #tb.polling(interval=3)

if __name__ == '__main__':
    start_telebot()