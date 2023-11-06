'''
Pandas testing
'''
import pandas as pd
s = pd.Series((1,2,-3,5,6))
print(s)
print(s.abs())
print(s.add_prefix("Row Index "))
print(s.add_suffix(" Index"))
print(s.add(35))


print(s.apply(lambda x: x * 2))

ns = pd.Series(1,range(4))
print(ns)
print(ns[1])
print(ns.count())

a = pd.Series([1,2,3,4,5,6,7])
print(a)
# I can use individual functions here as well
print(a.describe())

#Series cannot be sets. They can be dictionaries. and you can 
#make indexed arrays have custom row names with either an Index array option in
#the constructor of the Series or with add_prefix. add_suffix

print(a.dtype)

