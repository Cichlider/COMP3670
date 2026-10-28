# Lecture 12：优化、SVM 与神经网络，按幻灯片逐页复述

来源：[lecture12.pdf](/Users/cichlidfish/COMP3670/comp3670_lectures/lecture12.pdf)，共 60 个 PDF 页面，印刷编号从 0/53 到 53/53，另含章节页。以下按 PDF 实际顺序逐页讲述，保留公式、算法、数值表、图意、条件、参考来源和总结页。每节附原页核对图。“理解补充”用于澄清课件简化表述，不与原课件陈述混淆。本讲所列算法默认值是在复述课件，不是额外查询的当前软件配置建议。

## 第 1 页（课件 0/53）：本讲主题

COMP3670/COMP6670《Introduction to Machine Learning》，Lecture 12：Optimisation, SVMs and neural networks，即优化、支持向量机与神经网络。讲师 Diego Marcondes，ANU，2026 年第二学期。

<details>
<summary>展开第 1 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 1 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-01.jpg)

</details>

## 第 2 页（课件 0/53，章节页）：Optimisation problems

先从优化问题入手，把上一讲的梯度与凸性变成可计算参数的办法。

<details>
<summary>展开第 2 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 2 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-02.jpg)

</details>

## 第 3 页（课件 1/53）：回顾 Lecture 11

已有两个工具：梯度 $\nabla J(\theta)$ 指出当前位置的上坡方向及陡峭程度；凸性成立时，零梯度点是全局最小点。上一讲用手算解决硬币、过原点直线、带截距直线三个问题。但真实模型常有数百乃至数百万个方程，通常无法手解。因此本讲问：怎样真正到达零梯度处，是用公式还是迭代算法？这是线性代数与微积分相遇的地方。

<details>
<summary>展开第 3 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 3 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-03.jpg)

</details>

## 第 4 页（课件 2/53）：本讲路线

先讲优化问题、凸性、最小二乘公式和梯度下降；再讲随机梯度下降（SGD）与非线性 SVM；最后讲分类神经网络、动量与 Adam。图以三个框和箭头表示此顺序。

<details>
<summary>展开第 4 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 4 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-04.jpg)

</details>

## 第 5 页（课件 3/53）：优化问题的定义

给定目标函数 $J:\mathbb R^m\to\mathbb R$，无约束优化要求找到

$$\widehat\theta\in\arg\min_{\theta\in\mathbb R^m}J(\theta).$$

$\widehat\theta$ 是最小点，$J(\widehat\theta)$ 是最小值。学习中的目标可以是训练误差、训练误差加惩罚，或负对数似然，变量则是模型参数。无约束指所有实参数向量均允许；有约束问题还需满足条件，例如 SVM 的间隔要求。使用集合包含记号，也允许最优解不止一个。

<details>
<summary>展开第 5 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 5 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-05.jpg)

</details>

## 第 6 页（课件 4/53）：学习问题作为优化问题

| 模型 | 目标 | 凸？ | 有闭式公式？ |
|---|---|---|---|
| 最小二乘 | $\frac1N\|Y-X\theta\|^2$ | 是 | 是，满足相应秩条件 |
| Ridge | $\|Y-X\theta\|^2+\lambda\|\theta\|^2$ | 是 | 是 |
| 逻辑回归 | 平均交叉熵 $-LL(w)/N$ | 是 | 无一般闭式公式 |
| 软间隔 SVM | $\frac12\|w\|^2+C\sum_i\max\{0,1-y_i(\langle w,x_i\rangle+b)\}$ | 是 | 无一般闭式公式 |
| 神经网络 | 训练误差 | 一般非凸 | 无一般闭式公式 |

它们都是 Lecture 1 的经验风险最小化 $\widehat h=\arg\min_{h\in\mathcal H}E_{in}(h)$ 的实例。表里有四个凸问题，其中两个有公式、两个通常靠迭代；另有一个非凸问题。

<details>
<summary>展开第 6 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 6 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-06.jpg)

</details>

## 第 7 页（课件 5/53）：公式与迭代两种路线

公式路线尝试直接解 $m$ 个方程，方程线性时通常可能，例如最小二乘和 ridge。迭代路线先选起点、逐步改进，直到梯度近零，适用范围更广。公式精确，但不常存在，规模大时计算公式也可能昂贵；梯度下降等迭代只给近似解，却是大多数模型实际可用的办法。

<details>
<summary>展开第 7 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 7 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-07.jpg)

</details>

## 第 8 页（课件 6/53）：怎样识别凸问题

通常不必每次计算 Hessian 特征值，而可从凸的组成部分判断。保凸规则有：凸函数的和与正倍数；凸函数与线性或仿射映射复合；若干凸函数的最大值。平方范数与 $Y-X\theta$ 复合给出最小二乘；加凸平方惩罚给出 ridge；逻辑回归是关于线性分数的凸负对数概率项之和；hinge 是两条直线的最大值，再与线性间隔复合并加 $\frac12\|w\|^2$，得到凸 SVM 目标。

<details>
<summary>展开第 8 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 8 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-08.jpg)

</details>

## 第 9 页（课件 7/53）：凸与严格凸

