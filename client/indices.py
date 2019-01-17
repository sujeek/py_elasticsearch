# -*- encoding=utf-8 -*-

from elasticsearch import Elasticsearch

# 设置索引
index = 'test-index'
# 设置type
type = 'test-type'
# 设置实例 fields
fields = ["name"]
# 设置别名
name = "index-alias"
# mapping 这儿为空，可以自定义设置
mapping = {}

es = client = Elasticsearch("localhost:9200")

# 创建索引 忽略400错误
es.indices.create(index, ignore=400)

# 删除索引 忽略400 404错误
es.indices.delete(index, ignore=[400, 404])

# 检查索引是否存在
es.indices.exists(index)

# 检查索引下面的类型是否存在
es.indices.exists_type(index, type)

# 打开索引
es.indices.open(index)

# 关闭索引
es.indices.close(index)

# 索引刷新
es.indices.flush(index)

# 设置mapping
es.indices.put_mapping(doc_type=type, body=mapping, index=index)

# 查看指定index的mapping信息
es.indices.get_mapping(index=index)

# 索引别名是否存在
es.indices.exists_alias(index, name=None)

# 索引设置特定的别名
es.indices.put_alias(index, name)

# 查看所有索引别名
es.indices.get_alias()

# 删除别名
es.indices.delete_alias(index, name, params=None)

# 查询所有index名称
es.indices.get_alias().keys()

# 查询index信息,包含mapping  settings信息
es.indices.get(index)

# 检索特定字段的映射定义。
es.indices.get_field_mapping(fields, index=None, doc_type=None, params=None)