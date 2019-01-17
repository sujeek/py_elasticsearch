# -*- encoding=utf-8 -*-


from elasticsearch import Elasticsearch

es = client = Elasticsearch("localhost:9200")


index = 'test-index'

es.indices.create(index, ignore=400)

es.indices.delete(index, ignore=[400, 404])

es.indices.exists(index)

es.indices.open(index)

es.indices.close(index)

es.indices.flush(index)

# 查看指定index的mapping信息
es.indices.get_mapping(index=index)

# 查看所有索引
es.indices.get_alias()

# 查询所有index名称
es.indices.get_alias().keys()

# 查询index信息,包含mapping  settings信息
es.indices.get(index)