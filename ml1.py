from sklearn import tree
    
def MarvellousML(weight,surface):
   BallsFeatures=[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
   Name=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
   
   clf=tree.DecisionTreeClassifier()
   
   clf=clf.fit(BallsFeatures,Name)
   result=clf.predict([[weight,surface]])
   
   if result==1:
     print("your object look like Tennis ball")
   elif result==2:
     print("your object look like cricket ball")



def main():
    print("----------------marvellous infosystem -------------------")
    
    print("enter weight of object")
    weight=input()
    
    print("what is the surface  type of your objects Rough or smooth")
    surface=input()
    
    if surface.lower()=="rough":
       surface=1
    elif surface.lower()=="smooth":
         surface=0
    else:
         print("error:wrong input")
         exit()
    
    MarvellousML(weight,surface)



if __name__=="__main__":
   main();
