# Lecture 11：微积分，按幻灯片逐页复述

来源：[lecture11.pdf](/Users/cichlidfish/COMP3670/comp3670_lectures/lecture11.pdf)，共 69 个 PDF 页面，课件印刷编号从 0/62 到 62/62，另含不增加编号的章节页。下文按 PDF 实际顺序逐页复述，同时标注印刷页码，保留全部定义、表格、例题、推导、图意与提醒。每节附原页核对图。数学上的必要限定标为“理解补充”，以免把讲义的简化说法误当成无条件定理。

## 第 1 页（课件 0/62）：主题与讲师

本讲是 COMP3670/COMP6670《Introduction to Machine Learning》的 Lecture 11：Calculus，讲师 Diego Marcondes，2026 年第二学期，Australian National University。主题是为模型训练建立微积分语言。

<details>
<summary>展开第 1 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 1 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-01.jpg)

</details>

## 第 2 页（课件 1/62）：回到 Lecture 4 留下的问题

Lecture 2、3 讨论能否学习，Lecture 4 提供模型，但很多地方最后都说“接下来最小化这个式子”。硬币最大似然曾在五个候选值中读出 $\widehat\theta=7/10$，尚未解释如何计算一般的最大似然估计；逻辑回归要最小化交叉熵，却没有闭式解；最小二乘要使残差平方和最小；SVM 暂交给数值方法，并承诺之后介绍凸优化。现在要回答：知道目标函数以后，怎样真正算出最优参数？

<details>
<summary>展开第 2 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 2 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-02.jpg)

</details>

## 第 3 页（课件 2/62）：优化的是参数的函数

| 问题 | 固定什么 | 改变什么 | 目标 |
|---|---|---|---|
| 硬币 | 10 次中 7 次正面 | $\theta$ | 最大化 $L(\theta)=120\theta^7(1-\theta)^3$ |
| 逻辑回归 | 样本 $D_N$ | $w_0,\ldots,w_d$ | 最小化平均交叉熵 $-LL(w)/N$ |
| 最小二乘 | 样本 $D_N$ | $\theta$ | 最小化 $\sum_i(Y_i-h(X_i;\theta))^2$ |
| 软间隔 SVM | 样本及 $C$ | $w,b$ | 最小化 $\frac12\|w\|^2+C\sum_i\max\{0,1-y_i(\langle w,x_i\rangle+b)\}$ |

每行都固定数据、改变参数，因此是在研究参数的函数。最大化 $L$ 等价于最小化 $-L$。右图把横轴参数与纵轴目标值连起来，标出曲线谷底：训练最终成为找函数最小值的问题。

<details>
<summary>展开第 3 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 3 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-03.jpg)

</details>

## 第 4 页（课件 3/62）：拟合模型的内部是优化算法

教程中一行 `LinearRegression().fit(features, y_reg)` 能返回模型参数，是因为内部运行了优化算法。其实已经手动接触过三种：PLA 找误分类点、修正权重、重复；K-means 重算质心、重分配点、重复；SVM 更新先缩小权重，再根据违反间隔的点修正、重复。共同结构是“选择起点、改进一点、不断重复”。下一讲研究怎样设计改进步骤并期望它收敛；本讲先用微积分研究函数行为以及最小、最大点的特征。

<details>
<summary>展开第 4 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 4 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-04.jpg)

</details>

## 第 5 页（课件 4/62）：贯穿全讲的单参数回归

模型为过原点直线 $h_\theta(x)=\theta x$，$\theta\in\mathbb R$，观测为 $(1,2),(2,5),(3,4),(4,9)$。平方损失下

$$E_{in}(\theta)=\frac14\sum_{i=1}^4(y_i-\theta x_i)^2=7.5\theta^2-30\theta+31.5.$$

左图画出 $\theta=1,2,3$ 三条候选直线与数据；右图画每个参数的误差，$\theta=0,1,2,3,4$ 时分别是 $31.5,9,1.5,9,31.5$。拟合就是找右图最低点，这里可看出 $\widehat\theta=2$。若有数百参数，就不能靠画图，需要算法。

<details>
<summary>展开第 5 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 5 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-05.jpg)

</details>

## 第 6 页（课件 5/62）：本讲与后续课程的安排

本讲提供语言：函数与极限、导数及求导规则、最大最小值、凸性、多变量。之后讨论算法：凸问题、最小二乘、梯度下降、随机梯度下降以及 Adam。图用箭头表示从数学语言走向训练算法。

<details>
<summary>展开第 6 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 6 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-06.jpg)

</details>

## 第 7 页（课件 5/62，章节页）：Calculus

正式进入微积分，先讲函数、极限与连续性。此页只是章节标题，没有新增公式。

<details>
<summary>展开第 7 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 7 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-07.jpg)

</details>

## 第 8 页（课件 6/62）：函数的定义

函数 $f:A\to B$ 给每个输入 $x\in A$ 恰好分配一个输出 $f(x)\in B$。图例是输入 3，经规则 $h(x)=2x$ 后输出 $h(3)=6$。“恰好一个输出”是关键：两个输入可以有相同输出，但一个输入不能同时有两个输出。函数不一定以公式表示，表格、图或计算机程序也可以定义函数。

<details>
<summary>展开第 8 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 8 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-08.jpg)

</details>

## 第 9 页（课件 7/62）：本课程里两种不同的函数

