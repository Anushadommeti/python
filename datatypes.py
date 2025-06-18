#numeric data type
#integer
a=5
print(type(a))
print(id(a))
print(a)

#float
a=1.35
print(id(a))
print(type(a))
print(a)

#complex
a=1+7j
print(id(a))
print(type(a))
print(a)

#text data type
#string
a="hello"
print(type(a))
print(id(a))
print(a[1])
print(a)

#sequence data type
#list
a=[1,4,5,6,7]
print(type(a))
print(id(a))
print(a[1])
print(a)

#tuple
a=(1,4,6,8,9)
print(id(a))
print(type(a))
print(a[3])
print(a)

#boolean data type 
#bool
a=True
print(id(a))
print(type(a))
print(a)

b=False
print(id(b))
print(type(b))
print(b)

#mapping data type
#dictionary
a={"nmae":"anusha","age":"21","city":"hyd"}
print(type(a))
print(id(a))
print(a)

#set data type
#set
a={1,4,6,7,2,3,8}
print(type(a))
print(id(a))
a.add(10)
a.remove(2)
print(a)

#frozen set
a=frozenset({1,4,6,8})
print(type(a))
print(id(a))
print(a)
