def logo():
    print('''
    __    __  __    __        __    __  __            
   / /_  / /_/ /____\ \      / /_  / /_/ /_____  _____
  / __ \/ __/ __/ __ \ \    / __ \/ __/ __/ __ \/ ___/
 / / / / /_/ /_/ /_/ /\ \  / / / / /_/ /_/ /_/ (__  ) 
/_/ /_/\__/\__/ .___/  \_\/_/ /_/\__/\__/ .___/____/  
             /_/                       /_/            
          
Mass Add http / https
Author: NuLz | Haxorstars
    ''')

def nulz(listnya, chose, domain):
    if chose == "http":
        http = "http://"
        fname = listnya+".saved-"+chose+".txt"
        for url in domain:
            resHttp = http+url
            saveHttp = open(fname, "a").write(str(resHttp+"\n"))
            print(resHttp + " => " + fname)
    elif chose == "https":
        https = "https://"
        fname = listnya+".saved-"+chose+".txt"
        for url in domain:
            resHttps = https+url
            saveHttp = open(fname, "a").write(str(resHttps+"\n"))
            print(resHttps + " => " + fname)

if __name__ == "__main__":
    logo()
    listnya = input("List > ")
    chose = input("http / https > ")
    domain = open(listnya, "r").read().splitlines()
    nulz(listnya, chose, domain)