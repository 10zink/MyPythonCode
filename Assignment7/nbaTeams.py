import json
import Epic


def fileReader():
    jsonTxt = ""
    f = open('playerlist.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    PlayerList = json.loads(jsonTxt)

    return PlayerList


def roster(PlayerList, name):
    starters = " "
    comma = ", "
    for team in PlayerList:
        if team["Team"] == name:
            print ""
            print "Starters:"
            for player in team["Players"]:
                starters += player + comma
    
    return starters
            

def main():
   
    print "Teams in the Atlantic Division: (Boston Celtics, Brooklyn Nets, New York Knicks, Philadelphia 76ers, Toronto Raptors)"
    name = Epic.userString("Enter a Team name:")
   
    # while(name != roster(fileReader(), name)):
    #     print "Please enter a valid team name!"
    #     name = Epic.userString("Enter a Team name:")
    # else:    
    b = roster(fileReader(), name)
    print " %s " % b
        
main()
    