# 归并排序（Merging Sort）
# 采用递归方法实现归并排序

def merge(leftlist, rightlist):
    
    result = []  # 存储排序以后的结果
    i, j = 0, 0
    while i < len(leftlist) and j < len(rightlist):
        if leftlist[i] <= rightlist[j]:
            result.append(leftlist[i])
            i += 1
        else:
            result.append(rightlist[j])
            j += 1
    
    # 剩余元素复制到结果列表中
    result = result + leftlist[i:] + rightlist[j:]
    return result


def merge_sort(datalist):
    
    if len(datalist) == 0:
        return
    if len(datalist) == 1:
        return datalist
    
    mid = len(datalist)//2
    
    # 采用递归方法划分left/right
    left = merge_sort(datalist[:mid])
    right = merge_sort(datalist[mid:])
    
    return merge(left, right)
    
    
# 数据测试
if __name__ == "__main__":
    nums = [1, 0, 3, 4, 5, 6, 7]
    nums = merge_sort(nums)
    print(nums)
    