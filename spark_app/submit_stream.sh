#!/usr/bin/env bash

if [ -z $1 ];then
    PYTHON_VERSION=3.7
else
    PYTHON_VERSION=$1
fi

# 
export PYSPARK_PYTHON=/usr/bin/python$PYTHON_VERSION
export PYSPARK_DRIVER_PYTHON=/usr/bin/python$PYTHON_VERSION

# Necessary on my system. Not in docker...
export HADOOP_HOME=/usr/lib/hadoop-3.2.1/

# ENSURE JAVA VERSION IS 8

echo "Starting spark..."
spark-submit --py-files "src/spark_streamer_service.py" --packages org.elasticsearch:elasticsearch-hadoop:7.6.0 --master local[2] src/netcat_spark_streamer.py localhost 2000
