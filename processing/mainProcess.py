import preprocess as pre
import process as pro
import plot_graph as plotG
import pandas as pd
import os

# Instructions:
# To run this code you need the following Folde structure
#     ./
#      |
#      |---- [to_process]   --> this must contain your json files
#      |---- [CSV]          --> after pre-processing files
#      |---- [Bulk]         --> one grouped file containing all csv
#      |---- [Final_files]  --> summary result files (Tweets & Users)
#


if __name__ == '__main__':

    # Pre processing
    # Will read all json files from input directory and will produce new files
    # after data cleaning.
    # Will also produce a Bulkfile containing all data.
    pre.execute()

    # Processing
    # Will read bulk file and calculate the number of tweets and users
    # found in each day.
    # The result is two csv files. Tweets and Users csv
    pro.execute()

    # Final merge of Tweets and Users Datasets
    # todo: Implement a for loop to cover all tweets and users csv files

    rootdir = './Final-files'
    file='processed-tweets.csv'
    filepath = rootdir + os.sep + file
    dfTweets=pd.read_csv(filepath, names=['Date', 'Hour', 'Tweets'])
    rootdir = './Final-files'
    file='processed-users.csv'
    filepath = rootdir + os.sep + file
    dfUsers=pd.read_csv(filepath, names=['Date', 'Hour', 'Users'])
    df=pd.merge(dfTweets, dfUsers, left_on=['Date', 'Hour'], right_on=['Date', 'Hour'])
    print(df.info())
    print()
    # This section is responsible to plot and save the Graphs
    plotG.plot_graph(df,'ResultsDemo.png','Tweets Comparison\nKey: DEMO')

# T H E   E N D



