from spark_client import SparkClient

spark = SparkClient().create("raw_crypo_spark_job")

print(spark.version)
