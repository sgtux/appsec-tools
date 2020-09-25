#!/bin/python3

import requests
import sys

def set_error_color():
	print('\033[91m')

if len(sys.argv) < 2:
	set_error_color()
	print('Invalid parameter domain.')
	print('Ex.: ' + sys.argv[0] + ' example.domain.com')
	exit()

print('Searching by ' + sys.argv[1] + ' ...')

r = requests.get('https://rdap.registro.br/domain/' + sys.argv[1])

if int(r.status_code) != 200:
	set_error_color()
	print('Invalid domain.')
	print('Status code: ' + str(r.status_code))
	exit()

result = r.json()

ip = result['nameservers'][0]['ipAddresses']['v4'][0]

r = requests.get('https://rdap.db.ripe.net/ip/' + ip)

if int(r.status_code) != 200:
	set_error_color()
	print('Invalid ip: ' + ip)
	exit()

result = r.json()
print('Range: ' + result['startAddress'] + ' - ' + result['endAddress'])
