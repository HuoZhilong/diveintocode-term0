WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

# 結果出力文言フォマート
HOLIDAY_STRING = '{}曜日は、お休みです。'
WORKDAY_STRING = '{}曜日は、{}時間勉強する予定です。'
SUBJECT_STRING = '{}限目 {}'

#########################################################
# メソッド名：output_schedule
# 引数:study_time_list 曜日ごとの勉強時間スケジュールデータ
# 戻り値:なし
# 機能:文章の中の指定の文字の数をカウント
# 作成日:2018/04/10
# 作成者:KAKU
#########################################################
def output_schedule(study_time_list):

    # 学習項目取得用(数学から始めるため、初期値は1)
    Subject_index = 1

    # 曜日ごとにループ
    for day in range(0,len(WEEK_LIST)):
        # 勉強時間がない場合
        if study_time_list[day] == 0:
            print(HOLIDAY_STRING.format(WEEK_LIST[day]))
        # 勉強予定がある場合
        else:
            print(WORKDAY_STRING.format(WEEK_LIST[day],study_time_list[day]))
            # 時限ごとにループ
            for time in range(1,study_time_list[day] + 1):
                print(SUBJECT_STRING.format(time,SUBJECT_LIST[Subject_index]))
                # 順に学習項目をやっていくので、1個ずつ取得
                Subject_index += 1
                # 最後の項目まで行ったら、リセット
                if (Subject_index == len(SUBJECT_LIST)):
                    # 最初に項目に戻る
                    Subject_index = 0


def main():
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()
