# Lecture 09：特征分解与主成分分析，按幻灯片逐页复述

来源：[lecture09.pdf](/Users/cichlidfish/COMP3670/comp3670_lectures/lecture09.pdf)，共 79 个 PDF 页面。下文严格按 PDF 页面顺序，章节页也单独保留。公式中的数据点默认是列向量，数据矩阵则把数据点转置后放在各行。每节附原页核对图；图中的点、颜色、坐标、球员姓名等细节也属于本节内容。原页没有展开的证明不冒充课件原文，必要的解释标为“理解补充”。

## 第 1 页：课程与本周主题

这是 COMP3670/6670《Introduction to Machine Learning》第 9 周，主题是 Eigen-decompositions 与 Principal Component Analysis，即特征分解和主成分分析（PCA）。讲师为 ANU School of Computing 的 Senior Lecturer Yun Kuen Cheung（Marco）。本讲先建立矩阵的特征方向，再用这些方向压缩数据。

<details>
<summary>展开第 1 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 1 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-01.jpg)

</details>

## 第 2 页：学习目标

本讲有五个目标：理解为什么要减少数据集的维度；用特征向量解释协方差矩阵记录的变化；找到保留最多方差的方向；用 PCA 编码并重构数据；选择保留多少主成分，并正确解释二维或三维 PCA 图。

<details>
<summary>展开第 2 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 2 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-02.jpg)

</details>

## 第 3 页：章节页——为什么减少特征数

接下来先讨论降维的动机，再进入线性代数工具。

<details>
<summary>展开第 3 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 3 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-03.jpg)

</details>

## 第 4 页：数据维度、相关特征和计算代价

设 $X\in\mathbb R^{n\times d}$，它存储 $n$ 个数据点，每个点有 $d$ 个特征。$n$ 是样本数，$d$ 是原始空间维度（ambient dimension）。MNIST 图像有 784 个像素特征，但相邻像素往往一起变化；足球运动员的铲球、拦截等防守指标也可能正相关。特征多可能有帮助，却会增加计算量，并让有限样本更难覆盖整个空间。这说明“特征数”不一定等于“独立信息量”。

<details>
<summary>展开第 4 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 4 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-04.jpg)

</details>

## 第 5 页：例 1——二元特征空间的组合爆炸

假设 $d$ 个特征各取 0 或 1，并且允许所有组合，可能的特征向量有 $2^d$ 个。当 $d=20$ 时，$2^{20}=1,048,576$。即使有 1,000 个样本，最多也只看到 1,000 种不同组合，覆盖率还不到 0.1%。这里用一个具体计数说明高维空间为何很快变得稀疏。

<details>
<summary>展开第 5 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 5 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-05.jpg)

</details>

## 第 6 页：维数灾难与低维结构

覆盖没有结构可利用的高维特征空间，可能需要随维度指数增长的样本，这叫维数灾难。但并不是每个学习任务都需要 $2^d$ 个样本：真实数据可能靠近一个远小于原空间的子空间。降维希望用 $k<d$ 个坐标保留重要变化。

<details>
<summary>展开第 6 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 6 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-06.jpg)

</details>

## 第 7 页：例 2——投影去除与信号垂直的误差

设有用信号位于单位向量 $q=\frac15(3,4,0)^T$ 张成的直线上。干净信号为 $s=(15,20,0)^T$，误差为 $e=(0,0,3)^T$，观测到 $x=s+e=(15,20,3)^T$。因为误差垂直于信号直线，正交投影得到

$$\langle q,x\rangle q=25q=s.$$

也就是说，保留该直线方向、丢弃垂直方向，就能在这个特定例子里恢复干净信号。

<details>
<summary>展开第 7 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 7 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-07.jpg)

</details>

## 第 8 页：投影不等于自动识别噪声

测量误差和不需要的波动都是噪声；投影会去掉与保留子空间垂直的成分。然而 PCA 是从观测数据的变化学习子空间，并不知道真实干净信号。因此被丢弃的变化不能自动被认定为噪声。这一限制贯穿后面的应用解释。

<details>
<summary>展开第 8 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 8 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-08.jpg)

</details>

## 第 9 页：章节页——方阵的特征向量

转入特征向量与特征值，它们将为 PCA 提供方向和方向上的变化量。

<details>
<summary>展开第 9 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 9 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-09.jpg)

</details>

## 第 10 页：特征向量和特征值

一般矩阵会混合输入向量的坐标；我们寻找经矩阵作用后只发生缩放的方向。对于 $A\in\mathbb R^{d\times d}$，如果非零向量 $v\in\mathbb R^d$ 满足

$$Av=\lambda v,$$

则 $v$ 是特征向量，$\lambda\in\mathbb R$ 是对应特征值。如果这样的方向足够组成一组基，换成这组基后，矩阵就分别缩放各个坐标。

<details>
<summary>展开第 10 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 10 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-10.jpg)

</details>

## 第 11 页：特征值的几何意义

$\lambda>0$ 表示缩放而不反向；$\lambda<0$ 表示缩放并反向；$\lambda=0$ 表示该特征向量被映射到零。零向量不算特征向量，否则因为 $A0=\lambda0$ 对任意标量都成立，每个标量都会变成“特征值”。

<details>
<summary>展开第 11 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 11 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-11.jpg)

</details>

## 第 12 页：特征空间与求解方法

给定特征值 $\lambda$，其特征空间是

