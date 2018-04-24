# 主成分分析とは
多次元データの情報をできるだけ損なわずに低次元データに圧縮し、
それにより、データの特徴がより可視化され、データが持つ情報を
解釈しやすくすることが主成分分析といいます。

# 主成分分析を素人に説明する
例えば、食料品のアンケートデータの分析に主成分分析は使用される。
ユーザーには、いくつかの質問（甘い、辛い、キレがある・・・など）に５段階評価など数値化できる形で答えてもらい、アナリストが分析する。
このままだと一見、データの特徴を掴みきれないが、主成分分析を使い、新たな軸を設けることで「辛さとキレが好まれている」など、より明確な傾向を見て取れるようになる。

# 主成分分析を数式で説明する
データがたくさんある時に、共分散行列を使って、データ間の偏差を求めて、
偏差の値を正方行列にする。偏差値の正方行列を固有値問題を使用して、
固有値と固有ベクトルを求める。固有値の大きさ順に主成分を決めます。

**１）準備**

下記、2次元データの主成分分析を数式を用いて説明する。

$
\vec{a_1}=
\begin{pmatrix}
a_{1x} \\
a_{1y} 
\end{pmatrix}
、
\vec{a_2}=
\begin{pmatrix}
a_{2x} \\
a_{2y} 
\end{pmatrix}
、
\vec{a_3}=
\begin{pmatrix}
a_{3x} \\
a_{3y} 
\end{pmatrix}　①　※重心が原点(０,０)となるような、データとする。
$

また①の転置は、それぞれ下記のように表される。

$
\vec{a_1}^T=
\begin{pmatrix}
a_{1x} & a_{1y} 
\end{pmatrix}
、
\vec{a_2}^T=
\begin{pmatrix}
a_{2x} & a_{2y}
\end{pmatrix}
、
\vec{a_3}^T=
\begin{pmatrix}
a_{3x} & a_{3y}
\end{pmatrix}　②
$

今後のため、①②のデータ成分の行列を下記のように定義する。

$
X\equiv
\begin{pmatrix}
\vec{a_{1}}^T \\
\vec{a_{2}}^T \\ 
\vec{a_{3}}^T
\end{pmatrix}
=
\begin{pmatrix}
a_{1x} & a_{1y} \\
a_{2x} & a_{2y} \\
a_{3x} & a_{3y}
\end{pmatrix}
、
X^T\equiv
\begin{pmatrix}
\vec{a_{1}} &  \vec{a_{2}} & \vec{a_{3}}
\end{pmatrix}
=
\begin{pmatrix}
a_{1x} & a_{2x} & a_{3x} \\
a_{1y} & a_{2y} & a_{3y}
\end{pmatrix} ③
$

よって、

$
X^TX=
\begin{pmatrix}
a_{1x} & a_{2x} & a_{3x} \\
a_{1y} & a_{2y} & a_{3y}
\end{pmatrix}
\begin{pmatrix}
a_{1x} & a_{1y} \\
a_{2x} & a_{2y} \\
a_{3x} & a_{3y}
\end{pmatrix}
=
\begin{pmatrix}
a_{1x}^2 + a_{2x}^2 + a_{3x}^2 &  a_{1x} a_{1y} + a_{2x} a_{2y} + a_{3x} a_{3y} \\
a_{1x} a_{1y} + a_{2x} a_{2y} + a_{3x} a_{3y} & a_{1y}^2 + a_{2y}^2 + a_{3y}^2
\end{pmatrix}
$

$X^TX$を**共分散行列**という。
また、$X^TX$は対称行列になっているので、$X^TX=(X^TX)^T$

ここで、さらに下記のように定義する。

$
\sum\equiv
\frac{1}{3}X^TX　(\sum=\sum^T)　④
$

**２）分散を求める**

ある方向の単位ベクトルを$\vec{e}=
\begin{pmatrix}
e_{x} \\
e_{y} 
\end{pmatrix}$と表す。  
①のデータを原点から$\vec{e}$の方向に射影して、1次元データとなった後の分散を求める。

例えば、ある１次元データ$(x_1 x_2 x_3)$に対して、平均値$\bar x$からの差の二乗和の平均から分散(var)を求めることができる。

$
var
=
\frac{(x_1-\bar{x})^2+(x_2-\bar{x})^2+(x_3-\bar{x})^2}{3}　⑤
$

また、重心が原点(０,０)となるようなデータのため、平均値は０となる。 ⑥

さらに、単位ベクトル方向へ射影した長さは単位ベクトルとの内積に等しい。 ⑦

