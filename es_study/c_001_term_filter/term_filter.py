# -*- encoding=utf-8 -*-

# The bulk() api accepts index, create, delete, and update actions.
# Use the _op_type field to specify an action (_op_type defaults to index):

from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")
print client

index = "forum"
type = "article"

print client.indices.exists(index)

# print client.cluster.health(wait_for_status='yellow', request_timeout=1)

# body = {"query":{"match":{"doc.userID":1}}}
body = {
    "query": {
        "constant_score": {
            "filter": {
                "term": {
                    "doc.userID": 1
                }
            }
        }
    }
}

response = client.search(index=index, doc_type=type, body=body)

count = response["hits"]["total"]

print "获取总数:%s" % count

for hit in response["hits"]["hits"]:
    print hit["_source"]['doc']
