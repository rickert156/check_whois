import requests
from bs4 import BeautifulSoup


def whois(domain):
	params = {'domain':{domain}}
	site = 'https://whois.ru/'
	response = requests.get(site, params=params)
	if response.status_code == 200:
		print(f'Доступ к сайту есть, Status Code: {response.status_code}\n')
		response = response.text
		bs = BeautifulSoup(response, 'lxml')
		try:
			for information in bs.find_all(class_='raw-domain-info-pre'):
				print(information.get_text())
			print('\n')
		except Exception as ex:
			print(f'Error: {ex}')
	else:print(f'Доступ к сервису ограничен: Status Code: {response.status_code}\n')


domain = input('Введите домен: ')
whois(domain)