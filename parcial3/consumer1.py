import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1'
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.sql.functions import when
import argparse
from pyspark.sql.types import IntegerType


parser =argparse.ArgumentParser()
parser.add_argument("--maximo",help ="maximo valor: ")
parser.add_argument("--minimo",help ="minimo valor: ")
arg = parser.parse_args()

if arg.maximo:
     maximo = arg.maximo
  
if arg.minimo:
     minimo= arg.minimo

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

lines = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","quickstart-events") \
    .option("batchDuration","10")\
    .load()

df=lines.withColumn("Price", f.conv(f.col("value"), 16, 16).cast("bigint"))


df2 = df.select("Price")
dfPrice=df2.select(f.min("Price").alias("minPrice").cast(IntegerType()),
                    f.max("Price").alias("maxPrice").cast(IntegerType()))

dfFinal1=dfPrice.withColumn("alertaMinimo", when(dfPrice.minPrice < minimo,"Debajo del minimo").otherwise("> minimo"))
dfFinal = dfFinal1.withColumn("alertaMaximo", when(dfPrice.maxPrice > maximo,"Arriba del maximo").otherwise("< maximo"))



query = dfFinal \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

query.awaitTermination()