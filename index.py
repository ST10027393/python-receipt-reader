from bs4 import BeautifulSoup
import csv

with open('input.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    table = soup.find('table')
    headers = [th.text.strip() for th in table.find_all('th')]
    data = [headers] + [[td.text.strip() for td in row.find_all('td')] for row in table.find_all('tr')]
    with open('output.csv', 'w', newline='') as outfile:
        csv.writer(outfile).writerows(data)
