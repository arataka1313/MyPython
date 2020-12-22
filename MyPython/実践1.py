class Student:  #class
    #アトリビュート
    def __init__(self,name):
        self.name =name
    #メソッド   平均の計算
    def calculate_avg(self,date):
        sum=0
        
        for num in date:
            sum+=num        #要素の合計
            
        avg=sum/len(date)   #要素の合計/要素数
        return avg      #平均を返す
    #メソッド    合否判定
    def judge(self,avg):
        #60以上だったら合格,それ以外は不合格
        if(avg>=60):
            result="passed"
        else:
            result="failed"
        return result

#satoの場合
a001=Student("sato")
date= [70,60,50,90,30]  #リスト 要素5個
#avgにa001でcalculate_avg(date)にインスタンス化したものを入れる
avg=a001.calculate_avg(date)
#resultにa001でインスタンス化した判定結果を代入    
result=a001.judge(avg)

print(avg)  #平均標示
print(a001.name+" "+result) #判定標示
        