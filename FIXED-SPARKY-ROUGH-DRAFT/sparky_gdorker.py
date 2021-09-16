#SPARKY GDORKER
try:
  from googlesearch import search
  import time
  from bs4 import BeautifulSoup
  import pyfiglet
  from termcolor import colored
  from pyfiglet import figlet_format
  from colorama import init
  import urllib
except ImportError as err:
  raise ModuleNotFoundError (
    "[SPARKYSYSTEM$] | Has detected a potential error |"
    " [SPARKYSYSTEM$] {PSOL:} | Verify Import Is in poetry.lock, if not use (pip install {IMPORT}) | ", "Cause Of Problem: ", err
  ) from err

def search_loop():
  for i in search(query,pause=4.0,num=4):
      print(i + '\n')
  if urllib.error.HTTPError:
    print("[SPARKYSYSTEM$", "DETECTED HTTP REQUEST ERROR")
    time.sleep(1)
    print("[SPARKYSYSTEM$//FAIL:SAFE] Restarting..")
    google_dorker()
  else:
      pass
  sub3 = input("[SPARKYSYSTEM$] Satisfied With Results? ")
  if sub3 == 'yes':
    google_dorker()
  elif sub3 == 'Yes':
    google_dorker()
  else:
    print("Exiting")
    exit()

def banner():
  print((colored(figlet_format("SPARKY GDORKER"), color="green")))
  print("Input Google Dork Below, Wait For Search Results.")
  print("""
---------------------------------------------------
Sparky Gdorker Created By: Ma6 (Malware And Or AOD)
---------------------------------------------------
  """)
  print("For Further Information Or Concerns Use -h")

def query_input():
  if query == '-h':
      print("""
      SPARKY GDORKER - (DOCUMENTATION)

      -[Sparky Gdorker] is a google dorking assistance tool. Enter in the dork you would like to use and Sparky will find it and return all possible urls with the containing parameters-
                        
                      - Example: inurl:"website" intext:"choiceofdork"
      
      -[SPARKYSYSTEM$], Errors. Errors will typically come up if a module or import doesn't load in correctly, if this happens make sure to verify all installs are in poetry.lock
                                Typically a HTTP Request error will appear, this is due to the program having issues requesting all of the http urls. Sparky will enable a Fail safe restart command to try an prevent further issues.
      -NOTICES: Please note actions done with Sparky are not correlated to the creator of this program nor responsible for repercussions that occurr 
                If any problems are discovered with Sparky please leave a notice with the creator to notify for further updates and edits.
      
      -THANK YOU: Thank you for using Sparky Gdorker, this program is simple and used for assistance. Much appreciation for usage!

      """)
  google_dorker()


def google_dorker():
  time.sleep(1) 
  global query
  query = input("sparky@sparky:~$ ")
  if query == '-h':
    query_input()
      
  time.sleep(2)
  print(["SPARKYSYSTEM$"], ["+"], "LOADING RESULTS")
  time.sleep(1)
  print(["SPARKYSYSTEM$"], ['+'], "Results Obtained")
  search_loop()
  
if __name__ == '__main__':
  banner()
  google_dorker()