$$E_\lambda=\{v\in\mathbb R^d:Av=\lambda v\}=\operatorname{Nul}(A-\lambda I_d).$$

它是包含零向量的子空间，其中每个非零向量都是特征向量。因此要区分“特征空间包含零”与“零不是特征向量”。已知 $\lambda$ 后，对 $(A-\lambda I_d)v=0$ 做高斯消元，就能找到这个空间。

<details>
<summary>展开第 12 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 12 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-12.jpg)

</details>

## 第 13 页：例 3——检查三个候选方向

课件给出

$$A=\begin{pmatrix}1&10&-3\\10&4&18\\-3&18&-15\end{pmatrix},\quad
v_1=\begin{pmatrix}-1\\2\\-3\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\2\\1\end{pmatrix},\quad
v_3=\begin{pmatrix}-4\\1\\2\end{pmatrix}.$$

任务是分别计算 $Av_i$，检查结果是不是原向量的一个标量倍数。

<details>
<summary>展开第 13 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 13 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-13.jpg)

</details>

## 第 14 页：例 3 的计算结果

$$Av_1=(28,-56,84)^T=-28v_1,\quad Av_2=(18,36,18)^T=18v_2,\quad Av_3=0.$$

因此三个向量都是特征向量，对应特征值为 $-28,18,0$。对于大矩阵，实际使用数值软件求特征值与特征向量。

<details>
<summary>展开第 14 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 14 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-14.jpg)

</details>

## 第 15 页：章节页——对称矩阵有标准正交特征基

接下来说明为什么协方差矩阵能提供一套互相垂直、长度为 1 的方向。

<details>
<summary>展开第 15 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 15 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-15.jpg)

</details>

## 第 16 页：对称矩阵与标准正交特征基

实方阵 $A$ 对称是指 $A^T=A$，等价于对所有 $i,j$ 都有 $a_{ij}=a_{ji}$。并非所有实方阵都有一组实特征向量构成的基，但实对称矩阵一定有标准正交特征基。以这种基改变坐标会保留长度和角度。

<details>
<summary>展开第 16 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 16 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-16.jpg)

</details>

## 第 17 页：命题 1——不同特征值的特征向量正交

若 $A$ 为实对称矩阵，$Au=\lambda u$、$Av=\mu v$ 且 $\lambda\ne\mu$，则 $u\perp v$。课件证明写到这些假设后以“Then...”留作推导。

理解补充：$\lambda u^Tv=(Au)^Tv=u^TA^Tv=u^TAv=\mu u^Tv$，所以 $(\lambda-\mu)u^Tv=0$，从而 $u^Tv=0$。

<details>
<summary>展开第 17 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 17 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-17.jpg)

</details>

## 第 18 页：谱定理

每个实对称矩阵 $A\in\mathbb R^{d\times d}$ 都有标准正交特征基 $q_1,\ldots,q_d$ 和实特征值 $\lambda_1,\ldots,\lambda_d$。令 $Q=(q_1\ \cdots\ q_d)$、$\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)$，则 $Q$ 是正交矩阵，而且

$$A=Q\Lambda Q^T=\sum_{j=1}^d\lambda_jq_jq_j^T.$$

这把矩阵写成按特征方向分别作用的形式，也写成一系列秩一矩阵之和。

<details>
<summary>展开第 18 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 18 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-18.jpg)

</details>

## 第 19 页：例 4——把例 3 标准化并组成 Q

例 3 三个向量的长度分别为 $\sqrt{14},\sqrt6,\sqrt{21}$。除以各自长度，按列排列：

$$Q=\begin{pmatrix}
-1/\sqrt{14}&1/\sqrt6&-4/\sqrt{21}\\
2/\sqrt{14}&2/\sqrt6&1/\sqrt{21}\\
-3/\sqrt{14}&1/\sqrt6&2/\sqrt{21}
\end{pmatrix}.$$

原矩阵就是 $A=Q\operatorname{diag}(-28,18,0)Q^T$。这里各列长度为 1，并且彼此正交。

<details>
<summary>展开第 19 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 19 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-19.jpg)

</details>

## 第 20 页：例 4——在特征坐标中理解矩阵作用

继续使用 $A=Q\operatorname{diag}(-28,18,0)Q^T$。若 $x=\alpha_1q_1+\alpha_2q_2+\alpha_3q_3$，则

$$Ax=-28\alpha_1q_1+18\alpha_2q_2.$$

第一坐标乘以 -28，第二坐标乘以 18，第三坐标被消去。这具体展示了“用特征基使坐标分别缩放”。

<details>
<summary>展开第 20 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 20 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-20.jpg)

</details>

## 第 21 页：半正定矩阵

对称矩阵 $A$ 对应的标量 $v^TAv$ 叫作在 $v$ 处的二次型。如果对所有 $v\in\mathbb R^d$ 都有 $v^TAv\ge0$，就称 $A$ 半正定（positive semidefinite）。用矩阵描述平方的平均值时，需要的正是这种非负性。

<details>
<summary>展开第 21 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 21 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-21.jpg)

</details>

## 第 22 页：命题 2——半正定等价于所有特征值非负

对实对称矩阵，半正定当且仅当所有特征值都非负。证明的一个方向是利用谱定理写 $v=\sum_j\alpha_jq_j$，于是

$$v^TAv=\sum_{j=1}^d\lambda_j\alpha_j^2.$$

