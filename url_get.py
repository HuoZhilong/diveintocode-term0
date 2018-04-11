import requests

# リンク検索用の前後文字列
Search_word = 'href="'
Search_word_end = '"'

# スクレイピングしたリンクリスト
already_url_list = []

###################################################
# メソッド名：get_link
# 引数:url_list スクレイピング対象のurlリスト
# 戻り値:Get_Url スクレイピングしたリンクのリスト
# 機能:対象ページからリンクをすべて取得
# 作成日:2018/04/11
# 作成者:KAKU
###################################################
def get_link(url_list):

    Get_Url = []

    # 対象URLリストの最後の要素取得
    url = url_list.pop()

    # htmlソース取得
    page = requests.get(url)

    # 該当ページがすでにスクレイピングした場合は空の結果を返す
    if url not in already_url_list:
        already_url_list.append(url)
    else:
        return Get_Url

    # 検索位置リセット
    End_Position = 0
    Start_Position = 0

    # hrefが見つからないまでループ
    while page.text.find('href="',End_Position) != -1:
            # 「href="」を検索し、ヒットした位置 + 「href="」の文字数で開始位置を確定
            Start_Position = page.text.find(Search_word,End_Position) + len(Search_word)
            # 開始位置以降から「"」を検索し、ヒットした位置を終了位置とする
            End_Position = page.text.find(Search_word_end,Start_Position)
            # 開始位置と終了位置を使用してリンク内容を取得
            Get_Url.append(page.text[Start_Position:End_Position])

    # 取得したすべてのリンクを返す
    return Get_Url

###################################################
# メソッド名：Join_Url
# 引数:url_list スクレイピング対象のurlリスト
#      get_url スクレイピングしたリンクのリスト
# 戻り値:なし
# 機能:スクレイピングしたリンクを検索対象に入れ、すでにあるものを除く
# 作成日:2018/04/11
# 作成者:KAKU
###################################################
def Join_Url(url_list,get_url):
    # 取得したリンクリストにデータがある場合
    if len(get_url) > 0:
        # リンクごとにループ
        for url in get_url:
            # 重複したものでなければ
            if url not in url_list:
                # スクレイピング対象に加える
                url_list.append(url)


# 親URL設定
url_list = ['https://diveintocode-crawling-sample.herokuapp.com/']

# スクレイピング対象がなくなるまでループ
while len(url_list) != 0:
    Join_Url(url_list,get_link(url_list))

print(already_url_list)