凸目标的每个临界点都是全局最小，每个局部最小也全局最小，因而没有非全局的局部谷底陷阱。严格凸且最优点存在时，最小点唯一，例如处处正定 Hessian 的情况；一般凸目标可能有平坦谷底和多个等价最小点。图分别画单一最小点与一段平底。

课件用“起点只影响耗时、不影响终点”强调凸问题的优势。理解补充：多个最小点时具体终点仍可随起点改变，只是达到的最优目标值相同；算法还需合适步长和收敛条件，凸性本身不让任意迭代自动成功。

<details>
<summary>展开第 9 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 9 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-09.jpg)

</details>

## 第 10 页（课件 8/53）：最小二乘的矩阵表示

Lecture 4 的基函数模型为 $Y=\theta_0\phi_0(X)+\cdots+\theta_k\phi_k(X)+\varepsilon$。把响应堆叠为 $Y=(Y_1,\ldots,Y_N)^T$，设计矩阵为

$$X=\begin{pmatrix}\phi_0(X_1)&\cdots&\phi_k(X_1)\\\vdots&&\vdots\\\phi_0(X_N)&\cdots&\phi_k(X_N)\end{pmatrix},\quad RSS(\theta)=\|Y-X\theta\|^2.$$

每行一个观测，每列一个参数，记参数数目 $m=k+1$。$X\theta$ 的第 $i$ 项为预测，$Y-X\theta$ 为残差。例子 $\phi_0=1,\phi_1(x)=x$，行是 $(1,1),(1,2),(1,3),(1,4)$，$Y=(2,5,4,9)^T$。参考：Braga-Neto（2024）《Fundamentals of Pattern Recognition and Machine Learning》§11.3.1，式 (11.20)–(11.25)。

<details>
<summary>展开第 10 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 10 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-10.jpg)

</details>

## 第 11 页（课件 9/53）：正规方程

最小二乘凸，因此解零梯度就能找最优点：

$$-2X^T(Y-X\theta)=0\ \Longrightarrow\ 2X^TY=2X^TX\theta\ \Longrightarrow\ X^TX\theta=X^TY.$$

这是 $m$ 个未知数的 $m$ 个线性方程。若 $X$ 满列秩，$X^TX$ 可逆且解唯一。几何上，$X^T(Y-X\widehat\theta)=0$ 表示残差垂直于每个设计矩阵列，所以 $X\widehat\theta$ 是 $Y$ 在 $\operatorname{Col}(X)$ 的正交投影。例子方程 $\begin{pmatrix}4&10\\10&30\end{pmatrix}\theta=(20,60)^T$ 的解为 $(0,2)^T$。参考：同书 §11.3.1，式 (11.26)、练习 11.3。

<details>
<summary>展开第 11 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 11 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-11.jpg)

</details>

## 第 12 页（课件 10/53）：最小二乘闭式解

模型关于系数线性且 $X$ 满列秩时，

$$\widehat\theta=(X^TX)^{-1}X^TY,\qquad \widehat h(x)=\Phi(x)^T\widehat\theta.$$

对一元带截距直线，还原为 $\widehat\theta_1=\sum_i(x_i-\bar x)(y_i-\bar y)/\sum_i(x_i-\bar x)^2$，$\widehat\theta_0=\bar y-\widehat\theta_1\bar x$。课件以“No algorithm is needed”强调不必用梯度下降寻找解析解；理解补充：在计算机上仍需数值求解线性系统，公式不是零计算成本。参考：同书 §11.3.1，式 (11.23)–(11.29)。

<details>
<summary>展开第 12 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 12 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-12.jpg)

</details>

## 第 13 页（课件 11/53）：惩罚最小二乘与 ridge

高阶多项式可能过拟合；可以用验证选择阶数，也可以保留阶数而限制系数过大。Ridge 定义为

$$\widehat\theta^{RIDGE}=\arg\min_\theta\{\|Y-X\theta\|^2+\lambda\|\theta\|^2\},\quad\lambda>0,$$
$$\widehat\theta^{RIDGE}=(X^TX+\lambda I)^{-1}X^TY.$$

前项拟合数据，后项表达偏好简单模型。与软间隔 SVM 的“hinge 加平方范数”对应。$\lambda=0$ 回到普通最小二乘，$\lambda$ 大使系数向零收缩。参考：同书 §11.3.3，式 (11.44)–(11.45)。本页采用未除 $N$ 的 RSS 标度。

<details>
<summary>展开第 13 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 13 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-13.jpg)

</details>

## 第 14 页（课件 12/53）：正则化为什么也改善计算

$$\nabla J=-2X^T(Y-X\theta)+2\lambda\theta.$$

令零得 $(X^TX+\lambda I)\theta=X^TY$。Hessian 为 $2(X^TX+\lambda I)$。加 $\lambda I$ 将 $X^TX$ 每个非负特征值增加 $\lambda$，从而全为正。因此 $\lambda>0$ 时严格凸，解存在且唯一，$X^TX+\lambda I$ 总可逆，即使参数比观测多、或者有重复特征使 $X$ 不满列秩。正则化让问题成为良定问题。参考：同书 §11.3.3。

