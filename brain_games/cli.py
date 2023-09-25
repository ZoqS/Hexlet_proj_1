import prompt
import datetime

def welcome_user() -> str:
    debug('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    welcome_message = f'Hello, {name}!'
    debug(welcome_message)
    return name


def debug(message):
    current_dat = datetime.datetime.now( )
    message_once = f"{current_dat}: {message}"
    print(message_once)

