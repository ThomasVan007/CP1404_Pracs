usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
access = False
my_username = str(input("Please enter your username"))
for i in range(len(usernames)):
    if my_username == usernames[i]:
        access = True
if access == True:
    print("Access Granted")
else:
    print("Access Denied")