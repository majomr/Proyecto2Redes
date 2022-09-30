import os

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def enter_to_continue():
    '''Press enter to continue, game stop'''
    input('\n\nPress enter to continue...')
    screen_clear()