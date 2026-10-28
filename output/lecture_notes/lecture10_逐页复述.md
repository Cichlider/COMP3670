# Lecture 10：奇异值分解、低秩近似与推荐系统，按幻灯片逐页复述

来源：[lecture10a.pdf](/Users/cichlidfish/COMP3670/comp3670_lectures/lecture10a.pdf)，共 44 个 PDF 页面。目录中本讲的文件名是 lecture10a，而不是 lecture10。以下严格按页顺序保留章节页、定义、证明、例题、数值表、算法、参考来源和限制条件。每节末附原页核对图。

## 第 1 页：课程与主题

这是 COMP3670/6670《Introduction to Machine Learning》Week 10a：Singular Value Decomposition & Low-Rank Approximation，即奇异值分解（SVD）与低秩近似。讲师是 ANU School of Computing 的 Yun Kuen Cheung（Marco），职称 Senior Lecturer。

<details>
<summary>展开第 1 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 1 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-01.jpg)

</details>

## 第 2 页：学习目标

本讲要学会用 SVD 描述矩形矩阵；找到最佳低秩近似并计算误差；把矩阵因子解释为用户和物品的表示；在不把缺失评分当作零的前提下拟合评分模型；用验证集选超参数，并用留出的评分评价预测表现。

<details>
<summary>展开第 2 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 2 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-02.jpg)

</details>

## 第 3 页：章节页——SVD 使用两组标准正交方向

上一讲对称矩阵使用同一组特征方向。本讲从输入空间、输出空间可能维度不同的情况出发。

<details>
<summary>展开第 3 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 3 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-03.jpg)

</details>

## 第 4 页：为什么需要 SVD

谱定理处理实对称方阵。但用户与物品数量通常不相等，评分表可以是矩形矩阵。对于 $A\in\mathbb R^{m\times d}$，输入属于 $\mathbb R^d$，输出属于 $\mathbb R^m$。因此 SVD 在两个空间各用一组标准正交方向，而不是要求同一套特征基同时适用两边。

<details>
<summary>展开第 4 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 4 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-04.jpg)

</details>

## 第 5 页：紧致 SVD 的定义

每个秩为 $r$ 的非零矩阵 $A\in\mathbb R^{m\times d}$ 都能写成

$$A=U_r\Sigma_rV_r^T=\sum_{i=1}^r\sigma_i u_iv_i^T,$$

其中 $U_r\in\mathbb R^{m\times r}$、$\Sigma_r\in\mathbb R^{r\times r}$、$V_r\in\mathbb R^{d\times r}$。$U_r,V_r$ 各自的列互相正交且长度为 1，$\Sigma_r=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$，并约定 $\sigma_1\ge\cdots\ge\sigma_r>0$。这些 $\sigma_i$ 是正奇异值；只保留正奇异值及相应方向的形式叫紧致 SVD（compact SVD）。

<details>
<summary>展开第 5 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 5 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-05.jpg)

</details>

## 第 6 页：左右奇异向量与矩阵形状

显式写为 $U_r=(u_1\ \cdots\ u_r)$，$V_r=(v_1\ \cdots\ v_r)$。$u_i$ 称左奇异向量，$v_i$ 称右奇异向量，满足 $U_r^TU_r=V_r^TV_r=I_r$。它们一般不是方阵，因此不能把反过来的 $U_rU_r^T$、$V_rV_r^T$ 也当成单位矩阵。

<details>
<summary>展开第 6 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 6 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-06.jpg)

</details>

## 第 7 页：例 1——把因子看成用户和物品嵌入

先假设评分矩阵 $A$ 的所有条目已知。$U_r$ 的每一行给出一个用户的嵌入，$V_r$ 的每一行给出一个物品的嵌入。坐标 $1,\ldots,r$ 是潜在因子（latent factors），可能体现类型、风格等模式，但学出的坐标未必具有明确的人类可解释含义。图中把 $U_r$、奇异值对角矩阵和 $V_r^T$ 分别展开。

<details>
<summary>展开第 7 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 7 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-07.jpg)

</details>

## 第 8 页：加权内积如何给出评分

把用户与物品行向量写为 $p_i^T,q_j^T$，则

$$a_{ij}=\langle p_i,\Sigma_rq_j\rangle=\sum_{\ell=1}^r\sigma_\ell p_{i\ell}q_{j\ell}.$$

