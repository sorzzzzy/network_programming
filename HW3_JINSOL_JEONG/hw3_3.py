user_input = 'led=on&motor=off&switch=off'
res1 = user_input.split('&')
res2 = {}

for i in res1:
    key,val =(i.split('='))
    res2[key] = val
print(res2)