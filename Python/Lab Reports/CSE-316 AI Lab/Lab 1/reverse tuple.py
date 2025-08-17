tuple1=tuple(map(int, input("Enter first tuple (space seperated): ").split()))
tuple2=tuple(map(int, input("Enter first tuple (space seperated): ").split()))
tuple1,tuple2=tuple2,tuple1 #we can swap like this in python
print("tuple1:",tuple1)
print("tuple2:",tuple2)