这是加权内积：第 $\ell$ 个坐标的贡献由 $\sigma_\ell$ 加权。同号坐标增加评分，异号坐标减少评分。余弦相似度先将向量长度标准化再比较方向；这里的评分则有权重且没有长度归一化，二者不能直接等同。

<details>
<summary>展开第 8 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 8 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-08.jpg)

</details>

## 第 9 页：例 1——评分数值计算

取 $p_i=(0.6,0.2)^T$、$q_j=(0.5,-0.4)^T$、$\Sigma_2=\operatorname{diag}(10,2)$。预测评分是

$$a_{ij}=10(0.6)(0.5)+2(0.2)(-0.4)=3-0.16=2.84.$$

第一潜在因子产生正贡献，第二产生负贡献，最后相加。

<details>
<summary>展开第 9 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 9 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-09.jpg)

</details>

## 第 10 页：命题 1——奇异向量与特征向量的联系

每对奇异向量满足 $Av_i=\sigma_iu_i$、$A^Tu_i=\sigma_iv_i$，所以

$$A^TAv_i=\sigma_i^2v_i,\qquad AA^Tu_i=\sigma_i^2u_i.$$

$A^TA$、$AA^T$ 的正特征值都是 $\sigma_1^2,\ldots,\sigma_r^2$，重复值按重数计算。剩下的特征值为零：$A^TA$ 有 $d-r$ 个，$AA^T$ 有 $m-r$ 个。

<details>
<summary>展开第 10 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 10 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-10.jpg)

</details>

## 第 11 页：命题 1 的证明提纲

将 SVD 展开并乘 $v_i$：

$$Av_i=\left(\sum_{j=1}^r\sigma_ju_jv_j^T\right)v_i
=\sum_j\sigma_ju_j\langle v_j,v_i\rangle=\sigma_iu_i.$$

正交性使 $j\ne i$ 的项全为零，$j=i$ 时内积是 1。类似得到 $A^Tu_i=\sigma_iv_i$，再分别作用 $A^T$ 或 $A$，即可得到上一页的特征向量方程。

<details>
<summary>展开第 11 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 11 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-11.jpg)

</details>

## 第 12 页：通过谱定理理解 SVD

$A^TA$ 对称且半正定，因为 $x^TA^TAx=\|Ax\|_2^2\ge0$。先求它的正特征值 $\lambda_i$ 和相应标准正交特征向量 $v_i$，再设

$$\sigma_i=\sqrt{\lambda_i},\qquad u_i=\frac{Av_i}{\sigma_i}.$$

这解释了 SVD 与上一讲谱定理的联系。数值软件可以直接计算 SVD，不需要先显式构造 $A^TA$。

<details>
<summary>展开第 12 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 12 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-12.jpg)

</details>

## 第 13 页：例 2——从 AᵀA 得到右奇异向量

$$A=\begin{pmatrix}20&10\\8&19\\-2&14\end{pmatrix},\qquad A^TA=\begin{pmatrix}468&324\\324&657\end{pmatrix}.$$

后者有标准正交特征向量 $v_1=\frac15(3,4)^T$、$v_2=\frac15(4,-3)^T$，相应特征值为 900 和 225。因此 $\sigma_1=30,\sigma_2=15$。

<details>
<summary>展开第 13 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 13 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-13.jpg)

</details>

## 第 14 页：例 2——计算左奇异向量

继续使用上页 $A,v_1,v_2$，由 $u_i=Av_i/\sigma_i$ 得

$$u_1=\frac{Av_1}{30}=\tfrac13(2,2,1)^T,\qquad u_2=\frac{Av_2}{15}=\tfrac13(2,-1,-2)^T.$$

二者范数平方都是 1，内积为 $(4-2-2)/9=0$，因此组成所需标准正交方向。

<details>
<summary>展开第 14 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 14 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-14.jpg)

</details>

## 第 15 页：例 2——完整分解和三步几何解释

$$A=\left[\tfrac13\begin{pmatrix}2&2\\2&-1\\1&-2\end{pmatrix}\right]
\begin{pmatrix}30&0\\0&15\end{pmatrix}
\left[\tfrac15\begin{pmatrix}3&4\\4&-3\end{pmatrix}\right]^T.$$

