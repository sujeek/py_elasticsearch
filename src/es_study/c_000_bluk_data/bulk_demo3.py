# -*- encoding=utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# The bulk() api accepts index, create, delete, and update actions.
# Use the _op_type field to specify an action (_op_type defaults to index):

from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")
print client

index = "news"
type = "title"

# 如果index存在先删除
print client.indices.delete(index, ignore=[400, 404])

# 创建索引
print client.indices.create(index, ignore=400)

mapping = {
    "properties": {
        'doc': {
            "properties": {
                "content": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                }
            }
        }
    }
}

# 设置mapping
client.indices.put_mapping(doc_type=type, body=mapping, index=index)


# 生成数据
def gendata():
    mywords = [{"content": "向着更高水平的平安中国法治中国接续奋斗"},
               {"content": "麦当劳失去“巨无霸”商标独家使用权"},
               {"content": "政法工作四大任务怎么干?习近平这样部署"},
               {"content": "让华北明珠重绽风采  河北雄安新区总体规划解读"},
               {"content": "以史鉴今 把握新时代造就高素质干部队伍规律"},
               {"content": "商务部：刘鹤副总理将于1月30日至31日访美"},
               {"content": "A股三大股指全线下挫，创业板指跌超1% 煤炭板块逆市走强"},
               {"content": "房地产老板竟成这些人的“摇钱树” 还能接手整个楼盘"},
               {"content": "约六成台湾民众不满民进党当局大陆政策"},
               {"content": "经销商确实存在夸大宣传"},
               {"content": "赵薇承担连带赔偿责任"},
               {"content": "旧鞋也被低价卖出"},
               {"content": "网易考拉加拿大鹅纠纷一波三折"},
               {"content": "德国法院驳回高通对苹果的最新专利诉讼"},
               {"content": "董明珠：未来十年 空调老大的地位是不会变的"},
               {"content": "康丽数码获得香港数码印刷大奖2018银奖"},
               {"content": "美国留给伊拉克的是个烂摊子吗"},
               {"content": "美国留给伊拉克的是个烂摊子吗"}]
    for word in mywords:
        yield {
            "_op_type": "index",
            "_index": index,
            "_type": type,
            "doc": word
        }


# 插入数据
client.helpers.bulk(client, gendata())

# 检查索引是否存在
print client.indices.exists(index)