如果各 $\lambda_j\ge0$，此和非负。另一个方向取 $v=q_j$，得到 $q_j^TAq_j=\lambda_j$，因此半正定要求每个特征值非负。

<details>
<summary>展开第 22 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 22 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-22.jpg)

</details>

## 第 23 页：章节页——协方差记录特征共同变化

线性代数工具准备好后，开始构造用于数据分析的协方差矩阵。

<details>
<summary>展开第 23 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 23 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-23.jpg)

</details>

## 第 24 页：中心化

要研究的是数据点彼此的变化，而不是所有数据共同偏离原点的程度。对 $n\ge2$ 个数据点，定义

$$\mu=\frac1n\sum_{i=1}^nx_i,\quad \widetilde x_i=x_i-\mu,\quad X_c=X-\mathbf1\mu^T\in\mathbb R^{n\times d}.$$

$X_c$ 的第 $i$ 行是 $\widetilde x_i^T$，每个特征列的均值都是零；$\mathbf1\in\mathbb R^n$ 的各项都是 1。

<details>
<summary>展开第 24 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 24 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-24.jpg)

</details>

## 第 25 页：经验方差

对均值为 $\bar t$ 的数 $t_1,\ldots,t_n$，课件采用

$$\operatorname{Var}(t_1,\ldots,t_n)=\frac1n\sum_{i=1}^n(t_i-\bar t)^2.$$

方差描述围绕均值的分散程度。中心化后 $\bar t=0$，方差就成为这些数平方的平均值。

<details>
<summary>展开第 25 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 25 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-25.jpg)

</details>

## 第 26 页：协方差矩阵的定义和各元素

$$C=\frac1nX_c^TX_c\in\mathbb R^{d\times d},\qquad
C_{j\ell}=\frac1n\sum_i(x_{ij}-\mu_j)(x_{i\ell}-\mu_\ell).$$

对角元素 $C_{jj}$ 是特征 $j$ 的方差，非对角元素记录两特征如何共同变化。本讲统一使用 $1/n$；若改为 $1/(n-1)$，所有特征值会按同一比例缩放，但主成分方向和解释方差比例不变。

<details>
<summary>展开第 26 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 26 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-26.jpg)

</details>

## 第 27 页：命题 3——协方差矩阵对称且半正定

由转置规则，$C^T=\frac1n(X_c^TX_c)^T=\frac1nX_c^TX_c=C$，因此它对称。对任何 $v\in\mathbb R^d$，

$$v^TCv=\frac1n\|X_cv\|_2^2\ge0.$$

所以它也半正定，能够使用谱定理，而且所有特征值非负。

<details>
<summary>展开第 27 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 27 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-27.jpg)

</details>

## 第 28 页：例 5——四个二维点的中心化

$$X=\begin{pmatrix}16&24\\14&26\\4&16\\6&14\end{pmatrix},\quad
\mu=\begin{pmatrix}10\\20\end{pmatrix},\quad
X_c=\begin{pmatrix}6&4\\4&6\\-6&-4\\-4&-6\end{pmatrix}.$$

先按列求均值，再从每行数据减去同一个均值向量，使点云中心移到原点。

<details>
<summary>展开第 28 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 28 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-28.jpg)

</details>

## 第 29 页：例 5——正协方差

$$C=\frac14
\begin{pmatrix}6&4&-6&-4\\4&6&-4&-6\end{pmatrix}
\begin{pmatrix}6&4\\4&6\\-6&-4\\-4&-6\end{pmatrix}
=\begin{pmatrix}26&24\\24&26\end{pmatrix}.$$

两个特征方差均为 26，协方差为正的 24：两个特征倾向于同时高于均值或同时低于均值。方向 $(1,1)^T$ 和 $(1,-1)^T$ 的特征值分别为 50 和 2，因此点云主要沿同向变化的方向延伸。

<details>
<summary>展开第 29 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 29 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-29.jpg)

</details>

## 第 30 页：例 5——同样均值下的负协方差

$$X'=\begin{pmatrix}16&14\\14&16\\4&26\\6&24\end{pmatrix},\quad
X'_c=\begin{pmatrix}6&-6\\4&-4\\-6&6\\-4&4\end{pmatrix},\quad
C'=\frac14(X'_c)^TX'_c=\begin{pmatrix}26&-26\\-26&26\end{pmatrix}.$$

均值仍是 $(10,20)^T$，但两特征总和固定为 30，因此一个增加时另一个等量减少，呈负协方差。

<details>
<summary>展开第 30 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 30 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-30.jpg)

</details>

## 第 31 页：例 5——正、负协方差的点图

横轴为 Feature 1，纵轴为 Feature 2，两图均画中心化后的点并标出 $\pm6$。左图为正协方差 24，四点是 $(6,4),(4,6),(-6,-4),(-4,-6)$，沿左下到右上分布。右图为负协方差 -26，四点是 $(6,-6),(4,-4),(-6,6),(-4,4)$，沿左上到右下的一条直线分布。图形直观展示了前两页数值的含义。

<details>
<summary>展开第 31 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 31 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-31.jpg)

</details>

## 第 32 页：章节页——第一主成分保留最多方差

接下来把“选重要方向”精确定义为“使投影方差最大”。

<details>
<summary>展开第 32 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 32 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-32.jpg)

</details>

## 第 33 页：标准正交基与投影

