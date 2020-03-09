'''
题目：每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了
一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额
有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
'''

'''
思路：约瑟夫环问题
     递推公式：f[i] = (f[i-1]+m)%i
     详细解释：http://blog.csdn.net/u012505432/article/details/51747181

26ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        temp = 0
        for i in range(1, n + 1):
            temp = (temp + m) % i
        return temp




# solution 2
class Solution:
    def lastRemaining(self, n, m):
        # 特判
        if n == 0 and m == 0:
            return -1

        l = [i for i in range(n)]
        bt = 0
        while len(l) > 1:
            
            # 在这一行模拟约瑟夫环操作
            # 1、m - 1 ：因为当前数字算 1 个，走 m - 1 步
            # 2、len(l)：每次删去一个数，所以得动态取
            bt = (bt + m - 1) % len(l)
            
            l.pop(bt)
        return l[0]