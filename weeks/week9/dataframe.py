'''
Testing Dataframes out
'''
import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)
df = pd.DataFrame([[3,4,2,5],[2,6,7,4],[2,3,7,3],[2,3,6,3]], index=['time','markers','something','what'],columns=['timecol','markerscol','somethingcol','whatcol'])
print(df)

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
'Bob': [83, 65, 85]}

# grades = pd.DataFrame(grades_dict)
# grades.index = ['Test1', 'Test2', 'Test3']
# print(grades)

print(df.loc['something'])
print(df.iloc[2])
print(df.loc[['time','something']])#when you want individuals you need a collection within the collection
print(df.loc['time':'something'])

print(df.iloc[[0,2]])
print(df.iloc[0:3])

print(df.loc[['time','something'], 'timecol':'somethingcol'])
print(df.loc['time':'something', ['timecol', 'whatcol']])

print(df.at['time','timecol'])
# print(df.iat[0,1])

print(df.describe())
print(df.T)
