# Import Modules
import subprocess
import os 
from colorama import Fore


# Here You Can Put Your Window Title && Your Markdown
os.system("title Show Wifi Passwords By: !@A.I.T!@")
print(Fore.YELLOW + """
        A                                                                
        AAA                    IIIIIIIIII     TTTTTTTTTTTTTTTTTTTTTTT
        A:::A                   I::::::::I     T:::::::::::::::::::::T
        A:::::A                  I::::::::I     T:::::::::::::::::::::T
        A:::::::A                 II::::::II     T:::::TT:::::::TT:::::T
        A:::::::::A                  I::::I       TTTTTT  T:::::T  TTTTTT
        A:::::A:::::A                 I::::I               T:::::T        
        A:::::A A:::::A                I::::I               T:::::T        
        A:::::A   A:::::A               I::::I               T:::::T        
        A:::::A     A:::::A              I::::I               T:::::T        
        A:::::AAAAAAAAA:::::A             I::::I               T:::::T        
        A:::::::::::::::::::::A            I::::I               T:::::T        
        A:::::AAAAAAAAAAAAA:::::A           I::::I               T:::::T        
        A:::::A             A:::::A        II::::::II           TT:::::::TT      
        A:::::A               A:::::A       I::::::::I           T:::::::::T      
        A:::::A                 A:::::A      I::::::::I           T:::::::::T      
        AAAAAAA                   AAAAAAA     IIIIIIIIII           TTTTTTTTTTT      
"""+Fore.RESET)

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('cp1252').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for  i in profiles:
    results = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('cp1252').split('\n')
    results = [a.split(":")[1][1:-1] for a in results if "Key Content" in a]

    try:
        print(Fore.GREEN+"[+] {:<30}|   {:<}".format(i, results[0]))
    except:
        print(Fore.RED + "[-] {:<30}|   {:<}".format(i, ""))


input(Fore.YELLOW+"[*] Hit ENTER To Close: ")