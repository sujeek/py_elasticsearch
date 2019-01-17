# -*- encoding=utf-8 -*-

# The bulk() api accepts index, create, delete, and update actions.
# Use the _op_type field to specify an action (_op_type defaults to index):

from elasticsearch import Elasticsearch
from elasticsearch import helpers

client = Elasticsearch("localhost:9200")
print client

index = "forum"
type = "article"

# print client.indices.delete(index, ignore=[400, 404])

mapping = {
    'forum': {
        'mappings': {
            'article': {
                'properties': {
                    'doc': {
                        'properties': {
                            'userID': {
                                'type': 'long'
                            },
                            'hidden': {
                                'type': 'boolean'
                            },
                            'articleID': {
                                'fields': {
                                    'keyword': {
                                        'ignore_above': 256,
                                        'type': 'keyword'
                                    }
                                },
                                'type': 'text'
                            },
                            'postDate': {
                                'type': 'date'
                            }
                        }
                    }
                }
            }
        }
    }
}


#client.indices.create(index)
#client.indices.put_mapping(doc_type=type, body=mapping, index=index)


def gendata():
    mywords = [{"articleID": "XHDK-A-1293-#fJ3", "userID": 0, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "KDKE-B-9947-#kL5", "userID": 1, "hidden": False, "postDate": "2017-01-02"},
               {"articleID": "JODL-X-1937-#pV7", "userID": 2, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "XHDK-A-1293-#fJ3", "userID": 3, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "KDKE-B-9947-#kL5", "userID": 4, "hidden": False, "postDate": "2017-01-02"},
               {"articleID": "JODL-X-1937-#pV7", "userID": 5, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "XHDK-A-1293-#fJ3", "userID": 6, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "KDKE-B-9947-#kL5", "userID": 7, "hidden": False, "postDate": "2017-01-02"},
               {"articleID": "JODL-X-1937-#pV7", "userID": 8, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "XHDK-A-1293-#fJ3", "userID": 8, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "KDKE-B-9947-#kL5", "userID": 10, "hidden": False, "postDate": "2017-01-02"},
               {"articleID": "JODL-X-1937-#pV7", "userID": 11, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "XHDK-A-1293-#fJ3", "userID": 12, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "KDKE-B-9947-#kL5", "userID": 13, "hidden": False, "postDate": "2017-01-02"},
               {"articleID": "JODL-X-1937-#pV7", "userID": 14, "hidden": False, "postDate": "2017-01-01"},
               {"articleID": "QQPX-R-3956-#aD8", "userID": 15, "hidden": True, "postDate": "2017-01-02"}]
    for word in mywords:
        yield {
            "_op_type": "index",
            "_index": index,
            "_type": type,
            "doc": word
        }


# client.indices.create(index=index, ignore=400)
# print client.indices.delete(index, ignore=[400, 404])

# helpers.bulk(client, gendata())

print client.indices.exists(index)

# print client.cluster.health(wait_for_status='yellow', request_timeout=1)

# print client.search(index, filter_path=['hits.hits._*'])
# print client.search(index, filter_path=['hits.hits._id', 'hits.hits._type'])

# body = {"query":{"match":{"doc.userID":1}}}
body = {"query": {"constant_score": {"filter": {"term": {"doc.userID": 1}}}}}

# print client.indices.get_mapping(index=index)

response = client.search(index=index, doc_type=type, body=body)

for hit in response["hits"]["hits"]:
    print hit["_source"]['doc']
