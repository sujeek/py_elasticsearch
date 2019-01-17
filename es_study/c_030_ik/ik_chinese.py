# -*- encoding=utf-8 -*-
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
# The bulk() api accepts index, create, delete, and update actions.
# Use the _op_type field to specify an action (_op_type defaults to index):

from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")
print client

index = "news"
type = "title"

body = {
    "query": {
        "match": {
            "doc.content": "美国"
        }
    },
    "highlight": {
        "pre_tags": ["<tag1>", "<tag2>"],
        "post_tags": ["</tag1>", "</tag2>"],
        "fields": {
            "content": {}
        }
    }
}


response = client.search(index=index, doc_type=type, body=body)

count = response["hits"]["total"]

print "获取总数:%s" % count

for hit in response["hits"]["hits"]:
    print json.dumps(hit).decode("unicode_escape")
    print json.dumps(hit.get("_source", {}).get("doc", {}).get("content", {})).decode("unicode_escape")

