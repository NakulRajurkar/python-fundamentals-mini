list1=[]
n=int(input("Enter number of crops:"))
for i in range(n):
    crop=input("Enter crop name:")
    y=float(input("ENter yield:"))
    data={
        "crop":crop,
        "yield":y
    }
    list1.append(data)
print(list1)
    
    
