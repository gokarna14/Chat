import random
from useful_functions import strings
from data import add_data

class User:
    def __init__(self,OTN):
        self.one_time_number = OTN
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.username = ''
        self.email = ''
        self.phone_number = ''
        self.password = ''
        self.set_data()

    def set_name(self, firts_name='', last_name='', mn = ''):
        self.first_name = firts_name
        self.last_name = last_name
        self.middle_name = mn
        self.record()

    def set_username(self, username=''):
        self.username = username
        self.record()

    def set_email_phonenumber(self, email, phone_number):
        self.email = email
        self.phone_number = phone_number
        self.record()

    def set_password(self, password):
        self.password = password
        self.record()

    def show_identity(self):
        fr = open('data/users/user'+str(self.one_time_number)+'.txt', 'r')
        lines = fr.read().split('\n')
        print(f'''
        Full name       : {lines[1]} {lines[2]} {lines[3]}
        Username        : {lines[4]}
        Email           : {lines[5]}
        Phone number    : {lines[6]} 

        ''')
        fr.close()
        return self.first_name

    def record(self):
        fr = open('data/users/user'+str(self.one_time_number)+'.txt', 'w')
        fr.write(f'''{self.one_time_number}
{self.first_name}
{self.middle_name}
{self.last_name}
{self.username}
{self.email}
{self.phone_number} 
{self.password}
        ''')
        print('RECORDED !')
        fr.close()

    def set_data(self):

        fr = open('data/users/user' + str(self.one_time_number) + '.txt', 'r')
        lines = fr.read().split('\n')
        if not len(lines) <= 7:
            self.first_name = lines[1]
            self.middle_name =  lines[2]
            self.last_name =  lines[3]
            self.username =  lines[4]
            self.email =  lines[5]
            self.phone_number =  lines[6]
            self.password =  lines[7]
        fr.close()