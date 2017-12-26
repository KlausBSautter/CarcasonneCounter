import PlayerClass
import datetime
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def Welcome_Msg():
    print("""  ______      ___      .______        ______      ___           _______.  ______   .__   __. .__   __.  _______ 
 /      |    /   \     |   _  \      /      |    /   \         /       | /  __  \  |  \ |  | |  \ |  | |   ____|
|  ,----'   /  ^  \    |  |_)  |    |  ,----'   /  ^  \       |   (----`|  |  |  | |   \|  | |   \|  | |  |__   
|  |       /  /_\  \   |      /     |  |       /  /_\  \       \   \    |  |  |  | |  . `  | |  . `  | |   __|  
|  `----. /  _____  \  |  |\  \----.|  `----. /  _____  \  .----)   |   |  `--'  | |  |\   | |  |\   | |  |____ 
 \______|/__/     \__\ | _| `._____| \______|/__/     \__\ |_______/     \______/  |__| \__| |__| \__| |_______| 
 """                                                                                          
)


def Create_Players():
    try:
        number_of_players = int(input('Please enter the number of players: '))
        players_array = []
        try:
            for i in range(number_of_players):
                text_i = 'Name of player ' + str(i+1) + ': '
                name_i = input(text_i)
                player_i = PlayerClass.Player(name_i)
                players_array.append(player_i)
            return number_of_players,players_array
        except TypeError:
            print('no valid name ! please retry')
            Create_Players() 
    except ValueError :
        print('no valid number ! please retry')
        Create_Players()     


def SaveCurrentDate():
    return (datetime.datetime.now())

def CurrentTime():
    return (timer())

def ElapsedTime(StartTime):
    return (timer() - StartTime)

def GameStates(number_of_players,players_array):
    text_output = players_array[0].return_player_stats()
    for i in range(number_of_players-1): 
        text_output = text_output + ' || ' + players_array[i+1].return_player_stats()
    print(text_output)

def TableOfContent(number_of_players,players_array):
    player_names = players_array[0].name + '(1)'
    for i in range(number_of_players-1): 
        player_names = player_names + ' || ' + players_array[i+1].name + '(' + str(i+2)+')'

    point_names = 'castle(a) || farmer(b) || farmer house(c) || shepherd(d) || highwayman(e) || cloister(f)\
    || goodies(g) || market(h) || ransom(i)'
    print(player_names)
    print(point_names)


def PrintInfo(number_of_players,players_array):
    print('\n')
    print('#############################################################################################')
    print('Current points: ')
    GameStates(number_of_players,players_array)
    print('---------------------------------------------------------------------------------------------')    
    print('Table of Contents: ')
    TableOfContent(number_of_players,players_array)

def UpdateAllPlayers(number_of_players,players_array,time):
    for i in range(number_of_players):
        players_array[i].add_up_all_points()
    for i in range(number_of_players):
        players_array[i].update_class_arrays(time)   


def PlotTotalPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_total_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('total points - time')
    plt.show()

def PlotCastlePoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_castle_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('castle points - time')
    plt.show()

def PlotFarmerPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_farmer_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('farmer points - time')
    plt.show()

def PlotFarmerHousePoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_farmer_house_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('farmer house points - time')
    plt.show()

def PlotShepherdPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_shepherd_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('shepherd points - time')
    plt.show()

def PlotHighwaymanPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_highwayman_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('highwayman points - time')
    plt.show()

def PlotCloisterPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_cloister_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('cloister points - time')
    plt.show()

def PlotGoodiesPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_goodies_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('goodies points - time')
    plt.show()

def PlotMarketPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_market_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('market points - time')
    plt.show()

def PlotRansomPoints(number_of_players,players_array):
    
    for i in range(number_of_players):
        plt.plot(players_array[i].time_steps,players_array[i].points_ransom_array,label = players_array[i].name)

    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('points')
    plt.title('ransom points - time')
    plt.show()


def MainUpdateFunction(text_input,startTime,points_input,number_of_players,players_array):
    try:
        try:
            player_id = int(list(text_input)[0])-1
            category_id = list(text_input)[1]
            
            # update player
            CurrentTime = ElapsedTime(startTime)
            try:
                players_array[player_id].update_points(category_id,points_input)
                UpdateAllPlayers(number_of_players,players_array,CurrentTime)
            except IndexError:
                print('player not available -> retry')
                pass
        except IndexError:
            print('empty input -> retry')
    except ValueError:
        print('could not register player id -> retry')

            
def InputPoints():
    try:
        points_input = int(input('Points: '))
    except ValueError:
        print('could not register points -> retry')
        points_input = 0
    return points_input

def Goodbye(number_of_players,players_array):
    print('Game finished ! I hope you enjoyed it :)')
    winner_array,max_points = FindWinner(number_of_players,players_array)
    print('Endpoints:')
    for i in range(number_of_players):
        print(i+1,'. : ', winner_array[number_of_players-i-1], ' - ', max_points[number_of_players-i-1], 'points')
    return winner_array,max_points




def FindWinner(number_of_players,players_array):
    max_points = []
    for i in range(number_of_players):
        max_points.append(players_array[i].points_total)
    for i in range(number_of_players-1):
        for j in range(number_of_players-1):
            if (max_points[j]>=max_points[j+1]):
                temp = max_points[j+1]
                max_points[j+1] = max_points[j]
                max_points[j] = temp       

    winner_array = []
    for i in range(number_of_players):
        for j in range(number_of_players):
            if (max_points[i] == players_array[j].points_total):
                winner_array.append(players_array[j].name)
    return winner_array,max_points


def PrintPostInfo():
    point_names = 'total(1) || castle(2) || farmer(3) || farmer house(4) || shepherd(5) || highwayman(6) || cloister(7)\
    || goodies(8) || market(9) || ransom(10)'
    print(point_names)
