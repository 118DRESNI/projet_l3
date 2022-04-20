adc-read.py : un prog qui effectue des lectures continuelles sur le bus I2C
adcRead.py : meme chose mais le nom a été changé pour ne plus avoir de tiret pour pouvoir être appelé par un autre programme.
main.py : un programme de test qui ne fait qu'appeler adcRead.py

Le but de la manip est de structurer le programme global en plusieurs sous programmes ayant chacun un role défini
1 programme de lecture i2c
1 programme d'écriture de fichier csv
1 programme d'affichage
1 programme d'enregistrement de données, etc....


