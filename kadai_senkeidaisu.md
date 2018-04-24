# スカラーとは
ベクトル空間においてベクトルを乗算することができる量

# 縦ベクトル
列になっているベクトルのこと

# 横ベクトル
行になっているベクトルのこと

# ベクトルの内積
二つの点のｘとｙを相乗してプラスし、x*x+y*yのこと、結果が大きいほど、二つのベクトルの
向きが似ている

# ノルム
あるベクトルのすべての値の2乗の合計を２の平方根にしたものがノルムです。

# 単位ベクトル
$\begin{equation*}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
\end{equation*}$
のような対角線以外が0で、対角線上は全部1のベクトルのこと

# 直交
あるベクトルが自分自身の転置行列と内積すると単位ベクトルになることです。

# 固有ベクトル
あるベクトルが固有ベクトルとの乗積結果が、固有ベクトルとある定数の乗積結果が同じになるような
ベクトル

# ベクトルの概要
ベクトルとは値の羅列で、ある空間内の向きと長さを持つデータです

# 行列の積
たとえば行列A,Bがあり、(A*Bの時は、Aの列数がBの行数と同じの時しかできません。)<br>
 A = $\begin{equation*}
\begin{bmatrix}
1 & 3 \\
2 & 4 \\
\end{bmatrix}
\end{equation*}$  

B = $\begin{equation*}
\begin{bmatrix}
4 & 6\\
5 & 7 \\
\end{bmatrix}
\end{equation*}$    
A*B = $\begin{equation*}
\begin{bmatrix}
(1*4) + (3*5) & (1*6) + (3*7) \\
(2*4) + (4*5) & (2*6) + (4*7) \\
\end{bmatrix}
\end{equation*}$ 

# 行列の和
  A = $\begin{equation*}
\begin{bmatrix}
1 & 3 \\
2 & 4 \\
\end{bmatrix}
\end{equation*}$  

B = $\begin{equation*}
\begin{bmatrix}
4 & 6\\
5 & 7 \\
\end{bmatrix}
\end{equation*}$    
A+B = $\begin{equation*}
\begin{bmatrix}
1+4 & 3+6\\
2+5 & 4+7 \\
\end{bmatrix}
\end{equation*}$ 

# 正則行列
逆行列を持つ行列のことを正則行列といいます

# 逆行列
ある行列が自分の逆行列と掛け合わせると単位行列になるようなものが逆行列です

# 転置行列
行列の列を行に、行を列に転置したものが転置行列です

# 対角行列
行列の対角線以外が0の行列が対角行列といいます。

# 対称行列
転置しても、変わらない行列が対称行列です

# 直交行列
行列同士の内積が０に場合に、直交行列といいます

# 固有値分解
ある行列Aの固有値と固有行列を使って、 p-1Apの行列を求めることが固有値分解といいます。

# 行列の概要
数や記号や式などを行と列に沿って矩形状に配列したものが行列です

# 線形代数が機械学習および深層学習における役割
機械学習および深層学習ではたくさんのデータを扱うことが多いので、線形代数を使うと、
より簡単にデータを扱い、重みなどを求めやすくなるのが、線形代数の役割です

# 例題①次の固有値と固有ベクトルを求めよう
$\begin{equation*}
\begin{bmatrix}
3 & 2 & 4 \\
2 & 0 & 2 \\
4 & 2 & 3 \\
\end{bmatrix}
\end{equation*}$

$回答：$<br>
$\begin{equation*}
\begin{bmatrix}
3 & 2 & 4 \\
2 & 0 & 2 \\
4 & 2 & 3 \\
\end{bmatrix}
\end{equation*}$ = 
$\begin{equation*}
\begin{bmatrix}
3 - λ& 2 & 4 \\
2 & 0 - λ& 2 \\
4 & 2 & 3 - λ\\
\end{bmatrix}
\end{equation*}$

$よって$<br>
$-λ・(3-λ)・(3-λ) + 2*2*4 + 2*2*4 - 4*4*(-λ) - 2*2*(3-λ) - 2*2*(3-λ)$

$よって$<br>
$λ^3 - 6λ^2 -15λ - 8 = 0$

$よって$<br>
$固有値は λ = -1 , λ = 8$

$λ = -1の時$<br>

$A = \begin{equation*}
\begin{bmatrix}
4 & 2 & 4 \\
2 & 1 & 2 \\
4 & 2 & 4 \\
\end{bmatrix}
\end{equation*}$

