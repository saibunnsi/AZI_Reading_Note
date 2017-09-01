# coding:utf-8
import random
from function_timer import deco_timer

initial_list = [w for w in range(0,10000000) ]
sam_image_list = random.sample(initial_list, 30000)
random.shuffle(sam_image_list)
'''
@deco_timer
def list_sort(A):
    f_list = [0]*10000000
    b = 0
    while b < len(A):
        k = A[b]
        b += 1
        f_list[k-1] = 1
    s = 0
    B = []
    while s < 10000000:
        if f_list[s] == 1:
            #print (["%07d" % (s+1)]) 整数前空位补全，这里补全7位
            #print(s+1)
            B.append(s+1)
        else:
            pass
        s += 1
    return B

if __name__ == '__main__':
    print(list_sort(sam_image_list))

# ('running : my_sort', 'costs: 7.84099984169')
#8000: ('running : my_sort', 'costs: 4.05700016022')
#80000: ('running : my_sort', 'costs: 22.8960001469')
#80000:('running : my_sort', 'costs: 1.60800004005')
#80000:('running : my_sort', 'costs: 1.45300006866')
#30000:('running : list_sort', 'costs: 1.39499998093 seconds')
#300000:('running : list_sort', 'costs: 1.68300008774 seconds'))
'''
'''
# 插入排序：
# 扫描数组，每次将一个待排序的记录，
# 按其关键字大小插入到前面已经排好序的子序列中的适当位置，直到全部记录插入完成为止。
@deco_timer
def insert_sort_asc(A):
    n = len(A) #A的长度
    for j in range(1,n): # 遍历数组，从第二个元素开始：
        value, i = A[j], j # 保存当前元素的值value
        #if reverse == False:
        while i>0 and A[i-1]>value:# 当前一个元素的值大于当前元素：
            A[i] = A[i-1] # 把前一个元素的值赋给当前元素
            i -= 1
        A[i] = value
    
        #elif reverse == True:
         #   while i > 0 and A[i - 1] < value:  # 当前一个元素的值小于当前元素：
          #      A[i] = A[i - 1]  # 把前一个元素的值赋给当前元素
           #     i -= 1
            #A[i] = value
        
    return A

A=sam_image_list
print (insert_sort_asc(A))
# 30000:('running : insert_sort_asc', 'costs: 70.2400000095 seconds')

'''
'''
@deco_timer
def smallest_num_select_sort(A):
    p = len(A)
    m = A[0]
    for a in range(0,p-1):
        B = A[a:p]
        l = p-a
        i = 0
        k = i + 1
        while 0 <= i < l and 0 < k < l :
            if B[i] < B[k]:
                m = B[i]
                k = k+1
            elif B[i] > B[k]:
                m = B[k]
                i = k
                k = i + 1
        B.remove(m)
        B.insert(a, m)
    return A
if __name__ == '__main__':
    print(smallest_num_select_sort(sam_image_list))
#800:('running : smallest_num_select_sort', 'costs: 0.160000085831')
#8000:('running : smallest_num_select_sort', 'costs: 16.5490000248')
#30000：('running : smallest_num_select_sort', 'costs: 332.101999998')
'''
'''
# 选择排序
@deco_timer
def SELECTION_SORT_DESC(A):
    n = len(A)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n): #找出当前位置最小的
            if A[j]<A[min]:
                min=j
        if i!=min:
            A[i],A[min] = A[min],A[i]
    return A
print(SELECTION_SORT_DESC(sam_image_list))
#8000：('running : SELECTION_SORT_DESC', 'costs: 4.23600006104')
#30000：('running : SELECTION_SORT_DESC', 'costs: 97.6119999886')
'''
'''
# 冒泡排序
# 反复交换相邻的未按次序排列的元素。即把小的元素往前调，或者把大的元素往后调

@deco_timer
def BUBBLE_SORT_ASC(A):
    n = len(A)
    for i in range(0, n-1):
        for j in range(i+1, n)[::-1]:
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1],A[j]
    return A
print(BUBBLE_SORT_ASC(sam_image_list))
# 8000:('running : BUBBLE_SORT_ASC', 'costs: 9.60500001907 seconds')
# 30000:('running : BUBBLE_SORT_ASC', 'costs: 179.68900013 seconds')
#相同元素的前后顺序不会改变，因此是一种稳定的排序算法。
#低效的简单排序算法

'''
# 归并排序
# 分解：分解待排序的n个元素的序列成各具n/2个元素的两个子序列
# 解决：使用归并排序递归地排序两个子序列
# 合并(MERGE)：合并两个已排序的子序列以产生已排序的答案















