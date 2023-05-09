# 堆排序（Heap Sort）
# 堆排序的基本思想：
#   堆排序是利用堆这种数据结构所设计的一种排序算法。
#   堆是一个近似完全二叉树的结构，并且满足堆的性质：双亲节点的总是大于或小于其左右孩子。
#   堆分类：
#       1.大根堆：每个根节点的值大于或者等于其子节点的值，用于升序排列；
#       2.小根堆：每个根节点的值小于或者等于其子节点的值，用于降序排列。

# 堆排序的步骤：
# （1）构建完全二叉树
# （2）比较当前根节点与左右孩子节点的大小与调整根节点与孩子节点的位置
# （3）层次遍历输出完全二叉树的节点

# 双亲节点与孩子节点比较大小的步骤：
# （1）比较节点是从最后一个节点N开始，比较其双亲节点(N//2)与该孩子节点的大小关系；
# （2）再比较双亲节点(N//2 -1) 与其孩子节点的大小关系，依次类推，比较完所有节点；
# （3）输出堆顶元素，再由堆的最后一个替补为堆顶元素；
# （4）重复步骤（1）（2）（3）直到只有一个堆元素为止。


# 堆树的调整
import math


def heaptreeadjust(datalist):
    """堆排序生成大顶堆"""
    if datalist is None:  # 堆树为空
        return
    if len(datalist) == 1:  # 堆树仅有一个节点
        return datalist
    length = len(datalist)
    # 循环比较的趟数
    runmax = math.ceil(math.log(length, 2))
    # 调整的次数
    adjtimes = (length-1)//2
    while runmax:
        i = 0
        while i <= adjtimes:
            root = i
            left = 2 * i + 1
            right = 2 * i + 2
            # 左孩子右孩子均在列表范围内
            if left < length - 1 and right <= length - 1:
                # 左孩子最大，调整双亲节点与左孩子的位置
                if datalist[left] > datalist[root] and datalist[left] > datalist[right]:
                    datalist[left], datalist[root] = datalist[root], datalist[left]
                # 右孩子最大，调整双亲节点与右孩子的位置
                elif datalist[right] > datalist[left] and datalist[right] > datalist[root]:
                    datalist[right], datalist[root] = datalist[root], datalist[right]
                # 双亲节点最大，不调整双亲节点与左右 孩子节点的位置
                else:
                    i = i + 1
            # 左孩子在列表范围内，右孩子不在在列表范围内
            elif left == length - 1 and right == length:
                if datalist[left] > datalist[root]:
                    datalist[left], datalist[root] = datalist[root], datalist[left]
                else:
                    i = i + 1

            else:
                i = i + 1

        runmax -= 1
    return datalist

    
# 堆树的排序
def heaptreesort(datalist):
    length = len(datalist)
    
    # 构造大顶堆
    datalist = heaptreeadjust(datalist)
    
    # 堆排序
    for i in range(1, length):
        datalst_pre = datalist[0:i]
        datalst_post = heaptreeadjust(datalist[i:])
        datalist = datalst_pre + datalst_post
    return datalist
    

# 数据测试
if __name__ == '__main__':
    nums = [1, 0, 6, 7, 5, 9]
    
    print(nums)
    print('>> 堆树的调整1：')
    heaptreeadjust(nums)
    print('>> 堆树的排序：')
    print(heaptreesort(nums))
