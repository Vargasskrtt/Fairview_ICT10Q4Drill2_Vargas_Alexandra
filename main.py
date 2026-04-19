from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    document.getElementById("output").innerHTML = " "

    days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

    donuts_sold = np.array([12, 18, 25, 20, 30])

    plt.plot(days, donuts_sold, marker='o', color='orange')
    plt.title('Donuts Sold During the Week')
    plt.xlabel('Weekdays')
    plt.ylabel('Number of Donuts')
    plt.grid(True)
    plt.show()
