# coding:utf-8
# usr/bin/python3
# python src/chapter30/chapter30note.py
# python3 src/chapter30/chapter30note.py
"""

Class Chapter30_1

Class Chapter30_2

Class Chapter30_3


"""
from __future__ import absolute_import, division, print_function

import math
import numpy as np

class Chapter30_1:
    """
    chapter30.1 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter30.1 note

        Example
        ====
        ```python
        Chapter30_1().note()
        ```
        """
        print('chapter30.1 note as follow')
        print('第30章 多项式与快速傅里叶变换')
        print('两个n次多项式相加的花不达标方法所需的时间为Θ(n),而相乘的简单方法所需的时间为Θ(n^2)')
        print('在本章中,将快速傅里叶变换FFT方法是如何使多项式相乘的运行时间降低为Θ(nlgn)')
        print('傅里叶变换的最常见用途是信号处理，也是FFT最常见的用途，在时间域内给定的信号把时间映射到振幅的一个函数',
            '傅里叶分析允许将信号表示成各种频率的相移正弦曲线的一个加权总和')
        print('和频率相关联的权重和相位在频率域中刻画出信号的特性')
        print('在一个代数域F上，关于变量x的多项式定义为形式和形式表示的函数A(x)=∑ajxj')
        print('称值a0,a1,...,an-1为多项式的系数，所有系数都属于域F，典型的情况是复数集合C.如果一个多项式A(x)的最高次的非零系数为ak',
            '则称A(x)的次数(degree)是k.任何严格大于一个多项式次数的整数都是这个多项式的次数界.因此,对于次数界为n的多项式来说,其次数可以是0到n-1之间的任何整数',
            '也包括0和n-1在内')
        print('在多项式上可以定义各种运算,在多项式加法中,如果A(x)和B(x)是次数界为n的多项式,那么它们的和也是一个次数界为n的多项式C(x),',
            '并满足对所有属于定义域的x,都有C(x)=A(x)+B(x)')
        print('在多项式乘法中,如果A(x)和B(x)都是次数界为n的多项式,则说它们的乘积是一个次数界为2n-1的多项式积C(x),并满足对所有属于定义域的x,都有C(x)=A(x)B(x)')
        print('注意degree(C)=degree(A)+degree(B)蕴含degree-bound(C)=degree-bound(A)+degree-bound(B)-1<=degree-bound(A)+degree-bound(B)')
        print('但是不说C的次数界为A的次数界与B的次数界的和,这是因为如果一个多项式的次数界为k,也可以说该多项式的次数界为k+1')
        print('30.1 多项式的表示')
        # !从某种意义上说,多项式系数表示法与点值表示法是等价的
        print('从某种意义上说,多项式系数表示法与点值表示法是等价的,即用点值形式表示的多项式都对应唯一一个系数形式的多项式',
            '这两种表示结合起来，从而使这两个次数界为n的多项式乘法运算在Θ(nlgn)时间内完成')
        print('系数表示法')
        print('对一个次数界为n的多项式A(x)=∑ajxj来说,其系数表示法就是由一个由系数组成的向量a=(a0,a1,...,an-1)',
            '在本章所涉及的矩阵方程中,一般将它作为列向量看待')
        print('采用系数表示法对于某些多项式的运算是很方便的.例如对多项式A(x)在给定点x0的求值运算就是计算A(x0)的值',
            '如果使用霍纳法则,则求值运算的运行时间为Θ(n):')
        print('  A(x0)=a0+x0(a1+x0(a2+...+x0(an-2+x0(an-1))...))')
        print('类似地,对两个分别用系数向量a=(a0,a1,...,an-1)和b=(b0,b1,...,bn-1)表示的多项式进行相加时,所需的时间是Θ(n):',
            '仅输出系数向量c=(c0,c1,...,cn-1),其中对j=0,1,...,n-1,有cj=aj+bj')
        print('现在来考虑两个用系数形式表示的、次数界为n的多项式A(x)和B(x)的乘法运算,完成多项式乘法所需要的时间就是Θ(n^2)',
            '因为向量a中的每个系数必须与向量b中的每个系数相乘。当用系数形式表示时,多项式乘法运算似乎要比求多项式的值和多项式加法困难的多')
        print('卷积运算c=a＊b,多项式乘法与卷积的计算都是最基本的问题')
        print('点值表示法')
        print('  一个次数界为n的多项式A(x)的点值表示就是n个点值对所形成的集合：{(x0,y0),(x1,y1),...,(xn-1,yn-1)}')
        print('  其中所有xk各不相同,并且当k=0,1,...,n-1时有yk=A(xk)')
        print('  一个多项式可以有很多不同的点值表示,这是由于任意n个相异点x0,x1,...,xn-1组成的集合,都可以作为这种表示法的基础')
        print('  对于一个用系数形式表示的多项式来说,在原则上计算其点值表示是简单易行的,因为我们所要做的就是选取n个相异点x0,x1,...,xn-1',
            '然后对k=0,1,...,n-1,求出A(xk).根据霍纳法则,求出这n个点的值所需要的时间为Θ(n^2),在稍后可以看到,如果巧妙地选取xk的话,就可以加速这一计算过程,使其运行时间变为Θ(nlgn)')
        print('  求值计算的逆(从一个多项式的点值表示确定其系数表示中的系数)称为插值(interpolation).下列定理说明插值具有良定义,',
            '假设插值多项式的次数界等于已知的点值对的数目')
        print('定理30.1 (多项式插值的唯一性) 对于任意n个点值对组成的集合：{(x0,y0),(x1,y1),...,(xn-1,yn-1)},存在唯一的次数界为n的多项式A(x),',
            '满足yk=A(xk),k=0,1,...,n-1')
        print('要对n个点进行插值,还可以用另一种更快的算法,基于拉格朗日插值公式,拉格朗日插值公式等式右端是一个次数界为n的多项式',
            '可以在Θ(n^2)的运行时间内,运用拉格朗日公式来计算A的所有系数')
        print('n个点的求值运算与插值运算是良定义的互逆运算,它们将多项式的系数表示与点值表示进行相互转换,关于这些问题,上述算法的运行时间为Θ(n^2)')
        print('因此,对两个点值形式表示的次数界为n的多项式相加,所需时间为Θ(n)')
        print('如果已知两个扩充点值形式的输入多项式,使其相乘而得到点值形式的结果需要Θ(n)的时间,这要比采用系数形式的两个多项式相乘所需的时间少得多')
        print('考虑对一个点值表示的多项式,如何求其在某个新点上的值这一问题.对这个问题来说,最简单不过的方法显然就是先把该多项式转化为其系数形式,然后再求其在新点处的值')
        print('系数形式表示的多项式的快速乘法')
        print('  能否可以利用关于点值形式表示的多项式的线性时间乘法算法,来加快系数形式表示的多项式乘法运算的速度呢？',
            '答案依赖于能否快速把一个多项式从系数形式转换为点值形式(求值),和从点值形式转换为系数形式(插值)')
        print('可以采用需要的任何点作为求值点,但精心地挑选求值点,可以把两种表示法之间转化所需的时间压缩为Θ(nlgn)')
        print('如果选择“单位复根”作为求值点,则可以通过对系数向量进行离散傅里叶变换DFT,得到相应的点值表示')
        print('同样,也可以通过对点值对执行“逆DFT运算”,而获得相应的系数向量,这样就完成了求值运算的逆运算----插值',
            '可以在Θ(nlgn)的时间内执行DFT和逆DFT运算')
        print('两个次数界为n的多项式的积是一个次数界为2n的多项式。因此,在对输入多项式A和B进行求值之前,首先通过增加n个值为0的高阶系数,使其次数界增加到2n',
            '因为向量包含2n个元素,所以用到了2n次单位复根')
        print('如果已知FFT,就有下列运行时间为Θ(nlgn)的过程,该过程把两个次数界为n的多项式A(x)和B(x)进行乘法运算',
            '其中输入与输出均采用系数表示法。假定n为2的幂，通过加入为0的高阶系数,这个要求总能被满足：')
        print('(1) 使次数界增加一倍：通过加入n个值为0的高阶系数,把多项式A(x)和B(x)扩充为次数界为2n的多项式并构造其系数表示')
        print('(2) 求值：两次应用2n阶的FFT计算出A(x)和B(x)的长度为2n的点值表示。这两个点值表示中包含了两个多项式在2n次单位根处的值')
        print('(3) 点乘：把A(x)的值与B(x)的值逐点相乘,就可以计算出多项式C(x)=A(x)B(x)的点值表示,这个表示中包含了C(x)在每个2n次单位根处的值')
        print('(4) 插值：只要对2n个点值对应用一次FFT以计算出其逆DFT,就可以构造出多项式C(x)的系数表示')
        print('执行第1步和第3步所需时间为Θ(n),执行第2步和第4步所需时间为Θ(nlgn)')
        print('定理30.2 当输入与输出都采用系数形式来表示多项式时,就能够在Θ(nlgn)的时间内,计算出两个次数界为n的多项式的积')
        print('练习30.1-1 运用多项式乘法计算A(x)=7x^3-x^2+x-10和B(x)=8x^3-6x+3的乘积')
        print('练习30.1-2 求一个次数界为n的多项式A(x)在某已知点x0的值也可以用以下方法获得：把多项式A(x)除以多项式(x-x0)',
            '得到一个次数界为n-1的商多项式q(x)和余项r,并满足A(x)=q(x)(x-x0)+r',
            '显然A(x0)=r,试说明如何根据x0和A的系数,在Θ(n)的时间内计算出余项r以及q(x)中的系数')
        print('练习30.1-3 根据A(x)=∑ajx^j的点值表示推导出Arev(x)=∑an-1-jx^j的点值表示,假定没有一个点是0')
        print('练习30.1-4 证明：为了唯一确定一个次数界为n的多项式,n个相互不同的点值对是必需的,也就是说,如果给定少于n对不同的点值',
            '它们就无法确定唯一一个次数界为n的多项式')
        print('练习30.1-5 可以使用拉格朗日等式在Θ(n^2)的时间内进行插值运算')
        print('练习30.1-6 试解释在采用点值表示法时,用“显然”的方法来进行多项式除法错误在何处,即除以相应的y值',
            '试对除法有确切结果与无确切结果两种情况分别进行讨论')
        print('练习30.1-7 考察两个集合A和B,每个集合包含取值范围在0到10n之间的n个整数,要计算出A与B的笛卡尔和,它的定义如下：C={x+y,x∈A且y∈B}',
            '注意,C中整数的取值范围在0到20n之间.希望计算出C中的元素,并且求出C的每个元素可为A与B中元素和的次数。证明：解决这个问题需要Θ(nlgn)的时间')
        # python src/chapter30/chapter30note.py
        # python3 src/chapter30/chapter30note.py

