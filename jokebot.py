import telebot
import pyjokes
import tweepy


TELEBOT_TOKEN = os.environ.get('TELEBOT_TOKEN', '') 
TW_CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY', '') 
TW_CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET', '') 


def start_telebot():
    tb = telebot.TeleBot(TELEBOT_TOKEN)
    consumer_key = TW_CONSUMER_KEY
    consumer_secret = TW_CONSUMER_SECRET
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

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

    @tb.message_handler(commands=["pycones15",])
    def get_pycones_handler(message):
        status_list = api.search(q="pycones15", count="10")
        status_text = u'\n'.join([st.text for st in status_list])
        tb.send_message(message.chat.id, status_text)
    #Use none_stop flag let polling will not stop when get new message occur error.
    print 'Polling...'
    tb.polling()
    # Interval setup. Sleep 3 secs between request new message.
    #tb.polling(interval=3)

if __name__ == '__main__':
    start_telebot()