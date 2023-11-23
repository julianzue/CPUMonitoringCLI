from colorama import Fore, Style, init
import psutil
import time
import os

init()

dim = Style.DIM
res = Style.RESET_ALL

y = Fore.YELLOW
re = Fore.RESET

min_percentage_input = input(y + "[+] Enter MIN Percentage: " + re)
max_percentage_input = input(y + "[+] Enter MAX Percentage: " + re)

count = 0

print("")

with open("log.txt", "r") as lr:
    for linenumber, line in enumerate(lr.readlines(), 1):
        percentage_file = line.strip("\n").split(" | ")[3].strip(" %")

        split = line.strip("\n").split(" | ")

        if float(percentage_file) >= float(min_percentage_input) and float(percentage_file) <= float(max_percentage_input):

            if float(percentage_file) < 20.0:
                color = Fore.LIGHTBLUE_EX

            elif float(percentage_file) < 50.0:
                color = Fore.LIGHTGREEN_EX

            elif float(percentage_file) >= 80.0:
                color = Fore.LIGHTRED_EX
            
            elif float(percentage_file) >= 50.0:
                color = Fore.LIGHTYELLOW_EX

            count += 1

            done = "#" * int(int(round(float(percentage_file), 0)) / 4)
            todo = " " * int(25 - int(round(float(percentage_file), 0) / 4))

            print("{:04d}".format(count) + "  " + dim + "{:04d}".format(linenumber) + res + "  " + split[0] + " " + split[1] + " " + split[2] + "  "\
                   + color + "{:5.1f}".format(float(percentage_file)) + " %" + re + dim + "  [" + done + todo + "]" + res)