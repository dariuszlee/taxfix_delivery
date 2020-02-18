#!/usr/bin/env bash

if [ -z $1 ];then
    PYTHON_VERSION=3.7
else
    PYTHON_VERSION=$1
fi

if [ -z $2 ];then
    ELASTIC_HOST=localhost
else
    ELASTIC_HOST=$2
fi

while [ true ];do
    echo "Waiting in elastic service at: $ELASTIC_HOST"
    curl -s $ELASTIC_HOST:9200 > /dev/null
    if [[ $? == 0 ]]; then
        break
    fi
    sleep 2
done

export PYSPARK_PYTHON=/usr/bin/python$PYTHON_VERSION
export PYSPARK_DRIVER_PYTHON=/usr/bin/python$PYTHON_VERSION

# Necessary on my system. Not in docker...
export HADOOP_HOME=/usr/lib/hadoop-3.2.1/

# ENSURE JAVA VERSION IS 8

echo "Starting spark..."
spark-submit --py-files "src/spark_streamer_service.py" --packages org.elasticsearch:elasticsearch-hadoop:7.6.0 --master local[2] src/netcat_spark_streamer.py localhost 2000 $ELASTIC_HOST
