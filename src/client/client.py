from elasticsearch import Elasticsearch


def get_default_es_client(es_addr):
    client = Elasticsearch("localhost:9200")


def get_es_client(es_addr):
    """
    :param es_addr: host:port 
                    [host1:port,host2:port]
                    ['http://user:secret@host1:port','http://user:secret@host1:port']
    :return: client
    """
    client = Elasticsearch(es_addr)
    return client


def get_connections_client(hosts=["localhost:9200"], maxsize=25):
    # allow up to 25 connections to each node
    client = Elasticsearch(hosts, maxsize)
    return client