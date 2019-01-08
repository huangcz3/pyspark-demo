# def multiply(n1, n2, result=None):
#     arr = []
#     for i in range(len(n1) + len(n2)):
#         arr.append(0)
#
#     for x in range(len(n1)):
#         for y in range(len(n2)):
#             arr[x + y] += int(n1[x]) * int(n2[y])
#
#     for i in range(len(arr) - 1, -1, -1):
#         arr[i - 1] = arr[i - 1] + arr[i] / 10
#         arr[i] = arr[i] % 10
#
#     result = ""
#
#     for j in range(len(arr) - 1):
#         result += str(arr[j])
#
#     return result
#
#
# if __name__ == '__main__':
#     print(1234*12345)
#     print(multiply("1234", "12345"))
from psutil._compat import xrange


def mul(n1,n2):
    n1.reverse()
    n2.reverse()
    n3=[]
    print(n1, n2)
    for i0 in xrange(len(n1)+len(n2)):
        n3.append(0)
    for i1 in xrange(len(n1)):
        for i2 in xrange(len(n2)):
            n3[i1+i2] += n1[i1]*n2[i2]
    for i3 in xrange(len(n3)):
        if(n3[i3]>9):
            n3[i3+1] += n3[i3]/10
            n3[i3] = n3[i3]%10
    n3.reverse()
    return n3


print(mul([2, 4, 5, 6, 6], [4, 5, 2, 0, 5, 3]))
