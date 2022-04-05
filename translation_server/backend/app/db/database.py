#!/usr/bin/env python3
from elasticsearch import AsyncElasticsearch

from typing import List
from app.db.config import Parameters


class ElasticsearchClient:
    es = AsyncElasticsearch(Parameters.ES_BROKER)
    """
    @staticmethod
    def get_conneciton():
        print("<===Connection established===>")
        # es_client = AsyncElasticsearch(Parameters.ES_BROKER)
        while True:
            yield AsyncElasticsearch(Parameters.ES_BROKER)
    """
if __name__ == '__main__':
    app.main()