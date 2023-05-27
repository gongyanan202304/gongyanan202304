# 插值查找（InsertionSearch）

# 插值查找的基本思想：
# 基于二分查找算法，将查找点修改为自适应选择，可以提高效率，也是一种有序查找。
# 计算中间值的方法： mid = low+ [(key-arr[low])/(arr[high]-arr[low])] * (high-low)
# 这种方法是将mid值更加靠近关键字key。

# 插值查找也是一种有序查找

# 插值查找程序设计：
def insertionsearch(datalist, setvalue):

    low = 0
    high = len(datalist) - 1
    mid = low + int(((setvalue - datalist[low])/(datalist[high] - datalist[low])) * (high - low))
    while low <= high and mid >= 0:
        if datalist[mid] == setvalue:
            return mid
        elif datalist[mid] > setvalue:
            high = mid - 1
        else:
            low = mid + 1
            
    return False


# 主函数
if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(insertionsearch(nums, 6))
