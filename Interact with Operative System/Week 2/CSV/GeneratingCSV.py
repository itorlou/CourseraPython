from os.path import dirname, join
import csv

current_dir = dirname(__file__)
file_path = join(current_dir, "./hosts.csv")

hosts =[["workstation.local", "192.168.0.52"],["webserver.cloud","10.2.5.6"]]

with open(file_path, 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


