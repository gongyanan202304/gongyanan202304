# 桶排序（Bucket Sort）
# 桶排序的原理：
# （1）假设待排序的数据列表中的数据是均匀分布的；
# （2）将待排序的数据分到有限的桶中；
# （3）每个桶再分别排序（有可能使用其它的排序算法，或者使用递归方法对桶中的数据进行桶排序）；
# （4）在额外空间足够的情况下，尽量使用增大桶的数量；
# （5）使用的映射函数能够将输入的N个数据均匀的分配到K个桶中。


# 桶排序的关键字：
# 桶、映射函数、均匀


# 桶排序的算法步骤：
# （1）设置桶数量BucketSize，作为每个桶存放数据值的个数；
# （2）遍历输入函数，将数据依次映射到对应的桶中；
# （3）对每个非空桶中的数据进行排序（可以使用其它的排序方式或者桶排序的递归方法）；
# （4）从非空的桶中，把已经排好序的数据拼接起来，并输出。


# 桶排序的程序设计：

# 1-插入排序（辅助排序）
def insertionsort(datalist):
    """插入排序，升序排列"""
    lenght = len(datalist)
    
    for i in range(1, lenght):
        newdata = datalist[i]  # 新的数据元素
        curindex = i - 1  # 有序序列中的最后一个元素的索引位置
        curdata = datalist[curindex]  # 有序序列中的最后一个元素（有序序列中第一个与新元素比较的元素）
        while curindex >= 0 and newdata <= curdata:
            # 序列元素向索引较大方向移动1位
            datalist[curindex + 1] = datalist[curindex]
            curindex -= 1
            # 当前元素
            curdata = datalist[curindex]
        # 在新元素大于或者等于当前元素的索引位置的高一位处添加新元素
        datalist[curindex + 1] = newdata
    
    return datalist


# 分桶排序程序设计
def bucketsort(numberlist):
    """分桶排序"""

    # 1-求数字列表的元素个数length
    length = len(numberlist)
    if length == 0 and length == 1:
        return numberlist
    
    # 2-求最值max/min与极差range
    maxnumb = max(numberlist)
    minnumb = min(numberlist)
    
    numberrange = maxnumb - minnumb

    base = numberrange//5  # 以极差的1/5为一个分段即为一个桶

    # 3-求桶的数量与均分个数
    buckets = numberrange // base + 1
    
    # 4-构建桶
    bucket = [[] for _ in range(buckets)]
    
    for numb in numberlist:
        # 确定数据元素要进入的桶编号，并进行插入排序
        pos = (numb - minnumb) // base
        bucket[pos].append(numb)
    
    # 5-清空数据列表
    numberlist.clear()
    
    # 6-有序的子桶的数据写入到数据列表中
    for item in bucket:
        item = insertionsort(item)
        numberlist += item
    
    return numberlist


# 主函数
if __name__ == "__main__":
    nums = [3, 4, 5, 2, 1, 0, 6, 9, 10, 23, 45, 34, 36, 38]
    print('>>bucketsort:')
    print(bucketsort(nums))
    