<details>
<summary>展开第 14 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 14 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-14.jpg)

</details>

## 第 15 页（课件 13/53）：收缩例子

两图分别拟合 6 阶与 12 阶多项式；每图比较 $\lambda=0,10,100$，并画出观测散点。惩罚越强，曲线整体越平滑、越平坦。可将其理解为在给定基函数中，给系数一个预算，主动接受更多偏差以换取较低方差。$\lambda$ 能连续调节复杂度，不必只在整数阶数之间跳变。来源：Braga-Neto（2024）图 11.4，例 11.6。

<details>
<summary>展开第 15 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 15 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-15.jpg)

</details>

## 第 16 页（课件 14/53）：交叉熵的梯度

逻辑回归用 $\sigma(w^TX)$ 估计类别 1 概率，特征前加常数 1 以吸收偏置。单点损失为

$$\ell_i(w)=-Y_i\log\sigma(w^TX_i)-(1-Y_i)\log(1-\sigma(w^TX_i)).$$

结合链式法则和 $\sigma'=\sigma(1-\sigma)$，

$$\nabla\ell_i(w)=(\sigma(w^TX_i)-Y_i)X_i,\qquad
\nabla J(w)=\frac1N\sum_i(\sigma(w^TX_i)-Y_i)X_i.$$

仍是“误差乘输入”，这里误差是预测概率减标签。目标凸，所以有限的零梯度点是全局最小。参考：同书 §4.3，式 (4.31)、(4.32)。

<details>
<summary>展开第 16 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 16 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-16.jpg)

</details>

## 第 17 页（课件 15/53）：逻辑回归没有一般解析解

零梯度要求 $\sum_i(\sigma(w^TX_i)-Y_i)X_i=0$。未知数 $w$ 出现在 sigmoid 内，方程非线性，不能像正规方程那样一般地代数分离求解。因此改用迭代，例如梯度下降。

<details>
<summary>展开第 17 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 17 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-17.jpg)

</details>

## 第 18 页（课件 15/53，章节页）：Gradient descent

开始正式介绍梯度下降训练算法。

<details>
<summary>展开第 18 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 18 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-18.jpg)

</details>

## 第 19 页（课件 16/53）：梯度下降算法

选择起点 $\theta(0)$，对 $t=0,1,2,\ldots$ 重复计算当前梯度并更新

$$\theta(t+1)\leftarrow\theta(t)-\alpha\nabla J(\theta(t)),$$

直到满足停止规则。$\alpha>0$ 是学习率或步长，控制沿下坡方向走多远，是超参数，不是模型从数据中拟合出的系数。

<details>
<summary>展开第 19 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 19 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-19.jpg)

</details>

## 第 20 页（课件 17/53）：手算梯度下降

取贯穿例子 $J(\theta)=7.5\theta^2-30\theta+31.5$，$J'=15\theta-30$，从 $\theta(0)=0$、学习率 $\alpha=0.04$ 开始：

| $t$ | $\theta(t)$ | $J'(\theta(t))$ | $J(\theta(t))$，课件舍入 |
|---:|---:|---:|---:|
| 0 | 0 | -30 | 31.5 |
| 1 | 1.2 | -12 | 6.3 |
| 2 | 1.68 | -4.8 | 2.27 |
| 3 | 1.872 | -1.92 | 1.62 |
| 4 | 1.949 | -0.77 | 1.52 |

图中迭代沿抛物线向底部移动。梯度变平，步子从 1.2、0.48 缩小到约 0.19、0.08。每一步将到最优点 2 的误差乘 $1-15\alpha=0.4$；不会有限步精确到达，但 10 步后距离约 0.0002。

<details>
<summary>展开第 20 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 20 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-20.jpg)

</details>

## 第 21 页（课件 18/53）：学习率的作用

三幅图比较 $\alpha=0.005$（太小，8 步后进展仍慢）、0.04（合适）、0.14（过大、反复跨过谷底且越走越远）。因为有符号误差的更新因子是 $1-15\alpha$，当 $\alpha>2/15\approx0.133$，因子小于 -1，导致交替发散。曲率 $J''=15$；曲率越大，允许的学习率通常越小。学习率调的是算法，所寻找的目标最小点没有改变。

<details>
<summary>展开第 21 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 21 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-21.jpg)

</details>

## 第 22 页（课件 19/53）：凸目标上梯度下降的保证

设 $J$ 凸、足够光滑，所有位置、所有方向的曲率最多为 $K$，也就是 Hessian 最大特征值不超过 $K$。若 $0<\alpha\le1/K$，并有最优点 $\widehat\theta$，则任意起点满足

$$J(\theta(t))-J(\widehat\theta)\le\frac{\|\theta(0)-\widehat\theta\|^2}{2\alpha t}.$$

课件不证明。目标差距上界按 $1/t$ 缩小，迭代数增加十倍，上界缩小十倍。凸性和学习率条件都关键；不能把此保证无条件用于神经网络或过大步长。

<details>
<summary>展开第 22 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 22 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-22.jpg)

</details>

## 第 23 页（课件 20/53）：停止规则

