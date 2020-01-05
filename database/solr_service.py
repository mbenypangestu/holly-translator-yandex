import pysolr
from SolrClient import SolrClient


class SolrService:
    def __init__(self):
        uri = "http://localhost:8983/solr"
        # self.uri = "http://10.252.175.133:8983/solr"
        self.solr = None

        self.connect_solr()

    def connect_solr(self):
        try:
            # self.solr = SolrClient(self.uri)
            self.solr = pysolr.Solr(self.uri, timeout=10)
            print("Success connecting to Solr !\n")

            self.solr.add([
                {
                    "id": "doc_1",
                    "title": "A very small test document about elmo",
                }
            ])
            # self.solr.ping()
        except:
            print("Failed to connect Solr !\n")

    def getCollection(self, collection, doc_id):
        try:
            res = self.solr.get(collection, doc_id)
            return res.get_results_count()
        except:
            print("Failed to get collection")
