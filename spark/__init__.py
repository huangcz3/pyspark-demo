import os
import sys

# Path for spark source folder

os.environ['SPARK_HOME'] = "D:\\hadoop\\spark-2.3.2-bin-hadoop2.7"

# Append pyspark to Python Path
sys.path.append("D:\\hadoop\\spark-2.3.2-bin-hadoop2.7/python/")


from pyspark.sql import SparkSession

sparkSession = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sparkContext = sparkSession.sparkContext