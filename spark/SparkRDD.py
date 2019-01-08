import config.spark_config

from pyspark import SparkContext

sc = SparkContext()


def parallelizeData(data):
    return sc.parallelize(data, 3)


if __name__ == '__main__':
    # data = [1, 2, 3, 4, 5]
    # print(parallelizeData(data).collect())
    #
    # a = range(1, 4)
    #
    # rdd = sc.parallelize(a).map(lambda x: (x, "a" * x))
    # rdd.saveAsSequenceFile("d:\\tmp\\test")
    # sorted(sc.sequenceFile("d:\\tmp\\test").collect())

    lines = sc.wholeTextFiles("d:\\tmp\\test")

    linesLength = lines.map(lambda x: len(x))
    totalLength = linesLength.reduce(lambda a, b: a + b)

    print(linesLength.collect())
    print(totalLength)

    sc.stop()
