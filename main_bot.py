import random
import objects
from useful_functions import strings, list_, emoji
from data import add_data


class Bot:
    def __init__(self, OTN):
        self.one_time_number = OTN
        self.emotion_reset()
        self.main_user_name = ''
        self.name = 'Prabrobot'
        self.hello_messages = self.message_store('data/strings/hello_message.txt')
        self.sorry_messages = self.message_store('data/strings/sorry_message.txt')
        self.names = self.message_store('data/strings/names.txt')
        self.fpprn = self.message_store('data/pronoun/1p.txt')
        self.spprn = self.message_store('data/pronoun/2p.txt')
        self.tpprn = self.message_store('data/pronoun/3p.txt') + self.names
        self.first_message = True
        self.hello_message_deliver = False
        self.questions = self.message_store('data/learn/' + str(self.one_time_number) + 'question.txt')
        self.shortcut_message = ''
        self.ask_user_name = self.message_store('data/strings/user_ask_name.txt')
        self.ask_name_messages = self.message_store('data/questions/ask_name.txt')
        self.answers = self.message_store('data/learn/' + str(self.one_time_number) + 'answer.txt')

    def user_message_recive(self,user_message = ''):
        self.user_message = user_message
        self.ot_user_message = user_message
        if strings.return_alphabet(user_message) in list_.remove_number(self.questions):
            self.shortcut_message = self.answers[list_.remove_number(self.questions).index(strings.return_alphabet(user_message))]
            self.user_message = ''
        if self.user_message != '':
            self.reset()
            umessage_list = list_.remove_empty_member(user_message.split(' '))
            self.decide_emotion(umessage_list)
            self.decide_reffering(umessage_list)
        if self.user_message != '':
            self.process_message(umessage_list)
        if self.user_message != '':
            self.second_step_processing(user_message)
        if self.user_message != '':
            self.final_process_message()
        self.reply()

    def decide_reffering(self, umessage_list):
        name = ''
        pronoun = ''
        for elements in umessage_list:
            elements = strings.return_alphabet(elements)
            if elements in self.names:
                self.detect_name = True
            if (self.first_message or len(umessage_list) == 1) and strings.return_alphabet(elements) in self.hello_messages:
                self.first_message = False
                self.message = self.hello_message()
                self.hello_message_deliver = True
                self.user_message = ''
            else:
                self.hello_message_deliver = False
                pronoun = elements
                if self.detect_name:
                    name = elements
                if elements in self.fpprn:
                    self.fpr = True
                elif elements in self.spprn:
                    self.spr = True
                elif elements in self.tpprn:
                    self.tpr = True
                    pronoun = elements
        self.mname = name
        self.mpronoun = pronoun

    def process_message(self,user_message_words = []):
        if self.sad or self.afraid or self.angry or self.confused or self.depressed or self.helpless or self.hurt or self.indifferent or self.sad:
            self.unpleasant = True
        else:
            self.pleasant = True
        if self.unpleasant and (self.fpr or self.spr or self.tpr):
            if self.fpr:
                print('You are not feeling pleasant !')
            if self.tpr:
                if self.detect_name:
                 self.message = f'You said {self.mname} is feeling unpleasant'
                else:
                    self.message += f'You are talking about {strings.change_pronoun(pronoun)}'

        elif self.pleasant:
            pass


    def second_step_processing(self,user_message):
        if (self.universal_true('data/strings/user_ask_cemail.txt')
                or
            self.universal_true('data/strings/user_ask_add_email.txt')
        ):
            print('Do you want to change/add email ?')
            if self.yess():
                self.add_email()
            else:
                self.user_message = ''
            self.user_message = ''
        elif (self.universal_true('data/strings/delete information.txt')):
            print("Sorry you cannot do that but you can change your information as much as you want !")
            self.user_message = ''

        elif (self.universal_true('data/strings/user_ask_cphone.txt') or self.universal_true('data/strings/user_ask_add_phone.txt')):
           print('Do you want to change/add phone number ?')
           if self.yess():
               self.add_phone_number()
           else:
               self.user_message = ''
           self.user_message = ''
        elif (self.universal_true('data/strings/user_ask_cname.txt')):
           print('Do you want to change/add name ?')
           if self.yess():
               self.record_name()
           else:
               self.user_message = ''
           self.user_message = ''
        elif self.universal_true('data/strings/exit.txt'):
            print('Are you sure want to exit? ')
            if self.yess():
                exit()
            else:
                print('OK....I am glad')
                self.user_message = ''
            self.user_message = ''
        elif strings.string_in_string(strings.return_alphabet(user_message).lower(),
                                        list_.last_filter(self.ask_name_messages)):
                self.shortcut_message = (f'''My name is {self.name}, a chat bot.''')
                self.reply()
                p = objects.User(1)
                if p.first_name == '':
                    print('Do you want to record your name?')
                    if self.yess():
                        self.record_name()
                self.user_message = ''
        elif (strings.string_in_string(strings.return_alphabet(user_message).lower(), list_.last_filter(self.ask_user_name))
                                                                                     or
            self.universal_true('data/strings/user_ask_email.txt')
                                      or
            self.universal_true('data/strings/user_ask_phone.txt')):
            self.show_user_identity()
            self.user_message = ''


    def final_process_message(self, name = '', pronoun = ''):
        print(name)
        pronoun = self.mpronoun
        if not self.detect_name and not self.hello_message_deliver:
            print(f'''I dont know hot to respond this >> {self.user_message} << 
but you can teach me. Will you ?''')
            if self.yess():
                print(f'''So how would you answer this:
                > {self.user_message}
(please reply as if I am asking this question to you :))''')
                answer = input()
                print(f'''So,can we answer like:
     {self.user_message}   >>>   {answer}       ''')
                if self.yess():
                    try:
                        add_data.add('data/learn/' + str(self.one_time_number) + 'answer.txt', answer)
                        add_data.add('data/learn/' + str(self.one_time_number) + 'question.txt', self.user_message)
                        print('Done, I will remember from next time when you start again :) and thanks !')
                        print('Because I write data when I am in rest state ie. reboot the program for change to take effect')
                    except UnicodeEncodeError:
                        print("Error: No emojis acceptable")
            print('OK')


    def record_name(self):
        print(list_.random_return(self.ask_name_messages))
        name_ = input('Enter your full name: ')
        name_list = name_.split(' ')
        mn = ''
        if len(name_list) == 3:
            fn = name_list[0]
            mn = name_list[1]
            ln = name_list[2]
            print(f'Is this your name: {fn} {mn} {ln}')
        else:
            try:
                fn = name_list[0]
                ln = name_list[1]
                print(f'Is this your name: {fn} {ln}')
            except IndexError:
                ln = ''
                print(f'Is this your name: {fn} {ln}')

        if self.yess():
            self.main_user_name = f'{fn} {ln}'
            user = objects.User(1)
            user.set_name(fn, ln, mn)
            print('Do you have nickname which I can call  you?')
            if self.yess():
                user.set_username(input("Enter your nickname: "))
            else:
                user.set_username(fn + str(user.one_time_number))
        print('Do you want to see your information ?')
        if self.yess():
            p = objects.User(1)
            print(f'''Your information: {p.show_identity()}''')


    def decide_emotion(self,user_message_words = []):
        for word in user_message_words:
            if list_.string_present_bool(word, self.message_store('data/emotion/pleasant/alive.txt')):
                self.alive = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/pleasant/good.txt')):
                self.good = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/pleasant/happy.txt')):
                self.happy = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/pleasant/interested.txt')):
                self.interested = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/pleasant/love.txt')):
                self.love = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/pleasant/optimism.txt')):
                self.positive = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/pleasant/strong.txt')):
                self.strong = True
            if list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/afraid.txt')):
                self.afraid = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/angry.txt')):
                self.angry = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/confused.txt')):
                self.confused = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/depressed.txt')):
                self.depressed = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/helpless.txt')):
                self.helpless = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/hurt.txt')):
                self.hurt = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/indifferent.txt')):
                self.indifferent = True
            elif list_.string_present_bool(word, self.message_store('data/emotion/unpleasant/sad.txt')):
                self.sad = True


    def emotion_reset(self):
        self.pleasant = False
        self.alive = False
        self.good = False
        self.happy = False
        self.interested = False
        self.love = False
        self.optimism = False
        self.positive = False
        self.strong = False
        self.unpleasant = False
        self.afraid = False
        self.angry = False
        self.confused = False
        self.depressed = False
        self.helpless =False
        self.hurt = False
        self.indifferent = False
        self.sad = False


    def reply(self):
        if self.shortcut_message != '':
            self.message = self.shortcut_message
        ll = list_.remove_empty_member(self.message.split('\n'))
        if len(ll) > 0:
            l = ll[0].split(' ')
            l = emoji.emoji(l)
        else:
            l = ll
        self.message = ' '.join(l)
        if self.message != '':
            print(self.message)
        self.reset()
        return self.message


    def message_store(self,filename):
        fr = open(filename, 'r')
        a = fr.read().split('\n')
        fr.close()
        return a


    def hello_message(self):
        return list_.random_return(self.hello_messages)


    def sorry_message(self):
        return list_.random_return(self.sorry_messages)


    def reset(self):
        self.shortcut_message = ''
        self.fpr = False
        self.spr = False
        self.tpr = False
        self.message = ''
        self.detect_name = False


    def yess(self):
        if strings.string_in_string(strings.return_alphabet(input().lower()), list_.last_filter(self.message_store('data/strings/agree.txt'))):
            return True
        else:
            return False


    def noo(self):
        if strings.string_in_string(strings.return_alphabet(input().lower()), list_.last_filter(self.message_store('data/strings/disagree.txt'))):
            return True
        else:
            return False


    def add_email(self):
        p = objects.User(1)
        email = input('Enter your email address to add/change: ')
        p.set_email_phonenumber(email, p.phone_number)
        if p.phone_number == '\n':
            print('Do you wanna store phone number also?')
            if self.yess():
                p.set_email_phonenumber(email, input('Enter phone number: '))


    def add_phone_number(self):
        p = objects.User(1)
        phone = input('Enter your phone number to add/change: ')
        p.set_email_phonenumber(p.email, phone)
        if p.email == '':
            print('Do you wanna store email also?')
            if self.yess():
                p.set_email_phonenumber(input('Enter email address: '), p.phone_number)


    def show_user_identity(self):
        p = objects.User(1)
        print(f'Your information: {p.first_name}')
        p.show_identity()
        if 'change' in self.user_message.split(' '):
            print('''(Note: To change the information ask to change specefic information)
(Eg: To change name, Type: 'change name' or 'chnage my name' or something like this)
(Username cannot be changed, it is generated automatically after new name is given)''')

    def universal_true(self,filename):
        user_message = self.ot_user_message
        return strings.string_in_string(strings.return_alphabet(user_message).lower(), list_.last_filter(self.message_store(filename)))