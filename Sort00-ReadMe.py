# ReadMe
# （1）在十大排序算法中，有些排序算法可以修改为一边添加元素，一边排序的方式进行，即动态地排序，可以将其修改为动态类型的排序；
# （2）有些排序是采用了递归方法来实现的，可以将其修改为非递归方法来实现；
# （3）有些算法是可以实现本地排序，不需要额外的存储空间；
# （4）


# 关于冒泡算法（01-BubbleSort）
# （1）冒泡算法比较经典，是其它算法开始的算法，是典型的采用移动比较元素的方式来实现的排序算法；
# （2）冒泡算法是外部多趟嵌套内层多轮比较移动元素的算法；
# （3）冒泡算法有个优化的地方是内层多轮比较，比较的次数是逐渐减少的，以外部的趟次有关联；


# 突发奇想-1
# 本地交换一个列表中的元素，使得整个列表是升序排列的
# 本地交换的规则：
#   （1）对列表list设计2个指针,左指针i,右指针j,i右移(i++)，j左移(j++)；
#   （2）当list[i] > list[j]时：list[i]与list[j]互换,右指针j += 0，左指针i += 1；
#   （3）当list[i] < list[j]时：list[i]与list[j]不交换,右指针j -= 1，左指针i += 0；
#   （4）当i=j 时：退出返回列表


def inplacesort(numbs):
    n = len(numbs)
    if n == 0 or n == 1:
        return numbs
    
    left, right = 0, n-1  # 左右指针初始位置

    while left < right:
        
        while left < right:
            if numbs[left] > numbs[right]:
                numbs[left], numbs[right] = numbs[right], numbs[left]

            left += 1

        left = 0
        right -= 1
    return numbs

        
# 主函数
if __name__ == "__main__":
    nums = [0, 1, 4, 3, 2, 15, -1, -2, -3, -4, -5, 5, 6, 8, 7, 9, 10, 11, 14, 12, 13]
    # print(inplacesort(nums))
    
# 突发奇想-2
# 采用逆序数来设计排序
#  （1）逆序数是指在该数据在列表中，在从左往右遍历过程中，若数据比当前数据大，则当前的逆序数增加1；
#  （2）需要额外的存储空间来存放逆序数；
#  （3）怎么根据逆序数来排序需要设计程序(待思考！)


def inversenumber(lst):
    """生成逆序数innum"""
    innum = [0]  # 逆序数的存储列表
    n = len(lst)  # 数据列表的长度
    
    if n == 0 or n == 1:
        return lst
    insum = 0  # 逆序数之和
    for i in range(1, n):
        inv = 0
        for j in range(0, i):
            if lst[i] <= lst[j]:
                inv += 1
        
        innum.append(inv)
        insum += inv
        
    print(innum, insum, '偶数排列' if insum % 2 == 0 else '奇数排列')


# 主函数
if __name__ == "__main__":
    nums = [5, 4, 3, 6, 1, 2, 7]
    # print(inversenumber(nums))
    
    
# 突发奇想-3
# 采用动态排序的方式设计程序
#  (1) 数据列表是一个空列表；
#  (2) 数据是逐个添加到数据列表中；
#  (3) 数据比较的方式是插入排序；
#  (4) 此处的插入排序与静态列表的插入排序有异同；
#  (5) 可以设计成动态排序的算法：插入排序、快速排序

# 定义排序
# 动态插入程序设计（辅助方法）
def dynamicinsertion(lst, new):
    curindex = 0
    curval = lst[curindex]
    while curindex < len(lst) and curval < new:
        curindex += 1
        if curindex >= len(lst):
            break
        else:
            curval = lst[curindex]
    lst.insert(curindex, new)
    return lst


# 动态程序设计1-动态插入排序
def dynamicinsertionsort(reslst: list[int], newdata: int) -> list[int]:
    if len(reslst) == 0:
        reslst.append(newdata)
    else:
        dynamicinsertion(reslst, newdata)
    
    return reslst
 
 
# 动态程序设计2-动态快速排序
def dynamicquicksort(reslst: list[int], newdata: int) -> list[int]:
  
    if len(reslst) == 0:
        reslst.append(newdata)
    
    else:
        pivot = reslst.pop()  # 参照基准数据
        left = reslst
        right = []
        
        if newdata <= pivot:
            if len(left) == 0:
                left.append(newdata)
            else:
                left = dynamicinsertion(left, newdata)
        else:
            if len(right) == 0:
                right.append(newdata)
            else:
                right = dynamicinsertion(right, newdata)
                
        reslst = left + [pivot] + right
 
    return reslst


# 主函数
if __name__ == "__main__":
    datalist = [9, 7, 6]
    res_insertion = []
    print('>> 动态插入排序:')
    for data in datalist:
        res_insertion = dynamicinsertionsort(res_insertion, data)
    print(res_insertion)

    print('>> 动态快速排序:')
    res_quick = []
    for data in datalist:
        res_quick = dynamicquicksort(res_quick, data)
    print(res_quick)

    
        