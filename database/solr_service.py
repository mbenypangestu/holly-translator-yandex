import pysolr
from SolrClient import SolrClient


class SolrService:
    # uri = "http://10.252.175.134:8983/solr"
    uri = "http://localhost:8983/solr"
    solr = None

    def __init__(self):
        self.connect_solr()

    def connect_solr(self):
        try:
            self.solr = SolrClient(self.uri)
            print("Success connecting to Solr !\n")
            # self.solr.ping()
        except:
            print("Failed to connect Solr !\n")