假设函数 $h$ 把数据点 $x$ 变成预测，参数固定，例如 $x\mapsto\theta x$。误差函数 $E_{in}$ 把参数 $\theta$ 变成一个数，数据固定，例如 $\theta\mapsto\frac14\sum_i(y_i-\theta x_i)^2$。表达式中虽然都有 $\theta x$，自变量却不同。要根据上下文与记号辨认输入，例如 $f(x),f(t),f(x,t),g(x),h(x),E_{in}(\theta),L(\theta),L_n(\theta)$。

<details>
<summary>展开第 9 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 9 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-09.jpg)

</details>

## 第 10 页（课件 8/62）：五类基本函数

图中依次画直线 $ax+b$、抛物线 $x^2$、指数 $e^x$、对数 $\log x$、逻辑曲线 $1/(1+e^{-x})$。本课的 $\log$ 均指自然对数，它是指数函数的逆，$\log(e^x)=x$。对数把乘积变成和：$\log(ab)=\log a+\log b$，这正是 Lecture 4 把似然乘积改成对数似然和式的原因。$e^x$ 和 $\log x$ 都随输入增加而增加。

<details>
<summary>展开第 10 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 10 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-10.jpg)

</details>

## 第 11 页（课件 9/62）：由基本函数组合模型

主要有三种构造方式：和 $(f+g)(x)=f(x)+g(x)$，例如逐观测损失相加；积 $(fg)(x)=f(x)g(x)$，例如硬币似然 $\theta^7(1-\theta)^3$；复合 $(g\circ f)(x)=g(f(x))$，例如先算残差 $y-\theta x$，再平方。流程图用标签为 1 的单个观测解释逻辑回归：参数 $w_0,w_1$ 先给出分数 $z=w_1x+w_0$，再给出概率 $p=1/(1+e^{-z})$，最后给出损失 $-\log p$。

<details>
<summary>展开第 11 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 11 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-11.jpg)

</details>

## 第 12 页（课件 10/62）：靠近一点时发生什么——极限

考虑分段函数

$$f(x)=\begin{cases}(x^2-1)/(x-1),&x<3,\\1,&x\ge3.\end{cases}$$

在 $x=1$ 处第一段无定义。图在 $(1,2)$ 有空洞，在 $x=3$ 有从接近 4 跳到 1 的阶跃。趋近 2 时左右都趋于 3，等于 $f(2)$；趋近 1 时左右都趋于 2，虽然 $f(1)$ 不存在；趋近 3 时左边趋于 4、右边趋于 1，因此两侧极限不存在。写作 $\lim_{x\to1}f(x)=2$，强调靠近而不必到达该点。

<details>
<summary>展开第 12 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 12 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-12.jpg)

</details>

## 第 13 页（课件 11/62）：极限的含义

$\lim_{x\to a}f(x)=L$ 表示让 $x$ 足够接近 $a$、但不等于 $a$，便能使 $f(x)$ 任意接近 $L$。$f(a)$ 的值不参与决定极限，它可能不存在，也可能不等于 $L$。左右趋近不同数时，极限可能不存在。Lecture 2 的定积分也是一个极限：矩形宽度 $\Delta x\to0$ 时，黎曼和趋向积分。严格的 $\epsilon$–$\delta$ 定义超出本课范围。

<details>
<summary>展开第 13 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 13 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-13.jpg)

</details>

## 第 14 页（课件 12/62）：连续、不连续和替代损失

在 $a$ 连续意味着 $\lim_{x\to a}f(x)=f(a)$，即输入微变时输出也微变，没有跳跃。前述五类函数在各自定义域连续，指示函数则从 0 跳到 1。

取阈值模型 $h_\theta(x)=\mathbf1\{x>\theta\}$，四个点 $x_1<x_2<x_3<x_4$ 标签为 $0,0,1,1$，则

$$E_{in}(\theta)=\tfrac14\sum_{i=1}^4\mathbf1\{h_\theta(x_i)\ne y_i\}
=\tfrac14[\mathbf1\{x_1>\theta\}+\mathbf1\{x_2>\theta\}+\mathbf1\{x_3\le\theta\}+\mathbf1\{x_4\le\theta\}].$$

每个指示项在参数经过相应 $x_i$ 时切换，误差图是阶梯，在大部分位置微调参数不会改变误差。图对比了阶梯二元损失与平滑替代损失，这就是需要 surrogate loss 的动机。

<details>
<summary>展开第 14 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 14 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-14.jpg)

</details>

## 第 15 页（课件 12/62，章节页）：The derivative

从函数值转向函数变化速度，也就是导数。

<details>
<summary>展开第 15 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 15 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-15.jpg)

</details>

## 第 16 页（课件 13/62）：平均变化率

输入从 $x$ 到 $x+\Delta x$，输出变化 $\Delta f=f(x+\Delta x)-f(x)$，平均变化率为

$$\frac{\Delta f}{\Delta x}=\frac{f(x+\Delta x)-f(x)}{\Delta x}.$$

它是图上连接两点的割线斜率。贯穿例子中，$\theta$ 从 0 到 1、1 到 2、2 到 3、3 到 4、0 到 4 的平均变化率依次为 $-22.5,-7.5,7.5,22.5,0$。图标出第一段 $\Delta\theta=1,\Delta E_{in}=-22.5$。平均值依赖区间，也可能掩盖区间内部的先降后升，所以要研究某一个点的瞬时变化率。

<details>
<summary>展开第 16 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 16 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-16.jpg)

</details>

## 第 17 页（课件 14/62）：从割线到切线

固定第一个点，让第二点靠近，割线逐渐趋近切线。对于 $f(x)=x^2$ 在 $x=1$，当 $\Delta x=1,0.1,0.01,0.001$ 时，割线斜率为 $3,2.1,2.01,2.001$，趋于 2。不能直接令 $\Delta x=0$，因为原差商将成为 $0/0$；要取极限。

