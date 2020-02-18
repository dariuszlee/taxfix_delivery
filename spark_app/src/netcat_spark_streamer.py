import sys
import json
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from heapq import nlargest
from spark_streamer_service import line_to_json, saveStateFunc, INVALID_EVENT

es_write_conf = {
        "es.nodes" : '0.0.0.0',
        "es.port" : '9200',
        "es.resource" : 'spark/data',
        "es.input.json" : "yes",
        "es.mapping.id": "Id",
        }

def main():
    conf = SparkConf().setAppName("NetCatLineStreamer")\
            .set("es.index.auto.create", "true")
    sc = SparkContext(conf = conf)

    ssc = StreamingContext(sc, 2)
    ssc.checkpoint("stream")
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
   
    parsed_input = lines.map(line_to_json)
    parsed_input = parsed_input.filter(lambda x: x[0] != INVALID_EVENT[0])
    save_stated = parsed_input.updateStateByKey(saveStateFunc)
    save_stated_formatted = save_stated.map(lambda x: (x[0], 
        json.dumps({"Id": x[0], "Urls":[{"Url":url, "Time": time} for url, time in x[1]]})))

    save_stated_formatted.foreachRDD(lambda rdd: rdd.saveAsNewAPIHadoopFile(
            path='-', 
            outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
            keyClass="org.apache.hadoop.io.NullWritable",
            valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
            conf=es_write_conf))

    ssc.start()
    ssc.awaitTermination() 

if __name__ == '__main__':
    print("Starting python file")
    main()
