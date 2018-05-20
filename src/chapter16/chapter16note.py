# coding:utf-8
# usr/bin/python3
# python src/chapter16/chapter16note.py
# python3 src/chapter16/chapter16note.py
'''
Class Chapter16_1

Class Chapter16_2

'''
from __future__ import absolute_import, division, print_function

import math as _math
import random as _random
import time as _time
from copy import copy as _copy
from copy import deepcopy as _deepcopy
from random import randint as _randint

import numpy as np
from numpy import arange as _arange
from numpy import array as _array
from numpy import *

class Chapter16_1:
    '''
    chpater16.1 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter16.1 note

        Example
        ====
        ```python
        Chapter16_1().note()
        ```
        '''
        print('chapter16.1 note as follow')   
        print('第16章 贪心算法')
        # !适用于最优化问题的算法往往具有一系列步骤，每一步有一组选择
        print('适用于最优化问题的算法往往具有一系列步骤，每一步有一组选择')
        print('对许多最优化的问题来说，采用动态规划有点大材小用的意思，只要采用另一些更简单的方法就行了')
        # !贪心算法使得所做的选择在当前看起来都是最佳的，期望通过所做的局部最优得到最终的全局最优
        print('贪心算法使得所做的选择在当前看起来都是最佳的，期望通过所做的局部最优得到最终的全局最优')
        print('贪心算法对大多数最优化问题都能产生最优解，但也不一定总是这样的')
        print('在讨论贪心算法前，首先讨论动态规划方法，然后证明总能用贪心的选择得到其最优解')
        print('16.2给出一种证明贪心算法正确的方法')
        # !有许多被视为贪心算法应用的算法，如最小生成树，Dijkstra的单源最短路径，贪心集合覆盖启发式
        print('有许多被视为贪心算法应用的算法，如最小生成树，Dijkstra的单源最短路径，贪心集合覆盖启发式')
        print('16.1 活动选择问题')
        # !活动选择问题：对几个互相竞争的活动进行调度,它们都要求以独占的方式使用某一公共资源
        print('对几个互相竞争的活动进行调度,它们都要求以独占的方式使用某一公共资源')
        print('设有n个活动和某一个单独资源构成的集合S={a1,a2,...,an}，该资源一次只能被一个活动占用')
        print('各活动已经按照结束时间的递增进行了排序')
        print('每个活动ai都有一个开始时间si和一个结束时间fi，资源一旦被活动ai选中后')
        print('活动ai就开始占据左闭右开时间区间，如果两个活动ai，aj的时间没有交集，称ai和aj是兼容的')
        # !活动选择问题就是要选择出一个由互相兼容的问题组成的最大子集合
        print('动态规划方法解决活动选择问题时，将原方法分为两个子问题，',
            '然后将两个子问题的最优解合并成原问题的最优解')
        # !贪心算法只需考虑一个选择(贪心的选择)，再做贪心选择时，子问题之一必然是空的，因此只留下一个非空子问题
        print('贪心算法只需考虑一个选择(贪心的选择)，再做贪心选择时，子问题之一必然是空的，因此只留下一个非空子问题')
        print('因此找到一种递归贪心算法解决活动选择问题')
        print('活动选择问题的最优子结构')
        print(' 首先为活动选择问题找到一个动态规划解，找到问题的最优子结构。')
        print(' 然后利用这一结构，根据子问题的最优解来构造出原问题的一个最优解')
        print(' 定义一个合适的子问题空间Sij是S中活动的子集，其中，每个活动都在活动ai结束之后开始，且在活动aj开始之前结束')
        print(' 实际上，Sij包含了所有与ai和aj兼容的活动，并且与不迟于ai结束和不早于aj开始的活动兼容')
        print(' 假设活动已按照结束时间的单调递增顺序排序：')
        print(' 一个非空子问题Sij的任意解中必包含了某项活动ak，而Sij的任一最优解中都包含了其子问题实例Sik和Skj的最优解。')
        print(' 因此，可以可以构造出Sij中的最大兼容活动子集。',
            '将问题分成两个子问题(找出Sik和Skj的最大兼容活动子集)，找出这些子问题的最大兼容活动子集Aik和Akj',
            '而后形成最大兼容活动子集Aij如:Aij=Aik ∪ {ak} ∪ Akj')
        print(' 整个问题的一个最优解也是S0,n+1的一个解')
        print('一个递归解')
        print(' 动态规划方法的第二步是递归地定义最优解的值。对于活动选择问题')
        print(' 考虑一个非空子集Sij,如果ak在Sij的最大兼容子集中被使用，则子问题Sik和Skj的最大兼容子集也被使用')
        print(' 递归式：c[i, j] = c[i, k] + c[k, j] + 1')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        # python src/chapter16/chapter16note.py
        # python3 src/chapter16/chapter16note.py

class Chapter16_2:
    '''
    chpater16.2 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter16.2 note

        Example
        ====
        ```python
        Chapter16_2().note()
        ```
        '''
        print('chapter16.2 note as follow')   
        # python src/chapter16/chapter16note.py
        # python3 src/chapter16/chapter16note.py

chapter16_1 = Chapter16_1()
chapter16_2 = Chapter16_2()

def printchapter16note():
    '''
    print chapter16 note.
    '''
    print('Run main : single chapter sixteen!')  
    chapter16_1.note()
    chapter16_2.note()

# python src/chapter16/chapter16note.py
# python3 src/chapter16/chapter16note.py
if __name__ == '__main__':  
    printchapter16note()
else:
    pass
