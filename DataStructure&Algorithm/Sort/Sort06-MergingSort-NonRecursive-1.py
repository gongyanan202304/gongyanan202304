# 归并排序（Merging Sort）
# 采用非递归方法实现归并排序
# 非递归方法与递归方法设计的脚本的最大的差别在于，left/right 2个子序列的划分方法不同

# 合并程序设计
def merge(datalist, low, mid, high):
    result = []  # 存放有序数据列表
    left = datalist[low:mid]
    right = datalist[mid:high]
    i, j = 0, 0
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 剩余数据复制到结果列表中
    result += left[i:]
    result += right[j:]
    
    # 将调整好的结果赋给列表（局部有序）
    datalist[low: high] = result


# 合并排序程序设计
def mergingsort(datalist):
    step = 1  # 步长初始值为1
    while step < len(datalist):
        low = 0
        while low < len(datalist):
            mid = low + step
            high = min(mid + step, len(datalist))
            if mid < high:
                merge(datalist, low, mid, high)  # 局部有序
                
            low += 2 * step  # 下一组列表合并的开始位置
        
        step *= 2  # 下一轮合并步长
        
    return datalist  # 返回全局有序
  

#  主程序
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 2, 4, 6, 8, 0]
    print(mergingsort(nums))
