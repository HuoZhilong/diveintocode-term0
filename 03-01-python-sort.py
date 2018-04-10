import csv,operator

#################################
# メソッド名:CSV_READER
# 引数:path CSVファイルパス(str)
# 戻り値:なし
# 機能:CSVファイル読み込み、郵便番号を昇順にソートする
# 作成日:2018/04/10
# 作成者:KAKU
################################
def CSV_READER(path):
    try:
        CSV_file = open(path, "r", encoding="ms932", errors="", newline="" )
        # 正常にオーブンした場合
        if CSV_file is not None:
            print('CSVファイルの読み取りが成功しました。')
            f = csv.reader(CSV_file, delimiter=",", doublequote=True,
                            lineterminator="\r\n", quotechar='"',
                            skipinitialspace=True)
            # 1行目のヘッダーを取得
            Header = next(f)
            # 郵便番号を昇順にソートする
            Row_datas = sorted(f,key=operator.itemgetter(1))
            # ヘッダー出力
            print(' '.join(Header))
            # データ出力
            for row in Row_datas:
                print(' '.join(row))
        # 正常にオーブンできなかった場合
        else:
            print('CSVファイルの読み取りが失敗しました。。')
    except Exception as e:
        print('予期せぬエラーが発生しました。原因は' + str(e))


CSV_READER('./sample.csv')
