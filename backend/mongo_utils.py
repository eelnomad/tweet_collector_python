import pymongo
import backend.config as cfg
from bson import ObjectId


def create_collection(keywords, desc=None):
    organizer = pymongo.MongoClient(cfg.mongo.get('host'), cfg.mongo.get('port'))['twitterDB']['collectionOrganizer']

    normalized = sorted(list(set([' '.join(sorted(list(set(x.split(' '))))).lower() for x in keywords])))
    existing = organizer.find_one({'keywords': normalized})
    created = False
    if existing:
        id = existing.get('_id')
    else:
        id = organizer.insert_one({'keywords': normalized, 'desc': desc, 'active_flag': False}).inserted_id
        created = True
    return str(id), created


def update_description(id, description):
    organizer = pymongo.MongoClient(cfg.mongo.get('host'), cfg.mongo.get('port'))['twitterDB']['collectionOrganizer']
    organizer.update_one({'_id': id}, {'$set': {'desc': description}}, False)
    return id


def update_active_flag(id, value):
    organizer = pymongo.MongoClient(cfg.mongo.get('host'), cfg.mongo.get('port'))['twitterDB']['collectionOrganizer']
    organizer.update_one({'_id': ObjectId(id)}, {'$set': {'active_flag': value}}, False)
    return id


def get_keywords(id):
    organizer = pymongo.MongoClient(cfg.mongo.get('host'), cfg.mongo.get('port'))['twitterDB']['collectionOrganizer']
    result = None
    try:
        result = organizer.find_one({'_id': ObjectId(id)}).get('keywords')
    except:
        pass
    return result


def get_collections():
    organizer = pymongo.MongoClient(cfg.mongo.get('host'), cfg.mongo.get('port'))['twitterDB']['collectionOrganizer']
    documents = []
    for document in organizer.find({}):
        document['_id'] = str(document.pop('_id'))
        documents.append(document)
    return documents