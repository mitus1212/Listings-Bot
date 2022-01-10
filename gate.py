import requests
import datetime
from bs4 import BeautifulSoup
import urllib.request
# open a connection to a URL using urllib
from urllib.request import Request
import sqlite3

bot = "2147060992:AAE3Sy6l2LYTHkgv0V5B_WokZBBPS87zn0s"
chat_id = "1437944800"


connection = sqlite3.connect('listingi.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS listingi
              (title TEXT)''')
connection.commit()




connection.commit()

cursor.execute("SELECT * FROM listingi")
fetch = cursor.fetchall()
print(fetch)

    
url = 'https://www.kucoin.com/news/1'



def send_message(chat_id="1437944800"):
    '''
    Takes the chat id of a telegram bot and the text that was  crawled from the
    website and sends it to the bot
    Args: chat_id = string; chat id of the telegram bot, 
          text = string; crawled text to be sent
    Returns: None
    '''
    print("listingi")
    print(datetime.datetime.now())  

    URL = 'https://www.gate.io/articlelist/ann?fbclid=IwAR2rXyAloIwsWW4xMnDCte__zDY495MMxdxcqGR7IqP1ffdZ-yMlapTXRkQ'
    content = requests.get(URL)   
    soup = BeautifulSoup(content.text, 'html.parser')
    parameters = {"chat_id": chat_id}
    '''if len(lista) > 50:
        del lista[:25]
    elif len(lista_2) > 50:
        del lista_2[:25]
    else:
        pass'''

    rows = soup.find_all('h3')
    for row in rows:
        new_row = str(row)
        if "offering" in new_row and ("{new_row}".format(new_row=new_row),) not in fetch:
            cursor.execute("INSERT INTO listingi VALUES ('{text}')".format(text=new_row))
            message = requests.post("https://api.telegram.org/bot"+ bot + "/sendMessage?chat_id=" + chat_id + "&text=https://www.gate.io/articlelist/ann?fbclid=IwAR2rXyAloIwsWW4xMnDCte__zDY495MMxdxcqGR7IqP1ffdZ-yMlapTXRkQ", data=parameters)
            connection.commit()
        elif "Offering" in new_row and ("{new_row}".format(new_row=new_row),) not in fetch:
            cursor.execute("INSERT INTO listingi VALUES ('{text}')".format(text=new_row))
            message = requests.post("https://api.telegram.org/bot"+ bot + "/sendMessage?chat_id=" + chat_id + "&text=https://www.gate.io/articlelist/ann?fbclid=IwAR2rXyAloIwsWW4xMnDCte__zDY495MMxdxcqGR7IqP1ffdZ-yMlapTXRkQ", data=parameters)
            connection.commit()
        else:
            pass
    
    URL_2 = 'https://www.binance.com/en/support/announcement/c-48?navId=48'

    content_2 = requests.get(URL_2)   
    soup_2 = BeautifulSoup(content_2.text, 'html.parser')

    rows_2 = soup_2.find_all('div')
    for row in rows_2:
        new_row = str(row)
        if "Will List" in new_row and ("{new_row}".format(new_row=new_row),) not in fetch:
            cursor.execute("INSERT INTO listingi VALUES ('{text}')".format(text=new_row))
            message = requests.post("https://api.telegram.org/bot"+ bot + "/sendMessage?chat_id=" + chat_id + "&text=https://www.binance.com/en/support/announcement/c-48?navId=48", data=parameters)
            connection.commit()
        elif "will list" in new_row and ("{new_row}".format(new_row=new_row),) not in fetch:
            cursor.execute("INSERT INTO listingi VALUES ('{text}')".format(text=new_row))
            message = requests.post("https://api.telegram.org/bot"+ bot + "/sendMessage?chat_id=" + chat_id + "&text=https://www.binance.com/en/support/announcement/c-48?navId=48", data=parameters)
            connection.commit()
        else:
            pass
    #cursor.execute("DELETE FROM listingi WHERE title LIKE '%<h3> Gate.io Startup Initial Offering: Solvent(SVT) </h3>%'")
    #connection.commit()
    cursor.close()
    connection.close()


#send_message("1437944800")
send_message("-643192834")




#https://api.telegram.org/bot2147060992:AAE3Sy6l2LYTHkgv0V5B_WokZBBPS87zn0s/sendMessage?chat_id=1437944800&text=test
