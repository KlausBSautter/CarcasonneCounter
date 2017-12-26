#  License:		                BSD License 
#  PythonTOP default license:   license.txt

import os
import json
import numpy as np

#also save winner and do this -> for every player
def dumpJsonData(number_of_players,player_array,date,winner_array,max_points):
    file_name = str(date)
    with open(file_name+'.json', 'w') as outfile:
        data = {}
        for i in range(number_of_players):
            player1 = player_array[i]
            player_name = player1.name
            data['time_steps_'+player_name] = player1.time_steps
            data['points_total_'+player_name] = player1.points_total
            data['points_total_array_'+player_name] = player1.points_total_array
            data['points_total_array_'+player_name] = player1.points_total_array 
            data['points_castle_array_'+player_name] = player1.points_castle_array 
            data['points_farmer_array_'+player_name] = player1.points_farmer_array 
            data['points_farmer_house_array_'+player_name] = player1.points_farmer_house_array 
            data['points_shepherd_array_'+player_name] = player1.points_shepherd_array 
            data['points_highwayman_array_'+player_name] = player1.points_highwayman_array 
            data['points_cloister_array_'+player_name] = player1.points_cloister_array 
            data['points_goodies_array_'+player_name] = player1.points_goodies_array 
            data['points_market_array_'+player_name] = player1.points_market_array 
            data['points_ransom_array_'+player_name] = player1.points_ransom_array 
            
        data['winner_array'] = winner_array
        data['max_points'] = max_points
        json.dump(data, outfile, sort_keys=True)

    print('data successfully saved')


''' date = (datetime.datetime.now())
player1 = [[1,2,3,4,5,123123,13,2,1,21],2131]
dumpJsonData(player1,date) '''