<details>
<summary>展开第 17 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 17 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-17.jpg)

</details>

## 第 18 页（课件 15/62）：导数的定义

$$f'(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}.$$

极限存在就称 $f$ 在 $x$ 可微。图形上是切线斜率，变化率上是瞬时变化速度；对 $E_{in}(\theta)$，它描述参数在当前值微动时误差变化多快。导数也写作 $df/dx$。积分是薄矩形和的极限，导数是小变化比值的极限，两者都研究 $\Delta x\to0$。

<details>
<summary>展开第 18 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 18 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-18.jpg)

</details>

## 第 19 页（课件 16/62）：从定义算一次导数

对 $x^2$，

$$\frac{(x+\Delta x)^2-x^2}{\Delta x}
=\frac{x^2+2x\Delta x+(\Delta x)^2-x^2}{\Delta x}
=\frac{2x\Delta x+(\Delta x)^2}{\Delta x}=2x+\Delta x\to2x.$$

因此 $(x^2)'=2x$，在 $x=1$ 时等于 2，与割线表一致。贯穿例子的平均变化率为 $15\theta-30+7.5\Delta\theta$，所以 $E'_{in}(\theta)=15\theta-30$。课件说明这是本课程唯一直接计算的极限；之后提供求导规则而不逐一证明。

<details>
<summary>展开第 19 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 19 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-19.jpg)

</details>

## 第 20 页（课件 17/62）：导数的三种解释

导数既是切线斜率，又是输出的瞬时变化率，也表示对输入的敏感度：输入微动 $\Delta x$ 时，输出约变 $f'(x)\Delta x$。正号表示输入增加时输出增加，负号表示输出减少；绝对值越大，敏感程度越强。机器学习最关心第三种解释：参数改一点，误差会向哪个方向、改变多少？

<details>
<summary>展开第 20 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 20 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-20.jpg)

</details>

## 第 21 页（课件 18/62）：导数本身也是函数

每一点都有切线斜率，因此导数也是输入的函数。贯穿例子 $E'_{in}(\theta)=15\theta-30$，在 $\theta=0,1,2,3,4$ 时分别为 $-30,-15,0,15,30$。图上方是误差抛物线，下方是导数直线：2 左侧导数为负、误差下降；2 右侧导数为正、误差上升；2 处导数为零、切线水平。

<details>
<summary>展开第 21 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 21 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-21.jpg)

</details>

## 第 22 页（课件 19/62）：局部线性近似

$$f(x+\Delta x)\approx f(x)+f'(x)\Delta x\qquad(\Delta x\text{ 很小时}).$$

即“新值约等于旧值加斜率乘步长”，函数在一点附近像它的切线。例子在 $\theta=1$ 时误差 9、导数 -15；走 0.1，预测误差为 7.5，真实为 7.575。若走 1，预测到 $\theta=2$ 的误差是 -6，但真实为 1.5。图显示切线向下延长后的巨大偏差，强调近似只在局部可靠。

<details>
<summary>展开第 22 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 22 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-22.jpg)

</details>

## 第 23 页（课件 20/62）：往哪个方向下坡

小步的函数变化约为 $f'(x)\Delta x$。要让它为负，步长应与导数异号：斜率正就向左，斜率负就向右。所以沿 $-f'(x)$ 走。梯度下降的初步形式是反复执行 $x\leftarrow x-\alpha f'(x)$，$\alpha>0$ 足够小。只使用当前位置导数；在导数非零且步长足够小的情况下，函数值会下降。

<details>
<summary>展开第 23 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 23 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-23.jpg)

</details>

## 第 24 页（课件 21/62）：导数不存在的地方

图中有三种例子：$|x|$ 在 0 有尖角，左斜率 -1、右斜率 +1，没有唯一切线；hinge loss $\max\{0,1-m\}$ 在间隔 $m=1$ 有尖角；指示函数有跳跃，甚至不连续。可微必连续。尖角之外通常仍能求导，因此尖角比跳跃温和；损失通常设计成连续，并尽量平滑。

<details>
<summary>展开第 24 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 24 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-24.jpg)

</details>

## 第 25 页（课件 21/62，章节页）：Rules of differentiation

进入求导规则，以便不必每次重新计算极限。

<details>
<summary>展开第 25 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 25 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-25.jpg)

</details>

## 第 26 页（课件 22/62）：怎样计算导数

需要两部分：少数基本函数的导数表，以及组合函数的求导规则。知道基本函数的导数及和、积、复合的规则，就能处理很大一类函数。对本课损失，简单情形可以手算，复杂情形交给计算机。

<details>
<summary>展开第 26 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 26 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-26.jpg)

</details>

## 第 27 页（课件 23/62）：基本导数表

| 函数 | 导数 |
|---|---|
| 常数 $c$ | $0$ |
| $x$ | $1$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\log x$ | $1/x$ |

常数不变，故变化率为 0。幂函数规则是指数移到前面、指数减一，也适用于 $x^{-1}$ 和 $x^{1/2}$：$(1/x)'=-1/x^2$，$(\sqrt x)'=1/(2\sqrt x)$。指数函数越大增长越快，而且导数等于自身。对数仍增加，但斜率 $1/x$ 随 $x$ 增大而减小。各结果都能由定义证明，本页省略证明。

<details>
<summary>展开第 27 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 27 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-27.jpg)

</details>

## 第 28 页（课件 24/62）：和与常数倍

