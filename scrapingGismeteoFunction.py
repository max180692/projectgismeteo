import requests
from bs4 import BeautifulSoup
import lxml
import json

HEADERS = {'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
session = requests.Session()
URL = 'https://www.gismeteo.ru'
URL_API = 'https://www.gismeteo.ru/api/v2/search/searchresultforsuggest/'


def connect(url,session=session,headers=HEADERS):
	request = session.get(url,headers=headers)
	return request


def get_city_url(city,url_api=URL_API):
	url = url_api + city
	json_city = json.loads(connect(url).text)
	url_city = json_city['items'][0]['url']
	return url_city


def get_weather_city(url_city,url=URL):
	url_weather = url + url_city
	print(url_weather)
	contents = connect(url_weather).content
	soup = BeautifulSoup(contents,'lxml')
	list_div_tab_wrap = soup.find('div',{'class':'tabs _center'}).find_all('div',{'class':'tab_wrap'})
	#print(len(list_div_tab_wrap))
	for div in list_div_tab_wrap:
		date = div.find('div',{'class':'date'}).text.strip()
		print(date)
		list_temperature = div.find_all('span',{'class':'unit unit_temperature_c'})
		temperature_night = list_temperature[0].text.strip()
		print(temperature_night)
		temperature_day = list_temperature[1].text.strip()
		print(temperature_day)



def main():
	print("Программа прогноз погоды!")
	action = True
	while action:
		print("Введите ваш город!")
		enter_city = input()
		if enter_city != '':
			get_weather_city(get_city_url(enter_city))
			print('Завершить программу ? y/n')
			end_program = input().lower()
			if end_program == 'y' or end_program == 'у':
				action = False



if __name__ == '__main__':
	main()