若 $\{q_1,\ldots,q_d\}$ 是 $\mathbb R^d$ 的标准正交基，则任意 $u$ 都能唯一表示为 $u=\sum_ic_iq_i$，其中 $c_i=\langle u,q_i\rangle$。向量 $c_iq_i$ 是 $u$ 沿 $q_i$ 的投影。图中紫色向量 $u$ 分解为沿 $q_1,q_2$ 的两条红色投影，虚线连接分解形成的平行四边形。

<details>
<summary>展开第 33 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 33 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-33.jpg)

</details>

## 第 34 页：怎样衡量一个方向重要不重要

当 $d\ge2$ 时，有无穷多组标准正交基。降维希望选一组基，使其中前面少数几个向量就足以代表数据。这里的“重要”使用投影后的方差衡量，即数据沿该方向展开的程度。

<details>
<summary>展开第 34 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 34 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-34.jpg)

</details>

## 第 35 页：投影方差小的方向

图中的四个绿色数据向量投影到 $q_i$ 轴，得到四个红点。如果红点挤得很近，投影方差就小，原来的点在这个表示下很难区分。因此，这个方向对保留当前数据变化不够重要。

<details>
<summary>展开第 35 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 35 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-35.jpg)

</details>

## 第 36 页：投影方差大的方向

换一个方向 $q_j$ 后，四个投影红点相距更远，容易区分，因此此方向更适合保留数据变化。两页的对比提供了 PCA 最大化方差的直观动机；它说的是保留变化，并没有使用类别标签。

<details>
<summary>展开第 36 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 36 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-36.jpg)

</details>

## 第 37 页：命题 4——投影得分的方差是二次型

每个中心化数据点只存一个数时，选择单位方向 $q$，保存 $t_i=\langle q,\widetilde x_i\rangle$。这些得分均值为零，而且

$$\operatorname{Var}(t_1,\ldots,t_n)=\frac1n\sum_i\langle q,\widetilde x_i\rangle^2=q^TCq.$$

原因是中心化点的和为零，整个得分向量为 $t=X_cq$。要求单位长度非常关键：把 $q$ 乘以 $a$ 会把方差乘以 $a^2$，否则可仅靠拉长向量无限增大方差。

<details>
<summary>展开第 37 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 37 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-37.jpg)

</details>

## 第 38 页：第一主成分与定理 2

第一主成分方向定义为使 $q^TCq$ 最大的单位向量。将协方差矩阵的标准正交特征向量按 $\lambda_1\ge\cdots\ge\lambda_d\ge0$ 排列，则

$$\max_{\|q\|_2=1}q^TCq=\lambda_1.$$

所有最优方向恰好是最大特征值 $\lambda_1$ 的特征空间里的单位向量，特别地 $q_1$ 就是一个第一主成分方向。

<details>
<summary>展开第 38 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 38 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-38.jpg)

</details>

## 第 39 页：定理 2 的证明

将单位向量展开成 $q=\sum_j\alpha_jq_j$，标准正交性给出 $\sum_j\alpha_j^2=1$。于是

$$q^TCq=\sum_j\lambda_j\alpha_j^2\le\lambda_1\sum_j\alpha_j^2=\lambda_1.$$

等号成立当且仅当所有满足 $\lambda_j<\lambda_1$ 的方向上系数都是零。因此最优向量只能由最大特征值所对应的特征向量组成。

<details>
<summary>展开第 39 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 39 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-39.jpg)

</details>

## 第 40 页：例 6——后续贯穿使用的六个四维点

$$X=\begin{pmatrix}38&43&41&50\\20&31&53&68\\26&40&50&56\\19&30&22&37\\7&12&40&49\\10&24&34&40\end{pmatrix},\quad
\mu=\begin{pmatrix}20\\30\\40\\50\end{pmatrix},$$

$$X_c=\begin{pmatrix}18&13&1&0\\0&1&13&18\\6&10&10&6\\-1&0&-18&-13\\-13&-18&0&-1\\-10&-6&-6&-10\end{pmatrix}.$$

接下来的主成分、编码、重构、误差和可视化，都针对这一组数据。

<details>
<summary>展开第 40 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 40 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-40.jpg)

</details>

## 第 41 页：例 6——协方差与特征值

$$C=\frac16X_c^TX_c=\begin{pmatrix}105&98&26&27\\98&105&27&26\\26&27&105&98\\27&26&98&105\end{pmatrix}.$$

排好序的特征值是 $256,150,8,6$。每个原始特征的方差都是 105，但合适的线性组合可以有更大的方差。

<details>
<summary>展开第 41 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 41 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-41.jpg)

</details>

## 第 42 页：例 6——第一主成分和得分

$$q_1=\tfrac12(1,1,1,1)^T,\qquad t=X_cq_1=(16,16,16,-16,-16,-16)^T.$$

得分均值为零，方差 $\frac16\sum_{i=1}^6t_i^2=\frac16(6\times16^2)=256$，大于任一单独原始特征的方差 105。这展示 PCA 选择的是原始特征的线性组合。

<details>
<summary>展开第 42 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 42 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-42.jpg)

</details>

## 第 43 页：一个主成分的回顾

最大协方差特征值就是单位方向上可保留的最大方差。把 $q_1$ 换成 $-q_1$ 会使所有得分反号，但保留的直线及重构误差不变。如果最大特征值重复，可能存在多个不同的最优方向。

<details>
<summary>展开第 43 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 43 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-43.jpg)

