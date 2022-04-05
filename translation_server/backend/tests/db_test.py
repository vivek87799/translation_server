
from datetime import datetime
import asyncio
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk

es = AsyncElasticsearch('http://gs-search:9200/')

doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
doc1 = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
doc2 = {
    'author': 'author_name1',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}

async def main():
    resp = await es.index(
        index="test-index",
        id=1,
        document=doc,
    )
    resp = await es.index(
        index="test-index",
        id=2,
        document=doc1,
    )
    resp = await es.index(
        index="test-index",
        id=3,
        document=doc2,
    )
    # print(resp)

    resp = await es.search(index="tmx_data", query={"match_all": {}})
    print("Got %d Hits:" % resp['hits']['total']['value'])
    for hit in resp['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        print(rest)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
