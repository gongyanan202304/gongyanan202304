# 斐波那契查找（FibonacciSearch）

# 斐波那契查找的基本过程：
# （1）构建斐波那契数列；
# （2）计算数组长度对应的斐波那契数列元素个数；
# （3）对数组进行填充；
# （4）循环进行区间分隔，查找中间值；
# （5）判断中间值与给定值之间的大小，确定更新策略。

# 斐波那契序列是有序的（升序或者降序排列）
# 斐波那契查找也是一种有序查找

# 数组填充成长度为斐波那契数列中的某个项

# 斐波那契查找程序设计

# 1-设计斐波那契数列
def fibonaccisequence(k):
    
    # 根据输入的k值输出最接近的数列的项
    fib = [0, 1]  # 存放斐波那契数列的项
    i = 2
    while True:

        fi = fib[i-1] + fib[i-2]
        fib.append(fi)
        if fib[i] < k:
            i += 1
        else:
            i += 1
            break

    fi = fib[i-1] + fib[i-2]
    fib.append(fi)
    
    return fib


def fibonaccisearch(datalist, setvalue):
    
    # 1-判定数组元素个数
    n = len(datalist)
    
    # 2-构建斐波那契数列
    fs = fibonaccisequence(n)
    maxlen = max(fs)
    
    # 3-填充数组(最大值填充法)
    padding = [datalist[n-1] for _ in range(maxlen-n)]
    dlst = datalist + padding
    
    # 4-对区间进行分割
    i = len(fs) - 1
    left = 0
    right = fs[i]
    while left <= right and i > 0:
        
        mid = left + fs[i-1] - 1  # 确定中间值的计算方法
        
        if dlst[mid] == setvalue:
            if mid >= n:
                return n-1
            else:
                return mid
        
        elif dlst[mid] < setvalue:
            left = mid+1
            i = i-2
            
        else:
            right = mid-1
            i = i-1
    
    return False


# 主函数
if __name__ == "__main__":
    nums = [3, 4, 5, 7, 8, 9, 10, 11, 15]
    print(fibonaccisearch(nums, 8))
    