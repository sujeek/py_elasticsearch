# -*- encoding=utf-8 -*-

from elasticsearch import Elasticsearch

# 设置索引
index = 'test-index'
# 设置type
type = 'test-type'

es = client = Elasticsearch("localhost:9200")

print client.search(index, filter_path=['hits.hits._*'])

print client.search(index, filter_path=['hits.hits._id', 'hits.hits._type'])
