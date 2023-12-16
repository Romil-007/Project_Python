from colorama import Fore
from Project.Food_Ordering import *
from Project.Event_menu import *
from Project.dine_in_menu import *





def main():
    d = {1:food_menu,2:dine_in_menu,3:Events_menu,4:{}}
    print(Fore.RED , "\n\n           HEY WELCOME TO \n       HOTEL MANAGEMENT SERVICE ")
    ask = 5
    while(int(ask) not in d):
        ask = input(f"\n\n{Fore.GREEN}CHOOSE ONE OF THE FOLLOWING SERVICE TO USE : \n1.Food Ordering\n2.Dine-In\n3.Event\n4.Guide Manual\n : ")
        if(not(int(ask) in d)):
            print(Fore.RED,"\n\nERROR : WRONG INPUT TOKEN :(\nOOPS LOOKS LIKE YOU ARE TRYING TO ACCESS NON ACCESSIBLE ITEM")
    print(Fore.BLUE)
    d[int(ask)]()

    
    
    
    


main()