</details>

## 第 44 页：章节页——多个主成分保留一个子空间

从只保留一个坐标，推广到保留 $k$ 个互相正交的坐标。

<details>
<summary>展开第 44 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 44 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-44.jpg)

</details>

## 第 45 页：PCA 基矩阵

重复使用第一方向只会重复存相同信息，所以需要互相正交的方向。将协方差标准正交特征向量按特征值降序排列，选 $1\le k\le d$，定义

$$Q_k=(q_1\ \cdots\ q_k)\in\mathbb R^{d\times k},\qquad S_k=\operatorname{span}\{q_1,\ldots,q_k\}.$$

$S_k$ 是所保留的子空间。

<details>
<summary>展开第 45 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 45 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-45.jpg)

</details>

## 第 46 页：PCA 坐标与批量编码

单个点编码为 $z_i=Q_k^T(x_i-\mu)\in\mathbb R^k$；整个训练集编码为 $Z=X_cQ_k\in\mathbb R^{n\times k}$，第 $i$ 行是 $z_i^T$。这些是数据点投影到保留子空间后的坐标，通常不是整个原始点的无损表示。

<details>
<summary>展开第 46 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 46 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-46.jpg)

</details>

## 第 47 页：命题 5——后续主成分与得分协方差

$q_j$ 在所有垂直于 $q_1,\ldots,q_{j-1}$ 的单位方向中，使方差最大，最大值为 $\lambda_j$。保留的得分均值为零，且

$$\frac1nZ^TZ=Q_k^TCQ_k=\operatorname{diag}(\lambda_1,\ldots,\lambda_k).$$

第 $j$ 个坐标贡献方差 $\lambda_j$，不同得分坐标的协方差为零，所以它们不相关。这里是不相关，不是课件声称它们相互独立。

<details>
<summary>展开第 47 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 47 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-47.jpg)

</details>

## 第 48 页：命题 5 的证明

一个垂直于前 $j-1$ 个特征向量的单位向量可写成 $q=\sum_{\ell=j}^d\alpha_\ell q_\ell$，其中 $\sum_{\ell=j}^d\alpha_\ell^2=1$。因此 $q^TCq=\sum_{\ell=j}^d\lambda_\ell\alpha_\ell^2\le\lambda_j$，取 $q=q_j$ 达到等号。另一方面，

$$q_j^TCq_\ell=\lambda_\ell\langle q_j,q_\ell\rangle=\begin{cases}\lambda_j,&j=\ell,\\0,&j\ne\ell.\end{cases}$$

结合 $Z=X_cQ_k$，就得到对角的得分协方差矩阵。

<details>
<summary>展开第 48 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 48 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-48.jpg)

</details>

## 第 49 页：例 7——完整的有序特征基

六点数据的一组标准正交特征基为

$$q_1=\tfrac12(1,1,1,1)^T,\quad q_2=\tfrac12(1,1,-1,-1)^T,$$
$$q_3=\tfrac12(1,-1,-1,1)^T,\quad q_4=\tfrac12(1,-1,1,-1)^T.$$

对应特征值依次为 $256,150,8,6$。选择保留 $q_1,q_2$，丢掉方差明显较小的 $q_3,q_4$。

<details>
<summary>展开第 49 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 49 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-49.jpg)

</details>

## 第 50 页：例 7——二维编码结果

$$Q_2=\tfrac12\begin{pmatrix}1&1\\1&1\\1&-1\\1&-1\end{pmatrix},\qquad
Z=X_cQ_2=\begin{pmatrix}16&15\\16&-15\\16&0\\-16&15\\-16&-15\\-16&0\end{pmatrix}.$$

例如第一点编码为 $z_1=(16,15)^T$。两列得分的方差分别是 256 和 150。

<details>
<summary>展开第 50 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 50 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-50.jpg)

</details>

## 第 51 页：章节页——PCA 最小化重构误差

现在从另一个角度解释同一选择：在固定维度下，PCA 能使平均平方重构误差最小。

<details>
<summary>展开第 51 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 51 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-51.jpg)

</details>

## 第 52 页：重构和平均平方重构误差

Lecture 5 已介绍用标准正交坐标乘基矩阵还原投影；此处还需要把均值加回来。对具有标准正交列的 $U\in\mathbb R^{d\times k}$，

$$\widehat x_i=\mu+UU^T(x_i-\mu),\qquad E(U)=\frac1n\sum_{i=1}^n\|x_i-\widehat x_i\|_2^2.$$

第一式是选择子空间后的重构，第二式对每个数据点的残差平方长度取平均。

<details>
<summary>展开第 52 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 52 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-52.jpg)

</details>

## 第 53 页：定理 3——PCA 的最优性

若协方差特征值按 $\lambda_1\ge\cdots\ge\lambda_d\ge0$ 排列，对任何由 $k$ 个标准正交方向组成的 $U$，都有

$$E(U)\ge\sum_{\ell=k+1}^d\lambda_\ell.$$

选择 $U=Q_k$ 能达到等号。因此 PCA 同时最大化保留方差、最小化重构误差；最小平均平方误差等于被丢掉的协方差特征值之和。本页陈述定理，没有展开证明。

<details>
<summary>展开第 53 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 53 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-53.jpg)

</details>

## 第 54 页：例 8——重构第一个点

利用例 7 的两个得分：

