# 折半查找（二分查找）（BinarySearch）

# 使用折半查找要求数据表是有序的数据表
# 二分查找也是一种有序查找

# 折半查找的基本思想：
#  （1）折半查找是在数据列表（有序表）中进行折半查找；
#  （2）从表的中间元素开始，与目标值进行比较；
#  （3）若相等时，则查找成功；若大于给定值，则在前半段区间进行折半查找；若小于给定值，则在后半段区间进行折半查找。
#  （4）当越界时，则表示查找失败。

# 折半查找的基本步骤：
# （1）求取有序表的位置指针low, mid, right;
# （2）比较mid(key) 与setvalue 的大小：
#       若相等，则查找成功；
#       若不相等，且mid(key)>setvalue, 则 low = low, high = mid -1, mid = (low + high)//2;
#       若不相等，且mid(key)<setvalue, 则 low = mid + 1, high = high, mid =  (low + high)//2;
#  (3) 当low > high 时，表示查找失败。


# 折半查找的程序设计：
def binarysearch(numblist, setvalue):
    if len(numblist) == 0:
        return
    low = 0  # 低位索引
    high = len(numblist) -1  # 高位索引
    mid = (low + high) // 2  # 中间位置索引
    
    while low <= high:
        if numblist[mid] == setvalue:
            return mid  # 返回中间位置索引
        elif numblist[mid] < setvalue:
            low = mid + 1
            high = high
            mid = (low + high) // 2
        else:
            low = low
            high = mid - 1
            mid = (low + high) // 2
    
    return False


# 主函数
if __name__ == "__main__":
    nums = [2, 3, 4, 5, 6, 7, 10, 11, 13, 15]
    print(binarysearch(nums, 15))
    