通常组合四种：梯度足够小；目标一段时间不再明显下降；验证误差停止改善；达到最大迭代预算。画目标值对迭代次数曲线，能诊断步长：太大时波动或上升，太小时下降缓慢，合适时较快下降后趋于平坦。训练目标停滞与验证表现停滞是不同标准。

<details>
<summary>展开第 23 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 23 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-23.jpg)

</details>

## 第 24 页（课件 21/53）：三个问题的具体更新

平均平方误差：$\theta\leftarrow\theta+\frac{2\alpha}{N}X^T(Y-X\theta)$。

未除 $N$ 的 ridge：$\theta\leftarrow(1-2\alpha\lambda)\theta+2\alpha X^T(Y-X\theta)$。

逻辑回归：$w\leftarrow w-\frac\alpha N\sum_i(\sigma(w^TX_i)-Y_i)X_i$。

三者都从当前参数加上基于“误差乘输入”的修正。Ridge 还先乘 $1-2\alpha\lambda$ 来收缩参数。不同目标的归一化标度不同，所以不能遗漏 $N$ 或随意替换系数。

<details>
<summary>展开第 24 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 24 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-24.jpg)

</details>

## 第 25 页（课件 22/53）：每步计算的代价

上述梯度都要遍历所有观测：$\nabla J(\theta)=\frac1N\sum_i\nabla\ell_i(\theta)$。每一步成本约与 $N\times m$ 成正比，分别是观测数和参数数。例子只有 4 个点，但现代训练数据及参数可能达到百万、十亿量级，并且还要做数百、数千步。因此“每次精确计算全数据平均梯度”成了瓶颈。

<details>
<summary>展开第 25 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 25 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-25.jpg)

</details>

## 第 26 页（课件 22/53，章节页）：Stochastic gradient descent

转向用随机样本的梯度近似全梯度。

<details>
<summary>展开第 26 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 26 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-26.jpg)

</details>

## 第 27 页（课件 23/53）：统计学思路——无偏梯度估计

从 $\{1,\ldots,N\}$ 均匀随机抽 $i$，取 $g=\nabla\ell_i(\theta)$，则

$$\mathbb E[g]=\sum_{i=1}^N\frac1N\nabla\ell_i(\theta)=\nabla J(\theta).$$

它虽有噪声，平均却正确。抽大小为 $b$ 的随机 mini-batch $B$，使用 $g=\frac1b\sum_{i\in B}\nabla\ell_i(\theta)$，仍无偏，批越大通常波动越小。$b=N$ 回到全梯度，$b=1$ 最便宜也最嘈杂。一次精确梯度的计算预算，大致能换取 $N/b$ 次小批梯度及参数更新。

<details>
<summary>展开第 27 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 27 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-27.jpg)

</details>

## 第 28 页（课件 24/53）：SGD 算法、batch 和 epoch

先选起点 $\theta(0)$ 和批大小 $b$。每次随机取 $B_t$，计算

$$g(t)=\frac1b\sum_{i\in B_t}\nabla\ell_i(\theta(t)),\qquad\theta(t+1)\leftarrow\theta(t)-\alpha_tg(t),$$

重复直到停止。课件列常见批大小 32–512。一个 epoch 指遍历一次数据，约 $N/b$ 次更新；实践中往往先打乱数据，再划分连续小批。学习率带下标 $t$，表示可在训练中改变。

<details>
<summary>展开第 28 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 28 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-28.jpg)

</details>

## 第 29 页（课件 25/53）：GD 与 SGD 的路径

图用有 100 个观测、两个参数的最小二乘等高线比较两条路径。全梯度下降 15 步，每步用 100 个样本梯度，共 1,500 次；$b=1$ 的 SGD 走 150 步，共 150 次样本梯度，只需十分之一计算。GD 路径较平稳，SGD 四处摆动，却能以少量代价到达最小点附近；随后它还会继续徘徊。

<details>
<summary>展开第 29 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 29 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-29.jpg)

</details>

## 第 30 页（课件 26/53）：随机噪声的代价

贯穿例子中各观测若单独拟合，偏好斜率 $y_i/x_i$ 分别为 $2,2.5,1.33,2.25$。在整体最优斜率 2，全梯度为零，但单点梯度一般不为零，只是平均抵消。每次 SGD 被某个观测拉向它自己的最优值，所以固定学习率下在最优附近震荡。图比较 0.02 与 0.004：大步到得快、波动大；小步到得慢、波动小。这是本例的行为，不意味着所有特殊数据都必然持续震荡。

<details>
<summary>展开第 30 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 30 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-30.jpg)

</details>

## 第 31 页（课件 27/53）：学习率调度

办法是前期大步快速接近，后期小步逐渐稳定。图用相同随机观测和相同顺序，对比固定 $\alpha=0.02$ 与递减 $\alpha_t=0.02/(1+t/6)$。学习率随时间变化的规则称 schedule。常见形式包括：分段常数，在指定 epoch 将学习率除以 10；指数衰减 $\alpha_t=\alpha_0\,0.1^{t/s}$，$s>0$。

<details>
<summary>展开第 31 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 31 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-31.jpg)

</details>

## 第 32 页（课件 28/53）：为什么 SGD 常用

