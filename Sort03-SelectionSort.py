# 选择排序（selection sort）
# 选择排序的原理：
#   选择排序是一种简单直观的排序算法，无论什么数据进去都是O(N^2)的时间复杂度。
#   所以用到这个排序算法的时候，数据规模越小越好，唯一的优点是不需要额外占据内存空间。
#   在未排序的序列中找到最大或者最小的元素，存放到排序序列的起始位置，
#   再从剩余未排序元素中继续找到最大或最小元素，然后放到已经排序的序列的末尾。
#   以此类推，直到所有元素均排序完毕。

# 选择排序的步骤：
#   （1）在未排序的序列中找到最小或最大的元素，存放到排序序列的起始位置；
#   （2）从剩余未排序的序列中继续寻找最大或最小的元素，然后放到已排序的序列的末尾。
#   （3）重复步骤（2），直到所有元素均排序完成。


# 选择排序算法程序设计

def selectionsort(datalist):
    length = len(datalist)
    for i in range(0, length-2):
        # 初始化列表的最大值
        maxval = datalist[i]
        # 初始化列表的最大值的索引位置
        maxidx = i
        # 循环遍历未排序的列表元素，并记录下最大值和其对应的索引位置
        for j in range(i+1, length):
            if datalist[j] > maxval:
                maxval = datalist[j]
                maxidx = j
        # 从未排序的列表中弹出最大值
        maxval = datalist.pop(maxidx)
        # 将最大值插入到已经将排序的序列的末尾
        datalist.insert(i, maxval)  # 降序排列
    # 返回已经排序的数据列表
    return datalist


# 数据测试
nums = [8, 2, 3, 4, 8, 1, 5, 6, 7, 7]

print(selectionsort(nums))
