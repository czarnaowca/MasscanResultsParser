import json
import sys

def parse_results(json_file):
    with open(json_file) as file:
        data = json.load(file)

        ips = {}    # dict of ip addresses

        """ colecting ip addresses from json """
        for line in data:
            ips[line["ip"]] = []

        """ searching results for specific ip address """
        for ip in ips:
            for line in data:
                if line["ip"] == ip:
                    ports_line = line["ports"][0]
                    ips[ip].append([ports_line["port"], ports_line["proto"], ports_line["status"]]) # extracting info about port

        print("Results:")
        for ip in ips:
            print(f"\t{ip}")
            for ports in ips[ip]:
                print(f"\t\tport: {ports[0]}/{ports[1]} is {ports[2]}")


if __name__ in "__main__":
    print("Author: Czarna Owca")
    print("Source: https://github.com/czarnaowca/MasscanResultsParser")
    print("Contact: czarna.owca.mail@gmail.com")
    
    if len(sys.argv) != 2:
        print("\nJson file path is missing!")
        exit(0)

    parse_results(sys.argv[1])
