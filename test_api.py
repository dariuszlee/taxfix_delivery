import requests

res = requests.get('http://localhost:9200/spark/data/_search?q=Id:3')
end_data = res.json()['hits']['hits'][0]['_source']["Urls"]

expected = [
    {"Url": "https://test6.com", "Time": 123557},
    {"Url": "https://test9.com", "Time": 123558},
    {"Url": "https://test8.com", "Time": 123559},
    {"Url": "https://test4.com", "Time": 123458},
    {"Url": "https://test5.com", "Time": 123459}
        ]

assert len(end_data) == 5
for e in expected:
    try:
        assert e in end_data
    except Exception as ex:
        print(e, end_data)
        raise AssertionError()


print("Tests passed successfully")
