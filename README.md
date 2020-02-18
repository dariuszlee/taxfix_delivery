# Taxfix Coding Test

## Quick Start with integration test

NOTE: Ensure port 9200 is free.

1. Run `docker-compose up`
2. When you see an endless repeating stream run:
    `docker exec -ti sparkstreamer bash -c "cat testData/test_jsons.json | ncat -l -p 2000"`
3. Run `python3 test_api.py`

NOTE pip3 install requests is required for test.

## Opening netcat server input and testing input
1. Run: `docker exec -ti sparkstreamer ncat -l -p 2000`
2. Input or copy data and press enter.

## ElasticSearch Location
1. The index is located at localhost:9200/spark/data
    a. Example query: curl http://localhost:9200/spark/data_search\?q\=Id:2

## Assumptions:
1. Id and Time must be valid integers
    a. Time is the sorting key. It does not matter when the event arrives to the application but by what the value is in Time.
2. Url must be a 'valid' url. (Parseable by urlparse in python standard library)
3. elasticsearch delete and post operations will not function correctly. This is because the SparkStreamer is checkpointing against local files, not elastic search.
