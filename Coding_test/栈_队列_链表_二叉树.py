'''
栈 Stack - 队列 Queue - 链表 Linked List - 数组 Array - 哈希表 Hash Table - 二叉树 Binary Tree - 堆 Heap - 并查集 Union Find - 字典树 Trie
'''

'''
# 字符串


# 数组：
数组的基本操作：
Insert——在给定索引位置插入一个元素
Get——返回给定索引位置的元素
Delete——删除给定索引位置的元素
Size——获取数组内所有元素的总数

常问的数组面试问题：
找到数组中第二小的元素
找到数组中第一个没有重复的整数
合并两个分类数组
重新排列数组中的正值和负值



# 栈的基本操作：
Push——在顶部插入元素
Pop—— 从堆栈中删除后返回顶部元素
isEmpty——如果堆栈为空，则返回 true
Top ——返回顶部元素，但不从堆栈中删除

常见的堆栈面试问题：
使用堆栈计算后缀表达式
对堆栈中的值进行排序
检查表达式中的括号是否平衡



# 队列的基本操作：
Enqueue() —— 向队列末尾插入元素
Dequeue() —— 从队列头部移除元素
isEmpty() —— 如果队列为空，则返回 true
Top() —— 返回队列的第一个元素

常问的队列面试问题：
使用队列来实现堆栈
颠倒队列中前 k 个元素的顺序
使用队列生成从 1 到 n 的二进制数



# 链表：
单链表（单向) - 双链表（双向）

链表的基本操作：
InsertAtEnd —— 在链表末尾插入指定元素
InsertAtHead —— 在链表头部插入指定元素
Delete —— 从链表中删除指定元素
DeleteAtHead —— 删除链表的第一个元素
Search —— 返回链表中的指定元素
isEmpty —— 如果链表为空，返回 true

常问的链表面试问题：
翻转列表
检测链表中的循环
返回链表中倒数第 n 个节点
移除链表中的重复值



# 树：
N叉树 - 平衡树 - 二叉树 - 二叉搜索树 - 平衡二叉树 - 红黑树
其中，二叉树和二叉搜索树是最常用的树。

常问的树面试问题：
找到一个二叉树的高度
找到一个二叉搜索树中第 k 个最大值
找到距离根部“k”个距离的节点
找到一个二叉树中给定节点的祖先（ancestors）



# 图的类型：
无向图 - 有向图
在编程语言中，图可以表示为两种形式：
邻接矩阵 - 邻接列表

常见的图遍历算法：
广度优先搜索
深度优先搜索

常问的图面试问题：
实现广度优先搜索和深度优先搜索
检查一个图是否为树
计算一张图中的边的数量
找到两个顶点之间的最短路径



# 常问的哈希面试问题：
找到数组中的对称对
追踪遍历的完整路径
查看一个数组是否为另一个数组的子集
检查给定数组是否不相交
'''




'''
栈
'''
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self, item):
        return self.items.pop()



'''
队列
'''
class Queue(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self, item):
        return self.items.pop(0)




'''
链表
https://blog.csdn.net/qq_39422642/article/details/78988976
'''



'''
二叉树
https://juejin.im/post/5bfa45a1f265da612c5d8da9
https://zhuanlan.zhihu.com/p/35574577
'''
from graphviz import Digraph
import uuid
from random import sample

# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树
        self.dot = Digraph(comment='Binary Tree')

    # 前序遍历
    def preorder(self):

        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 层序遍历
    def levelorder(self):

        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()

    # 利用Graphviz实现二叉树的可视化
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

        # 绘制以某个节点为根节点的二叉树
        def print_node(node, node_tag):
            # 节点颜色
            color = sample(colors,1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())            # 左节点的数据
                self.dot.node(left_tag, str(node.left.data), style='filled', color=color)    # 左节点
                label_string = 'L' if label else ''    # 是否在连接线上写上标签，表明为左子树
                self.dot.edge(node_tag, left_tag, label=label_string)   # 左节点与其父节点的连线
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, str(node.right.data), style='filled', color=color)
                label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        # 如果树非空
        if self.data is not None:
            root_tag = str(uuid.uuid1())                # 根节点标签
            self.dot.node(root_tag, str(self.data), style='filled', color=sample(colors,1)[0])     # 创建根节点
            print_node(self, root_tag)

        self.dot.render(save_path)                              # 保存文件为指定文件

