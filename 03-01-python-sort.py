import csv,operator

def CSV_READER(str_path):
    try:
        CSV_file = open(str_path, "r", encoding="ms932", errors="", newline="" )
        if CSV_file is not None:
            print('CSVファイルの読み取りに成功しました。')
            f = csv.reader(CSV_file, delimiter=",", doublequote=True,
                            lineterminator="\r\n", quotechar='"',
                            skipinitialspace=True)
            Header = next(f)
            Row_datas = sorted(f,key=operator.itemgetter(1))
            print(' '.join(Header))
            for row in Row_datas:
                print(' '.join(row))
        else:
            print('CSVファイルが空もしくはファイルの読み取りに失敗しました。')
    except Exception as e:
        print('予期せぬエラーが発生しました。原因は' + str(e))


CSV_READER('./sample.csv')