若 $f,g$ 可微，$c$ 为常数，则 $(f+g)'=f'+g'$，$(cf)'=cf'$。因此贯穿例子求导为 $7.5\times2\theta-30\times1+0=15\theta-30$。若 $E_{in}(\theta)=\frac1N\sum_i\ell_i(\theta)$，其中 $\ell_i=(y_i-\theta x_i)^2$，则

$$E'_{in}(\theta)=\frac1N\sum_i\ell'_i(\theta).$$

平均的导数就是导数的平均，每个观测贡献自己的导数。

<details>
<summary>展开第 28 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 28 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-28.jpg)

</details>

## 第 29 页（课件 25/62）：乘积法则

$$(fg)'(x)=f'(x)g(x)+f(x)g'(x).$$

不是两个导数直接相乘。对 $x^2=x\times x$，结果为 $1\times x+x\times1=2x$，不是 1。表中三个例子分别是 $(x^2e^x)'=2xe^x+x^2e^x$，$(x\log x)'=\log x+1$，$(p(1-p))'=1-2p$。

<details>
<summary>展开第 29 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 29 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-29.jpg)

</details>

## 第 30 页（课件 26/62）：链式法则

若 $u=f(x),y=g(u)$，则

$$\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}=g'(f(x))f'(x).$$

图从输入微动 $\Delta x$，经第一环放大 $f'(x)$，再经第二环放大 $g'(u)$，说明变化率相乘。如果 $u$ 变化速度是 $x$ 的 3 倍，$y$ 又是 $u$ 的 2 倍，则 $y$ 是 $x$ 的 6 倍。外层导数必须在内层输出 $u=f(x)$ 处求值，不能误代入 $x$。这是机器学习中尤其关键的规则。

<details>
<summary>展开第 30 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 30 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-30.jpg)

</details>

## 第 31 页（课件 27/62）：链式法则三步骤与四个例子

先命名内层函数 $u$，再对 $u$ 求外层导数，最后乘以内层对输入的导数：

| 原函数 | 内层 $u$ | 外层 | 导数 |
|---|---|---|---|
| $(x^3-1)^{100}$ | $x^3-1$ | $u^{100}$ | $100(x^3-1)^{99}3x^2$ |
| $e^{-x^2}$ | $-x^2$ | $e^u$ | $e^{-x^2}(-2x)$ |
| $\log(1-\theta)$ | $1-\theta$ | $\log u$ | $-1/(1-\theta)$ |
| $e^{-z}$ | $-z$ | $e^u$ | $-e^{-z}$ |

第一例若不用链式法则，可能要先展开 300 次多项式。课件要求练习写出表格中的计算细节。

<details>
<summary>展开第 31 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 31 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-31.jpg)

</details>

## 第 32 页（课件 28/62）：对平方损失使用链式法则

单个固定观测 $(x,y)$，$h_\theta(x)=\theta x$，$\ell(\theta)=(y-\theta x)^2$。内层残差 $u=y-\theta x$ 的导数为 $-x$，外层平方的导数为 $2u$，所以

$$\ell'(\theta)=-2x(y-\theta x),\quad E'_{in}(\theta)=-\frac2N\sum_ix_i(y_i-\theta x_i).$$

这叫“残差乘输入”。贯穿例子为 $-\frac24[(2-\theta)+2(5-2\theta)+3(4-3\theta)+4(9-4\theta)]=15\theta-30$，与先展开再求导一致。

<details>
<summary>展开第 32 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 32 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-32.jpg)

</details>

## 第 33 页（课件 29/62）：逻辑函数及其导数

令 $\sigma(z)=1/(1+e^{-z})$。内层 $u=1+e^{-z}$，外层 $1/u$，链式法则得到

$$\sigma'(z)=\frac{e^{-z}}{(1+e^{-z})^2}=\sigma(z)(1-\sigma(z)).$$

课件在等价化简处提出“why?”。理解补充：$1-\sigma(z)=e^{-z}/(1+e^{-z})$，相乘即上式。图画 S 形的 $\sigma$ 和钟形的 $\sigma'$；最大斜率在 $z=0$，$\sigma(0)=1/2,\sigma'(0)=1/4$。远离 0 时曲线变平、导数接近零。

<details>
<summary>展开第 33 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 33 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-33.jpg)

</details>

## 第 34 页（课件 30/62）：长链、自动微分与反向传播

模型可能是一条很长的复合链。例子是 $w\to z=wx\to p=\sigma(z)\to\ell=-\log p$，各环局部导数分别为 $x,p(1-p),-1/p$。相乘得到

$$\frac{d\ell}{dw}=-\frac1p\,p(1-p)x=-(1-p)x.$$

每个模块只需要自己的导数和输入值。自动微分（automatic differentiation）把这种机械过程算法化，是 PyTorch、JAX、TensorFlow 等库的基础；在神经网络中从损失往回应用链式法则，称为反向传播（backpropagation）。

<details>
<summary>展开第 34 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 34 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-34.jpg)

</details>

## 第 35 页（课件 31/62）：求导规则回顾

本页再次并列列出常数、幂、指数、对数的导数，以及和、常数倍、乘积、复合规则。商不需要独立新规则：把 $f/g$ 写成 $f\,g^{-1}$，结合乘积与链式法则。后续最常用的三个结果为平方损失导数 $-2x(y-\theta x)$、$\log\theta$ 的导数 $1/\theta$，以及 $\sigma'(z)=\sigma(z)(1-\sigma(z))$。

<details>
<summary>展开第 35 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 35 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-35.jpg)

</details>

## 第 36 页（课件 31/62，章节页）：Maxima and minima

开始用导数研究最大值和最小值。

<details>
<summary>展开第 36 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 36 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-36.jpg)

</details>

