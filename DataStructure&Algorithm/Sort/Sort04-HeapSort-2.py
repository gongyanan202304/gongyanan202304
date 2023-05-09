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
def heap_sink(heap, heapsize, parent_index):
    child_index = 2 * parent_index + 1
    
    temp = heap[parent_index]
    
    while child_index < heapsize:
        
        if child_index + 1 < heapsize and heap[child_index + 1] > heap[child_index]:
            child_index += 1
        
        if temp >= heap[child_index]:
            break
        
        heap[parent_index] = heap[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1
    heap[parent_index] = temp
    
    
# 堆树的排序
def heap_sort(datalist):
    n = len(datalist)
    
    # 构建大顶堆
    for i in range(n-2//2, -1, -1):
        heap_sink(datalist, n, i)
     
    for i in range(0, n):
        datalist[0], datalist[n-i-1] = datalist[n-i-1], datalist[0]
        heap_sink(datalist, n-i-1, 0)


# 数据测试
if __name__ == '__main__':

    nums = [1, 0, 6, 7, 5, 9]
    print(nums)
    print('>> 堆树的调整2：')
    heap_sink(nums, len(nums), 0)
    print('>> 堆树的排序2：')
    heap_sort(nums)
    print(nums)
