marks={'subu':{'maths':88,'Eng':60,'SSt':95},
       'Amol':{'maths':78,'Eng':68,'SSt':89},
       'raka':{'maths':56,'Eng':66,'SSt':77}}
print('marks obtained by amol in english:',marks['Amol']['Eng'])
marks['raka']['maths']='77'
print(marks)
marks=dict(sorted(marks.items()))
print(marks)
