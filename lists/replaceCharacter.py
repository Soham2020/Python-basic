a = ['1', '2', '3', '4', '5', '1', '1', '9', '15', '55']
c = '1'
d = '$'
r = [i if i==c else d for i in a]
print("New List is :: ", r)