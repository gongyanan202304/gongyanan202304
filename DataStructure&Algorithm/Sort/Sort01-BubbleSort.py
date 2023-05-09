# 排序-冒泡排序算法
# 期望的顺序：升序排序
# 经过k轮排序以后，数据列表的最后k个元素是已经排序好的元素，
# 因为数据列表中的最后k个元素是整个数据列表中的前k个最大的元素。所以在内层循环的数据范围是逐渐缩小的。

# 冒泡排序算法设计
def bubblesort(datalist):
    if len(datalist) == 0 or len(datalist) == 1:
        return datalist
    
    # 排序数据列表的长度
    length = len(datalist)
    for i in range(0, length):
    
        for j in range(0, length-1-i):  # 注意内层多轮比较与移动元素的关键点
            
            if datalist[j] > datalist[j+1]:
                datalist[j], datalist[j+1] = datalist[j+1], datalist[j]

    return datalist
    

# 数据测试
arr = [5, 3, 4, 6, 2, 1, 0, 9, 8, 7, 12, 13, 15, 20, 21, 22, 34, 32, 33, 31]
print(bubblesort(arr))
