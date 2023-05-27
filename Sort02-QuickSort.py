# 快速排序（quick sort）
# 快速排序的基本思想：
#   通过一趟排序将待排的序列分隔成独立的两部分，
#   其中一部分记录的元素均比另外一部分的元素小，
#   则可以对这两部分子序列继续进行排序，以达到整个序列的有序。

# 快速排序的基本步骤：
#   快速排序使用分治策略来把一个序列分为较小和较大的2个子序列，
#   然后递归的排序两个子序列。
#   步骤如下：
#      （1）从序列中随机挑选一个元素，作为"基准"（pivot）；
#      （2）重新排序序列，将所有比基准值小的元素摆放在基准前面，
#           所有比基准值大的元素摆在后面（相同的元素可以在前面，也可以在后面）
#      （3）递归地把小于基准值元素的子序列、大于基准值元素的子序列，分别进行快速排序。


# 快速排序的程序设计：

def quicksort(datalist):
    if len(datalist) <= 1:
        return datalist
    pivot = datalist[0]  # 取第一个元素作为基准值
    
    # 生成左右两个子序列
    left = [datalist[i] for i in range(1, len(datalist)) if datalist[i] < pivot]
    right = [datalist[i] for i in range(1, len(datalist)) if datalist[i] >= pivot]
    
    # 递归方法实现
    return quicksort(left) + [pivot] + quicksort(right)


# 数据测试
if __name__ == "__main__":
    nums = [2, 4, 3, 5, 9, 6, 7]
    print(quicksort(nums))

# 思考：
# （1）快速排序，我们容易理解为这个排序算法是最快的，而其它排序算法没有这个算法快，
#     实际上，并不是这样的，比这个算法快的排序算法还有基数排序等非比较类型的排序算法，时间复杂度在O(n)级别；
# （2）快速排序，其实是参照基准数据来实现排序，即选择一个基准数据来进行数据大小比较。