⑤⑥⑦より、

$
var
=
\frac{(\vec{a_1}・\vec{e}-0)^2+(\vec{a_2}・\vec{e}-0)^2+(\vec{a_3}・\vec{e}-0)^2}{3}
=
\frac{(\vec{a_1}・\vec{e})^2+(\vec{a_2}・\vec{e})^2+(\vec{a_3}・\vec{e})^2}{3}
$

これを行列の積の形に分解する。

$
var
=
\frac{1}{3}
\begin{pmatrix}
\vec{a_1}・\vec{e} & \vec{a_2}・\vec{e} & \vec{a_3}・\vec{e}
\end{pmatrix}
\begin{pmatrix}
\vec{a_{1}}・\vec{e} \\
\vec{a_{2}}・\vec{e} \\ 
\vec{a_{3}}・\vec{e}
\end{pmatrix}
$

③より、

$
var
=
\frac{1}{3}
(X\vec{e})^T(X\vec{e})
=
\frac{1}{3}
\vec{e}^TX^TX\vec{e}
$

④より、

$
var
=
\vec{e}^T\sum\vec{e}　⑧
$

**３）方向を求める**

varが最大値をとるときの$\vec{e}$（主成分軸）を求める。

また、$\vec{e}$のノルム（絶対値）は1である。

このように、ある制約条件（この場合、$e_x^2 + e_y^2 - 1=0$）のもとで、関数の最大（最小）を決定する時には、**ラグランジュの未定乗数法**がよく用いられる。

**ラグランジュの未定乗数法**

変数$x,y$について、$g(x,y)=0$ の制約条件下で $f(x,y)$ という関数を最大（最小）化するのは、

$L(x,y,λ) \equiv f(x,y) - λg(x,y)$

という関数を定義したときに、

$\frac{\delta L}{\delta x}=0, \frac{\delta L}{\delta y}=0, \frac{\delta L}{\delta \lambda}=0$ 

を満たすような解 $(x,y)$ である。

ラグランジュの未定乗数法を用いると、⑧より

$
L(x,y,\lambda)
\equiv
var - \lambda(\vec{e} - 1) 
=
\vec{e}^T\sum\vec{e} - \lambda(\vec{e} - 1) 
=
\begin{pmatrix}
e_x & e_y
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
 - \lambda(e_x^2 + e_y^2 - 1) 
$

$
\frac{\delta L(e_x,e_y,\lambda)}{\delta e_x} \\
=
\begin{pmatrix}
1 & 0
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
+
\begin{pmatrix}
e_x & e_y
\end{pmatrix}
\sum
\begin{pmatrix}
1 \\
0
\end{pmatrix}
 - 
2\lambda e_x \\
=
\begin{pmatrix}
1 & 0
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
+
\bigl(
\begin{pmatrix}
e_x & e_y
\end{pmatrix}
\sum
\begin{pmatrix}
1 \\
0
\end{pmatrix}
\bigr)^T
 - 
2\lambda e_x \\
=
\begin{pmatrix}
1 & 0
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
+
\begin{pmatrix}
1 & 0
\end{pmatrix}
\sum^T
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
 - 
2\lambda e_x
$

④より、

$
=
2
\begin{pmatrix}
1 & 0
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
 - 
2\lambda e_x
$
⑨

同様に、

$
\frac{\delta L(e_x,e_y,\lambda)}{\delta e_y}
=
2
\begin{pmatrix}
0 &1
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
 - 
2\lambda e_y
$
⑩

$
\frac{\delta L(e_x,e_y,\lambda)}{\delta \lambda}
=
e_x^2 + e_y^2 - 1
$
⑪

⑨⑩⑪が０になるので、

$
\begin{pmatrix}
1 & 0
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
=
\lambda e_x
$

$
\begin{pmatrix}
0 & 1
\end{pmatrix}
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
=
\lambda e_y
$

単位行列を省略し、２つの方程式をまとめると、

$
\sum
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
=
\lambda
\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}
$

これは共分散行列Σに対する**固有値問題**を解いたことになり、固有値が$\lambda$、そのときの固有ベクトルが
$\begin{pmatrix}
e_x \\
e_y
\end{pmatrix}$
である。

また、分散値は固有値のことであり、大きい固有値のときの固有ベクトルが第1主成分軸、小さい固有値のときの固有ベクトルが第２主成分軸である

# その他
どうやって効率よくネット必要な情報を探すかを考えさせられました。
今後仕事現場も調査力というのが大切だと思うので、その力を養って
行かないといけないと感じました。
