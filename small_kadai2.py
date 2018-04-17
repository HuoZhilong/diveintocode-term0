def show_staffs(name_list = None):

    if name_list is not None:
        if type(name_list) == str:
            print('今日出勤する人は、{}さんです'.format(name_list))
        else:
            for name in name_list:
                print ('今日出勤する人は、{}さんです'.format(name))
    else:
        print('今日出勤する人はいません。')

show_staffs()
show_staffs('一郎')
workers = ['一郎', '次郎', '三郎']
show_staffs(workers)
