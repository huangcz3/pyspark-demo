import os
import sys

# Path for spark source folder
os.environ['SPARK_HOME'] = "D:\\hadoop\\spark-2.3.2-bin-hadoop2.7"

# Append pyspark to Python Path
sys.path.append("D:\\hadoop\\spark-2.3.2-bin-hadoop2.7/python/")

from pyspark.sql import SparkSession


# sparkSession = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()
#
# sparkContext = sparkSession.sparkContext


def testLocalHive(spark):
    student_list = [("zhangsan", "man", 18, "address 1"), ("lisi", "man", 15, "address 1"),
                    ("kevin", "women", 28, "address 2"), ("aaaa", "women", 17, "address 3")]
    # 创建DataFrame
    studentDF = spark.createDataFrame(student_list)
    # studentDF.show()
    studentTableDF = studentDF.withColumnRenamed("_1", "name") \
        .withColumnRenamed("_2", "sex") \
        .withColumnRenamed("_3", "age") \
        .withColumnRenamed("_4", "address")

    studentTableDF.select("*").filter("address like '%1%'").show()
    studentTableDF.select("*").show()
    studentTableDF.select("name", studentTableDF['age'] + 1).show()

    studentTableDF.filter("age > 21").show()
    studentTableDF.groupBy("age").count().show()

    # 将DataFrame注册为SQL临时视图，sparksql操作
    studentTableDF.createOrReplaceTempView("t_student")

    spark.sql("select name,sex,age,address from t_student where address like '%1%'").show()

    spark.sql("select count(1) as nums from t_student where address like '%1%'").show()

    spark.sql("show databases").show()

    # spark.sql("select name,sex,age,address from t_student").rdd.saveAsTextFile("test1")
    #
    # spark.sql("select name,sex,age,address from t_student").write.save("test1", format="csv")
    # .write.save("test", format="parquet")


if __name__ == '__main__':
    # $example on:init_session$
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL data source example") \
        .getOrCreate()
    # $example off:init_session$
    testLocalHive(spark)

    spark.stop()
