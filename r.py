import numpy as np

def a():
    # 20 ye 20 lik içi 0 larla dolu bir matris oluituruyoruz.
    # dolu olmasını istediğim kısımları 1 yaptım ki ekrana rahat basabileyim.
    a = np.zeros((20,20))

    # sol dolu kısım
    for i in range(0,10):
        for j in range(0,7):
            if j==0:
                a[i][j]='1'
            if j <7 and i == 0:
                 a[i][j]='1'
    j =7
    for i in range(0,2):
            a[i][j]='1'
            j+=1
    j=9
    for i in range(2,5):
            a[i][j]='1'
            j-=1
    i=4
    for j in range(5,0,-1):
        a[i][j]='1'
    j=0
    for i in range(5,10):
        a[i][j]='1'
        j+=2




    # ekrana basıyoruz.
    for i in range(0,19):
        for j in range(20):
            if a[i][j]==1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')

a()