$固有ベクトルを B = \begin{equation*}
\begin{bmatrix}
X \\
Y \\
Z \\
\end{bmatrix}
\end{equation*}とする$

$A*B = \begin{equation*}
\begin{bmatrix}
0 \\
0 \\
0 \\
\end{bmatrix}
\end{equation*}$

$よって$<br>

$2X + Y + 2Z = 0になる$

$よって$<br>

$固有値が-1の時の固有ベクトルは$
$\begin{equation*}
\begin{bmatrix}
1 \\
0 \\
1 \\
\end{bmatrix}
\end{equation*}$と$\begin{equation*}
\begin{bmatrix}
1 \\
2 \\
0 \\
\end{bmatrix}
\end{equation*}$

$λ = 8の時$<br>

$A = \begin{equation*}
\begin{bmatrix}
-5& 2 & 4 \\
2 & -8 & 2 \\
4 & 2 & -5 \\
\end{bmatrix}
\end{equation*}$

$よって下記の式が得られる$<br>

$-5X + 2Y + 4Z = 0$<br>
$2X - 8Y + 2Z = 0$<br>
$4X + 2Y - 5Z = 0$<br>

$よって$<br>

$固有値が8の時の固有ベクトルは$
$\begin{equation*}
\begin{bmatrix}
2 \\
1 \\
2 \\
\end{bmatrix}
\end{equation*}$

# 例題②行列Aを対角化せよ
$A = \begin{equation*}
\begin{bmatrix}
1 & 0 & 0 \\
1 & 2 & -3 \\
1 & 1 & -2 \\
\end{bmatrix}
\end{equation*}$

$回答:$<br>

$\begin{equation*}
\begin{bmatrix}
1 & 0 & 0 \\
1 & 2 & -3 \\
1 & 1 & -2 \\
\end{bmatrix}
\end{equation*}$ = 
$\begin{equation*}
\begin{bmatrix}
1 - λ& 0 & 0 \\
1 & 2 - λ& -3 \\
1 & 1 & -2 - λ\\
\end{bmatrix}
\end{equation*}$

$よって$<br>

$(1-λ)(2-λ)(-2-λ) + 3(1 - λ)になる$

$よって$<br>

$固有値は$<br>
$λ = -1$<br>
$λ = 1(重解)$<br>

$よって$<br>

$対角化したものは$
$\begin{equation*}
\begin{bmatrix}
-1& 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1\\
\end{bmatrix}
\end{equation*}$

# 例題③Aの固有値と固有ベクトルを求めよ。また、$B^t$ABが対角行列になるような、直交行列Bを求めよ
$A = \begin{equation*}
\begin{bmatrix}
3 & 1 & -1 \\
1 & 2 & 0 \\
-1 & 0 & 2 \\
\end{bmatrix}
\end{equation*}$

$回答：$<br>
$\begin{equation*}
\begin{bmatrix}
3 & 1 & -1 \\
1 & 2 & 0 \\
-1 & 0 & 2 \\
\end{bmatrix}
\end{equation*}$ = 
$\begin{equation*}
\begin{bmatrix}
3 - λ& 1 & -1 \\
1 & 2 - λ& 0 \\
-1 & 0 & 2 - λ\\
\end{bmatrix}
\end{equation*}$

$よって$<br>

$(3-λ)(2-λ)(2-λ) - (2 - λ) - (2 - λ)になる$

$よって$<br>

$固有値は$<br>
$λ = 1$<br>
$λ = 4$<br>
$λ = 2$<br>

$よって$<br>

$固有値が1の時の固有ベクトルは$
$\begin{equation*}
\begin{bmatrix}
1 \\
-1 \\
1 \\
\end{bmatrix}
\end{equation*}$

$固有値が4の時の固有ベクトルは$
$\begin{equation*}
\begin{bmatrix}
2 \\
1 \\
-1 \\
\end{bmatrix}
\end{equation*}$

$固有値が2の時の固有ベクトルは$
$\begin{equation*}
\begin{bmatrix}
0 \\
1 \\
1 \\
\end{bmatrix}
\end{equation*}$

$よって$<br>
$対角化が\begin{equation*}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 4 & 0 \\
0 & 0 & 2 \\
\end{bmatrix}
\end{equation*}の時$

$直交行列は$
$\begin{equation*}
\begin{bmatrix}
1 & 2 & 0 \\
-1 & 1 & 1 \\
1 & -1 & 1 \\
\end{bmatrix}
\end{equation*}$