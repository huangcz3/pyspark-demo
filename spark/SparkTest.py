from pip._vendor.pyparsing import col
from pyspark.sql import SparkSession

import config.spark_config

from pyspark import SparkContext, Row

sc = SparkContext()
spark = SparkSession(sc)

# input_data = sc.parallelize([['a', 1], ['b', 2], ['b', 3], ['c', 4], ['a', 5], ['b', 6]])
#
#
# print(input_data.getNumPartitions())
# print(input_data.glom().collect())
# print(input_data.collect())


# textFile = sc.textFile("D:\logs\spring-boot-mybatis\spring-boot-mybatis.log")
# df = textFile.map(lambda r: Row(r)).toDF(["line"])
# errors = df.filter(col("line", df).like("%ERROR%"))
# # Counts errors mentioning MySQL
# errors.filter(col("line", df).like("%MySQL%")).count()
# # Fetches the MySQL errors as an array of strings
# errors.filter(col("line", df).like("%MySQL%")).collect()
#
# print(textFile.collect())
# print("errors.count()" + errors.count())

# def doubleIfOdd(x):
#     if x % 2 == 1:
#         return 2 * x
#     else:
#         return x
#
#
# numbersRDD = sc.parallelize(range(1, 10 + 1))
# print(numbersRDD.collect())
#
# # 映射，并将数字x转为x的2次方
# squareRDD = numbersRDD.map(lambda x: x ** 2)
# print(squareRDD.collect())
#
# # 筛选出满足和2取模为0的数
# filterRDD = numbersRDD.filter(lambda x: x % 2 == 0)
# print(filterRDD.collect())
#
# # flatMap() 对RDD中的item执行同一个操作以后得到一个list，然后以平铺的方式把这些list里所有的结果组成新的list
# sentencesRDD = sc.parallelize(['Hello, world', 'My name, is Patrick'])
# flatMapRDD = sentencesRDD.flatMap(lambda sentence: sentence.split(" "))
# print(flatMapRDD.collect())
# print(flatMapRDD.count())
#
# mapRDD = sentencesRDD.map(lambda sentence: sentence.split(" "))
# print(mapRDD.collect())
# print(mapRDD.count())
#
# resultRDD = numbersRDD.map(doubleIfOdd).filter(lambda x: x > 6).distinct()
# print("= = = = = = = = = = = = = = =")
# print(resultRDD.collect())


# testList = ["Hello hello", "Hello New York", "York says hello"]
#
# rdd = sc.parallelize(testList)
# resultRDD = rdd.flatMap(lambda ele: ele.split(" ")) \
#     .map(lambda word: word.lower())\
#     .map(lambda word: (word, 1))\
#     .reduceByKey(lambda x, y: x + y)
# print(resultRDD.collect())
# print(resultRDD.countByValue())
#
#
# print(resultRDD.collectAsMap())
#
# print(resultRDD.sortByKey(ascending=True).take(3))


# # 初始化两个RDD
# numbersRDD = sc.parallelize([1, 2, 3])
# moreNumbersRDD = sc.parallelize([2, 3, 4])
#
#
# # print(numbersRDD.union(moreNumbersRDD).collectAsMap())
# # 并集
# print(numbersRDD.union(moreNumbersRDD).collect())
# # 交集
# print(numbersRDD.intersection(moreNumbersRDD).collect())
#
# # 差集
# print(numbersRDD.subtract(moreNumbersRDD).collect())
#
# # 笛卡尔积
# print(numbersRDD.cartesian(moreNumbersRDD).collect())


# Home of different people
homesRDD = sc.parallelize([
    ('Brussels', 'John'),
    ('Brussels', 'Jack'),
    ('Leuven', 'Jane'),
    ('Antwerp', 'Jill'),
])

# Quality of life index for various cities
lifeQualityRDD = sc.parallelize([
    ('Brussels', 10),
    ('Antwerp', 7),
    ('RestOfFlanders', 5),
])


print("join操作：= = = = =", homesRDD.join(lifeQualityRDD).collect())

sc.stop()
