from tweepy import StreamListener
import json, time, sys


class SListener(StreamListener):
    def __init__(self, api=None, fprefix='coindesk'):
        #fprefix='cryptocurrency'
        self.counter = 0
        self.fprefix = fprefix
        self.output = open('./output/' + fprefix + '_'
                           + time.strftime('%Y%m%d-%H%M') + '.json', 'w')
        self.output.write("[")


    def __del__(self):
        self.output.write("]")
        self.counter = 0

    def on_data(self, data):
        try:
            self.on_status(data)
        except TypeError as e:
            pass
        except BaseException as e:
            print("Error : %s" % str(e))
            return

    def on_status(self, status):
        myData = json.loads(status)
        #myCounter=self.counter
        #print(json.dumps(myData,indent=4, sort_keys=False,separators=(',', ': '), ensure_ascii=False))
        #print(myData["text"])
        json_data = {"created_at": myData["created_at"],
                     "text": myData["text"],
                     "tweet_id": myData["id"],
                     "user_id": myData["user"]["id"],
                     "user_name": myData["user"]["name"]}
        if self.counter != 0:
            self.output.write(",")

        self.output.write(json.dumps(json_data,
                                     indent=4, sort_keys=False,
                                     separators=(',', ': '), ensure_ascii=False))

        print(json.dumps(json_data['text'],sort_keys=False, separators=(',', ': '), ensure_ascii=False))
        #print(Tweets collected: " + myCounter)
        self.output.flush()
        self.counter += 1
        if self.counter >= 1000:  #due to the low ammount of tweets Im limiting the filesize for 300
            self.output.write("]")
            self.output.close()
            self.output = open('./output/' + self.fprefix + '_'
                               + time.strftime('%Y%m%d-%H%M') + '.json', 'w')
            self.output.write("[")
            self.counter = 0
        return

    def on_delete(self, status_id, user_id):
        self.delout.write(str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return
