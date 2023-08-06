
from bs4 import BeautifulSoup
import requests
import pandas as pd

class PlayerRawStats:
    def __init__(self, save_to_database=False):
        '''
        This function initializes the PlayerRawStats class

        Args:
            save_to_database (bool, optional): Whether or not to save the data to the database. Defaults to False.
        '''

        # Save the data to the database if specified
        if save_to_database:
            # Connect to the database
            print("Connecting to the database...")
    

    def get_each_game(self, player_first_name, player_last_name, season, playoffs=False):
        '''
        This function returns the stats for each game for a player in a season
        
        Args:
            player_first_name (str): The first name of the player
            player_last_name (str): The last name of the player
            season (str): The season to get the stats for
            playoffs (bool, optional): Whether or not to get the playoff stats. Defaults to False.
            
        Returns:
            dict: A dictionary containing the player stats matrix, the stats dictionary, and the stats dataframe
        '''

        # format player name for url
        num_id = "01"
        if len(player_last_name) > 5:
            player_name = player_last_name[:5] + player_first_name[:2]
        else:
            player_name = player_last_name + player_first_name[:2]

        # format url
        url = f"https://www.basketball-reference.com/players/h/{player_name.lower()}{num_id}/gamelog/{season}"
        print(f"Using URL: {url}")

        # Get the response
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code != 200:
            # Print error messages
            print(f"Failed to retrieve data for {player_name} in {season}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")
            return None

        # Parse the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the stats
        table = soup.find('table', {'id': 'pgl_basic'})

        # Get the headers
        headers = [th.getText() for th in table.findAll('tr')[0].findAll('th')][1:]

        # Get the rows
        rows = table.findAll('tr')[1:]
        player_stats_matrix = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
        # format the data for pandas dataframe
        stats_dict = {}
        # iterate through each row
        for row_index in range(len(player_stats_matrix)):
            # check if the row is empty
            if player_stats_matrix[row_index] != []:
                # Check last column to see if player played in the game
                if ("+" not in player_stats_matrix[row_index][-1]) and ("-" not in player_stats_matrix[row_index][-1]):
                    # get the difference in length between the headers and the row
                    row_diff = len(headers) - len(player_stats_matrix[row_index])
                    # appending last value of player_stats_matrix[row_index] to the end of the list row_diff times
                    player_stats_matrix[row_index] = player_stats_matrix[row_index] + [player_stats_matrix[row_index][-1]] * row_diff
                # iterate through each column
                for header_index in range(len(headers)):
                    # Check if we are in the Hom/Away column and set the right header
                    if (headers[header_index-1] == "Tm") and (headers[header_index+1] == "Opp"):
                        headers[header_index] = "Home/Away"
                        # set the new value to Home or Away
                        if "@" in player_stats_matrix[row_index][header_index]:
                            player_stats_matrix[row_index][header_index] = "Away"
                        else:
                            player_stats_matrix[row_index][header_index] = "Home"
                    # Check if we are in the W/L column and set the right header        
                    if (headers[header_index-1] == "Opp") and (headers[header_index+1] == "GS"):
                        # set the new header
                        headers[header_index] = "W/L"
                    # set the key in the dictionary if it doesn't exist
                    if stats_dict.get(headers[header_index]) == None:
                        stats_dict[headers[header_index]] = []
                    # append the value to the dictionary
                    stats_dict[headers[header_index]].append(player_stats_matrix[row_index][header_index])

        # Create a dataframe
        stats_df = pd.DataFrame(stats_dict)

        # Return the stats
        return {"player_stats_matrix": player_stats_matrix, "stats_dict": stats_dict, "stats_df": stats_df}