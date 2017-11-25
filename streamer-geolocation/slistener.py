from tweepy import StreamListener
import json, time, sys


class SListener(StreamListener):
    def __init__(self, api=None, fprefix='streamer'):
        # self.api = auth
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
        #print(json.dumps(myData,indent=4, sort_keys=False,separators=(',', ': '), ensure_ascii=False))
        if((status.find('Stranger Things') != -1) or \
                   (status.find('Stranger_Things') != -1) or \
                   (status.find('stranger_things') != -1) or \
                   (status.find('strangerthings') != -1) or \
                   (status.find('StrangerThings') != -1) or \
                   (status.find('stranger things') != -1) ):
            #print(myData["text"])
            json_data = {"created_at": myData["created_at"],
                         "text": myData["text"],
                         "tweet_id": myData["id"],
                         "user_id": myData["user"]["id"],
                         "user_name": myData["user"]["name"],
                         "city": myData["place"]["full_name"],
                         "country": myData["place"]["country"],
                         "longitude_a": myData["place"]["bounding_box"]["coordinates"][0][0][0],
                         "latitude_a": myData["place"]["bounding_box"]["coordinates"][0][0][1],
                         "longitude_b": myData["place"]["bounding_box"]["coordinates"][0][1][0],
                         "latitude_b": myData["place"]["bounding_box"]["coordinates"][0][1][1]}
            self.output.write(json.dumps(json_data,
                               indent=4, sort_keys=False,
                               separators=(',', ': '), ensure_ascii=False))
            print(json.dumps(json_data, indent=4, sort_keys=False, separators=(',', ': '), ensure_ascii=False))
            #self.output.writelines(json.dumps(json_data))
            self.output.flush()
            self.counter += 1
            print(self.counter)
            if self.counter >= 300:  #due to the low ammount of tweets Im limiting the filesize for 300
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
