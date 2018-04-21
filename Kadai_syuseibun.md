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