from spark_client import SparkClient

spark = SparkClient().create("raw_crypo_spark_job")

if __name__ == "__main__":
    print(spark.appName)
