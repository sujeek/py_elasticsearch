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

body = {}