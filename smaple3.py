import webbrowser

class School():

    PRINT_FORMAT = '{}。そして、{}は{}にあり創立から{}年の学校で、生徒数は{}人です。'
    def __init__(self, name, address, number_of_students,founding_years, \
                 introduction_video_url, introduction_statement):
        self.name = name
        self.address = address
        self.number_of_students = number_of_students
        self.founding_years = founding_years
        self.introduction_video_url = introduction_video_url
        self.introduction_statement = introduction_statement


    # 学校紹介文を返却するインスタンスメソッドを定義
    def school_profile(self):
        print(self.PRINT_FORMAT.format(self.introduction_statement,self.name,
        self.address,self.founding_years,self.number_of_students))
    # 学校紹介動画ページを表示するインスタンスメソッドを定義
    def school_url(self):
        webbrowser.open(self.introduction_video_url, new=2, autoraise=True)


a_school = School("A学校", "東京都渋谷区..", 300, 100, "https://www.google.com", "A学校は自然豊かな...")
# 以下でインスタンスメソッドを呼び出そう
a_school.school_profile()
a_school.school_url()

b_school = School("B学校", "東京都新宿区..", 500, 30, "https://www.yahoo.com", "B学校は文武両立で...")
# 以下でインスタンスメソッドを呼び出そう
b_school.school_profile()
b_school.school_url()