对输入 $x\in\mathbb R^2$，先由 $V_2^T$ 取得输入方向坐标，再由 $\Sigma_2$ 按奇异值缩放，最后由 $U_2$ 合成输出 $Ax\in\mathbb R^3$。每个单位方向 $v_i$ 都映射为 $\sigma_iu_i$，所以 $\sigma_i$ 是对应拉伸倍数。

<details>
<summary>展开第 15 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 15 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-15.jpg)

</details>

## 第 16 页：章节页——截断得到最佳低秩近似

接下来只保留较大的奇异值及相应方向，以减少矩阵表示的复杂度。

<details>
<summary>展开第 16 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 16 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-16.jpg)

</details>

## 第 17 页：外积、秩一与 Frobenius 范数

对非零列向量 $u\in\mathbb R^m,v\in\mathbb R^d$，外积 $uv^T=(u_iv_j)_{i,j}$ 是秩一矩阵：每列都是 $u$ 的倍数，并且至少一列非零。定义

$$\|A\|_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^da_{ij}^2}.$$

因此 $\|A-B\|_F^2$ 是逐元素误差平方的总和，后面的最优性都针对这个误差。

<details>
<summary>展开第 17 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 17 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-17.jpg)

</details>

## 第 18 页：截断 SVD

紧致 SVD 把矩阵分成 $A=\sum_{i=1}^r\sigma_iu_iv_i^T$ 这些秩一贡献。仅保留前 $k$ 项（$1\le k\le r$），得到

$$A_k=\sum_{i=1}^k\sigma_iu_iv_i^T=U_k\Sigma_kV_k^T.$$

$A_k$ 每一列都在 $\operatorname{Col}(U_k)$ 中；反过来，对 $i\le k$ 有 $A_kv_i=\sigma_iu_i$，因此保留下来的方向确实能生成相应输出子空间。

<details>
<summary>展开第 18 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 18 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-18.jpg)

</details>

## 第 19 页：Eckart–Young 定理（1936）

对任意秩至多为 $k$ 的矩阵 $B$，

$$\|A-B\|_F^2\ge\|A-A_k\|_F^2=\sum_{i=k+1}^r\sigma_i^2.$$

因此截断 SVD 是总平方误差下的最佳秩至多 $k$ 近似，最小误差等于丢弃奇异值的平方之和。$k=r$ 时完全重构。注意这里要平方奇异值，与 PCA 中直接相加协方差特征值的公式不同。

<details>
<summary>展开第 19 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 19 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-19.jpg)

</details>

## 第 20 页：例 3——最佳秩一近似

回顾例 2 的 $A,u_1,v_1$，其奇异值为 30 和 15。只保留第一项：

$$A_1=30u_1v_1^T=\begin{pmatrix}12&16\\12&16\\6&8\end{pmatrix}.$$

每列都是 $(2,2,1)^T$ 的倍数，所以该近似的秩为 1。

<details>
<summary>展开第 20 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 20 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-20.jpg)

</details>

## 第 21 页：例 3——残差和误差验证

$$A-A_1=\begin{pmatrix}8&-6\\-4&3\\-8&6\end{pmatrix}.$$

总平方误差是 $64+36+16+9+64+36=225=15^2$，等于被丢弃奇异值的平方。由定理可知，不存在总平方误差更小的秩一矩阵。

<details>
<summary>展开第 21 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 21 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-21.jpg)

</details>

## 第 22 页：存储、非唯一性和任务表现

直接存 $A$ 需要 $md$ 个数；存 $U_k$、$\Sigma_k$ 的对角线、$V_k$ 需要 $k(m+d+1)$ 个数，只有 $k$ 足够小才真正节省空间。重复奇异值可能导致多个同样好的截断近似。最优性只针对平方重构误差，不能保证机器学习任务效果最佳。

<details>
<summary>展开第 22 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 22 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-22.jpg)

</details>

## 第 23 页：章节页——推荐系统使用用户与物品因子

将矩阵低秩表示转化为一个可用于评分预测的潜在因子模型。

<details>
<summary>展开第 23 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 23 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-23.jpg)

</details>

## 第 24 页：潜在因子评分模型

设 $R\in\mathbb R^{n\times m}$ 记录 $n$ 个用户对 $m$ 个物品的评分。给用户 $i$ 分配 $p_i\in\mathbb R^k$，给物品 $j$ 分配 $q_j\in\mathbb R^k$，预测 $\widehat r_{ij}=\langle p_i,q_j\rangle$。按行堆叠后

