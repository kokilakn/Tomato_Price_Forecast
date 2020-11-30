import requests
import csv
from bs4 import BeautifulSoup

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for year in range(2000,2021):
        for month in months:
            for day in range(1,32):
                response = requests.request("GET", "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom="+str(day)+"-"+str(month)+"-"+str(year)+"&DateTo=29-Sep-2020&Tx_Trend=2&Tx_CommodityHead=Tomato")
                soup = BeautifulSoup(response.text.encode('utf8'), 'html.parser')
                table = soup.find('table', class_='tableagmark_new')
                print(str(day)+'/'+str(month)+'/'+str(year))
                if(table) and (table.find('td',attrs={'width':"60"})):
                    tab_data = [[item.text for item in row_data.select("td")]for row_data in table.select("tr")]
                    for data in tab_data:
                        writer.writerow(data)