class Chapter30_2:
    """
    chapter30.2 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter30.2 note

        Example
        ====
        ```python
        Chapter30_2().note()
        ```
        """
        print('chapter30.2 note as follow')
        print('DFT与FFT')
        print('如果使用单位复根的话,就可以在Θ(nlgn)时间内完成求值与插值运算')
        print('单位复根')
        print('  n次单位复根是满足w^n=1的复数w.n次单位复根刚好有n个,它们是e^(2∏ik/n),k=0,1,...,n-1')
        print('  欧拉公式e^(iu)=cos(u)+isin(u)')
        print('单位复根的性质')
        print('  (1) 相消引理')
        print('  (2) 折半引理')
        print('  (3) 求和引理')
        print('折半引理是递归的FFT算法的基础，1个元素的DFT就是该元素自身')
        print('递归的FFT算法RECURSIVE-FFT的运行时间,除了递归调用外,每条命令执行所需的时间为Θ(n)',
            'n为输入向量的长度.因此,关于运行时间有下列递归式:')
        print('  T(n)=2T(n/2)+Θ(n)=Θ(nlgn)')
        print('因此,运用快速傅里叶变换,可以在Θ(nlgn)的时间内,求出次数界为n的多项式在n次单位复根处的值')
        print('对单位复根进行插值')
        print('  把一个多项式从点值表示转化成系数表示,进而完成多项式乘法方案.按如下方式进行插值：',
            '把DFT写成一个矩阵方程,然后再检查其逆矩阵的形式')
        print('  可以把DFT写成矩阵积y=Vna,其中Vn是由wn的适当幂组成的一个范德蒙德矩阵')
        print('定理30.7 对j,k=0,1,...,n-1,Vn^-1的(j,k)处的元素为wn^(-kj)/n')
        print('定理30.8 (卷积定理)对任意两个长度为n的向量a和向量b,其中n是2的幂',
            'a＊b=DFT^(-1)(2n)(DFT2n(a)·DFT2n(b))',
            '其中向量a和b用0扩充使其长度达到2n,“·”表示2个2n个元素组成的向量的点乘')
        print('练习30.2-1 略')
        print('练习30.2-2 计算向量(0,1,2,3)的DFT')
        print('练习30.2-3 使用运行时间在Θ(nlgn)的方案重做练习30.1-1')
        print('练习30.2-4 写出在Θ(nlgn)的运行时间内计算出DFT^(-1)n的伪代码')
        print('练习30.2-5 试着把FFT过程推广到n是3的幂的情形,写出其运行时间的递归式并求解该式')
        print('练习30.2-6 假定不是在复数域上执行n个元素的FFT(n为偶数),而是在整数模m所生成的环Zm上执行FFT',
            '其中m=2^(tn/2)+1,并且t是任意正整数.对模m,用w=2^t来代替wn作为主n次单位根.证明:在该系统中DFT与逆DFT有良定义')
        print('练习30.2-7 已知一组值z0,z1,...,zn-1(可能有重复),说明如何求出仅在z0,z1,...,zn-1处(可能有重复)值为0的次数界为n的多项式P(x)的系数',
            '所给出的过程的运行时间应该是O(nlg^2n),(提示：当且仅当P(x)是(x-zj)的倍数时,多项式P(x)在zj处的值为0)')
        print('练习30.2-8 DFT是线性调频变换的一种特殊情况(z=wn).证明:对任意复数z,可以在O(nlgn)的时间内求出线性调频变换的值',
            '可以把线性调频变换看作为卷积')
        # python src/chapter30/chapter30note.py
        # python3 src/chapter30/chapter30note.py