$$P\in\mathbb R^{n\times k},\quad Q\in\mathbb R^{m\times k},\quad \widehat R=PQ^T,$$

所以预测矩阵秩至多为 $k$。当表格完整时，取 $P=U_k\Sigma_k,Q=V_k$ 就给出 $\widehat R=R_k$；此处奇异值已经吸收进用户因子，因此不再显式写加权矩阵。

<details>
<summary>展开第 24 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 24 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-24.jpg)

</details>

## 第 25 页：例 4——六用户四电影完整评分表

评分满分为 10：

$$R=\begin{pmatrix}10&8&4&2\\8&10&2&4\\9&9&3&3\\4&2&10&8\\2&4&8&10\\3&3&9&9\end{pmatrix}.$$

高斯消元得到秩为 3，三个正奇异值为 $\sigma_1=12\sqrt6,\sigma_2=6\sqrt6,\sigma_3=4$。前三个用户更喜欢前两部电影，后三个更喜欢后两部电影。

<details>
<summary>展开第 25 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 25 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-25.jpg)

</details>

## 第 26 页：例 4——一个紧致 SVD

$$U_3=\begin{pmatrix}
1/\sqrt6&1/\sqrt6&1/2\\1/\sqrt6&1/\sqrt6&-1/2\\1/\sqrt6&1/\sqrt6&0\\
1/\sqrt6&-1/\sqrt6&1/2\\1/\sqrt6&-1/\sqrt6&-1/2\\1/\sqrt6&-1/\sqrt6&0
\end{pmatrix},$$

$$\Sigma_3=\operatorname{diag}(12\sqrt6,6\sqrt6,4),\quad
V_3^T=\tfrac12\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\end{pmatrix},\quad R=U_3\Sigma_3V_3^T.$$

$U_3$ 的行表示用户，$V_3$ 的行表示电影；评分是以 $12\sqrt6,6\sqrt6,4$ 加权的内积，与例 1 一致。

<details>
<summary>展开第 26 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 26 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-26.jpg)

</details>

## 第 27 页：例 4——保留两个因子并预测

保留前两个奇异值并吸收到用户因子：

$$P=U_2\Sigma_2=\begin{pmatrix}12&6\\12&6\\12&6\\12&-6\\12&-6\\12&-6\end{pmatrix},\quad
Q=V_2=\tfrac12\begin{pmatrix}1&1\\1&1\\1&-1\\1&-1\end{pmatrix}.$$

例如用户 1 的 $p_1=(12,6)^T$，电影 1 和 3 的因子分别是 $\frac12(1,1)^T$、$\frac12(1,-1)^T$。预测评分为 $12/2+6/2=9$ 与 $12/2-6/2=3$。

<details>
<summary>展开第 27 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 27 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-27.jpg)

</details>

## 第 28 页：例 4——秩二重构和 RMSE

$$R_2=PQ^T=\begin{pmatrix}9&9&3&3\\9&9&3&3\\9&9&3&3\\3&3&9&9\\3&3&9&9\\3&3&9&9\end{pmatrix}.$$

总平方误差为 $\|R-R_2\|_F^2=4^2=16$，均方根误差 $\operatorname{RMSE}=\sqrt{16/24}\approx0.82$。主要的组别偏好保留下来，但组内较小的差别消失了。

<details>
<summary>展开第 28 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 28 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-28.jpg)

</details>

## 第 29 页：章节页——缺失评分只能在已观测位置拟合

从完整矩阵转向实际推荐问题：大部分用户与物品的组合没有评分。

<details>
<summary>展开第 29 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 29 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-29.jpg)

</details>

## 第 30 页：缺失不等于零

多数用户只评价少数物品。未记录的评分表示未知，不是零分。普通 SVD 要求矩阵每个位置都有数值，填零等于凭空发明评分。因此仍可使用潜在因子模型，但必须只用已观测的训练用户–物品对拟合。

<details>
<summary>展开第 30 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 30 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-30.jpg)

</details>

## 第 31 页：已观测评分上的目标函数

设 $\Omega$ 为观测到的训练评分位置，拟合

$$L(P,Q)=\sum_{(i,j)\in\Omega}(r_{ij}-\langle p_i,q_j\rangle)^2
+\lambda\left(\sum_{i=1}^n\|p_i\|_2^2+\sum_{j=1}^m\|q_j\|_2^2\right),\quad\lambda\ge0.$$

