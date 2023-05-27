# 插入排序（insertion sort）
# 插入排序的基本思想：
#   插入排序是一种简单直观的排序算法，主要是构建有序的序列。
#   对于未排序的元素，则在已经排序的序列中，从后往前进行扫描，找到合适的位置，并插入该元素。

# 插入排序的基本步骤：
#   （1）从第一个元素开始，默认该元素已经排序；
#   （2）取下一个元素，在已经排序的元素序列中从后往前扫描；
#   （3）如果当前元素大于新元素，那么当前元素的下标往前移动；
#   （4）重复步骤（3）直到新元素大于或者等于当前元素，找到当前索引位置；
#   （5）将新元素插入到当前索引位置；
#   （6）重复步骤（2）（3）（4）（5），直到所有的元素插入到已经排序的序列中。


# 插入排序
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
        

# 主函数
if __name__ == "__main__":
    nums = [9, 5, 4, 8, 7, -1, 0, -2, 5, 6]
    print(insertionsort(nums))
    
    