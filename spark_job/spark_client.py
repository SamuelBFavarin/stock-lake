import findspark
findspark.init()

from pyspark import SparkContext  # noqa:E402


class SparkClient():

    def __init__(self) -> None:
        pass

    def create(self, app_name: str) -> SparkContext:
        return SparkContext(appName=app_name)