固定 batch 大小时，每步代价不随总样本数 $N$ 增长；全梯度一步的时间可做约 $N/b$ 次随机更新，远离最优点时即使带噪方向也能快速进步。另一方面，我们最终关心泛化：$E_{in}$ 本来就是 $E_{out}$ 的随机估计，超过泛化差距所需精度地求训练最小值通常没有意义。噪声也可能帮助非凸问题离开较差局部最小或鞍点。课件将 SGD 及其后继方法称为机器学习训练的默认选择，并说明实践中口语“gradient descent”常泛指随机版本；这不是全局最优的保证。

<details>
<summary>展开第 32 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 32 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-32.jpg)

</details>

## 第 33 页（课件 28/53，章节页）：Nonlinear SVMs

开始讨论怎样用线性算法产生非线性边界。

<details>
<summary>展开第 33 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 33 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-33.jpg)

</details>

## 第 34 页（课件 29/53）：SVM 回顾

标签 $y_i\in\{-1,+1\}$，分数 $f(x)=\langle w,x\rangle+b$，分数非负预测 +1，否则 -1。功能间隔 $m_i=y_if(x_i)$ 为正表示严格正确分类；边界上的平局要按预测约定单独理解。点到超平面距离为 $|f(x_i)|/\|w\|$。可分数据有无穷多个分离超平面，感知器给出先找到的一个，SVM 寻找离数据最远的边界。图中实心近邻点是支持向量，决定间隔；在可分、最大间隔的图示情形，非支持点在间隔之外移动而不改变约束活跃性时，边界不变。来源：Braga-Neto（2024）图 6.1。

<details>
<summary>展开第 34 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 34 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-34.jpg)

</details>

## 第 35 页（课件 30/53）：直线不总够用

感知器、逻辑回归、线性 SVM 都在超平面中选边界。图中一类点围在中心，另一类在外圈，没有直线能分开。但规则“当 $x_1^2+x_2^2<r^2$ 时判 +1”可以正确分类。它对原始变量是圆形边界，对平方后的量却是线性规则。虚线展示一个直线尝试，两侧仍混有两类点。

<details>
<summary>展开第 35 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 35 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-35.jpg)

</details>

## 第 36 页（课件 31/53）：变换变量后的非线性 SVM

预先选变换 $\phi$，把每个点改成 $\phi(x_i)$，然后使用普通线性 SVM：

$$J(w,b)=\frac12\|w\|^2+C\sum_{i=1}^N\max\{0,1-y_i(\langle w,\phi(x_i)\rangle+b)\}.$$

算法和目标结构不变，Week 8b 的更新直接用 $\phi(x_i)$ 替换 $x_i$。由于变换在训练前固定，关于 $(w,b)$ 仍凸。在新变量空间的超平面，解释回原空间就是曲线边界。参考：同书 §6.1.3。本页讲显式变量变换，没有另行展开核技巧。

<details>
<summary>展开第 36 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 36 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-36.jpg)

</details>

## 第 37 页（课件 32/53）：一维不可线性分例子

设 $d=1$，真实规则为 $1<x<3$ 时 $f^\star(x)=+1$，其他位置为 -1。一维线性分类器 $\operatorname{sign}(wx+b)$ 只有一个阈值，只能把某一侧判成 +1，无法让中间区间为正、两侧为负。图沿横轴画外侧橙点、内侧蓝点，说明数据在原变量下不可线性分。

<details>
<summary>展开第 37 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 37 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-37.jpg)

</details>

## 第 38 页（课件 33/53）：加入平方变量后可分

将 $x$ 变成 $\phi(x)=(x,x^2)=(z_1,z_2)$，点落在抛物线上。新平面中直线 $z_2=4z_1-3$ 将两类分开：内侧蓝点在直线下方、外侧橙点在上方。换回原变量，

$$x^2<4x-3\iff x^2-4x+3<0\iff(x-1)(x-3)<0\iff1<x<3.$$

二维的一条直线在原来一维表达成两个阈值；对 $(x,x^2)$ 线性，就是对 $x$ 二次。

<details>
<summary>展开第 38 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 38 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-38.jpg)

</details>

## 第 39 页（课件 34/53）：回到二维圆形例子

采用 $\phi(x)=(x_1,x_1^2+x_2^2)$，将第二坐标记为 $z$。左图在 $(x_1,z)$ 平面画水平分界线 $z=r^2$，把中心类和外圈类分开；右图把它解释回原坐标，就是半径为 $r$ 的圆。算法、目标没有变，只是特征向量改变，使直线边界变成圆形边界。

<details>
<summary>展开第 39 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 39 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-39.jpg)

</details>

## 第 40 页（课件 34/53，章节页）：Neural networks

接下来从手工固定变换转向由数据学习内部表示。

<details>
<summary>展开第 40 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 40 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-40.jpg)

</details>

## 第 41 页（课件 35/53）：逻辑回归就是单个神经元

神经元先算输入加权和加偏置 $z=\langle w,x\rangle+b$，再应用固定非线性激活函数。逻辑回归就是使用 sigmoid 激活 $\sigma(z)=1/(1+e^{-z})$ 的单神经元，输出估计 $\eta(x)=P(Y=1\mid X=x)$，边界仍为超平面。SVM 为曲线边界预先指定变量变换；神经网络在输入、输出之间插入神经元层，并从数据学习新的变量。参考：同书 §6.2.1、§6.2.2。

