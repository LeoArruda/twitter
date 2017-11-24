import json
import pandas as pd
import string
import os
import csv
import numpy as np
from datetime import datetime
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style



def plot_graph(dframe,output='ResultGraph.png', title='Tweets comparison\nKey: <>', subtitle=''):

    plt.figure(1)
    plt.clf()
    plt.style.use('seaborn')
    plt.rcParams["figure.figsize"] = (27,13)
    dframe.plot(x="Date", y=["Tweets", "Users"], kind="area", color=['y', 'b'], alpha=0.5,stacked=False)
    plt.suptitle(title,fontsize=35)
    plt.title(subtitle,fontsize=22)
    plt.xlabel('Days',fontsize=25)
    plt.ylabel('#of Tweets and Users',fontsize=25)
    plt.legend(loc=2,prop={'size': 20})
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.savefig(output)
    plt.show()
    return
