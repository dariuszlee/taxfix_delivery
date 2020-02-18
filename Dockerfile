# FROM bde2020/spark-submit:2.4.4-hadoop2.7
# FROM blacktop/elasticsearch:7.6
FROM elasticsearch:7.6.0

RUN yum install wget -y
RUN wget https://ftp.cc.uoc.gr/mirrors/apache/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
RUN tar -xzf spark-2.4.5-bin-hadoop2.7.tgz
RUN mv spark-2.4.5-bin-hadoop2.7 /spark
ENV PATH="/spark/bin:${PATH}"

RUN yum install python3 -y
RUN yum install java -y
RUN yum install nmap -y

COPY spark_app /spark_app
WORKDIR /spark_app

EXPOSE 2000