<details>
<summary>展开第 41 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 41 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-41.jpg)

</details>

## 第 42 页（课件 36/53）：全连接深度神经网络 FCDNN

图中输入有 $d=3$ 个坐标，两个隐藏层各有 4 个神经元，最后输出一个分数 $f_w(x)$，再经过 logistic 变成概率 $\widehat\eta(x)$。每个蓝色神经元连接前一层所有输出，进行加权和、加偏置、应用激活，因此叫全连接。隐藏层数 $k=2$、宽度 $d_1=d_2=4$；按课件把输入、输出也算层的约定，深度为 $k+2=4$。信息仅从左向右流，是前馈网络。最后一步相当于在末层隐藏表示上做逻辑回归。

<details>
<summary>展开第 42 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 42 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-42.jpg)

</details>

## 第 43 页（课件 37/53）：激活函数

图在同一坐标上比较五种激活：$\arctan(z)$；$\operatorname{ReLU}(z)=\max\{0,z\}$；sigmoid $1/(1+e^{-z})$；$\tanh(z)$；阈值函数 $\mathbf1\{z\ge0\}$。ReLU 负半轴为零、正半轴线性；sigmoid 输出介于 0 与 1；tanh 和 arctan 是两侧趋平的 S 形；阈值在 0 跳变。不同曲线、图例和坐标范围见原页。本页用于认识可选非线性，未逐一推导其梯度。

<details>
<summary>展开第 43 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 43 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-43.jpg)

</details>

## 第 44 页（课件 38/53）：网络的矩阵记号

第 $i$ 层权重组成 $A_i$，元素 $(A_i)_{\ell,j}=w^{(i)}_{\ell,j}$，激活按坐标逐项应用。前图网络为

$$f_w(x)=A_3\sigma(A_2\sigma(A_1x)).$$

| 矩阵 | 尺寸 | 映射 | 连接位置 |
|---|---|---|---|
| $A_1$ | $4\times3$ | $\mathbb R^3\to\mathbb R^4$ | 输入到隐藏层 1 |
| $A_2$ | $4\times4$ | $\mathbb R^4\to\mathbb R^4$ | 隐藏层 1 到 2 |
| $A_3$ | $1\times4$ | $\mathbb R^4\to\mathbb R$ | 隐藏层 2 到输出 |

一般形式为 $A_{k+1}\sigma(A_k\cdots\sigma(A_1x))$，隐藏层矩阵尺寸 $d_i\times d_{i-1}$，最后一层为 $1\times d_k$，$K$ 类时为 $K\times d_k$。参数 $w$ 包含所有矩阵元素。偏置可通过给输入补常数 1、给对应矩阵增加一列来表示。

<details>
<summary>展开第 44 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 44 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-44.jpg)

</details>

## 第 45 页（课件 39/53）：分类输出层

回归直接以 $f_w(x)$ 为预测；分类需进一步转换成概率。二分类：

$$\widehat\eta_w(x)=\frac1{1+e^{-f_w(x)}},\quad\widehat h(x)=\mathbf1\{\widehat\eta_w(x)>1/2\}=\mathbf1\{f_w(x)>0\}.$$

多分类最后一层输出 $K$ 个分数，用 softmax：

$$\widehat p_{w,k}(x)=\frac{e^{f_{w,k}(x)}}{\sum_{j=1}^Ke^{f_{w,j}(x)}},\quad\widehat h(x)=\arg\max_k\widehat p_{w,k}(x).$$

所有概率正且总和为 1。无隐藏层的二分类网络恰是逻辑回归。参考：同书 §6.2.2。

<details>
<summary>展开第 45 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 45 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-45.jpg)

</details>

## 第 46 页（课件 40/53）：神经网络的通用逼近定理

Cybenko（1989）定理：对定义在超立方体 $[0,1]^d$ 上的连续函数 $f$，任意 $\varepsilon>0$，存在一层隐藏层、sigmoid 激活的网络

$$\zeta(x)=\sum_{i=0}^{d_1}w_i^{(2)}\,\sigma\!\left(\sum_{j=0}^dw_{i,j}^{(1)}x_j\right),\qquad x_0=1,$$

使所有 $x\in[0,1]^d$ 都满足 $|f(x)-\zeta(x)|<\varepsilon$。这是表示能力的存在性结论。理解补充：不承诺给定宽度够用，不承诺有限训练样本或某优化算法必能找到这些参数。参考：同书 §6.2.7。

<details>
<summary>展开第 46 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 46 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-46.jpg)

</details>

## 第 47 页（课件 41/53）：训练分类神经网络

训练数据 $(X_i,Y_i)$，二分类标签 $Y_i\in\{0,1\}$。与逻辑回归一样使用经验交叉熵：

$$J(w)=-\frac1N\sum_{i=1}^N[Y_i\log\widehat\eta_w(X_i)+(1-Y_i)\log(1-\widehat\eta_w(X_i))].$$

