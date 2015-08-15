from DataCollector import DataCollector
import pprint
import json
import re

def main():

    m_id_list = [1852548676, 1852558827, 1852559208, 1852560871, 1852561073]

    crystal_scepter_id = 3116
    liandry_id         = 3151

    for id in m_id_list:
        my_dc = DataCollector(id,'na')
        #my_dc.printData()

        j = my_dc.getJSON()

        for x in range(10):
            for k,v in j["participants"][x]["stats"].items():
                #Level 1 Print
                if re.search("item",k):
                    if v == crystal_scepter_id or v == liandry_id:
                        print("{} -- {}".format(k,v))

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
