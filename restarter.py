import subprocess,json,os,ctypes,requests
from time import sleep

def clear():
    os.system('cls')
    sleep(1)
    check()

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    pn_lower = process_name.lower()
    return last_line.lower().startswith(pn_lower)

def open():
    os.startfile("Cry.ConsoleApp.exe")

def check():
    ctypes.windll.kernel32.SetConsoleTitleW("Made by LiteEagle262 | liteeagle.me")
    print("""
            ██████╗ ███████╗███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██████╗ 
            ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
            ██████╔╝█████╗  ███████╗   ██║   ███████║██████╔╝   ██║   █████╗  ██████╔╝
            ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
            ██║  ██║███████╗███████║   ██║   ██║  ██║██║  ██║   ██║   ███████╗██║  ██║
            ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                        
                    https://github.com/LiteEagle262/Viridian-Crash-Restarter                           
    """)
    while process_exists("Cry.ConsoleApp.exe") == True:
        sleep(5)
        pass
    else:
        if os.path.exists("players.txt") == True:
            os.remove("players.txt")
            open()
            clear()
            print("Restarted.")
        else:
            open()
            clear()
            print("Restarted.")
check()