import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import board
import adafruit_dht

# Déclaration d'un DHT22 sur la broche D17 du GPIO
dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)
# La prériode d'échantillonnage du DHT22
Tech = 3.0

# Creation du plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


def lireTemp():
        try:
                temp = dhtDevice.temperature
                #humi = dhtDevice.humidity
        except RuntimeError as error:
                print(error.args[0])
                time.sleep(Tech)
        except Exception as error:
                dhtDevice.exit()
                raise error
        return temp


def animer(i, xs, ys):

        # Effectuer une lecture
        temp_c = lireTemp()

        # Ajouter x et y aux listes
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(temp_c)

        # Limiter les listes x et y a 20 elements
        xs = xs[-20:]
        ys = ys[-20:]

        # plotter les listes x et y 
        ax.clear()
        ax.plot(xs, ys)

        # formattage du plot 
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Température du DHT22')
        plt.ylabel('Température (°C)')


ani = animation.FuncAnimation(fig, animer, fargs=(xs, ys), interval=1000*Tech)
plt.show()
