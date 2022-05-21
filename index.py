import pystyle;import requests;import os;from pystyle import *;import time
banner1 = '''

__      __           _     _               _          __  __                    __ _                 
\ \    / / ___  ___ | |__ | |_   ___  ___ | |__      |  \/  | __ _  _ _   __ _ / _` | ___  _ _       
 \ \/\/ / / -_)/ -_)|  _ \|   \ / _ \/ _ \| / /      | |\/| |/ _` || ' \ / _` |\__. |/ -_)| '_|      
  \_/\_/  \___|\___||____/|_||_|\___/\___/|_\_\      |_|  |_|\__/_||_||_|\__/_||___/ \___||_|        






                                    [ PRESS ENTER FOR OPEN THE TOOL ]




                                                                            by Wolf..#0001


'''
banner2 = Colorate.Horizontal(Colors.purple_to_blue, '''
                      __      __           _     _               _          __  __                    __ _                 
                      \ \    / / ___  ___ | |__ | |_   ___  ___ | |__      |  \/  | __ _  _ _   __ _ / _` | ___  _ _       
                       \ \/\/ / / -_)/ -_)|  _ \|   \ / _ \/ _ \| / /      | |\/| |/ _` || ' \ / _` |\__. |/ -_)| '_|      
                        \_/\_/  \___|\___||____/|_||_|\___/\___/|_\_\      |_|  |_|\__/_||_||_|\__/_||___/ \___||_|     
  ''', 1)
menu1 = Colorate.Horizontal(Colors.purple_to_blue,'''


                                [1] Envoyez un message              [2] Suprimer              [3] Spam



                                [4] Info                            




''', 1)
mode = [1,2,3,4,5]
System.Clear();System.Title("Weebhook-Manager");System.Size(150, 40);Anime.Fade(text=Center.Center(banner1), color=Colors.purple_to_blue, mode=Colorate.Diagonal, enter=True)
while True:
  System.Clear();System.Size(150, 40);print(banner2,'\n'*3,menu1,'\n'*1);choice1 = Write.Input("[?]>", Colors.red)
  if choice1 == "1":
    webhook = input("webhook URL :");msg = input("message :");username = input("Entre le nom du webhook (vide = celui de base) :");data = {"content" : msg,"username" : username};result = requests.post(webhook, json = data)
    try:
      result.raise_for_status()
    except requests.exceptions.HTTPError as err:
      print(err)
    else:
      print(Colorate.Color(Colors.green, "Message envoyez avec succès !", True))
      time.sleep(0.9)
  if choice1 == "3":
    webhook = input("webhook URL :");msg = input("message :");username = input("Entre le nom du webhook (vide = celui de base) :");counter = 0;data = {"content" : msg,"username" : username};print("FERMEZ LA FENETRE POUR ARRETER LE TOOL !", Colors.red);System.Title(f"Webhook-Manager{counter}");print("En cours...", Colors.blue)
    while True: 
      result = requests.post(webhook, json = data)
      try:
        result.raise_for_status()
      except requests.exceptions.HTTPError as err:
        time.sleep(43)
      else:
        counter = counter + 1
  if choice1 == "2":
    weebhook = input("webhook URL :");requests.delete(weebhook);print("Webhook Suprimer", Colors.green);time.sleep(1)
  if choice1 == "4":
    webhook = input("webhook URL :");os.system(f"start {webhook}");input("Press ENTER FOR CLEAR", Colors.red)
    

	
	
	