$K$ 类则 $J(w)=-\frac1N\sum_i\log\widehat p_{w,Y_i}(X_i)$，即真实类别被分配概率的负对数平均。ERM 在 $w\in\mathbb R^p$ 上最小化 $J$，$p$ 是参数数目。多层参数共同作用使问题一般非凸，可能有多个局部最小。参考：同书 §6.2.3。

<details>
<summary>展开第 47 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 47 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-47.jpg)

</details>

## 第 48 页（课件 42/53）：神经网络与过拟合

即使宽度深度并不夸张，全连接网络也代表很复杂的函数集合，可能完美分开小样本，却未正确掌握总体 $X,Y$ 的关系。可用复杂度正则化，例如最小化 $J(w)+\lambda\|w\|^2$，以抑制过拟合。课件也指出有些任务本来希望完全分离，例如标签是输入的确定性函数。正则化仍需结合任务目标与验证表现判断。

<details>
<summary>展开第 48 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 48 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-48.jpg)

</details>

## 第 49 页（课件 43/53）：高斯分类的网络例子

两类样本服从高斯分布，最优边界是一条穿过图中心、方向角约 -45° 的直线。网络一层隐藏层、一个输出神经元、sigmoid 激活，以交叉熵做 1,000 次梯度下降。四图比较 15、35、55、75 个隐藏神经元：15 个时边界明显弯曲、欠拟合；35 个时接近最优直线；继续增至 55、75 没改善，反而略变差，出现少量过拟合。来源：Braga-Neto（2024）图 6.8，例 6.4。

<details>
<summary>展开第 49 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 49 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-49.jpg)

</details>

## 第 50 页（课件 44/53）：XOR 例子

XOR 的两类点位于相对角，单条直线不能分离，因此单感知器不够。一层隐藏层、两个阶跃神经元，再接一个阶跃输出神经元，配合手设权重即可分类。两条隐藏边界为 $x_1+x_2+0.5=0$ 与 $x_1+x_2-0.5=0$，在图里形成中间带状区域。

原图还给出具体连接：上方隐藏单元输入权重 $(1,1)$、偏置 0.5，下方为 $(-1,-1)$、偏置 0.5；输出对两个隐藏值的权重都是 -1，偏置 1.5。若以阶跃函数 $H$ 表示，就是 $h_1=H(x_1+x_2+0.5)$、$h_2=H(-x_1-x_2+0.5)$、输出 $H(1.5-h_1-h_2)$。课件的四个角点不在阈值边界上，因此不受边界取等号约定影响。来源：同书图 6.7，例 6.3。

<details>
<summary>展开第 50 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 50 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-50.jpg)

</details>

## 第 51 页（课件 45/53）：网络的梯度下降与反向传播

随机初始化 $w(0)\in\mathbb R^p$，一般更新形式为 $w(t+1)=w(t)+\alpha v(t)$，其中 $\alpha>0$ 是学习率，$v(t)$ 是方向。标准梯度下降选择贪心的最陡局部下降方向 $v(t)=-\nabla J(w(t))$。网络梯度通过从输出往回、逐层应用链式法则计算，称反向传播。参考：同书 §6.2.4、§6.2.5。

<details>
<summary>展开第 51 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 51 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-51.jpg)

</details>

## 第 52 页（课件 46/53）：初始化

神经网络通常用 SGD 的变体训练，初始值对最后找到的局部解很重要。启发式方法从零均值均匀分布或高斯分布采样权重，并根据连接前后层宽度 $d_i,d_{i+1}$ 调整方差：LeCun 为 $1/d_i$；Xavier 或 Glorot 为 $2/(d_i+d_{i+1})$；He 为 $2/d_i$。这里列的是方差而非标准差，不能混用。参考：同书 §6.2.5。

<details>
<summary>展开第 52 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 52 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-52.jpg)

</details>

## 第 53 页（课件 46/53，章节页）：Momentum and Adam

最后介绍带历史状态、按坐标调整更新的优化算法。

<details>
<summary>展开第 53 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 53 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-53.jpg)

</details>

## 第 54 页（课件 47/53）：Heavy ball 动量法

普通梯度下降在高曲率方向可能振荡，平坦方向又可能走得太慢。Heavy ball 用动量类比“重球不易在壁间弹跳，在平地也滚得更快”：

$$m(t)=\beta m(t-1)-\alpha\nabla J(w(t)),\qquad w(t+1)=w(t)+m(t).$$

$m$ 是动量向量，初始设为零，$0<\beta<1$ 控制历史贡献的指数衰减；课件常用值为 0.9。为避免初始编号歧义，可把更新理解为从首个梯度开始，使用前一时刻零动量。参考：同书 §6.2.5，式 (6.71)。

<details>
<summary>展开第 54 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 54 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-54.jpg)

</details>

## 第 55 页（课件 48/53）：Nesterov 加速梯度

在 heavy ball 基础上，先按历史动量看向一个“未来”位置，再在那里计算梯度：

$$m(t)=\beta m(t-1)-\alpha\nabla J(w(t)+\beta m(t-1)),\qquad w(t+1)=w(t)+m(t).$$