$$\widehat x_1=\mu+16q_1+15q_2=\tfrac12(71,91,81,101)^T.$$

残差为 $x_1-\widehat x_1=\tfrac12(5,-5,1,-1)^T$。它描述编码时舍弃的方向所包含的部分。

<details>
<summary>展开第 54 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 54 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-54.jpg)

</details>

## 第 55 页：例 8——全部重构和残差

$$\widehat X=\tfrac12\begin{pmatrix}71&91&81&101\\41&61&111&131\\56&76&96&116\\39&59&49&69\\9&29&79&99\\24&44&64&84\end{pmatrix},$$

$$X-\widehat X=\tfrac12\begin{pmatrix}5&-5&1&-1\\-1&1&-5&5\\-4&4&4&-4\\-1&1&-5&5\\5&-5&1&-1\\-4&4&4&-4\end{pmatrix}.$$

残差矩阵每一行都是一个数据点的重构误差向量，不能把单个分量与整点误差混为一谈。

<details>
<summary>展开第 55 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 55 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-55.jpg)

</details>

## 第 56 页：例 8——计算重构误差

六个点各自的平方重构误差是 $13,13,16,13,13,16$。平均后

$$E(Q_2)=\frac{13+13+16+13+13+16}{6}=14=\lambda_3+\lambda_4.$$

若只保留第一主成分，则 $E(Q_1)=150+8+6=164$。这直接验证了丢弃特征值之和的误差公式。

<details>
<summary>展开第 56 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 56 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-56.jpg)

</details>

## 第 57 页：秩与精确重构的推论

如果 $X_c$ 的秩为 $r$，协方差矩阵恰有 $r$ 个正特征值，并且

$$\operatorname{rank}(C)=\operatorname{rank}(X_c)=r\le\min(d,n-1).$$

保留全部 $r$ 个正特征值方向，可以精确重构每个训练点。若 $r=0$，所有点相同，单独保存均值就能完全重构。

<details>
<summary>展开第 57 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 57 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-57.jpg)

</details>

## 第 58 页：精确重构不自动证明有意义的低维结构

当 $d\ge n$，中心化训练数据总在至多 $n-1$ 维的子空间里，即使数据完全是噪声也成立。因此用 $n-1$ 个主成分精确重构训练集，不能据此宣称发现了有意义的低维结构。更应该问：能否用远少于它的维度保留有用结构，并适用于新数据点？

<details>
<summary>展开第 58 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 58 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-58.jpg)

</details>

## 第 59 页：章节页——实际使用 PCA

接下来讲如何选维度、拟合变换、编码新数据，以及如何考虑单位和预测任务。

<details>
<summary>展开第 59 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 59 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-59.jpg)

</details>

## 第 60 页：累计解释方差比例

当总方差 $\sum_{j=1}^d\lambda_j>0$ 时，前 $k$ 个主成分保留的训练方差比例是

$$\rho_k=\frac{\sum_{j=1}^k\lambda_j}{\sum_{j=1}^d\lambda_j}.$$

分子是保留方差，分母是中心化后的总方差。一种选法是预先选择阈值，取达到阈值的最小 $k$。

<details>
<summary>展开第 60 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 60 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-60.jpg)

</details>

## 第 61 页：例 9——保留两维的解释方差

$$\rho_2=\frac{256+150}{256+150+8+6}=\frac{406}{420}\approx0.9667.$$

这保留约 96.67% 的训练方差，满足 95% 阈值，但不满足 99%。丢弃比例为 $1/30$，对应平均平方重构误差 14。

<details>
<summary>展开第 61 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 61 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-61.jpg)

</details>

## 第 62 页：算法 1——保留 k 个主成分的 PCA

输入是训练矩阵 $X\in\mathbb R^{n\times d}$ 和 $1\le k\le d$。按顺序执行：

1. 求训练均值 $\mu=\frac1n\sum_i x_i$。
2. 中心化 $X_c=X-\mathbf1\mu^T$。
3. 按需要缩放中心化特征，并保存缩放参数。
4. 构造 $C=\frac1nX_c^TX_c$；如使用缩放，此处使用缩放后的中心化数据。
5. 求标准正交特征向量，按特征值从大到小排列。
6. 取前 $k$ 列组成 $Q_k$。
7. 计算 $Z=X_cQ_k$。
8. 保存 $\mu,Q_k$ 以及所用缩放参数。

实际的特征值与特征向量计算由数值软件完成。

<details>
<summary>展开第 62 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 62 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-62.jpg)

</details>

## 第 63 页：新点编码、重构和训练集边界

不额外缩放时，新数据点使用 $z=Q_k^T(x-\mu)$ 编码，再用 $\widehat x=\mu+Q_kz$ 重构。整个训练集的重构是 $\widehat X=\mathbf1\mu^T+ZQ_k^T$。均值和方向只能在训练集拟合；验证集、测试集和未来数据都使用同一套已拟合变换，不能各自重新拟合。

<details>
<summary>展开第 63 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 63 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-63.jpg)

</details>

## 第 64 页：特征单位和缩放顺序

单位会改变 PCA：米变毫米使数值乘 1,000，方差乘 $10^6$。根据应用决定是否缩放中心化后的特征。编码前应用已拟合缩放；重构时先撤销缩放，再加均值。经过缩放后，“最大保留方差”和“最小重构误差”的最优性指的是缩放后的特征空间。

<details>
<summary>展开第 64 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 64 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-64.jpg)

