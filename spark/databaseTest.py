import config.spark_config

from pyspark import SQLContext, SparkContext, SparkConf

sc = SparkContext()

sqlContext = SQLContext(sc)

url = "jdbc:mysql://rm-bp1485293ipwpg5ohlo.mysql.rds.aliyuncs.com:3306/auto_report?useUnicode=true&characterEncoding=utf8&useSSL=false"

df = sqlContext \
    .read \
    .format("jdbc") \
    .option("url", url) \
    .option("dbtable", 'test'). \
    option("user", "auto_report"). \
    option("password", "ZtkhVvuw3Jj3EDcc"). \
    load()

df.printSchema()

# Counts people by age
countsByAge = df.groupBy("name").count()
countsByAge.show()