直觉是提前到更靠近目标的位置评估修正，通常可加快收敛。$0<\beta<1$，课件同样给出常用值 0.9。它与上一页的关键区别在梯度求值位置。参考：同书 §6.2.5。

<details>
<summary>展开第 55 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 55 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-55.jpg)

</details>

## 第 56 页（课件 49/53）：Adagrad

Adagrad（adaptive gradient descent）为每个坐标调整学习率：历史梯度大的方向步长小，历史梯度小的方向步长相对大。令 $g(t)=\nabla J(w(t))$，课件公式为

$$s(t)=s(t-1)+g(t)^2,\qquad w(t+1)=w(t)-\frac\alpha{\sqrt{s(t)+\epsilon}}\,g(t).$$

初始累计量为零，$\epsilon>0$ 防止除零，平方、除法、平方根等向量运算按坐标进行。注意本页原式的 $\epsilon$ 放在根号内；后面 Adam 的写法另有区别。参考：同书 §6.2.5。

<details>
<summary>展开第 56 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 56 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-56.jpg)

</details>

## 第 57 页（课件 50/53）：RMSProp

Adagrad 的一种变化是对历史平方梯度作指数衰减，让旧梯度逐渐被遗忘：

$$s(t)=\beta s(t-1)+(1-\beta)g(t)^2,\qquad w(t+1)=w(t)-\frac\alpha{\sqrt{s(t)+\epsilon}}\,g(t).$$

$0<\beta<1$，课件通常取 0.9。相较 Adagrad 的永久累计，此处 $s$ 是近期平方梯度的指数加权平均。参考：同书 §6.2.5。

<details>
<summary>展开第 57 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 57 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-57.jpg)

</details>

## 第 58 页（课件 51/53）：Adam

Adam（adaptive moment estimation）结合动量类与 Adagrad 类方法。严格按本课件的符号约定，动量存的是负梯度平均：

$$m(t)=\beta_1m(t-1)-(1-\beta_1)g(t),$$
$$s(t)=\beta_2s(t-1)+(1-\beta_2)g(t)^2,$$
$$\widehat m(t)=\frac{m(t)}{1-\beta_1^t},\qquad\widehat s(t)=\frac{s(t)}{1-\beta_2^t},$$
$$w(t+1)=w(t)+\frac\alpha{\sqrt{\widehat s(t)+\epsilon_{root}}+\epsilon}\,\widehat m(t).$$

各坐标分别运算，$0<\beta_1,\beta_2<1$，两个小量用于数值稳定。课件常用值 $\beta_1=0.9,\beta_2=0.999,\epsilon=10^{-8},\epsilon_{root}=0$。负梯度已经进入 $m$，所以最后是加号；如果改用正梯度动量，最后应改成减号，不能混搭。前两式积累方向和平方尺度，中间两式修正从零初始化产生的偏差。这里的偏差修正从 $t=1$ 开始使用，不能在 $t=0$ 直接除以零。课件将 Adam 称为网络训练的默认方法。参考：同书 §6.2.5，式 (6.75)。

<details>
<summary>展开第 58 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 58 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-58.jpg)

</details>

## 第 59 页（课件 52/53）：本讲要点

依序总结：训练是最小化可能带惩罚的经验误差；凸问题每个局部最小都是全局最小；正规方程和满列秩下的最小二乘解；梯度下降的学习率、收敛与停止；SGD 的小批量、epoch、学习率调度；非线性 SVM 的支持向量、变量变换与曲线边界；全连接神经网络的激活、深宽、分类输出与 softmax、交叉熵、通用逼近、过拟合、初始化；heavy ball、Nesterov、Adagrad、RMSProp、Adam。

<details>
<summary>展开第 59 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 59 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-59.jpg)

</details>

## 第 60 页（课件 53/53）：整个机器学习课程的结构

收尾图把机器学习画成建筑。屋顶是从有限样本归纳一般规律的科学；横梁是用 ERM 拟合统计模型：$\widehat h=\arg\min_{h\in\mathcal H}E_{in}(h)$。基础设定是样本 $D_N$ 从未知分布 $P$ 独立同分布采样，选假设集 $\mathcal H$ 与损失 $\ell$，目标为较小的 $E_{out}(\widehat h)$。

三根柱子分别是：

1. 学习理论，问能否泛化：泛化差距、Hoeffding 与 VC 界、PAC 学习、偏差与方差、过拟合、验证与测试集。
2. 模型，问拟合什么：感知器、逻辑回归、直方图与 kNN、树与随机森林、最小二乘与 ridge、K-means、PCA、SVM、神经网络。
3. 算法，问怎样计算：PLA、正规方程、K-means 迭代、PCA 特征向量、梯度下降、SGD、动量、Adam。

三者建立在概率、线性代数、微积分这些数学基础之上。右侧主要信息是：机器学习要从有限数据归纳规律；统计模型由经验风险最小化拟合，统计学习理论在相应假设下研究并给出泛化保证；线性代数与微积分构成的算法是训练模型的工具，模型、训练方法和泛化理论需要区分并联系起来理解。

<details>
<summary>展开第 60 页原始 slide，核对图表、标注和公式</summary>

![Lecture 12 第 60 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture12-60.jpg)

</details>
