import requests
import os
import time
from pystyle import Colors, Colorate, Center, Write

banner = """
                            ██████╗ ██╗   ██╗██████╗ ██╗   ██╗
                            ██╔══██╗██║   ██║██╔══██╗╚██╗ ██╔╝
                            ██████╔╝██║   ██║██████╔╝ ╚████╔╝ 
                            ██╔══██╗██║   ██║██╔══██╗  ╚██╔╝  
                            ██║  ██║╚██████╔╝██████╔╝   ██║   
                            ╚═╝  ╚═╝ ╚═════╝ ╚═════╝    ╚═╝
                              The best webhook destroyer.
"""

options = """
[1] Delete Webhook
[2] Spam Webhook
[3] Credits
[4] Exit
"""

credits = """
Credits:
  Creator: Shiba (chleba124)
  GitHub: https://github.com/chleba124
"""

color_banner = Colorate.Horizontal(Colors.yellow_to_red, banner, 1)
colored_options = Colorate.Horizontal(Colors.blue_to_green, options, 1)
colored_credits = Colorate.Horizontal(Colors.purple_to_yellow, credits, 1)

def main():
    os.system('cls')
    os.system('title Ruby Multitool v1.0')
    print(Center.XCenter(color_banner))
    print()
    print(Center.XCenter(colored_options))

def delete():
    os.system('cls')
    print(Center.XCenter(color_banner))
    print()
    webhook = Write.Input("Webhook -> ", Colors.red_to_purple, interval=0.0025)
    os.system('cls')
    print(Center.XCenter(color_banner))
    print()

    try:
        requests.delete(webhook)
        print(Colorate.Horizontal(Colors.yellow_to_red, "Webhook has been destroyed.", 1))
    except requests.exceptions.RequestException as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Error: {e}", 1))

    os.system('cls')
    print(color_banner)
    print()
    name = Write.Input("Press enter to go back to the main menu.", Colors.green_to_cyan, interval=0.1)

def spam():
    os.system('cls')
    print(Center.XCenter(color_banner))
    print()
    webhook = Write.Input("Webhook -> ", Colors.red_to_purple, interval=0.0025)
    message = Write.Input("Message to spam -> ", Colors.blue_to_white, interval=0.0025)
    cooldown = Write.Input("Cooldown (in seconds) -> ", Colors.green_to_yellow, interval=0.0025)
    amount = Write.Input("Number of requests -> ", Colors.purple_to_red, interval=0.0025)
    
    os.system('cls')
    print(Center.XCenter(color_banner))
    print()

    try:
        for _ in range(int(amount)):
            data = {"content": message}
            requests.post(webhook, json=data)
            time.sleep(float(cooldown))
        print(Colorate.Horizontal(Colors.yellow_to_red, "Spam complete.", 1))
    except requests.exceptions.RequestException as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Error: {e}", 1))

    os.system('cls')
    print(color_banner)
    print()
    name = Write.Input("Press enter to go back to the main menu.", Colors.green_to_cyan, interval=0.1)

def display_credits():
    os.system('cls')
    print(Center.XCenter(color_banner))
    print()
    print(Center.XCenter(colored_credits))
    name = Write.Input("Press enter to go back to the main menu.", Colors.green_to_cyan, interval=0.1)

while True:
    main()
    choice = Write.Input("Enter your choice -> ", Colors.green_to_yellow, interval=0.0025)
    
    if choice == '1':
        delete()
    elif choice == '2':
        spam()
    elif choice == '3':
        display_credits()
    elif choice == '4':
        exit()