## 第 37 页（课件 32/62）：递增与递减

如果一个区间上处处 $f'(x)>0$，函数在该区间递增；处处 $f'(x)<0$ 则递减。图用不同颜色的区段对应导数正、负、正。例子 $15\theta-30$ 在 $\theta<2$ 为负、$\theta>2$ 为正，所以误差降到 2 后再上升。导数为零的点，例如 2，称为临界点（critical point）。

<details>
<summary>展开第 37 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 37 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-37.jpg)

</details>

## 第 38 页（课件 33/62）：观察四个临界点

图中一条曲线有四个画出水平切线的点，两个蓝点位于局部峰顶，两个绿点位于局部谷底。课件提出两个问题：四个点的共同点是什么？绿色两点和蓝色两点各有什么共同点？理解补充：四者导数都为零；绿点是局部极小，蓝点是局部极大；两个谷底的高度不同，已暗示局部最小不一定全局最小。

<details>
<summary>展开第 38 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 38 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-38.jpg)

</details>

## 第 39 页（课件 34/62）：局部、全局最小与 arg min

若对所有 $x$ 都有 $f(c)\le f(x)$，$c$ 是全局最小点；只对 $c$ 附近所有 $x$ 成立，则是局部最小点。全局一定局部，反过来不成立。要分清最小点 $c=\arg\min_xf(x)$ 与最小值 $f(c)=\min_xf(x)$：学习要的是参数 $\widehat\theta=\arg\min_\theta E_{in}(\theta)$，最小误差只是该参数下的数值。目标是全局最小，而局部微积分检验首先看到的是局部。最大值有完全类似的定义。

<details>
<summary>展开第 39 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 39 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-39.jpg)

</details>

## 第 40 页（课件 35/62）：Fermat 定理

可微函数在局部极小或局部极大点 $c$ 满足 $f'(c)=0$。对于局部极小，若导数为正，向左走会降；若导数为负，向右走会降，都与局部最小矛盾。因此先求 $f'(x)=0$，再判断候选点并比较函数值，就把优化转化成求方程。有时能手算，更多时候要算法。

理解补充：这里针对定义域内部、可微且最优值存在的情形；一般有边界或不可微点的优化，还要检查这些位置，不能只检查零导数。

<details>
<summary>展开第 40 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 40 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-40.jpg)

</details>

## 第 41 页（课件 36/62）：零导数不充分

临界点可能是局部极小（导数由负变正）、局部极大（由正变负），也可能两者都不是，例如 $x^3$ 在 0 导数为零，但两侧导数仍为正。检查两侧导数符号就是一阶导数检验。即便确定是局部最小，也未必是全局最小，因此 $f'=0$ 一般只给候选点。

<details>
<summary>展开第 41 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 41 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-41.jpg)

</details>

## 第 42 页（课件 37/62）：二阶导数

$f''$ 是导数 $f'$ 的导数，表示斜率变化的速度。$f''>0$ 时斜率增加、曲线向上弯；$f''<0$ 时斜率减少、曲线向下弯。图里的 $x^2$ 与 $\sqrt x$ 都递增，但前者 $f''=2>0$ 向上弯，后者 $f''=-\frac14x^{-3/2}<0$ 向下弯。贯穿例子 $E''_{in}=15$。临界点斜率虽为零，仍可根据斜率怎样经过零来分类。

<details>
<summary>展开第 42 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 42 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-42.jpg)

</details>

## 第 43 页（课件 38/62）：二阶导数检验

若 $f'(c)=0,f''(c)>0$，则 $c$ 是局部最小点；若 $f''(c)<0$，是局部最大点。原因是斜率增加并经过零时，函数先降后升；斜率减少并经过零时，函数先升后降。图同时画函数和导数来对应这个变化。贯穿例子在 2 的二阶导数为 15，因此是局部最小。若 $f''(c)=0$，检验没有结论：$x^3$ 和 $x^4$ 在 0 都满足这一点，但前者没有局部最小、后者有。

<details>
<summary>展开第 43 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 43 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-43.jpg)

</details>

## 第 44 页（课件 39/62）：例子——推导硬币最大似然

10 次中 7 次正面，$L(\theta)=120\theta^7(1-\theta)^3$。因为 $\log$ 递增，最大化似然等价于最大化对数似然，也等价于最小化其负值：

$$-LL(\theta)=-\log120-7\log\theta-3\log(1-\theta).$$

逐项求导，$(-LL)'=-7/\theta+3/(1-\theta)$。令其为零，得到 $3\theta=7(1-\theta)$，即 $10\theta=7$，所以 $\widehat\theta=7/10$。这回不是从候选表读取，而是算出答案。

<details>
<summary>展开第 44 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 44 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-44.jpg)

</details>

## 第 45 页（课件 40/62）：一般成功比例的最大似然

$N$ 次独立试验中成功 $k$ 次，$-LL=\text{constant}-k\log\theta-(N-k)\log(1-\theta)$，因此

$$(-LL)'=-\frac{k}{\theta}+\frac{N-k}{1-\theta}=0\quad\Longrightarrow\quad\widehat\theta=\frac{k}{N}.$$

二阶导数 $k/\theta^2+(N-k)/(1-\theta)^2>0$，得到局部最小。图给出 $k=7,N=10$ 的负对数似然，在 0.7 处最低。相同的“取对数、求导、置零”方法也能推导 Lecture 4 正态族的均值与方差最大似然估计，本页没有展开其推导。

理解补充：上面的内点求导适用于 $0<k<N$；全成功或全失败时，最优比例位于参数区间边界 1 或 0。

