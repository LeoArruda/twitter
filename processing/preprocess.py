import pandas as pd
import string
import os
from nltk.corpus import stopwords

def Cleaning(dframe):
    # Remove punctuation
    dframe["text"]=dframe["text"].replace('[^{}]'.format(string.printable), ' ', regex=True)
    dframe["text"]=dframe["text"].replace('[^\w\s]'.format(string.printable),' ', regex=True)
    # Remove punctuation
    dframe["text"]=dframe["text"].replace('\d+'.format(string.printable), ' ', regex=True)
    # Remove linebreak, tab, return
    dframe["text"]=dframe["text"].replace('[\n\t\r]+',' ', regex=True)
    # Remove multiple whitespace  
    dframe["text"]=dframe["text"].replace('\s+\s+', ' ', regex=True)
    #dframe["SMS"]=dframe["SMS"]
    # SMS messages To lowercase 
    dframe["text"]=dframe["text"].str.lower().str.split()
    # Remove Stopwords
    stop = stopwords.words('english')
    dframe["text"] = dframe["text"].apply(lambda x: [item for item in x if item not in stop])
    dframe["date_at"]=[d.date() for d in dframe["created_at"]]
    dframe["time_at"]=[d.time() for d in dframe["created_at"]]
    dframe["hour_at"]=dframe.created_at.dt.hour
    return dframe


def execute(inputdir='./to_process', outputdir='./CSV', outputfile='./Bulk/BulkFile'):

    bulkDF=pd.DataFrame()
    for subdir, dirs, files in os.walk(inputdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                print('Reading file: %s' % (subdir + os.sep + file))
                df = pd.read_json(filepath)
                df = Cleaning(df)
                outpath = outputdir + os.sep + file + '.csv'
                print ('Saving %s ' %outpath )
                df.to_csv(outpath,columns=['date_at','time_at','hour_at','tweet_id','user_id','user_name','text'],index=False)
                bulkDF=bulkDF.append( df, ignore_index = True)
                df=''
    bulkDF.to_csv(outputfile+'.csv',columns=['date_at','time_at','hour_at','tweet_id','user_id','user_name','text'],index=False)

    return