import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Plotter():
    def __init__(self, data, bandwidth=80):
        self.bandwidth = bandwidth
        self.data = data
    
        nfft = int(bandwidth * 3.2)
        self.x = np.arange(-1 * nfft/2, nfft/2)

        fig, ax = plt.subplots()

        plt.ion()
        plt.show()
    
    def update_data(self, data):

        plt.cla()
        plt.plot(self.x, data)
        plt.draw()
        plt.pause(0.001)