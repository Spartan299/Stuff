import martypy, keyboard, time, sys

martydetails = []
details = {}
detailsItem = 0
chosen_one_ip = ""
subject = ""
chosen_one_found = 0

def print_marty_list():
    for marty in Martys:
        details = marty.keys()
        for key in details:
            details_ip = key[0]
            details_name = marty[key]
            print(details_name.decode("utf-8"))
            print("")
            
def select_marty():
    chosen_one = input('What is the name of your Marty? ')
    #print(chosen_one)
    for marty in Martys:
        details = marty.keys()
        for key in details:
            #print(key)
            details_ip = key[0]
            #print(details_ip)
            details_name = marty[key]
            #print(details_name)
            if details_name.decode("utf-8") == chosen_one:
                return details_name, details_ip
    return 0, "Nothing found"
    
print('Scanning...')
print('')
Martys = martypy.SocketClient.discover(timeout=10)

if len(Martys) == 0:
    print("No Martys Found :(")
    sys.exit()
else:
    if len(Martys) == 1:
        print("I found 1 Marty :)")
    else:
        print("I found " + str(len(Martys)) + " Martys :)")
    print("")
    if len(Martys) == 1:
        print("It's name is:")
    else:
        print("Their names are:")
    print('')
    print_marty_list()
    #chosen_one = input("What is the name of your Marty? ")
    chosen_one_name, chosen_one_ip = select_marty()
print(chosen_one_ip)
print()
print(f'{chosen_one_name.decode("utf-8")} selected')

'''
if chosen_one_found == 1:
    subject = martypy.Marty(url='socket://' + chosen_one_ip)
else:
    print('Error: Marty not Found')
    sys.exit()

subject = martypy.Marty(url='socket://192.168.8.216')
subject.buzz_prevention(enable=False)
subject.hello()
#def newWalk:
  #lean direction 1, lift foot 2, hip 1 back, hip 2 forward, foot 2 down, reverse
    
while True:
    if keyboard.is_pressed('w'):
        subject.walk(num_steps=2, move_time=1500)
        time.sleep(3)
    if keyboard.is_pressed('s'):
        subject.walk(num_steps=2, step_length=-40, move_time=1500)
        time.sleep(3)
    if keyboard.is_pressed('a'):
        subject.walk(step_length=0, num_steps=2, turn=100, move_time=1500)
        time.sleep(3)
    if keyboard.is_pressed('d'):
        subject.walk(step_length=0, num_steps=2, turn=-100, move_time=1500)
        time.sleep(3)
    if keyboard.is_pressed('q'):
        subject.move_joint(joint_id=7, move_time=500, position=-127)
        if current > 0.0055:
            print('Full Box')
        else:
            print('Empty box/No box')         
        hand = 1
        time.sleep(0.5)
    if keyboard.is_pressed('e'):
        subject.move_joint(joint_id=7, move_time=500, position=0)
        hand = 0
        time.sleep(0.5)
    current = subject.get_motor_current(7)
    #print(current)
'''
