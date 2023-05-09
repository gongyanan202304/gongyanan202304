# 采用非递归方法来设计快速排序算法

# 设计非递归的方式来实现快速排序的思想：
# （1）分解-合并


def getleftpivotright(left, pivot, right):
    """判定3个列表的长度与元素个数，生成有效的列表"""
    
    if len(left) == 0 and len(right) == 1:
        return [pivot, right[0]]
    
    elif len(right) == 0 and len(left) == 1:
        return [left[0], pivot]
    
    elif len(right) == 1 and len(left) == 1:
        
        return [left[0], pivot, right[0]]
    
    elif len(left) == 0 and len(right) >= 2:
        return [pivot, right]
    
    elif len(right) == 0 and len(left) >= 2:
        return [left, pivot]
    
    elif len(left) == 1 and len(right) >= 2:
        return [left[0], pivot, right]
    
    elif len(right) == 1 and len(left) >= 2:
        return [left, pivot, right[0]]
    
    else:
        return [left, pivot, right]


def dispersion_collection(datalist):
    """实现分散与收集的算法"""

    if len(datalist) == 0:
        return
    if len(datalist) == 1:
        return datalist
    
    length = len(datalist)
    
    pivot = datalist[0]
    left = [datalist[i] for i in range(1, length) if datalist[i] <= pivot]  # 小于或等于基准数据
    right = [datalist[j] for j in range(1, length) if datalist[j] > pivot]  # 大于基准数据
    
    result = getleftpivotright(left, pivot, right)
    
    return result


def quicksortnonr(datarry):
    """非递归方法实现快速排序"""
    maxlenght = len(datarry)
    
    # 对原始的数据列表进行"分散-收集"处理
    datalist = dispersion_collection(datarry)
    curlen = len(datalist)
    while curlen < maxlenght:  # 在循环的出口与入口之处设计的条件很巧妙
        # 循环遍历
        for i in range(len(datalist)):
            sublist = datalist[i]
            
            if isinstance(sublist, list) and len(sublist) >= 2:
                
                sortitem = dispersion_collection(sublist)
                
                if len(sortitem) == 2:
                    datalist.insert(i + 1, sortitem[0])
                    datalist.insert(i + 2, sortitem[1])
                
                if len(sortitem) == 3:
                    datalist.insert(i + 1, sortitem[0])
                    datalist.insert(i + 2, sortitem[1])
                    datalist.insert(i + 3, sortitem[2])
        
                datalist.pop(i)
                
        curlen = len(datalist)
    
    return datalist


# 数据测试
if __name__ == "__main__":

    nums = [27, 34, 43, 58, 65, 79, 86, 97, 100, 110, 112, 121, 211, 312, 333, 334, 335, 420, 423, 424, 425, 426]
    nums = sorted(nums, reverse=True)
    print(quicksortnonr(nums))
    