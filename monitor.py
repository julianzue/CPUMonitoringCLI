from colorama import Fore, init
import psutil
import time
import os

init()

# colors
c = Fore.LIGHTCYAN_EX
re = Fore.RESET

os.system("cls")
count = 0

while True:

    count += 1

    da = time.strftime("%A")
    d = time.strftime("%Y-%m-%d")
    t = time.strftime("%H:%M:%S")

    cpu = psutil.cpu_percent()

    output_cpu = "{:5.1f}".format(float(cpu)) + " %"

    done = "#" * int(int(round(cpu, 0)) / 2)
    todo = " " * int(50 - int(round(cpu, 0) / 2))

    print(c + "CPU Percentage" + re)
    print("")
    print(c + "Day:   " + re + da.upper()[:3])
    print(c + "Date:  " + re + d)
    print(c + "Time:  " + re + t)
    print(c + "Count: " + re + str(count))
    print("")
    print("[" + done + todo + "] " + c + output_cpu + re)

    with open("log.txt", "a") as la:
        la.write(da.upper()[:3] +  " | " + d + " | " + t + " | " + output_cpu + "\n")

    time.sleep(1)

    os.system("cls")