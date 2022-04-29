
import csv
import random
import time

x_value = 0
tiempo  = 0
total_1 = 0
total_2 = 0
bascule = False
maxVal  = 60
fieldnames = ["x_value", "total_1", "total_2"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        tiempo +=1
        if x_value % 10 == 0 :
            bascule = not bascule
            tiempo = 0

        if bascule :
            total_1 = maxVal + random.randint(-6, 8)
            total_2 = -0.5 * tiempo * maxVal + random.randint(-5, 6)
        else:          
            total_1 = -maxVal + random.randint(-6, 8)    
            total_2 = 0.5 * tiempo * maxVal + random.randint(-5, 6)

    time.sleep(1)
