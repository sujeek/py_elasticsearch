#-*- encoding=utf-8 -*-

import random

from elasticsearch import Elasticsearch
from elasticsearch import helpers

client = Elasticsearch("localhost:9200")

levels = ['info', 'debug', 'warn', 'error']
actions = []
for i in range(100):
    level = levels[random.randrange(0, len(levels))]
    action = {'_op_type': 'index',  # 操作 index update create delete  
              '_index': 'log_level',
              '_type': 'doc',
              '_source': {'level': level}}
    actions.append(action)

# 使用bulk方式
helpers.bulk(client=client, actions=actions)

# streaming_bulk与parallel_bulk类似  需要遍历才会运行
# 都可以设置每个批次的大小，parallel_bulk还可以设置线程数
# for ok,response in helpers.streaming_bulk(es,actions):
#       if not ok:
#             print(response)

print client.indices.exists('log_level')