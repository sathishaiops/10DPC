import time
import requests
import webbrowser
import math
import datetime
import os
time.sleep(1)

output = requests.get("https://www.google.com")
print(output)

webbrowser.open("https://www.google.com")

os.system("ls -l")  
print(math.sqrt(16))    
print(datetime.datetime.now())