误差项仅包含训练评分。平方范数项是正则化惩罚：类似 SVM，拟合训练数据与保持参数范数较小之间需要权衡。

<details>
<summary>展开第 31 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 31 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-31.jpg)

</details>

## 第 32 页：超参数、正交性和最优性边界

潜在因子数 $k$ 和惩罚强度 $\lambda$ 都是超参数，要使用验证评分选择。直接拟合得到的 $P,Q$ 不要求列标准正交。只有完整评分表、$\lambda=0$ 且 $k\le\operatorname{rank}(R)$ 时，截断 SVD 才由 Eckart–Young 定理给出全局最优解。缺失值或正惩罚出现后，不能再直接引用该定理得出同一结论。正则化能抑制过拟合，但不保证预测准确。

<details>
<summary>展开第 32 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 32 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-32.jpg)

</details>

## 第 33 页：交替最小二乘 ALS

固定物品因子 $Q$ 后，每个用户的预测都关于自己的 $p_i$ 线性。对于已选 $k$ 和 $\lambda>0$：先用较小随机数初始化因子，不能全设为零；固定 $Q$，根据各用户训练评分和平方范数惩罚拟合各 $p_i$；固定 $P$，同样拟合各物品 $q_j$；交替重复，直到目标变化很小或达到迭代上限。

<details>
<summary>展开第 33 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 33 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-33.jpg)

</details>

## 第 34 页：ALS 的下降性质与冷启动

如果每个交替步骤精确最小化对应子问题，训练目标不会增加。但联合优化一般非凸，不同初始值可能得到不同解，没有全局最优保证。如果某用户或物品没有任何训练评分，模型便没有数据学习其因子，这是冷启动问题。本讲例子只评价已有训练评分的用户和物品。

<details>
<summary>展开第 34 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 34 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-34.jpg)

</details>

## 第 35 页：例 5——只观察 18 个评分

原来的 $6\times4$ 完整表秩为 3，秩二重构 RMSE 约 0.82。现在只看到

$$\begin{pmatrix}10&8&?&2\\8&?&2&4\\9&9&3&?\\?&2&10&8\\2&4&?&10\\3&?&9&9\end{pmatrix}.$$

这里有 18 个已观测评分和 6 个问号。每个问号都是未知值，例 4 的原始隐藏评分不能用于拟合，也不能用于选择超参数。

<details>
<summary>展开第 35 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 35 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-35.jpg)

</details>

## 第 36 页：例 5——验证集与随机初始化

从 18 个已观测评分中留出 $r_{12}=8,r_{43}=10$ 作验证，用其余 16 个拟合：

$$\operatorname{RMSE}_{val}=\sqrt{\frac{(8-\widehat r_{12})^2+(10-\widehat r_{43})^2}{2}}.$$

尝试 $k\in\{1,2,3\}$ 与 $\lambda\in\{0.01,0.02,0.05,0.1,0.2,0.5,1,2,5\}$。每个组合做 10 次随机初始化，保留训练目标最小的一次；再用验证 RMSE 选择 $(k,\lambda)$，不能用训练误差选超参数。这是两层不同的选择依据。

<details>
<summary>展开第 36 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 36 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-36.jpg)

</details>

## 第 37 页：例 5——验证选择和缺失评分预测

用 16 条训练、2 条验证评分选择得到 $k=2,\lambda=0.01$，验证 RMSE 约 1.22。之后在全部 18 个已观测评分上重新拟合，预测六个未知位置：

| 位置 | (1,3) | (2,2) | (3,4) | (4,1) | (5,3) | (6,2) |
|---|---:|---:|---:|---:|---:|---:|
| 预测 | -1.50 | 7.33 | 5.61 | -0.41 | 11.00 | 4.79 |
| 原始隐藏评分，仅比较 | 4 | 10 | 3 | 4 | 8 | 3 |

原始值没有参加拟合或选择。模型输出是没有区间约束的内积分数，因此能出现低于 0 或高于 10 的结果。原 PDF 本页最末一句在“so they can lie”之后被页面下边界截断；这里依据已显示的预测数值说明其含义，不假装读到了被截掉的文字。

<details>
<summary>展开第 37 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 37 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-37.jpg)

</details>

## 第 38 页：章节页——预测 MovieLens 的缺失评分

从玩具例子转到公开的真实电影评分数据集。

