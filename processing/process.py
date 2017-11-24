
import pandas as pd
import os
import csv

def execute(inputdir='./Bulk', file='BulkFile-Demo.csv', output='processed'):

    filepath = inputdir + os.sep + file
    for subdir, dirs, files in os.walk(inputdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".csv"):
                print('Reading file: %s' % (subdir + os.sep + file))

    df=pd.read_csv(filepath)

    tweetSeries=df.groupby(['date_at','hour_at'])['tweet_id'].unique()
    userSeries=df.groupby(['date_at','hour_at'])['user_id'].unique()

    summList=[]
    for row in userSeries.iteritems():
        myStr=','.join(str(e) for e in list(row[0])) +',' +str(len(row[1]))
        summList.append(myStr)


    with open("./Final-files/"+output+"-users.csv", "w+") as csvfile:
        myfile = csv.writer(csvfile, quoting=csv.QUOTE_NONE,quotechar='',escapechar=' ')

        for row in userSeries.iteritems():
            myStr=','.join(str(e) for e in list(row[0])) +',' +str(len(row[1]))
            #myStr = myStr.replace('"', '')
            summList.append(myStr)
            myfile.writerow([myStr])

        csvfile.close()


    with open("./Final-files/"+output+"-tweets.csv", "w+") as csvfile:
        myfile = csv.writer(csvfile, quoting = csv.QUOTE_NONE,quotechar='', escapechar=' ')

        for row in tweetSeries.iteritems():
            myStr=','.join(str(e) for e in list(row[0])) +',' +str(len(row[1]))
            summList.append(myStr)
            myfile.writerow([myStr])

        csvfile.close()

    return True