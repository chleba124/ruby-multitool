import requests
import os
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

color_banner = Colorate.Horizontal(Colors.yellow_to_red, banner, 1)

def main():
    os.system('cls')
    os.system('title Ruby Multitool v1.0')
    print(Center.XCenter(color_banner))
    print()
    webhook = Write.Input("Webhook -> ", Colors.red_to_purple, interval=0.0025)
    os.system('cls')
    print(Center.XCenter(color_banner))
    print()
    requests.delete(webhook)
    print(Colorate.Horizontal(Colors.yellow_to_red, "Webhook has been destroyed.", 1))
    os.system('cls')
    print(color_banner)
    print()
    name = Write.Input("Press enter to go back to the main menu.", Colors.green_to_cyan, interval=1)


while True:
    main()
