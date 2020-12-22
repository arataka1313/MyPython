import time

#for文  1からxまでの和の標示  
n=0
x=100000000
"""
iは0からxまで   
"""             #コメントの仕方"""

#for i in range(x):
    #endキーワードのデフォルトが改行文字\nである
#    print(i+1,end='')
#    if i+1==x:
'''
continueでもbreakでもよい
'''     #コメントの仕方'''

#        continue 
#    print("+",end='')

#print("=",end='')
start = time.time() #時間計測開始
for i in range(x+1):
    n+=i #n=n+i 

#elapsed_timeに(現在時刻-start地点の時刻)を代入する．
elapsed_time = time.time() - start 

print(n)

print("計算時間:{0}".format(elapsed_time) + "[sec]")