class Chapter30_3:
    """
    chapter30.3 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter30.3 note

        Example
        ====
        ```python
        Chapter30_3().note()
        ```
        """
        print('chapter30.3 note as follow')
        print('30.3 有效的FFT实现')
        print('由于DFT的实际应用(如信号处理)需要极高的速度,所以本节将讨论两种有效的FFT实现方法.')
        print('运行时间为Θ(nlgn)的FFT算法的迭代实现方法隐含的常数要比递归实现方法中的常数小',
            '将深入分析迭代实现方法,设计出一个有效的并行FFT电路')
        print('ITERATIVE-FFT中要用到BIT-REVERSE-COPY算法,位转置算法')
        print('调用BIT-REVERSE-COPY的运行时间当然是Θ(nlgn),因为迭代了n次,并且可以在O(lgn)时间内,',
            '对一个在0到n-1之间的lgn位整数进行反向操作(在实际应用中,通常事先就知道了n的初值,所以可以计算出一张表,求出每个k的rev(k))',
            '使BIT-REVERSE-COPY的运行时间为Θ(n),且该式中隐含的常数也较小')
        print('并行FFT电路')
        print('  可以利用使得能够有效实现迭代FFT算法的许多性质,来产生一个有效的并行FFT算法,',
            '可以将并行FFT算法表示成一个与比较网络相似的电路。FFT电路使用蝴蝶操作而不是比较器')
        print('  关于n个输入的FFT的PARALLEL-FFT电路.电路一开始就对输入进行位反转置换,其后的电路分为lgn级,每一级由n/2并行执行的蝴蝶操作所组成',
            '因此电路的深度为Θ(nlgn)')
        print('  电路PARALLEL-FFT的最左边的部分执行位反转置换，其余部分模拟迭代的ITERATIVE-FFT过程',
            '因为最外层for循环的每次迭代均执行n/2次独立的蝴蝶操作,所以电路并行地执行它们,在过程ITERATIVE-FFT中每次迭代的值s对应于图中的一级蝴蝶',
            '在第s级中(s=1,2,...,lgn),有n/2^s组蝴蝶(对应于ITERATIVE-FFT中k的每个值),每组中有2^(s-1)个蝴蝶(对应于ITERATIVE-FFT中j的每个值)',
            '图中所示的蝴蝶对应于最内层循环,蝴蝶中用到的旋转因子对应于ITERATIVE-FFT中用到的那些旋转因子')
        print('练习30.3-1 试说明如何用过程ITERATIVE-FFT计算出输入向量(0,2,3,-1,4,5,7,9)的DFT')
        print('练习30.3-2 试说明如何把位反转置换放在计算过程的最后而不是在开始处,以实现FFT算法.(提示：考虑逆DFT)')
        print('练习30.3-3 ITERATIVE-FFT在每级中计算旋转因子多少次，重写ITERATIVE-FFT,使其在阶段s中只计算旋转因子2^(s-1)次')
        print('练习30.3-4 假设FFT电路中的加法器有时会发生错误:不论输入如何,它们的输出总是为0.假定确有一个加法器发生上述情况',
            '描述如何能够通过给整个FFT电路提供输入值并观察其输出,来找到那个产生错误的加法器')
        print('思考题30-1 分治算法')
        print('a) 说明如何仅用三次乘法,就能求出线性多项式ax+b与cx+d的乘积,有一个乘法运算是(a+b)·(c+d)')
        print('b) 试写出两种分治算法,使其在Θ(n^lg3)的运行时间内,求出两个次数界为n的多项式的乘积。第一个算法把输入多项式的系数分成高阶系数与低阶系数各一半',
            '第二个算法根据其系数下标的奇偶性来进行划分')
        print('c) 证明：用O(n^lg3)步可以计算出两个n比特的整数的乘积,其中每一步至多对固定数量1比特的值进行操作')
        print('思考题30-2 Toeplitz矩阵')
        print('  Toeplitz矩阵是一个满足如下条件的n*n矩阵A=(aij):aij=ai-1,j-1; i=2,3,...,n; j=2,3,...,n')
        print('a) 两个Toelitz矩阵的和是一定是Toeplitz矩阵，积也是Toelitz矩阵')
        print('b) 试说明如何表示Toeplitz矩阵,才能在O(n)时间内求出两个n*nToeplitz矩阵的和')
        print('c) 写出一个运行时间为O(nlgn)的算法,使其能够计算出n*nToeplitz矩阵与n维向量的乘积')
        print('d) 写出一个高效算法,使其能够计算出两个n*nToeplitz矩阵的乘积,并分析算法的运行时间')
        print('思考题30-3 多维快速傅里叶变换')
        print('  可以将1维的离散傅里叶变换推广到d维上')
        print('a) 证明可以通过依次在每个维上计算1维的DFT,来计算一个d维的DFT')
        print('b) 证明维的次序并无影响,因此可以通过在任意次序的d维中计算1维DFT来计算1个d维的DFT')
        print('c) 证明如果通过计算快速傅里叶变换来计算每1维的DFT,则计算一个d维的DFT的总时间是O(nlgn),与d无关')
        print('思考题30-4 求多项式在某一点的所有阶导数的值')
        print('  证明：可以在O(nlgn)的时间内,求出A(x)的所有非平凡单数在x0处的值')
        print('思考题30-5 多项式在多个点的求值')
        print('  运用霍纳(Horner)法则,就能够在O(n)的时间内,求出次数界为n-1的多项式在单个点的值',
            '运用FFT也能够在O(nlgn)的时间内,求出多项式在所有n个单位复根处的值.',
            '可以在O(nlg^2(n))的时间内,求出一个次数界为n的多项式在任意n个点的值')
        print('思考题30-6 运用模运算的FFT')
        print('  离散傅里叶变换(DFT)要求使用复数,因此,由于舍入误差而导致精确性下降.对某些问题来说,已知其答案仅包含整数,并且为了保证准确地计算出答案',
            '要求我们利用基于模运算的一种FFT的变异。例如求两个整系数的多项式对的积的问题就属于这类问题',
            '即运用一个长度为Ω(n)位的模来处理n个点的DFT.')
        print('a) 假定我们寻找最小的k,使p=kn+1为质数。证明：我们预计k约为lgn(k的值可能比lgn大一些或小一些),但我们能够',
            '合理地预计出k的O(lgn)个候选值的平均值。p的预计长度与n的长度有什么关系')
        # python src/chapter30/chapter30note.py
        # python3 src/chapter30/chapter30note.py

chapter30_1 = Chapter30_1()
chapter30_2 = Chapter30_2()
chapter30_3 = Chapter30_3()

def printchapter30note():
    """
    print chapter30 note.
    """
    print('Run main : single chapter thirty!')
    chapter30_1.note()
    chapter30_2.note()
    chapter30_3.note()

# python src/chapter30/chapter30note.py
# python3 src/chapter30/chapter30note.py

if __name__ == '__main__':  
    printchapter30note()
else:
    pass
