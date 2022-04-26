import csv
import time

#nom des colonnes
fieldnames = ["temps", "temperature", "humidite", "CO2", "CO"]


#creer un fichier csv sil nexiste pas et l'ouvrir pour ecrire les fieldnames
def create(chemin):
	with open(chemin, 'w') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		csv_writer.writeheader()

#ouvrir le fichier csv pour append les nouvelles valeurs
def newLine(chemin, Temp, Gaz):
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S",t)
	with open(chemin, 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		info = {
			"temps": current_time,
			"temperature": Temp[0],
			"humidite": Temp[1],
			"CO2": Gaz[0],
			"CO": Gaz[1]
			}	
		csv_writer.writerow(info)


