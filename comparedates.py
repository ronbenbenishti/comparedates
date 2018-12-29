#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
birthday = raw_input('Enter birthday (format: dd/mm/yyyy): ')
day, month, year = int(birthday.split('/')[0]), birthday.split('/')[1], birthday.split('/')[2]
greg_day = str(day)
after_sunset = raw_input('Were you born after sunset? (y/n): ')

if after_sunset == 'y':
    day += 1

def Heb_date(day, month, year):
    url = 'https://www.shoresh.org.il/dates/go.aspx?what=gth&d=' + str(day) + '&m=' + str(month) + '&y=' + str(year) + '&ass=no' + '&res=txt'
    r = requests.get(url)
    if r.status_code == 200:
        heb_date = r.content.split('^^')[4]
        return heb_date
    else:
        print 'Error: (code:', str(r.status_code) + ')'


my_heb_date = Heb_date(day, month, year)
print 'Born date:', my_heb_date, '(' + greg_day + '/' + month + '/' + year + ')'
year = int(year) +1
age = 1
my_heb_date = ''.join(my_heb_date.split(' ')[0]) + ' ' + ''.join(my_heb_date.split(' ')[1])
print 'Match between a Hebrew date and a Gregorian date at the ages:'
while age != 100:
    chk = Heb_date(day, month, year)
    chk_1 = ''.join(chk.split(' ')[0]) + ' ' + ''.join(chk.split(' ')[1])
    if chk_1 == my_heb_date:
        print 'Age:', age, '(' + greg_day + '/' + month + '/' + str(year), chk + ')'
    year += 1
    age += 1