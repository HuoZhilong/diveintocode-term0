# 在籍データ
course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}

# 結果出力用文言フォマート
BOTH_EXIST_STRING = '{}に{}は在籍しています。'
ONE_EXIST_STRING = '{}に{}のみ在籍しています。'
BOTH_NOT_EXIST_STRING = '{}に{}は在籍していません。'

##########################################################################
# メソッド名：find_person
# 引数:want_to_find_person 探したい人の配列
# 戻り値: なし
# 機能:在籍データに探したい人がいるかどうかにより、結果文言出力
# 作成日:2018/04/10
# 作成者:KAKU
##########################################################################
def find_person(want_to_find_person):
    #在籍データのコース種類でループ
    for key in course_dict.keys():
        # 両方在籍の場合
        if(want_to_find_person <= course_dict[key]) == True:
            print(BOTH_EXIST_STRING.format(key,want_to_find_person))
        # 片方しか在籍していない場合
        elif(len(want_to_find_person & course_dict[key]) > 0):
            print(ONE_EXIST_STRING.format(key,(want_to_find_person & course_dict[key])))
        # 両方在籍していない場合
        else:
            print(BOTH_NOT_EXIST_STRING.format(key,want_to_find_person))



def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
