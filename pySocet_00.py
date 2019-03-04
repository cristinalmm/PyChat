import os
import socket

target_ip = 'Target IP not set. Type "set ip <ip address> to set Target IP.'
port = 12345
s = '' #This should be a vairable used to set up the socket
is_server = False

def display_Banner():
    os.system('cls')
    print('-------------------------------------')
    print('  _____        _____ _           _   ')
    print(' |  __ \      / ____| |         | |  ')
    print(' | |__) |   _| |    | |__   __ _| |_ ')
    print(' |  ___/ | | | |    | \'_ \ / _` | __|')
    print(' | |   | |_| | |____| | | | (_| | |_ ')
    print(' |_|    \__, |\_____|_| |_|\__,_|\__|')
    print('         __/ |                       ')
    print('        |___/                        ')
    print('-------------------------------------')

def display_help(help_type):
    """Displays appropriate help menu for deffernt parts of the program. 
        In side of the chat room and outside where commands are needed.

    Attributes:
        help_type: a string that is used to disern the type of help menu
            that needs to be displayed.
    """
    print()
    if 'cmdPrompt' == help_type:
        print('{0:<12}|{1}'.format('help','Type "help" to display list of commands.'))
        print('{0:<12}|{1}'.format('enter','Enter the chat room.'))
        print('{0:<12}|{1}'.format('set ip','Type "set ip <ip address> to set Target IP.'))
        print('{0:<12}|{1}'.format('set server','Set this user as the host server.'))
        print('{0:<12}|{1}'.format('exit','Type "exit to exit from the program.'))
    elif 'chat' == help_type:
        print('{0:<10}|{1}'.format('help','Type "help" to display list of commands.'))
        print('{0:<10}|{1}'.format('exit','Type "exit to exit from the chat room.'))
    print()


def get_user_command():
    return input(' >> ')

def process_user_command(user_command):
    """Called outside of the chat room, this is where text will be 
        processed and the appropriate coresponding function calls will
        be made.

    'exit' should return a false so that the program ends
    'help' should call on a function to display a help menu
    'set ip' should set a TARGET ip that the user will connect to
    'set server' should set HOST as the hosting server
    'enter' should enter a chat room

    Attributes:
        user_command: this is string that is comparied to potential
            commands
    """
    if 'exit' == user_command.lower():
        return False
    elif 'help' == user_command.lower():
        display_help('cmdPrompt')
    elif 'enter' == user_command.lower():
        enter_chat_room()
    elif 'set ip'== user_command[0:6]:
        set_ip_target(user_command[7::])
    elif 'set server'== user_command:
        set_server()
    else:
         print('ERROR: command not recognized')
    
    return True


def set_ip_target(ip_string):
    """This function should set the IP address of the node that 
        the user wants to connect to.

    Attributes:
        ip_string: this is a string that contains an ip address
    """
    if 3 == ip_string.count('.'):
        global target_ip 
        target_ip = ip_string
        print( 'Target IP string set to {0}'.format( target_ip) )
    else:
        print('ERROR: invalid IP')


def set_server():
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """
    global s
    global port
    global is_server
    s = socket.socket()
    print ('Socket successfully created.')
    s.bind(('',port))
    print ("Socket binded to {0}".format(port))
    is_server = True
    


def get_chat_line():
    return input (' : ')

def process_chat_line(chat_line):
    if 'exit' == chat_line.lower():
        os.system('cls')
        display_Banner()
        return False
    elif 'help' == chat_line.lower():
        display_help('chat')
    '''
    Here will be where the user's message will be processed
    '''
    return True 


def enter_chat_room():
    os.system('cls')
    global s
    global port
    global target_ip
    chat_active = True
    if is_server:
        s.listen(5)
        print ("socket is listening...")
        c, addr = s.accept()
        print("Got connection from {0}".format(addr))
        c.send(b'Connected to host.') 
        while chat_active:
            print(c.recv(1024).decod())
            message = get_chat_line()
            if process_chat_line(message):
                c.send(str.encode(message))
            else:
                chat_active = False
        c.close()
    else:
        s = socket.socket()
        s.connect((target_ip, port) )
        while chat_active:
            print(s.recv(1024).decode() )
            message = get_chat_line()
            if process_chat_line(message):
                s.send(str.encode(message))
            else:
                chat_active = False

    while process_chat_line(get_chat_line()):
        continue


def run_Work_Space():
    display_Banner()
        
    while process_user_command(get_user_command()):
        continue



run_Work_Space()