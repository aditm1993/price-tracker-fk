import os
import requests
import re
import time
from bs4 import BeautifulSoup as bs

def generate_sound(inp):
    if inp == 1:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 5000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    elif inp == 2:
        beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
        beep(3)


def check_fk_price(url, amount):

    request = requests.get(url)
    soup = bs(request.content,'html.parser')

    product_name = soup.find("span",{"class":"B_NuCI"}).get_text()
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    prince_int = int(''.join(re.findall(r'\d+', price)))
    print(product_name + " is at " + price)
    if prince_int < amount:
        print("Book Quickly")
        generate_sound(1)
    else:
        print("No Slots found")



def main():
    URL = "https://www.flipkart.com/samsung-galaxy-watch-active-2-steel-smartwatch/p/itm973b10e6a04a8?pid=SMWFH4MVBUGEMMZB&lid=LSTSMWFH4MVBUGEMMZBEO8SV3&marketplace=FLIPKART&q=galaxy+active+2&store=ajy%2Fbuh&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=SEARCH&iid=00eba814-0c69-41b4-a8d8-bf9bd14160e4.SMWFH4MVBUGEMMZB.SEARCH&ppt=hp&ppn=homepage&ssid=33wtcykgyo0000001625894811993&qH=069c60520211e697"
    while True:
        check_fk_price(URL, 90000)
        time.sleep(3600)

if __name__ == "__main__":
    main()
