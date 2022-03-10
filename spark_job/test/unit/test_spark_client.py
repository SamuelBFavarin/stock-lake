from spark_client import SparkClient


def test_create_spark_client():
    spark_client_app_name = "test_spark_job"
    spark = SparkClient().create(spark_client_app_name)
    assert spark.appName == spark_client_app_name
