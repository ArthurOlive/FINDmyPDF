import webbrowser
import time
print ("""

  ______ _____ _   _ _____                      _____    _____    ______ 
 |  ____|_   _| \ | |  __ \                    |  __ \  |  __ \  |  ____|
 | |__    | | |  \| | |  | |  _ __ ___  _   _  | |__) | | |  | | | |__   
 |  __|   | | | . ` | |  | | | '_ ` _ \| | | | |  ___/  | |  | | |  __|  
 | |     _| |_| |\  | |__| | | | | | | | |_| | | |      | |__| | | |     
 |_|    |_____|_| \_|_____/  |_| |_| |_|\__, | |_|      |_____/  |_|     
                                         __/ |                           
                                        |___/                            

         """)
time.sleep(.750)
print ("\n1 - Search")
print ("2 - Exit\n")
time.sleep(.500)
menu = int(input("Your choice: "))

if(menu==1):
    url = "https://www.google.com/search?q="
    livro = str(input("Enter the desired BOOK: "))
    url += '"' + livro + '"'
    url += " filetype:pdf"
    webbrowser.open(url)
    print ("Search Completed!")
else:
    raise SystemExit
