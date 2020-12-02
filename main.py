import time
from CsiExplorer import Explorer
from CsiPlotter import Plotter

filename = input('filename: ')

explorer = Explorer(f'./files/{filename}')
plotter  = Plotter(explorer.get_sample(0).csi)

def display(index):
    sample = explorer.get_sample(index)
    print(sample)
    plotter.update_data(sample.get_csi(True, True))

while True:
    index = input('Which sample would you like to explore? ')

    if '-' in index:
        start = int(index.split('-')[0])
        end = int(index.split('-')[1])
        for i in range(start, end+1):
            display(i)
            time.sleep(0.1)
    else:
        display(int(index))

