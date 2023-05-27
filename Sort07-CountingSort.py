# 计数排序（Counting Sort）
# 计数排序主要是针对整数的排序

# 计数排序的主要思想：
# 对待排序的序列，将其中的数据值转化为键存储在额外开辟的数据空间中 NewSpace；
# 其中NewSpace的大小为最大整数与最小整数的差值加1决定；
# 在NewSpace的0号位置记录最小值出现的次数，其它位置上的数据一次记录其它数据出现的次数；
# 最后一次进行数据输出，NewSpace的位置上的元素的次数为输出的次数


# 计数排序程序设计

def countingsort(datalist):
    length = len(datalist)
    if length == 0:
        return
    if length == 1:
        return datalist
 
    # 求最大值与最小值
    maxint, minint = max(datalist), min(datalist)  # 最大值与最小值的初始化

    # 列表0号位置上的数据（也是最小值）
    zeronumb = minint
        
    # 新空间的大小size
    size = maxint - minint + 1
    
    # 开辟新的数据空间
    newspace = [0 for _ in range(0, size)]
    
    # 计算列表数据元素的个数
    for j in range(0, length):
        idx = datalist[j] - zeronumb
        newspace[idx] += 1

    # 从newspace列表中输出数据
    i = 0
    for k in range(0, size):
        while newspace[k] > 0:
            datalist[i] = zeronumb + k
            newspace[k] -= 1  # 输出的次数
            i += 1  # 每多输出一次，则插入到新的位置
    return datalist
    

# 主函数
if __name__ == "__main__":
    nums = [-1, 90, 90, 92, 93, 91, 94, 95, 90, 99]
    print(countingsort(nums))

# 思考：
# （1）计数排序有一定的局限性，排序的数据要求为整数；
# （2）待排序的列表中的数据极差不能太大，也不能太稀疏；
# （3）计数排序算法在输出部分的代码设计比较特殊，在需要输出数据多次之时。
