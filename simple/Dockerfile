FROM quay.io/jupyter/pyspark-notebook:latest

USER root
RUN curl -O https://downloads.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.5-bin-hadoop3.tgz -C /opt && \
    ln -s /opt/spark-3.5.5-bin-hadoop3 /opt/spark && \
    rm spark-3.5.5-bin-hadoop3.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

USER $NB_UID