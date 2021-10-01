# This is an example script for things that you can do with the ptero api.
# Made by MrRazamataz#6614 as an example for WitherHosting(.com) clients.
# Couldn't be bothered to make a proper command structure, so the trusty if/else will do for now.
# Install pydatyl correctly with `pip install py-dactyl==0.1.12` because newer versions are broken :(
from pydactyl import PterodactylClient
import urllib3
import json
import webbrowser
print("Loading config, logging in and checking version...")
f = open('config.json')
config = json.load(f)
apikey = config["ClientAPIkey"]
panellink = config["fullpanellink"]
f.close()
version = 0
try:
    version_url = "https://www.mrrazamataz.ga/archive/python/versions/pteroapi.txt"
    http = urllib3.PoolManager()
    response = http.request('GET', version_url)
    ver = response.data.decode('utf-8')
    vernum = int(ver)
    if vernum == version:
        print(f"You are running the latest version!")

    elif vernum < version:
        print("Your version number is corrupted (not matching online latest version, is bigger than online version), ignoring.")

    elif vernum > version:
        print(f"You are running an outdated version! Running: `{version}`, Latest: `{vernum}`.")
        print("An auto-update is not implemented in this script due to it being pointless for the context. Download the latest version if you so wish. ")
        webbrowser.open("https://github.com/MrRazamataz/pterodactyl-api-examples")


    else:
        print("An error occurred whilst checking the version, ignoring.")
except Exception as e:
    print(e)
    print("Version checker failed, ignoring and carrying on with the program.")
#print(f"pydactyl version is {pydactyl.__version__}, and it should be 0.1.12.")
serveramount = 0
client = PterodactylClient(panellink, apikey)

my_servers = client.client.list_servers()

for lines in my_servers:  # calc amount of servers
    serveramount = serveramount + 1

#srv_id = my_servers[0]['identifier']
serverrange = range(serveramount)
def helpcommand():
    print("The point of this script is to demo to the clients how to use the API, not to provide a full feature set. "
          "That being said, the commands are below.")
    print("Commands that are currently implemented:")
    print("`all servers on` - turns all servers on that you have access to")
    print("`all servers off` - turns all servers off that you have access to")
    print("`send command to all` - sends a command to all your servers")
    print("`help` - shows this")
def allserverson():
    for i in serverrange:
        srv_id = my_servers[i]['identifier']
        print(f"Turning on server with ID of `{srv_id}`!")
        client.client.send_power_action(srv_id, 'start')
def allserversoff():
    for i in serverrange:
        srv_id = my_servers[i]['identifier']
        print(f"Turning off server with ID of `{srv_id}`!")
        client.client.send_power_action(srv_id, 'stop')
def sendcommandtoall():
    command = input("Command: ")
    for i in serverrange:
        try:
            srv_id = my_servers[i]['identifier']
            print(f"Sending `{command}` to {srv_id}!")
            client.client.send_console_command(srv_id, command)
        except:
            srv_id = my_servers[i]['identifier']
            print(f"Server {srv_id} is offline!")
print(f"You have {serveramount} servers loaded in your panel.")
print("Run `help` for help.")
while True:
    # dont even come at me about this coding, its just an EXAMPLE. ok cool.
    simple_command_parse = input("> ")
    if simple_command_parse == "all servers on":
        allserverson()
    if simple_command_parse == "all servers off":
        allserversoff()
    if simple_command_parse == "help":
        helpcommand()
    if simple_command_parse == "send command to all":
        sendcommandtoall()

