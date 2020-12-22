#関数
def say_hello(greeting):
    print(greeting)

hello=say_hello #関数say_helloをhelloに渡す．

for i in range(3):
    hello("good morning")

#確認問題 平均
def ave(n1,n2,n3):
    return (n1+n2+n3)/3

print(ave(9,4,2))