<details>
<summary>展开第 38 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 38 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-38.jpg)

</details>

## 第 39 页：MovieLens 100K 的数据组织

GroupLens 的 MovieLens 100K 包含 100,000 条评分、943 个用户、1,682 部电影；评分为 1 至 5 的整数，约 6.3% 用户–电影组合有记录。配套 `movielens.py` 下载并缓存数据，保存已观测三元组 $(i,j,r_{ij})$，不为未知位置填零。脚本优化前面的观测评分目标，而不是对零填充矩阵做 SVD。

课件给出的数据来源为 [GroupLens MovieLens 100K](https://grouplens.org/datasets/movielens/100k/)，背景文献为 Harper 与 Konstan（2015），《The MovieLens Datasets: History and Context》。这里复述课件列出的来源，未额外调用外部数据。

<details>
<summary>展开第 39 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 39 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-39.jpg)

</details>

## 第 40 页：训练、验证、测试流程

先分成 80,000 条训练、10,000 条验证、10,000 条测试评分，并确保每个用户和每部电影都仍有训练评分。尝试 $k\in\{5,10,15,20,25,30\}$ 与前页九个 $\lambda$，共 54 个候选组合。每次拟合使用一次可复现随机初始化和 15 轮交替扫描，按验证 RMSE 选模型。然后在训练加验证共 90,000 条评分上重新拟合，最后评估完全没有参与训练与选择的测试集。

均值基线对每个组合都预测上述 90,000 条评分的平均值，测试评分不进入这个均值。

<details>
<summary>展开第 40 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 40 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-40.jpg)

</details>

## 第 41 页：截断预测和测试 RMSE

评分应在 $[1,5]$ 中，所以对原始内积分数作截断：

$$\widehat r_{ij}^{clip}=\min\{5,\max\{1,\langle p_i,q_j\rangle\}\}.$$

对留出的测试位置集合 $T$，

$$\operatorname{RMSE}_{test}=\sqrt{\frac1{|T|}\sum_{(i,j)\in T}(r_{ij}-\widehat r_{ij}^{clip})^2}.$$

验证和测试都使用相同截断处理，但拟合时的目标函数不变。

<details>
<summary>展开第 41 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 41 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-41.jpg)

</details>

## 第 42 页：MovieLens 结果与比较限制

54 个候选组合中，验证集选中 $k=5,\lambda=5$，之后在 90,000 条评分上重拟合。结果如下：

| 指标 | RMSE |
|---|---:|
| 验证集，截断后 | 0.9153 |
| 测试集，截断后 | 0.9305 |
| 同一模型测试集，未截断 | 0.9321 |
| 均值基线测试集 | 1.1320 |

课件还提到 Fan 等人在 ICLR 2024 的自编码器方法 AEMC-NE 报告 0.8767。但它平均了 20 次随机 90/10 划分，与本实验设置不同，只提供背景，不能视作受控的直接优劣比较。

<details>
<summary>展开第 42 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 42 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-42.jpg)

</details>

## 第 43 页：从预测评分得到推荐清单

对用户 1，将所有没有评分记录的电影按原始预测分排序，展示时才截断到评分区间：

| 电影 | 展示预测评分 |
|---|---:|
| A Close Shave | 5.00 |
| Dr. Strangelove | 5.00 |
| Paths of Glory | 4.95 |
| Ran | 4.88 |
| Casablanca | 4.88 |

这些用户–电影对的真实评分未知，因此不能计算它们各自的预测误差。这里还要区分“按原始分数排序”和“展示截断分数”：都显示 5.00 并不意味着原始分数相同。

<details>
<summary>展开第 43 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 43 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-43.jpg)

</details>

## 第 44 页：本讲总结

SVD 用左右两组标准正交方向描述矩形矩阵；截断 SVD 最小化总平方重构误差，最小误差是 $\sum_{i>k}\sigma_i^2$；低维用户与物品因子通过内积预测评分；缺失评分表示未知，只能在已观测训练位置拟合。验证集负责选超参数，留出测试评分负责评价预测，而好的评分预测误差并不保证推荐质量。

<details>
<summary>展开第 44 页原始 slide，核对图表、标注和公式</summary>

![Lecture 10 第 44 页原始幻灯片](/Users/cichlidfish/COMP3670/output/lecture_notes/assets/lecture10a-44.jpg)

</details>
