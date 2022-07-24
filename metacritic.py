from bs4 import BeautifulSoup

import requests

import csv

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.metacritic.com/game",headers=headers)
source = response.content
soup = BeautifulSoup(source, 'lxml')
csv_file = open('games.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['game_title', 'game_summary', 'game_score'])
# print the html file of the website
print(soup.prettify())
# the comment code below is for trying to print the pieces of information related to one game
"""
first_game = soup.find('td', class_='clamp-summary-wrap')
game_title = soup.find('a', class_='title').text.replace(' ','')
print(game_title)
game_summary = soup.find('div', class_='summary').text.replace(' ','')
print(game_summary)
game_score = soup.find('div', class_='metascore_w large game positive').text.replace(' ','')
print(game_score)
"""

""" search in the html tags to find the td tag with the class =c amp-summary-wrap """
# Now it is time for all games
all_games = soup.find_all('td', class_='clamp-summary-wrap')

# this loop is going to go over all games to provide the game title, summary, and score.
for game in all_games :
    game_title = game.find('a', class_='title').text.replace(' ','')
    print(game_title)
    game_summary = game.find('div', class_='summary').text.replace(' ','')
    print(game_summary)
    game_score = game.find('div', class_='metascore_w large game positive').text.replace(' ','')
    print(game_score)
    # add the results to our csv_file
    csv_writer.writerow([game_title, game_summary, game_score])
csv_file.close()
