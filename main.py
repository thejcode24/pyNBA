#!/python3

import numpy
import requests
import string
import json
from string import ascii_lowercase
from bs4 import BeautifulSoup, SoupStrainer

player_list = []
base_url = 'https://www.basketball-reference.com/players/'

# get player name from sorted alphabetical list 
for letter in string.ascii_lowercase:
    # request html using base url + player name
    r = requests.get(base_url + letter)
    # parse the requested text using BeautifulSoup
    soup = BeautifulSoup(r.text, "lxml")
    
    # find table within the parsed text soup
    # then find the tbody tag within the table if table exists
    table = soup.find('table')

    if table:
        table_body = soup.find('tbody')

        # loop over list of players
        for row in table_body.findAll('tr'):

            # get nba player names by finding 'a' tags 
            player_info = row.find('a')
            player_name = player_info.text
            
            # note to self, using [] instead of () to find the 
            # href reference whithin 'a' tag
            player_url = player_info['href']

            # get players' information from table by grabbing all 'td' tags 
            # within the 'tr' tag
            column_cells = row.findAll('td')
            
            # get certain information using the cells found in previous line
            player_drafted_year = int(column_cells[0].text)
            player_retired_year = int(column_cells[1].text)
            player_position = column_cells[2].text
            player_height = column_cells[3].text
            player_weight = column_cells[4].text
            player_bday = column_cells[5].text
            player_college = column_cells[6].text
            
            # make list of headers for our table
            player_entry = {'URL': player_url,
                            'Name': player_name,
                            'Year Drafted': player_drafted_year,
                            'Year Retired': player_retired_year,
                            'Position': player_position,
                            'Height': player_height,
                            'Weight': player_weight,
                            'Birthday': player_bday,
                            'College': player_college }
        
            # take player_entry dictionary and add to 
            # list of player information
            player_list.append(player_entry)

    # create and write to data.json file and 'dump' the contents 
    # scraped into the file as text.
    with open('data.json', 'w') as outfile:
        json.dump(player_list, outfile)

