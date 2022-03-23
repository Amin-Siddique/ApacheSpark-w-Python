from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


spark = SparkSession \
    .builder\
    .appName("TwitterTesting") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

lines =  spark.readStream\
    .format("kafka")\
    .option("kafka.bootstrap.servers","localhost:9092")\
    .option("subscribe","awesome") \
    .load()

lines.printSchema()

words = lines.select(
    explode(
        split(lines.value," ")
    ).alias("word")
)


def extract_tag(word):
    if word.lower().startswith("#"):
        return word
    else:
        return "notag"

extract_tags_udf = udf(extract_tag,StringType())

resultDF = words.withColumn("tags",extract_tags_udf(words.word))

hashtagCountDf = resultDF.where(resultDF.tags != "notag") \
    .groupBy("tags")\
        .count() \
            .orderBy("count",ascending=False)


query = hashtagCountDf.writeStream\
    .outputMode("complete")\
        .format("console")\
            .option("truncate",False)\
                .start() \
                    .awaitTermination()
