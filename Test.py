import config.spark_config
from operator import add

from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext('local')
    lines = sc.textFile('words.txt')
    counts = lines.flatMap(lambda x: x.split(',')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print ("%s: %i" % (word, count))

    sc.stop()