<details>
<summary>展开第 45 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 45 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-45.jpg)

</details>

## 第 46 页（课件 41/62）：例子——单参数最小二乘

对 $h_\theta(x)=\theta x$，由

$$E_{in}=\frac1N\sum_i(y_i-\theta x_i)^2,\quad E'_{in}=-\frac2N\sum_ix_i(y_i-\theta x_i)$$

令导数为零，得到 $\sum_ix_iy_i=\theta\sum_ix_i^2$，从而

$$\widehat\theta=\frac{\sum_ix_iy_i}{\sum_ix_i^2},\qquad E''_{in}=\frac2N\sum_ix_i^2>0.$$

贯穿例子为 $(2+10+12+36)/(1+4+9+16)=60/30=2$，二阶导数 $2\times30/4=15$。至此两个例子都找到了局部最小，但还没说明为什么是全局最小。

理解补充：公式要求 $\sum_ix_i^2>0$；若所有 $x_i=0$，误差与参数无关，不能这样相除。

<details>
<summary>展开第 46 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 46 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-46.jpg)

</details>

## 第 47 页（课件 41/62，章节页）：Convexity

引入整个函数的形状条件，以便从局部结论得到全局结论。

<details>
<summary>展开第 47 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 47 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-47.jpg)

</details>

## 第 48 页（课件 42/62）：为什么局部最小是全局最小

$f'(c)=0,f''(c)>0$ 都是某一点的条件，图中两个不同谷底都满足，但只有较低者全局最小。对比表：硬币在 0.7、回归在 2 都满足上述两条件，并且更强地在整个有效定义域都有正二阶导数；图中较高谷底虽满足点条件，却不满足处处正二阶导数。需要的正是能事先保证零导数意味着全局最小的全局性质——凸性。

<details>
<summary>展开第 48 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 48 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-48.jpg)

</details>

## 第 49 页（课件 43/62）：凸函数与凹函数的定义

对任意 $x,y$ 及 $a,b\ge0,a+b=1$，若

$$f(ax+by)\le af(x)+bf(y),$$

则 $f$ 凸。如果 $-f$ 凸，则 $f$ 凹。$ax+by$ 是输入的加权平均，右边是两端高度的加权平均，即弦上的高度。图中函数位于弦下面，因此一句话就是“任意连接两图像点的弦都在图像之上”。

<details>
<summary>展开第 49 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 49 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-49.jpg)

</details>

## 第 50 页（课件 44/62）：凸性的三种图像

三幅图依次说明：每条弦都在图像上方；图像在每条切线上方；斜率不递减，即适当光滑时处处 $f''\ge0$。对足够光滑的函数三者等价。第三种适合计算：求二阶导数并检查整个定义域符号。这里的“每条”“每一点”很关键，凸性不是只检查某个临界点。

<details>
<summary>展开第 50 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 50 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-50.jpg)

</details>

## 第 51 页（课件 45/62）：凸、凹、非凸非凹例子及组合规则

凸例子：$x^2$（二阶导数 2）、$e^x$（二阶导数 $e^x$）、$-\log x$（二阶导数 $1/x^2$）、$|x|$、hinge loss。凹例子：$\log x$（二阶导数 $-1/x^2$）、$\sqrt x$、$-x^2$。两者都不是：$x^3$（二阶导数 $6x$ 变号）、逻辑曲线、阶梯二元损失。

凸函数的和、凸函数的正倍数仍凸；若 $f$ 凸，$f(a\theta+b)$ 对任意实数 $a,b$ 仍凸。因此平方误差平均是凸函数：每项都是凸函数 $u^2$ 与参数仿射表达式的复合，再求和取平均。

<details>
<summary>展开第 51 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 51 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-51.jpg)

</details>

## 第 52 页（课件 46/62）：凸函数的临界点是全局最小

若 $f$ 凸且可微，$f'(c)=0$，则 $c$ 为全局最小点。理由是图像在所有切线之上，而 $c$ 处切线水平、高度为 $f(c)$，因此所有 $x$ 都满足 $f(x)\ge f(c)$。硬币负对数似然和回归误差都是凸函数，因此 0.7 与 2 分别是全局最小点。凸函数每个局部最小都是全局最小，零导数此时给出答案，而不只是候选名单。

<details>
<summary>展开第 52 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 52 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-52.jpg)

</details>

## 第 53 页（课件 47/62）：凸与非凸的下坡图

左图是一个凸谷；右图有两个谷，起点在右侧可能停在橙色局部最小，而错过绿色全局最小。课件列出的凸问题包括最小二乘、ridge、逻辑回归、SVM；非凸问题包括 K-means 与神经网络。图表达的是没有非全局局部最小的几何优势；具体算法能否收敛仍要满足步长等条件，下一讲会说明。

<details>
<summary>展开第 53 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 53 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-53.jpg)

</details>

## 第 54 页（课件 47/62，章节页）：Several variables

把单变量导数推广到多个参数。

<details>
<summary>展开第 54 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 54 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-54.jpg)

</details>

## 第 55 页（课件 48/62）：加入截距后的双参数误差

令 $h_\theta(x)=\theta_0+\theta_1x$，则

$$E_{in}(\theta_0,\theta_1)=\tfrac14\sum_i(y_i-\theta_0-\theta_1x_i)^2
=\theta_0^2+5\theta_0\theta_1+7.5\theta_1^2-10\theta_0-30\theta_1+31.5.$$

参数对 $(0,0),(1,1),(2,1),(0,2)$ 的误差分别是 $31.5,5,3,1.5$。一般模型有 $m$ 个参数，误差是 $f:\mathbb R^m\to\mathbb R$，输入为参数向量，输出仍是一个数。像 Lecture 2 的多维积分一样，核心思想不因维度增加而改变。

