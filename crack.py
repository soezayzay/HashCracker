import hashlib
import os,sys
#coder : $0ul
#date  : 14/2/2022
os.system("clear")
def banner():
    banner = """
                         \033[1;41m\033[1;37m Hash Cracker\033[0m\033[1;34m
                            
                    ▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
                    ▒▒█▒▒▒▄██████████▄▒▒▒▒
                    ▒█▐▒▒▒████████████▒▒▒▒
                    ▒▌▐▒▒██▄▀██████▀▄██▒▒▒
                    ▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
                    ▐┼▐▒▒██████████████▒▒▒
                    ▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
                    ▒▒█████──────────▐███▌
                    ▒▒█▀▀██▄█─▄───▐─▄███▀▒
                    ▒▒█▒▒███████▄██████▒▒▒
                    ▒▒▒▒▒██████████████▒▒▒
                    ▒▒▒▒▒█████████▐▌██▌▒▒▒
                    ▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
                    ▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒
                        \033[1;41m\033[1;37m Author : $0ul\033[0m\033[1;34m 
    \033[0m
    """
    print(banner)
#SHA-1
def sha1():
    hash_pass = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter SHA-1 password   \033[1;32m:\033[1;37m ")
    pass_list = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Password List    \033[1;32m:\033[1;37m ")
    print("")
    passwords = []
    password_list = open(pass_list,"r")
    pwlist = password_list.readlines()
    for password in pwlist:
        password = password.strip()
        passwords.append(password)
    #Password Cracking
    count = 1
    total = len(passwords)
    found = False
    for pw in passwords:
        encpw = pw.encode("utf-8")
        hashpass = hashlib.sha1(encpw).hexdigest()
        if hashpass == hash_pass :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
           found = True 
           break
        else :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
        count = count + 1   
    if found == True :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword Found!\033[0m")
       print(f" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mPassword \033[1;32m: \033[1;37m{pw}\033[0m")
    else :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword isn't is the list!\033[0m")
#SHA-256
def sha256():
    hash_pass = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter SHA-256 password \033[1;32m:\033[1;37m ")
    pass_list = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Password List    \033[1;32m:\033[1;37m ")
    print("")
    passwords = []
    password_list = open(pass_list,"r")
    pwlist = password_list.readlines()
    for password in pwlist:
        password = password.strip()
        passwords.append(password)
    #Password Cracking
    count = 1
    total = len(passwords)
    found = False
    for pw in passwords:
        encpw = pw.encode("utf-8")
        hashpass = hashlib.sha256(encpw).hexdigest()
        if hashpass == hash_pass :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
           found = True 
           break
        else :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
        count = count + 1   
    if found == True :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword Found!\033[0m")
       print(f" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mPassword \033[1;32m: \033[1;37m{pw}\033[0m")
    else :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword isn't is the list!\033[0m")
#SHA-512
def sha512():
    hash_pass = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter SHA-512 password \033[1;32m:\033[1;37m ")
    pass_list = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Password List    \033[1;32m:\033[1;37m ")
    print("")
    passwords = []
    password_list = open(pass_list,"r")
    pwlist = password_list.readlines()
    for password in pwlist:
        password = password.strip()
        passwords.append(password)
    #Password Cracking
    count = 1
    total = len(passwords)
    found = False
    for pw in passwords:
        encpw = pw.encode("utf-8")
        hashpass = hashlib.sha512(encpw).hexdigest()
        if hashpass == hash_pass :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
           found = True 
           break
        else :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
        count = count + 1   
    if found == True :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword Found!\033[0m")
       print(f" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mPassword \033[1;32m: \033[1;37m{pw}\033[0m")
    else :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword isn't is the list!\033[0m")
#md5
def md5():
    hash_pass = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter MD-5 password    \033[1;32m:\033[1;37m ")
    pass_list = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Password List   \033[1;32m :\033[1;37m ")
    print("")
    passwords = []
    password_list = open(pass_list,"r")
    pwlist = password_list.readlines()
    for password in pwlist:
        password = password.strip()
        passwords.append(password)
    #Password Cracking
    count = 1
    total = len(passwords)
    found = False
    for pw in passwords:
        encpw = pw.encode("utf-8")
        hashpass = hashlib.md5(encpw).hexdigest()
        if hashpass == hash_pass :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
           found = True 
           break
        else :
           print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;32m: \033[1;37m{total} \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mLoaded \033[1;32m: \033[1;37m{count:9} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Cracking  \033[1;36m==> \033[1;37m{pw}")
        count = count + 1   
    if found == True :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword Found!\033[0m")
       print(f" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mPassword \033[1;32m: \033[1;37m{pw}\033[0m")
    else :
       print("")
       print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mPassword isn't is the list!\033[0m")
def menu():
    print(" \033[1;34m(\033[1;31m1\033[1;34m) \033[1;33mSHA-1\033[0m")
    print(" \033[1;34m(\033[1;31m2\033[1;34m) \033[1;33mSHA-256\033[0m")
    print(" \033[1;34m(\033[1;31m3\033[1;34m) \033[1;33mSHA-512\033[0m")
    print(" \033[1;34m(\033[1;31m4\033[1;34m) \033[1;33mMD-5\033[0m")
    print("")
    option = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mChoose an option \033[1;32m      :\033[1;37m ")
    print("")
    if option == "1":
       sha1()
    elif option == "2":
       sha256()
    elif option == "3":
       sha512()
    elif option == "4":
       md5()
    else : 
      print(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;32mInvalid Option\033[0m")
      exit()
banner()
menu()
