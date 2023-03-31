print("""
      
      Welcome to my game to find the keyword. Use hints and then find the word! 
      
      You can use cd, cat and ls commands to see hints!
      
      Good luck! 

      """)
door = True

import subprocess



def game():
    print("Game is starting. Let's see your commands")
    command = ""
    second_err = ""
    second_out = ""
    proc = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.decode('utf-8').replace("\n", "")
    while door:
        new_command = input(out + " > ")
        if not second_err:
            if new_command.find('cd') == 0:        
                command = command + "\n" + new_command + "\n"
                proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
                proc_pwd = subprocess.Popen([command + "\n" +"pwd"], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc_pwd.communicate()
                out = out.decode('utf-8').replace("\n", "")
            else:
                proc = subprocess.Popen([command + "\n" + new_command + "\n"], stdout=subprocess.PIPE, shell=True)
        (second_out, second_err) = proc.communicate()
        if second_out:
            second_out = second_out.decode('utf-8')
            print(second_out)
        if second_err:
            second_err = second_err.decode('utf-8')
            print(second_err)


game()

# starting_game = ""
# while starting_game.lower() != 'q':
#     starting_game = input("Do you want to start. Please type y or Y. Otherwise q or Q to exit\n:").lower()
#     if starting_game == 'y':
#         starting_game = "q"
#         game()
#     elif starting_game == 'q':
#         starting_game = "q"
#         print('Bye bye')
#     else:
#         print('Please enter correct answer according to the question \n')

# while True:
#     input('Please enter a name: ')
#     print('Hello')