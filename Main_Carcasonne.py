import CustomFunctions
import json_tools



# welcome
CustomFunctions.Welcome_Msg()
# initialize players
number_of_players,players_array = CustomFunctions.Create_Players()
date = CustomFunctions.SaveCurrentDate()
startTime = CustomFunctions.CurrentTime()

text_input = 'start'

# run while gaming
while(text_input != 'end'):
    
    # input data
    CustomFunctions.PrintInfo(number_of_players,players_array)
    text_input = input('Category: ')

    if (text_input == 'info'):
        # print info
        CustomFunctions.PlotTotalPoints(number_of_players,players_array)
        pass
    elif (text_input == 'end'):
        pass
    else:
        points_input = CustomFunctions.InputPoints()
        CustomFunctions.MainUpdateFunction(text_input,startTime,points_input,number_of_players,players_array)   

text_input = 'start'
# goodbye
winner_array,max_points = CustomFunctions.Goodbye(number_of_players,players_array)
# info terminal
while (text_input != 'end'):
    CustomFunctions.PrintPostInfo()
    text_input = input('Open: ')
    if (text_input == '1'):
        # print info
        CustomFunctions.PlotTotalPoints(number_of_players,players_array)
        pass
    if (text_input == '2'):
        # print info
        CustomFunctions.PlotCastlePoints(number_of_players,players_array)
        pass
    if (text_input == '3'):
        # print info
        CustomFunctions.PlotFarmerPoints(number_of_players,players_array)
        pass
    if (text_input == '4'):
        # print info
        CustomFunctions.PlotFarmerHousePoints(number_of_players,players_array)
        pass
    if (text_input == '5'):
        # print info
        CustomFunctions.PlotShepherdPoints(number_of_players,players_array)
        pass
    if (text_input == '6'):
        # print info
        CustomFunctions.PlotHighwaymanPoints(number_of_players,players_array)
        pass
    if (text_input == '7'):
        # print info
        CustomFunctions.PlotCloisterPoints(number_of_players,players_array)
        pass
    if (text_input == '8'):
        # print info
        CustomFunctions.PlotGoodiesPoints(number_of_players,players_array)
        pass
    if (text_input == '9'):
        # print info
        CustomFunctions.PlotMarketPoints(number_of_players,players_array)
        pass
    if (text_input == '10'):
        # print info
        CustomFunctions.PlotRansomPoints(number_of_players,players_array)
        pass
    elif (text_input == 'end'):
        pass    
    else:
        pass
    

# save game data
json_tools.dumpJsonData(number_of_players,players_array,date,winner_array,max_points)

    