<details>
<summary>展开第 55 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 55 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-55.jpg)

</details>

## 第 56 页（课件 49/62）：偏导数

偏导数 $\partial f/\partial x_j$ 是把其他变量都固定后，只对 $x_j$ 求普通导数。固定的变量当成常数使用求导规则。例子中

$$\frac{\partial E_{in}}{\partial\theta_0}=2\theta_0+5\theta_1-10,\qquad
\frac{\partial E_{in}}{\partial\theta_1}=5\theta_0+15\theta_1-30.$$

图固定 $\theta_0=2,0,-2$ 时分别画关于 $\theta_1$ 的抛物线，展示多维曲面的截面。

<details>
<summary>展开第 56 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 56 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-56.jpg)

</details>

## 第 57 页（课件 50/62）：梯度

$$\nabla f(x)=\left(\frac{\partial f}{\partial x_1}(x),\ldots,\frac{\partial f}{\partial x_m}(x)\right)^T\in\mathbb R^m.$$

梯度把对每个输入的敏感度收集成向量；单变量时就是普通导数。贯穿例子 $\nabla E_{in}=(2\theta_0+5\theta_1-10,5\theta_0+15\theta_1-30)^T$。在 $(2,2)$ 为 $(4,10)^T$，对斜率的敏感度超过对截距的两倍；在 $(0,2)$ 为零向量。

<details>
<summary>展开第 57 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 57 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-57.jpg)

</details>

## 第 58 页（课件 51/62）：多变量局部线性近似

$$f(x+\Delta x)\approx f(x)+\nabla f(x)^T\Delta x,$$

其中 $\nabla f(x)^T\Delta x=\sum_j(\partial f/\partial x_j)\Delta x_j$，即各变量的“敏感度乘步长”相加。例子在 $(2,2)$ 时误差 5.5，梯度 $(4,10)^T$，走 $(-0.1,-0.1)^T$，预测变化为 $-1.4$、新误差约 4.1，真实误差 4.235。

<details>
<summary>展开第 58 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 58 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-58.jpg)

</details>

## 第 59 页（课件 52/62）：梯度指向最陡上坡

沿单位方向 $u$ 走小长度 $s$，$f(x+su)\approx f(x)+s\nabla f(x)^Tu$。由 Cauchy–Schwarz，$\nabla f(x)^Tu\le\|\nabla f(x)\|$，非零梯度时取 $u=\nabla f(x)/\|\nabla f(x)\|$ 达等号。故梯度方向最陡上升，梯度长度是该方向斜率，负梯度方向最陡下降。

图用 $f(x_1,x_2)=x_1^2+3x_2^2$ 的等高线 $f=0,1,3,6$ 说明：沿等高线函数不变，其切向方向与梯度内积为零，所以梯度垂直等高线。

<details>
<summary>展开第 59 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 59 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-59.jpg)

</details>

## 第 60 页（课件 53/62）：多变量临界点、极值与鞍点

多变量 Fermat 定理说：若 $f$ 在某个可微内点有局部极小或极大，则 $\nabla f=0$。梯度为零的点叫临界点。图分别画极小点（四周上升）、极大点（四周下降）和鞍点（某些方向上升、另一些方向下降）。鞍点是高维情况下特别需要注意的零梯度点。

<details>
<summary>展开第 60 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 60 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-60.jpg)

</details>

## 第 61 页（课件 54/62）：例子——带截距的最小二乘直线

对 $E_{in}=\frac1N\sum_i(y_i-\theta_0-\theta_1x_i)^2$，令两个偏导数都为零。第一个给出 $\theta_0=\bar y-\theta_1\bar x$；代入第二个，有 $0=\sum_ix_i[(y_i-\bar y)-\theta_1(x_i-\bar x)]$。最后得到

$$\widehat\theta_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad
\widehat\theta_0=\bar y-\widehat\theta_1\bar x.$$

斜率等于对中心化数据应用单参数公式。例子 $\bar x=2.5,\bar y=5$，斜率 $10/5=2$，截距 $5-2\times2.5=0$，最优直线碰巧过原点。接下来还要判断唯一临界点究竟是哪类点。分母为正是使用这个斜率公式的条件。

<details>
<summary>展开第 61 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 61 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-61.jpg)

</details>

## 第 62 页（课件 55/62）：矩阵形式的梯度表

| $x\in\mathbb R^m$ 的函数 | 梯度 | 单变量对应 |
|---|---|---|
| $a^Tx$ | $a$ | $(ax)'=a$ |
| $\|x\|^2=x^Tx$ | $2x$ | $(x^2)'=2x$ |
| $x^TAx$，$A$ 对称 | $2Ax$ | $(ax^2)'=2ax$ |

第一行逐项求导就得到 $a_j$。第三行在二维时展开成 $a_{11}x_1^2+2a_{12}x_1x_2+a_{22}x_2^2$，两个偏导数是 $2a_{11}x_1+2a_{12}x_2$ 与 $2a_{12}x_1+2a_{22}x_2$，正好是 $2Ax$。和与常数倍规则仍然成立。

<details>
<summary>展开第 62 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 62 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-62.jpg)

</details>

## 第 63 页（课件 56/62）：残差平方和的梯度

响应向量 $Y\in\mathbb R^N$，设计矩阵 $X\in\mathbb R^{N\times m}$ 每行对应一个观测，预测为 $X\theta$。展开

$$RSS(\theta)=\|Y-X\theta\|^2=\theta^TX^TX\theta-2Y^TX\theta+Y^TY.$$

