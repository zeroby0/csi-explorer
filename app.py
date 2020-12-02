import time
from os import listdir
from os.path import isfile, join

import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd

from CsiExplorer import Explorer
from CsiPlotter import Plotter

st.title('CSI Explorer')

pcapDir = 'files/'

bandwidth = st.sidebar.selectbox(
    'Select Bandwidth',
    [20, 40, 80],
    index=2
)

pcapfilename = st.sidebar.selectbox(
    'Select file to explore',
    [f for f in listdir(pcapDir) if isfile(join(pcapDir, f))]
)

remove_null = st.sidebar.checkbox(
    'Remove Null subcarriers',
    value=True
)

remove_pilot = st.sidebar.checkbox(
    'Remove Pilot subcarriers',
    value=True
)

show_animation = st.sidebar.checkbox(
    'Play animation',
    value=True
)


explorer = Explorer(pcapDir + pcapfilename)

if show_animation:
    fig, ax = plt.subplots()

    nfft = int(bandwidth * 3.2)
    x = np.arange(-1 * nfft/2, nfft/2)

    ax.set_ylim(0, 4000)
    plt.xlabel("Sub carrier index")
    plt.ylabel("Amplitude")

    line, = ax.plot(x, explorer.get_sample(0).get_csi(remove_null, remove_pilot))
    el_plot = st.pyplot(plt)

    el_status = st.markdown('### Showing sample 0')
    el_summary = st.text('Summary')

    

    def init():  # give a clean slate to start
        line.set_ydata([np.nan] * len(x))

    def animate(i):  # update the y values (every 1000ms)
        sample = explorer.get_sample(i)
        line.set_ydata(sample.get_csi(remove_null, remove_pilot))
        
        el_plot.pyplot(plt)
        el_status.markdown('### Showing sample %d' % (i))
        el_summary.text(sample)

    init()

    for i in range(explorer.get_max_index() + 1):
        animate(i)
        time.sleep(0.05)

else:
    samplenumber = st.sidebar.slider(
        label='Select CSI sample to explore',
        min_value=0,
        max_value=explorer.get_max_index(),
        value=0
    )


    sample = explorer.get_sample(int(samplenumber))
    st.line_chart(sample.get_csi(remove_null, remove_pilot))

    el_status = st.markdown('### Showing sample %d' % (samplenumber))
    el_summary = st.text(sample)
