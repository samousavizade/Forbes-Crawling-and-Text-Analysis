import pymongo
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings

class MongoDBPipeline:

    collection_name = 'Forbes Articles'

    def __init__(self,):
        settings = get_project_settings()
        self.mongo_host = settings["MONGODB_SERVER"]
        self.mongo_port = settings["MONGODB_PORT"]
        self.mongo_db = settings["MONGODB_DB"]
        self.mongo_collection = settings["MONGODB_COLLECTION"]

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_host, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item