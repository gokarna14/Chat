from useful_functions import strings, list_
from data import add_data
import objects
import main_bot

OTN = 1
p = main_bot.Bot(OTN)
user_message = ''
print('Start conversation with simple hi or anything...')
message_counter = 0
while 1:
    user_message = input(' >> ').lower()
    message_counter += 1
    if user_message != '':
        p.user_message_recive(user_message)
        p.reply()