</details>

## 第 65 页：PCA 能保证什么、不能保证什么

较少特征可以减少存储和后续模型计算代价。如果低方差方向主要是噪声，丢弃它们可能降噪。PCA 不使用类别标签，所以高方差方向不一定对预测有用；某个低方差方向反而可能恰好区分类别。解释方差高不等于分类表现好。

<details>
<summary>展开第 65 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 65 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-65.jpg)

</details>

## 第 66 页：章节页——高维数据可视化

最后把 PCA 得分当作二维或三维图的坐标，并说明怎样解释这些图。

<details>
<summary>展开第 66 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 66 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-66.jpg)

</details>

## 第 67 页：用前两个或三个主成分作图

高维点不能直接完整地显示成二维或三维点。二维时画

$$z_i=\begin{pmatrix}\langle q_1,x_i-\mu\rangle\\\langle q_2,x_i-\mu\rangle\end{pmatrix}.$$

三维时再加上 $q_3$ 的得分。每条轴都是原特征的线性组合，而不是简单选出某个原始特征。

<details>
<summary>展开第 67 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 67 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-67.jpg)

</details>

## 第 68 页：例 10——六个四维点的二维图

横轴为 PC 1 score，纵轴为 PC 2 score。$x_1,x_2,x_3$ 分别在 $(16,15),(16,-15),(16,0)$；$x_4,x_5,x_6$ 分别在 $(-16,15),(-16,-15),(-16,0)$。PC 1 将两组分开，PC 2 展示每组内部的变化。两轴保留 96.67% 训练方差，PC 3 和 PC 4 的变化在图中不可见。

<details>
<summary>展开第 68 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 68 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-68.jpg)

</details>

## 第 69 页：例 11——英超球员表现数据

使用 2024/25 赛季英格兰足球超级联赛球员表现数据。讲师说明数据不免费公开，因此无法分享。每名球员有 77 个特征，例如 `minutesPlayed`、`accurateLongBalls`、`accurateLongBallsPercentage`、`saves`。其中只有门将的扑救次数 `saves` 非零，这会影响主成分。

<details>
<summary>展开第 69 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 69 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-69.jpg)

</details>

## 第 70 页：例 11——出场筛选与按时间归一化

只研究充分参与比赛的球员，删除出场少于 900 分钟者。但剩余球员仍可能有人只踢约 900 分钟、有人超过 3,000 分钟，所以非百分比特征，例如长传成功次数，需除以出场分钟数，以便公平比较。再删除明显不利于区分球员类型的特征，例如 `appearances`、`matchesStarted`。百分比指标不按同样方式重复除时间。

<details>
<summary>展开第 70 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 70 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-70.jpg)

</details>

## 第 71 页：例 11——尚包含门将的 PCA 图

本页是纯图：横轴 PC 1、纵轴 PC 2，标题为“PCA Projection (PC3 → size/color)”，即 PC 3 同时由点大小和颜色编码。蓝、红不是本页给出的场上位置类别标签。图没有额外色标说明数值与颜色的精确映射，所以不推断哪种颜色一定对应正值。多数球员形成主体点云，右下方另有明显远离主体的点群。联系前页门将专属指标与下一页处理，可理解为门将差异主导了部分投影。点的精确位置、大小和刻度见本节原图。

<details>
<summary>展开第 71 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 71 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-71.jpg)

</details>

## 第 72 页：例 11——移除门将并标注突出球员

于是删除所有门将，同时删除门将专用特征，例如 `saves`、`punches`。重新作图时，凡在前三维中至少一维表现突出的球员，会在图中标出姓名。以下几页既展示整体，也放大局部，保留原图中的全部姓名和点标注供对照。

<details>
<summary>展开第 72 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 72 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-72.jpg)

</details>

## 第 73 页：例 11——去掉门将后的整体图

横轴 PC 1、纵轴 PC 2，PC 3 继续由点大小和颜色编码；标题说明已标注突出球员。左侧聚集较多防守球员，上方聚集若干创造型球员，右下出现多名前锋。这里的目的在于看到类型分布和异常位置，不能把 PC 轴直接当成某个原始足球指标。

为保留整体图的全部姓名，按图中区域列出标签；后面三页还会把多数标签所在区域放大：

- 左侧与中部：Rúben Dias、Manuel Akanji、Joachim Andersen、Lewis Dunk、William Saliba、Virgil van Dijk、Jannik Vestergaard、Tosin Adarabioyo、Gabriel Magalhães、Conor Coady、Nikola Milenković、Michael Keane、Joško Gvardiol、Tyler Adams、Nicolás Domínguez、Wilfred Ndidi、Ryan Yates。
- 上方与中场区域：Trent Alexander-Arnold、Kieran Trippier、Mateo Kovačić、Pedro Porro、Reece James、Mats Wieffer、Manuel Ugarte、İlkay Gündoğan、João Gomes、Will Hughes、Elliot Anderson、Mikkel Damsgaard、Enzo Fernández、Christian Eriksen、Martin Ødegaard、Bruno Fernandes、Jérémy Doku、Kevin De Bruyne、James Maddison、Savinho、Dwight McNeil、Bukayo Saka。
- 右侧及中部进攻区域：Facundo Buonanotte、Phil Foden、Eberechi Eze、Cole Palmer、Matheus Cunha、Julio Enciso、Heung-min Son、Jordan Ayew、Georginio Rutter、Luis Díaz、Bryan Mbeumo、Jarrod Bowen、Marcus Rashford、Omar Marmoush、Justin Kluivert、João Pedro、Danny Welbeck、Mohamed Salah。
- 右下区域：Edward Nketiah、Darwin Núñez、Diogo Jota、Cameron Archer、Kai Havertz、Kevin Schade、Dominic Solanke、Raúl Jiménez、Nicolas Jackson、Liam Delap、Yoane Wissa、Jean-Philippe Mateta、Alexander Isak、Jamie Vardy、Jørgen Strand Larsen、Paul Onuachu、Evanilson、Rodrigo Muniz、Dominic Calvert-Lewin、Beto、Ollie Watkins、Erling Haaland、Chris Wood。

