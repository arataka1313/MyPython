#class

class Student:
    
    def __init__(self,name): #初期化メソッド
        self.name=name
        
    
    #selfはインスタンス自身を示すもの．
    def ave(self,math,english):  
        print((math+english)/2)



#アトリビュート: クラス内に定義された変数   javaでいうフィールド
a001=Student("taka")  #インスタンス化
print(a001.name)

a002=Student("ayu")
print(a002.name)

