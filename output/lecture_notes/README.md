# COMP3670 讲义笔记目录与 cheatsheet 选材对账

目前共有 17 份逐页复述 Markdown。本表用于确认知识范围与选择重点，尚未制作 cheatsheet。公式栏列出核心公式及其他公式组，不重复展开具体数值例题、行政信息或每一步证明。正文及原图请进入各文件查看。

新增的 lecture 01–04 与 LA 05–08 共对应 340 个 PDF 页面，每页均附可展开原图；其余 9 份为此前已有笔记。所有文件沿用逐页中文讲解、数学公式、补充说明及原图核对的结构。

| 编号 / Markdown | 涉及知识点 | 核心公式与公式组 |
| --- | --- | --- |
| [01 · lecture01](lecture01_逐页复述.md) | 归纳与可证伪性；监督、无监督、强化学习；目标函数、假说集合、泛化；感知机与 PLA、可分时收敛。另含课程行政信息。 | $h(x)=\operatorname{sign}(w^Tx+b)$；$w\leftarrow w+y_ix_i,\ b\leftarrow b+y_i$；$E_{in}=N^{-1}\sum_i\mathbf1\{h(x_i)\ne y_i\}$；$\hat h\in\arg\min_{h\in\mathcal H}E_{in}(h)$。 |
| [02 · lecture02](lecture02_逐页复述.md) | 概率空间、事件与并集界；PMF/PDF、均匀与正态分布；期望、方差、积分、梯形与 Simpson；条件分布与条件期望；损失、Bayes 最优及不可约风险；i.i.d.、ERM、泛化间隔。 | $P(\cup_iA_i)\le\sum_iP(A_i)$；$\mathbb E[g(X)]=\sum_xg(x)p(x)$ 或 $\int g(x)f(x)dx$；$\operatorname{Var}(X)=\mathbb E[X^2]-(\mathbb EX)^2$；$p(y\mid x)=p(x,y)/p(x)$；$\eta(x)=\mathbb E[Y\mid X=x]$；平方损失最优为 $\eta$，二元分类最优为 $\mathbf1\{\eta>1/2\}$；Bayes 风险及数值积分公式。 |
| [03 · lecture03](lecture03_逐页复述.md) | Hoeffding、有限集合并集界；打散、增长函数、VC 维、Sauer、PAC、样本复杂度；逼近与估计误差；先验、模型选择、验证/CV/测试、数据泄漏。 | 固定规则尾界 $2e^{-2N\epsilon^2}$，有限集合尾界 $2M e^{-2N\epsilon^2}$；$S(\mathcal H,N)\le(N+1)^v$；VC 尾界 $8(N+1)^ve^{-N\epsilon^2/32}$；复杂度项 $\sqrt{32[v\log(N+1)+\log(8/\delta)]/N}$；$L(\hat h)-L(f^\star)=\Delta_{app}+\Delta_{est}$；验证、CV、测试误差与误差条。 |
| [04 · lecture04](lecture04_逐页复述.md) | 参数/非参数、plug-in 与 ERM；似然、MLE、逻辑回归、log-odds、交叉熵；直方图、核密度、kNN、核分类；CART、不纯度、bagging、随机森林；最小二乘、核回归、回归树。 | $\mathcal L(\theta)=\prod_ip(z_i\mid\theta)$；$\sigma(t)=(1+e^{-t})^{-1}$；$\log[p/(1-p)]=w^Tx+b$；$\ell_{CE}=-y\log p-(1-y)\log(1-p)$；$\hat\eta=\sum_iW_i\mathbf1\{Y_i=1\}$；Gini $2p(1-p)$、熵、加权不纯度下降；$RSS=\sum_i(y_i-h(x_i))^2$；$\hat h=\sum_iW_iY_i$。 |
| [05b · lecture05b](lecture05b_逐页复述.md) | 向量表示、范数和距离；质心；K-means 分配/更新、目标下降、终止、空簇与成本；凝聚层次聚类、三种 linkage、树状图。 | $\lVert x\rVert_p=(\sum_j\lvert x_j\rvert^p)^{1/p}$；$d(x,y)=\lVert x-y\rVert$；$\mu=n^{-1}\sum_ix_i$；$J=\sum_r\sum_{i\in C_r}\lVert x_i-\mu_r\rVert^2$；质心平方距离分解；single/complete/average 分别用最小、最大、平均跨簇距离。 |
| [06a · lecture06a](lecture06a_逐页复述.md) | 矩阵/张量、线性映射、乘法与复合、转置、批量变换；线性方程、行操作、高斯/Gauss–Jordan 消元；REF/RREF、主元/自由变量、解分类；逆矩阵。 | $T(sx+ty)=sT(x)+tT(y)$；$(AB)_{ij}=\sum_qa_{iq}b_{qj}$；$(AB)^T=B^TA^T$；$L(w)=n^{-1}\lVert Xw-y\rVert^2$；$Aw=b$；$A^{-1}A=AA^{-1}=I$；$[A\mid I]\to[I\mid A^{-1}]$。 |
| [06b · lecture06b](lecture06b_逐页复述.md) | 线性组合、span、子空间；列空间、零空间与方程解；线性相关/无关；基、坐标唯一、维数；秩、零度、主元列及低维表示。 | $\operatorname{Col}(A)=\{Aw\}$；$\operatorname{Nul}(A)=\{z:Az=0\}$；有解时解集 $w_0+\operatorname{Nul}(A)$；$\sum_i\alpha_iv_i=0\Rightarrow\alpha_i=0$；$x=B[x]_{\mathcal B}$；$\operatorname{rank}(A)+\operatorname{nullity}(A)=d$。 |
| [08a · lecture08a](lecture08a_逐页复述.md) | 点积、Cauchy–Schwarz、余弦相似度、正交；标准正交基、坐标、正交矩阵；Gram–Schmidt；正交投影、最近点与残差。 | $\langle x,y\rangle=x^Ty$；$\lvert x^Ty\rvert\le\lVert x\rVert\lVert y\rVert$；$\cos\theta=x^Ty/(\lVert x\rVert\lVert y\rVert)$；$Q^TQ=I$；$u_j=v_j-\sum_{i<j}(q_i^Tv_j)q_i$、$q_j=u_j/\lVert u_j\rVert$；$p=QQ^Tx$、$Q^T(x-p)=0$。 |
| [08b · lecture08b](lecture08b_逐页复述.md) | 仿射超平面、点到平面距离；函数/几何间隔、扰动鲁棒性；硬间隔、支持向量；软间隔、松弛、hinge、C、尺度；QP 与次梯度。 | $d(x,H)=\lvert w^Tx+b\rvert/\lVert w\rVert$；$m_i=y_i(w^Tx_i+b)$、$\gamma_i=m_i/\lVert w\rVert$；硬间隔 $\min\frac12\lVert w\rVert^2$ 且 $m_i\ge1$；软间隔 $\min\frac12\lVert w\rVert^2+C\sum_i\max(0,1-m_i)$；$\xi_i=\max(0,1-m_i)$；间隔宽 $2/\lVert w\rVert$；违反点集合驱动的次梯度更新。 |
| [09 · lecture09](lecture09_逐页复述.md) | 特征值、特征空间、谱定理；对称/半正定；中心化、协方差；PCA 最大方差、编码、重构、秩、解释方差、缩放、数据泄漏；二维图与英超球员案例。 | $Av=\lambda v$；$A=Q\Lambda Q^T$；$C=X_c^TX_c/n$；$\operatorname{Var}(X_cq)=q^TCq$；$Z=X_cQ_k$；$\hat x=\mu+Q_kQ_k^T(x-\mu)$；最小平均重构误差 $\sum_{j>k}\lambda_j$；$\rho_k=\sum_{j\le k}\lambda_j/\sum_j\lambda_j$；$\operatorname{rank}(X_c)\le\min(d,n-1)$。 |
| [10 · lecture10](lecture10_逐页复述.md) | 紧 SVD、左右奇异向量、与特征分解的联系；Frobenius 范数、截断 SVD、最佳低秩近似；嵌入与完整评分重构；缺失评分、正则因子模型、ALS、冷启动、MovieLens 评价。 | $A=U\Sigma V^T$；$Av_i=\sigma_iu_i$、$A^TAv_i=\sigma_i^2v_i$；$A_k=U_k\Sigma_kV_k^T$；$\lVert A-A_k\rVert_F^2=\sum_{i>k}\sigma_i^2$；$\hat R=PQ^T$；观测项平方误差加 $\lambda(\lVert P\rVert_F^2+\lVert Q\rVert_F^2)$；留出评分 RMSE。 |
| [11 · lecture11](lecture11_逐页复述.md) | 函数、极限、连续、可微；基本导数、乘积/链式法则、sigmoid；极值、二阶检验、凸性；偏导、梯度、Hessian、鞍点；MLE、最小二乘求导与唯一性。 | 基本导数表；$(g\circ f)'=g'(f)f'$；$\sigma'=\sigma(1-\sigma)$；$f(x+\Delta x)\approx f(x)+\nabla f(x)^T\Delta x$；$\nabla RSS=2X^T(X\theta-Y)$；$\nabla^2RSS=2X^TX\succeq0$；一元/带截距最小二乘解；二阶/Hessian 判别条件。 |
| [12 · lecture12](lecture12_逐页复述.md) | 凸优化与闭式解；正规方程、ridge；逻辑回归梯度；GD、步长、收敛、SGD、batch/epoch；特征变换 SVM；神经网络、激活、softmax、通用逼近、反传、初始化；Momentum、Nesterov、Adagrad、RMSProp、Adam。 | $X^TX\hat\theta=X^TY$；ridge $(X^TX+\lambda I)^{-1}X^TY$；$\nabla\ell_{CE}=(\sigma(w^Tx)-y)x$；$\theta_{t+1}=\theta_t-\alpha_tg_t$，GD 用全梯度、SGD 用小批量平均；网络层复合；$p_k=e^{z_k}/\sum_je^{z_j}$；各优化器的一/二阶动量与偏差修正公式。 |
| [LA05 · LA_lecture05](LA_lecture05_逐页复述.md) | 与 **08a** 对应的连续讲义版；点积、正交基、Gram–Schmidt、投影的证明和完整手算。 | 与 08a 共用公式：Cauchy–Schwarz、余弦、$[x]_{\mathcal Q}=Q^Tx$、$Q^{-1}=Q^T$（方形正交矩阵）、Gram–Schmidt、$p=QQ^Tx$ 与勾股分解。 |
| [LA06 · LA_lecture06](LA_lecture06_逐页复述.md) | 与 **08b** 对应的连续讲义版；距离证明、最大间隔等价性、硬/软 SVM、hinge、次梯度及收敛限制。 | 与 08b 共用距离、间隔、硬/软 SVM 公式；投影 $p=x-(w^Tx+b)w/\lVert w\rVert^2$；$w_{new}=(1-\eta)w+\eta C\sum_{i\in I}y_ix_i$、$b_{new}=b+\eta C\sum_{i\in I}y_i$。 |
| [LA07 · LA_lecture07](LA_lecture07_逐页复述.md) | 与 **09** 对应的连续讲义版；PCA、重构最优性证明更集中，另有谱定理存在性的完整可选附录；无英超球员案例。 | 与 09 共用谱分解、协方差、PCA 编码/重构、尾特征值误差、解释方差及秩公式；补充任意正交方向的保留方差上界和最佳均值偏移证明。 |
| [LA08 · LA_lecture08](LA_lecture08_逐页复述.md) | 与 **10** 对应的连续讲义版；SVD、低秩重构、推荐因子、缺失值训练、ALS、验证/测试、MovieLens；另含 NumPy SVD 用法。 | 与 10 共用 SVD、截断误差、因子目标和 RMSE；强调缩减 SVD 与紧 SVD 的区别、裁剪预测，以及完整表重构最优不等于未知评分预测保证。 |

## 选材时可以合并的主题

- 08a 与 LA05：点积、正交基、Gram–Schmidt、投影。
- 08b 与 LA06：超平面和 SVM。
- 09 与 LA07：特征分解和 PCA；09 另有球员应用，LA07 另有谱定理证明附录。
- 10 与 LA08：SVD 和推荐系统；LA08 另有 NumPy 示例。

两种来源可交叉核对，同一公式通常只需在最终 cheatsheet 出现一次。01 的感知机与 08b 的 SVM 对零分分类约定不同，最终选材时应保留各自条件。02 的损失/目标与 04 的模型、11 的求导与 12 的优化也有衔接，合并时应避免重复占用版面。

## 等待确认的事项

请指定各主题的重点、是否保留证明或手算模板，以及 cheatsheet 的纸张尺寸、页数、单/双面、语言和允许的考试格式。收到选择后再开始编写 cheatsheet；本目录不是最终 cheatsheet。
