# -*- encoding=utf-8 -*-

# The bulk() api accepts index, create, delete, and update actions.
# Use the _op_type field to specify an action (_op_type defaults to index):

from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")
print client

index = "forum"
type = "article"

print client.indices.exists(index)

# bool：must，must_not，should，组合多个过滤条件

body = {
    "query": {
        "constant_score": {
            "filter": {
                "bool": {
                    "should": [
                        {"term": {"doc.postDate": "2017-01-01"}},
                        {"term": {"productID": "XHDK-A-1293-#fJ3"}}
                    ]
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