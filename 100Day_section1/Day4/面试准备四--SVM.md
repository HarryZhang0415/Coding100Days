# SVM 总结

## 1. SVM原理小结

SVM是一种二分类模型，它的基本模型是在特征空间中寻找间隔最大化的分离超平面的线性分类器。(间隔最大化是它的独特之处)，通过该超平面实现对未知样本集的分类

* 当训练样本线性可分时，通过硬间隔最大化，学习一个线性分类器，即线性可分支持向量机
* 当训练数据近似线性可分时，引入松弛变量，通过软间隔最大化，学习一个线性分类器，即线性支持向量机
* 当训练数据线性不可分时，通过使用核技巧及软间隔最大化，学习非线性支持向量机

## 2.SVM核函数意义，种类与选择

### 意义：

原始样本空间中可能不存在可以将样本正确分类为两类的超平面，但是我们知道如果原始空间的维数是有限的，也就是说属性数是有限的，则一定存在一个高维特征空间能够将样本划分。SVM通过核函数将输入空间映射到高维特征空间，最终在高维特征空间中构造出最优分离超平面，从而把平面上本身无法线性可分的数据分开。

### 选择

* 如果特征的数量与样本数量相近，选用线性核函数或者LR
* 如果特征的数量小，样本的数量正常，则选用高斯核函数
* 如果特征的数量小，样本的数量很多，由于求解最优化问题的时候，目标函数涉及两两样本计算内积，使用高斯核明显会有很大计算量，所以手动添加一些特征，使得线性可分，然后可以用LR或者线性核SVM
* 可以交叉验证，试用不同的核函数，误差最小即为最好
* 混合核函数方法，将不同的核函数结合起来

## 3. SVM为什么采用间隔最大化

当训练数据线性可分时，存在无穷个分离超平面可以将两类数据正确分开。感知机或神经网络等利用误分类最小策略，求得分离超平面，不过此时的解有无穷多个。线性可分支持向量机采用间隔最大化求得分离超平面，此时，解是唯一的。另一方面，此时的分隔超平面所产生的分类结果是最鲁棒性的，对未知实例的泛化能力最强。

## 4. SVM对噪声敏感

1. 少数支持向量决定了最终结果，这不但可以帮助我们抓住关键样本、“剔除”大量冗余样本，而且使得该方法不但算法简单，其具有较好的鲁棒性。增、删非支持向量样本对模型没有影响，支持向量样本集具有一定的鲁棒性，有些应用中SVM方法对核的选取不敏感

2. 当噪声出现的过多，以及当噪声出现并成为支持向量的时候，噪声对模型的影响是巨大的。所以此时SVM对噪声不具有鲁棒性。有两种情况会增大噪声成为支持向量的概率：1、噪声太多 2、噪声以新的分布形式出现，与原先样本集的噪声分布表现差异明显。此时噪声也有大概率落在最大分类间隔中间，从而成为支持向量，影响模型

## 5.SVM缺失值影响

SVM没有缺失值处理策略，若存在缺失值，距离函数以及高斯核无法正常判断。所以特征的好坏对SVM的性能很重要。

## 6. SVM在大数据上有哪些缺陷

SVM的空间消耗主要是在存储训练样本和核函数，由于SVM是借助二次规划来求解支持向量，而求解二次规划将涉及m阶矩阵的计算(m为样本的个数)，当m数量很大时，该矩阵的存储和计算将耗费大量的内存以及运算时间。

## 7. SVM防止过拟合以及如何调节惩罚因子C

SVM自带L2正则项的分类器。SVM防止过拟合的主要技巧就在于调整软间隔松弛变量的惩罚因子C。C越大表明越不能容忍错分，当无穷大时则退化为硬间隔分类器。适合的C大小可以减小异常值的影响。

## 8.SVM优缺点

优点：

1. 非线性映射是SVM方法的理论基础， SVM利用内积核函数代替高维空间的非线性映射

2. 对特征空间划分的最优超平面是SVM的目标，最大化分类边界思想是SVM方法的核心

3. 支持向量是SVM训练的结果，SVM分类决策中起到决定作用的是支持向量

4. SVM的最终决策函数只由少数的支持向量所确定，计算的复杂性取决于支持向量的数目，而不是样本空间的维数。

5. 小样本集上分类效果通常比较好。

6. 少数支持向量决定了最终结果,这不但可以帮助我们抓住关键样本、“剔除”大量冗余样本,而且注定了该方法不但算法简单,而且具有较好的“鲁棒”性。这种“鲁棒”性主要体现在:

   ​	增、删非支持向量样本对模型没有影响; 支持向量样本集具有一定的鲁棒性; 有些成功的应用中,SVM 方法对核的选取不敏感

7. SVM 是一种有坚实理论基础的新颖的小样本学习方法。它基本上不涉及概率测度及大数定律等,因此不同于现有的统计方法。从本质上看,它避开了从归纳到演绎的传统过程,实现了高效的从训练样本到预报样本的“转导推理”,大大简化了通常的分类和回归等问题

缺点：

1. SVM算法对大规模训练样本难以实施。由于SVM是借助二次规划来求解支持向量，而求解二次规划将涉及m阶矩阵的计算（m为样本的个数），当m数目很大时该矩阵的存储和计算将耗费大量的机器内存和运算时间（上面有讲）。有比较多的改进算法及分布式的方法研究
2. 用SVM解决多分类问题存在困难。传统的SVM就是解决二分类问题的，上面有介绍不少解决多分类问题的SVM技巧，不过各种方法都一定程度上的缺陷。
3. 对缺失值敏感，核函数的选择与调参比较复杂。


