"""自定义"""
import pickle
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print (self.name+"_"+str(self.age))
aa = Person("JGood", 2)
aa.show()

data = "123"

with open(r"d:\p.txt","wb") as f:
    pickle.dump(data,f,0)

with open(r"d:\p.txt", "rb") as f:
    print(pickle.load(f))

if __name__ == '__main__':
    pass