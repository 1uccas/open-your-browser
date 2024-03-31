import webbrowser as web
from colorama import Fore as Colors

class URL:
    GOOGLE = "https://google.com"
    TWITTER = "https://twitter.com"
    NETFLIX = "https://www.netflix.com/br/"
    AMAZON = "https://www.amazon.com.br/"
    INSTAGRAM = "https://www.instagram.com/"
    MAX = "https://www.max.com/br/pt"
    HELP = "https://docs.python.org/pt-br/3/library/webbrowser.html#"

def StringtoMenu():
    defaultString = (Colors.YELLOW + "-=")
    calcString = defaultString * 58
    
    string = (f"{calcString}\n" + Colors.GREEN + '''
 __    __   _______  __       __        ______      ____    __    ____   ______   .______       __       _______  
|  |  |  | |   ____||  |     |  |      /  __  \     \   \  /  \  /   /  /  __  \  |   _  \     |  |     |       \ 
|  |__|  | |  |__   |  |     |  |     |  |  |  |     \   \/    \/   /  |  |  |  | |  |_)  |    |  |     |  .--.  |
|   __   | |   __|  |  |     |  |     |  |  |  |      \            /   |  |  |  | |      /     |  |     |  |  |  |
|  |  |  | |  |____ |  `----.|  `----.|  `--'  |       \    /\    /    |  `--'  | |  |\  \----.|  `----.|  '--'  |
|__|  |__| |_______||_______||_______| \______/         \__/  \__/      \______/  | _| `._____||_______||_______/ 
                                                                                                                  
'''+f"{calcString}")
    return string
    
def optionMenu():
    option_not_found = (Colors.RED+"~ Error #$ option not found ~")
    openyourBrowser = (Colors.GREEN+"~ #$ Open Your Browser ~")
    
    print(f"{Colors.BLUE}"+'''
[1] ~ Twitter\t[4] ~ Instagram
[2] ~ Google\t[5] ~ Amazon
[3] ~ Netflix\t[6] ~ Max\t[7] ~ Help
''')
    option = int(input(Colors.RED+f"~> "))
    if option == 1:
        web.open(URL.TWITTER)
        print(openyourBrowser)
    elif option == 2:
        web.open(URL.GOOGLE)
        print(openyourBrowser)
    elif option == 3:
        web.open(URL.NETFLIX)
        print(openyourBrowser)
    elif option == 4:
        web.open(URL.INSTAGRAM)
        print(openyourBrowser)
    elif option == 5:
        web.open(URL.AMAZON)
        print(openyourBrowser)
    elif option == 6:
        web.open(URL.MAX)
        print(openyourBrowser)
    elif option == 7:
        web.open(URL.HELP)
        print(openyourBrowser)
    else:
        print(option_not_found)
print(StringtoMenu())
optionMenu()