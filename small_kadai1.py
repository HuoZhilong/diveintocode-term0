def Num_print():
    for i in range(1,11):

        print('現在は、{}回目の処理です。'.format(i))

        # 奇数か偶数の判定
        if(i%2 == 0):
            print('偶数です。')
        else:
            print('奇数です。')

Num_print()
