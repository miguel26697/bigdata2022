from pyspark.sql import SparkSession
import pyspark.sql.functions as f


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
dfPrice=df2.select(f.min("Price").alias("PrecioMin"),
                    f.max("Price").alias("PrecioMax"))


query = dfPrice \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()