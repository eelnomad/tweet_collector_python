import tweepy
import pymongo
import backend.config as cfg
import backend.mongo_utils as mongo


class TwitterListener(tweepy.StreamListener):
    def __init__(self, id):
        tweepy.StreamListener.__init__(self)
        self.collection = pymongo.MongoClient(cfg.mongo.get('host'), cfg.mongo.get('port'))['twitterDB'][id]

    def on_status(self, status):
        document = status._json['retweeted_status'] if 'retweeted_status' in status._json else status._json
        try:
            document['_id'] = document.pop('id')
            self.collection.find_one_and_replace({'_id': document['_id']}, document, upsert=True)
        except KeyError:
            print("### Missing ID")
        except Exception as e:
            print(e)

    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        print('### Track Notice: {}'.format(track))
        return

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


class TwitterStream:
    def __init__(self, id):
        print('### Stream Opening')
        self.id = id
        auth = tweepy.OAuthHandler(cfg.twitter.get('consumer_key'), cfg.twitter.get('consumer_secret'))
        auth.set_access_token(cfg.twitter.get('access_token'), cfg.twitter.get('access_token_secret'))
        api = tweepy.API(auth, wait_on_rate_limit=True)

        self.stream = tweepy.Stream(auth=api.auth, listener=TwitterListener(self.id))
        self.stream.filter(track=mongo.get_keywords(self.id), is_async=True)
        mongo.update_active_flag(self.id, True)
        print('### Stream Listening')

    def __del__(self):
        self.stream.disconnect()
        print('### Stream Closed')
        mongo.update_active_flag(self.id, False)
