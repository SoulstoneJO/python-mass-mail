import configparser

config = configparser.ConfigParser()
config.read('properties.ini')

str1 = config["section0"]["sender"]

str2 = str1.split(",")

print(str2)

