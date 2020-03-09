'''
搜索算法:
- 无序列表的顺序查找，时间复杂度O(N)
- 二分查找，时间复杂度O(logN)
- Fibonacci查找，时间复杂度O(logN)
- 插值查找，时间复杂度O(log(logN))
- 哈希查找，时间复杂度O(1)
- 二叉树查找
'''



'''
遍历无序列表的顺序查找算法
'''
def sequential_search(lis, key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    else:
        return False



'''
二分查找
'''
def binarysearch(sorted_sequence,target):
    left=0
    right=len(sorted_sequence)-1
    while(left<=right):
        midpoint=(left+right)//2
        current_item=sorted_sequence[midpoint]
        if current_item==target:
            return midpoint
        elif target<current_item:
            right=midpoint-1
        else:
            left=midpoint+1
    return None



'''
插值查找
'''
def Interpolationsearch(sorted_sequence,target):
    left=0
    right=len(sorted_sequence)-1
    while(left<=right):
        midpoint= left + int((right - left) * (target - sorted_sequence[left]) / (sorted_sequence[right] - sorted_sequence[left]))
        current_item=sorted_sequence[midpoint]
        if current_item==target:
            return midpoint
        elif target<current_item:
            right=midpoint-1
        else:
            left=midpoint+1
    return None



'''
Fibonacci查找，前提是已经有一个包含斐波那契数据的列表
'''
import copy
def fibonacci_search(ord_data, target_value, max_size):
    """
    Args:
        ord_data: ordered data
        target_value: value that be searched
        max_size: max size of fibonacci number
    """
    # 0：首选深度复制数据
    D = copy.deepcopy(ord_data)
    
    # 1：构建斐波那契数列
    F = [0, 1] + [fibonacci(i) for i in range(2, max_size)]

    # 2：计算数据长度对应斐波那契数列元素
    index = 0
    while(F[index]<len(D)):
        index += 1

    # 3：对数据进行填充
    for i in range(len(D), F[index]):
        D.append(D[len(D)-1])
   
    # 4：对区间不断分割
    left = 0
    right = F[index]
    while left <= right and index>0:
        # 计算分割位置，左区间长度为F(n-2)，右区间长度为F(n-1)
        # -1是因为下标从0开始，即D[0]到D[20]对应21个元素
        mid = left + F[index-1] - 1
           
        # 判断中间值和目标值的关系
        if D[mid] == target_value:
            # 此时搜索到的目标值是填充的值
            if mid > len(ord_data):
                return len(ord_data)-1
            else:
                return mid
                
        elif D[mid] < target_value:
            left = mid + 1
            index = index - 2

        elif D[mid] > target_value:
            right = mid - 1
            index = index - 1
    return None



'''
快速查找
'''



'''
哈希查找
'''




'''
二叉树查找
'''



'''--------------------------------------------------------------------------------------------------------------------'''



'''
- 冒泡排序, 时间O(n2), 空间O(1), 稳定
- 选择排序, 时间O(n2), 空间O(1), 不稳定
- 快速排序, 时间O(nlogn), 空间O(nlogn), 不稳定
- 插入排序, 时间O(n2), 空间O(1), 稳定
- 归并排序, 时间O(nlogn), 空间O(n), 稳定
'''



'''
冒泡排序
'''
def bubbleSort(nums):
    for i in range(len(nums) - 1): # 遍历 len(nums)-1 次
        for j in range(len(nums) - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # Python 交换两个数不用中间变量
    return nums



'''
选择排序
'''
def selectionSort(nums):
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:  # 更新最小值索引
                minIndex = j  
        nums[i], nums[minIndex] = nums[minIndex], nums[i] # 把最小数交换到前面
    return nums




'''
快速排序
'''
def quicksort(lst):
    less = []
    greater = []
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[-1]
        for num in lst[:-1]:
            if num < pivot:
                less.append(num)
            if num >= pivot:
                greater.append(num)
    return quicksort(less) + [pivot] + quicksort(greater)



'''
插入排序
'''
def insertionSort(nums):
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        curNum, preIndex = nums[i+1], i  # curNum 保存当前待插入的数
        while preIndex >= 0 and curNum < nums[preIndex]: # 将比 curNum 大的元素向后移动
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = curNum  # 待插入的数的正确位置   
    return nums



'''
归并排序
'''
def MergeSort(lst):
    #合并左右子序列函数
    def merge(arr,left,mid,right):
        temp=[]     #中间数组
        i=left          #左段子序列起始
        j=mid+1   #右段子序列起始
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=right:
            temp.append(arr[j])
            j+=1
        for i in range(left,right+1):    #  !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i]=temp[i-left]
    #递归调用归并排序
    def mSort(arr,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        mSort(arr,left,mid)
        mSort(arr,mid+1,right)
        merge(arr,left,mid,right)
 
    n=len(lst)
    if n<=1:
        return lst
    mSort(lst,0,n-1)
    return lst