所有点的精确位置、大小、颜色及重叠关系见原图；文字列名不替代这些视觉信息。

<details>
<summary>展开第 73 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 73 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-73.jpg)

</details>

## 第 74 页：例 11——左侧与中部球员的放大图

本页放大整体图的左侧与中部，使防守球员和若干中场的姓名、相对位置更容易辨认。左侧聚集区标有 Rúben Dias、Manuel Akanji、Joachim Andersen、Lewis Dunk、Virgil van Dijk、William Saliba、Jannik Vestergaard、Tosin Adarabioyo、Gabriel Magalhães；更低处有 Conor Coady、Nikola Milenković、Michael Keane。上方与右上标有 Kieran Trippier、Mateo Kovačić、Pedro Porro、Trent Alexander-Arnold、Mikkel Damsgaard、Enzo Fernández、Christian Eriksen。中部还有 Reece James、Mats Wieffer、Manuel Ugarte、Elliot Anderson、İlkay Gündoğan、João Gomes、Will Hughes、Tyler Adams、Nicolás Domínguez、Joško Gvardiol、Wilfred Ndidi、Ryan Yates。横纵轴仍是 PC 1、PC 2，PC 3 用大小和颜色表示，局部放大没有新增或重新拟合主成分。

<details>
<summary>展开第 74 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 74 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-74.jpg)

</details>

## 第 75 页：例 11——右下前锋区域的放大图

这一页继续使用相同主成分，放大 PC 1 较高、PC 2 较低的区域。标出的全部姓名为 Edward Nketiah、Darwin Núñez、Diogo Jota、Kai Havertz、Kevin Schade、Dominic Solanke、Raúl Jiménez、Nicolas Jackson、Liam Delap、Yoane Wissa、Jean-Philippe Mateta、Jamie Vardy、Jørgen Strand Larsen、Paul Onuachu、Evanilson、Dominic Calvert-Lewin、Rodrigo Muniz、Beto、Ollie Watkins、Erling Haaland、Chris Wood。Jørgen Strand Larsen、Paul Onuachu、Evanilson 的标签在图中靠近或重叠。图展示该组球员在 PC 2 以及由大小和颜色表示的 PC 3 上仍有差异，不能因为都处于右侧就当作完全相同。

<details>
<summary>展开第 75 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 75 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-75.jpg)

</details>

## 第 76 页：例 11——右上与中部进攻创造区域的放大图

同一 PCA 图的另一局部突出 Bruno Fernandes、Kevin De Bruyne、Jérémy Doku、James Maddison、Martin Ødegaard、Bukayo Saka、Savinho、Dwight McNeil、Facundo Buonanotte、Phil Foden、Eberechi Eze、Matheus Cunha、Cole Palmer、Julio Enciso、Heung-min Son、Jordan Ayew；较低处还有 Georginio Rutter、Marcus Rashford、Jarrod Bowen、Bryan Mbeumo、Luis Díaz、Omar Marmoush、Justin Kluivert、João Pedro、Danny Welbeck。这些是本页的全部姓名标签。原图保留每个姓名、点位置、颜色与大小，包括文字重叠部分。不同局部是为了看清同一低维表示里的球员，而不是三个互不相关的新数据集。

<details>
<summary>展开第 76 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 76 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-76.jpg)

</details>

## 第 77 页：例 11——效果与信息损失

去掉门将后，前三主成分解释总方差约 45.5%，所以三维展示必然漏掉不少信息。尽管如此，它仍突出不少知名优秀球员，也能发现一些较少受到关注的球员，并且看起来能够较好地区分后卫、中场和前锋等类型。课件的表述是观察到的效果，不是分类准确率保证。

<details>
<summary>展开第 77 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 77 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-77.jpg)

</details>

## 第 78 页：PCA 图只是部分视图

二维或三维 PCA 图可以揭示组别、异常点和大体模式。但必须检查 $\rho_2$ 或 $\rho_3$，因为两三个主成分未必保留大部分方差。在图里重叠的点，可能在被丢弃方向上差异很大；图也不一定保留所有距离，或显示类别之间的每一种区别。

<details>
<summary>展开第 78 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 78 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-78.jpg)

</details>

## 第 79 页：本讲总结

中心化后的协方差记录变化；协方差特征向量给出正交方向，特征值给出各方向上的方差；PCA 保留领先方向，并最小化平均平方重构误差；解释方差比例可帮助选 $k$，但不能保证预测任务上的实用性。这四点连起本讲的数学推导与应用限制。

<details>
<summary>展开第 79 页原始 slide，核对图表、标注和公式</summary>

![Lecture 09 第 79 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture09-79.jpg)

</details>