根据上页三类梯度，

$$\nabla RSS=2X^TX\theta-2X^TY=-2X^T(Y-X\theta).$$

这把“残差乘输入”同时用于全部观测和参数。例子每行 $X_i^T=(1,x_i)$，$X^TX=\begin{pmatrix}4&10\\10&30\end{pmatrix}$、$X^TY=(20,60)^T$；梯度除以 $N=4$ 就回到平均误差的梯度。

<details>
<summary>展开第 63 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 63 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-63.jpg)

</details>

## 第 64 页（课件 57/62）：Hessian 矩阵

Hessian $\nabla^2f(x)$ 是所有二阶偏导数组成的 $m\times m$ 矩阵，第 $(j,k)$ 项为 $\partial^2f/(\partial x_j\partial x_k)$；足够光滑时对称。第 $j$ 行记录第 $j$ 个一阶偏导随各变量怎样变化，可以理解为“梯度的导数”。$x^TAx$ 的 Hessian 为 $2A$，$RSS$ 的为 $2X^TX$。例子中

$$\nabla^2E_{in}=\begin{pmatrix}2&5\\5&15\end{pmatrix},$$

处处相同。单位方向 $u$ 上的曲率是 $u^T\nabla^2f(x)u$；取斜率方向 $u=(0,1)^T$ 得到 15，与单参数误差的二阶导数一致。

<details>
<summary>展开第 64 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 64 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-64.jpg)

</details>

## 第 65 页（课件 58/62）：多变量凸性与 Hessian

定义仍为 $f(ax+by)\le af(x)+bf(y)$，只是 $x,y\in\mathbb R^m$。对足够光滑、定义域凸的函数，凸当且仅当每一点的 Hessian 都半正定，即对每个 $x,u$ 都有 $u^T\nabla^2f(x)u\ge0$。若凸且梯度为零，该点全局最小。半正定也等价于 Hessian 全部特征值非负。例子的矩阵特征值约 16.7 和 0.3，均正，故误差为凸函数。

<details>
<summary>展开第 65 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 65 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-65.jpg)

</details>

## 第 66 页（课件 59/62）：最小二乘一定是凸问题

任意 $v$ 都满足

$$v^T(2X^TX)v=2(Xv)^T(Xv)=2\|Xv\|^2\ge0.$$

所以无论数据是什么、选择了什么固定基函数，RSS 关于系数参数 $\theta$ 都凸。每个临界点都是全局最小，解 $\nabla RSS=0$ 就是在解最小二乘。例子的 $\frac2NX^TX=\begin{pmatrix}2&5\\5&15\end{pmatrix}$，因此 $(0,2)$ 是全局最小点。不过凸性本身没有保证最小点唯一。

<details>
<summary>展开第 66 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 66 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-66.jpg)

</details>

## 第 67 页（课件 60/62）：最小二乘解何时唯一

设 $\widehat\theta$ 为临界点，满足 $X^T(Y-X\widehat\theta)=0$。移动任意向量 $v$ 后，

$$RSS(\widehat\theta+v)=RSS(\widehat\theta)-2v^TX^T(Y-X\widehat\theta)+\|Xv\|^2
=RSS(\widehat\theta)+\|Xv\|^2.$$

所以另一参数同样好，当且仅当 $Xv=0$，即预测根本没变。若 $X$ 列线性无关、满列秩，只有 $v=0$ 满足，解唯一；若列相关，有非零零空间方向，则 $\widehat\theta+cv$ 对所有 $c$ 同样好。图左边是椭圆等高线和一个绿色最小点；右边是平行等高线和一条绿色最小线。例子两列 $(1,1,1,1)^T,(1,2,3,4)^T$ 独立，因此 $(0,2)$ 唯一；若所有 $x_i$ 相同，任何经过 $(\bar x,\bar y)$ 的直线会拟合同样好。

<details>
<summary>展开第 67 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 67 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-67.jpg)

</details>

## 第 68 页（课件 61/62）：一维与多维概念对照

| 含义 | 单变量 | 多变量 |
|---|---|---|
| 敏感度 | 数 $f'(x)$ | 向量 $\nabla f(x)$ |
| 小步近似 | $f(x)+f'(x)\Delta x$ | $f(x)+\nabla f(x)^T\Delta x$ |
| 下坡 | $-f'(x)$ 方向 | $-\nabla f(x)$ 方向 |
| 临界点 | $f'(x)=0$ | $\nabla f(x)=0$ |
| 弯曲 | 数 $f''(x)$ | 矩阵 $\nabla^2f(x)$ |
| 凸性检验 | 处处 $f''\ge0$ | 处处 Hessian 半正定 |
| 无非全局局部最小 | 凸且零导数即全局最小 | 凸且零梯度即全局最小 |

<details>
<summary>展开第 68 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 68 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-68.jpg)

</details>

## 第 69 页（课件 62/62）：本讲要点与下一讲

本讲依次覆盖：函数、极限、连续函数；平均变化率、导数、线性近似；基本导数表与和、常数倍、乘积、链式法则；局部和全局最小、临界点、一阶与二阶导数检验；凸凹定义、二阶导数判据及凸函数临界点的全局性质；偏导、梯度、最陡上升、鞍点、Hessian 及多变量凸性。应用包括成功比例的最大似然估计、最小二乘估计，以及 RSS 的梯度、凸性与解的唯一性。下一讲进入 Optimisation。

<details>
<summary>展开第 69 页原始 slide，核对图表、标注和公式</summary>

![Lecture 11 第 69 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture11-69.jpg)

</details>
