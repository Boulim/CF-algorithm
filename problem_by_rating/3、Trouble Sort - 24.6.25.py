Trouble Sort
"""
题目链接:
https://codeforces.com/contest/1365/problem/B
思路：（1300）
如果所有元素的类型相同，我们就不能交换任何两个元素。因此，在这种情况下，我们只需要检查给定的元素是否已经排序。
否则，至少有一个元素的类型是 0 ，至少有一个元素的类型是 1。在这种情况下，我们可以交换任意两个元素！
我们只需使用一种操作就可以交换不同类型的元素。假设我们要交换两个相同类型的元素 𝑎 和 𝑏。我们可以通过 3 次操作来实现。
假设 𝑐 是一个类型不同于 𝑎 和 𝑏 的元素。我们可以先交换 𝑎和 𝑐 ，然后交换 𝑏 和 𝑐 ，再交换 𝑎 和 𝑐 。
这样， 𝑐保持在初始位置，而 𝑎 和 𝑏 被交换。这正是我们使用临时变量交换两个整数的方法。由于我们可以交换任意两个元素，
因此在这种情况下总是可以对数组进行排序。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print('Yes' if len(set(b)) > 1 or a == sorted(a) else'No')

