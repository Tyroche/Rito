from DataCollector import DataCollector
import pprint
import json
import re

def main():

    m_id_list   = [1852548676, 1852558827, 1852559208, 1852560871, 1852561073]
    total_games = len(m_id_list)

    crystal_scepter_id = 3116
    liandry_id         = 3151

    crystal_scepter_wins = 0
    liandry_wins = 0
    both_wins = 0

    for id in m_id_list:
        my_dc = DataCollector(id,'na')
        exit()
        #my_dc.printData()

        j = my_dc.getJSON()

        # teamX [id, winner]
        team1 = getTeamInfo(j,0)
        team2 = getTeamInfo(j,1)

        teams = [team1, team2]

        #updateTeamBools(j,teams,crystal_scepter_id,liandry_id)
        for x in range(10):
            my_team = j["participants"][x]["teamId"]
            for k,v in j["participants"][x]["stats"].items():
                if re.search("item",k):
                    if v == crystal_scepter_id:
                        for t in teams:
                            if my_team == t["teamId"]:
                                t["rylai"] = True
                    elif v == liandry_id:
                            if my_team == t["teamId"]:
                                t["liandry"] = True

        for t in teams:
            if t["winner"] is True:
                if t["rylai"] is True:
                    crystal_scepter_wins += 1
                if t["liandry"] is True:
                    liandry_wins += 1
                if t["rylai"] is True and t["liandry"] is True:
                    both_wins += 1

    print("Liandry win %: {}%".format(liandry_wins/total_games*100))
    print("Rylai win   %: {}%".format(crystal_scepter_wins/total_games*100))
    print("Total win   %: {}%".format(both_wins/total_games*100))

def updateTeamBools(jobj,teamlist,csid,liid):
    for x in range(10):
        my_team = jobj["participants"][x]["teamId"]
        for k,v in jobj["participants"][x]["stats"].items():
            if re.search("item",k):
                if v == csid:
                    for t in teamlist:
                        print(t)
                        if my_team == t["teamId"]:
                            t["rylai"] = True
                elif v == liid:
                        if my_team == t["teamId"]:
                            t["liandry"] = True

#Makes a team given json object and teamnumber
def getTeamInfo(jobj,teamnumber):
    return { "teamId" : jobj["teams"][teamnumber]["teamId"] , "winner" : jobj["teams"][teamnumber]["winner"] , "rylai" : False, "liandry" : False }

#Creates an item file
def makeItemFile():
    my_dc = DataCollector('z','z',True)

    j = my_dc.getJSON()

    with open('items.txt',"w") as infile:
        for k,v in j["data"].items():
            #print("KEY: {} -- ITEMS {}".format(k,v))
            infile.write("{} : {}".format(j["data"][k]["name"],j["data"][k]["id"]))
            infile.write("\n")


if __name__ == "__main__":
    main()
