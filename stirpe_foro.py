import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/STRETCH-ARMSTRONG-10000-Stretch-Armstrong/dp/B01EARLEX0/ref=sr_1_1?keywords=stretch+armstrong&qid=1574096504&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}

def check_price():

    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if(converted_price < 20):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ethanbyeon@gmail.com', '')

    subject = 'PRICE DROP!'
    body = 'Check the Amazon link: ', URL
    
    msg = f"Subject : {subject}\n\n{body}"

    # server.sendmail(
    #     'sender email',
    #     'receiver email',
    #     msg
    # )
    # print('EMAIL HAS BEEN SENT')

    server.quit()

# while(True):
#     check_price()
#     time.sleep(3600)
