import operator
students={
    'dipti':{'maths':45,'eng':50,'hindi':55},
    'smriti':{'maths':50,'eng':55,'hindi':60},
    'subodh':{'maths':45,'eng':66,'hindi':87}
    }
tot={}
topper_name=''
topper_marks=0
for nam,info in students.items():
    total=0
    for sub,marks in info.items():
       total+=marks
avg=int(total/3)
students[nam]={'total':total,'average':avg}
if avg>topper_marks:
    topper_name=nam
    topper_marks=avg
print(students)
print('topper of the class:',topper_name)
print('topper marks:',topper_marks)
output:
{'dipti':{'total':150,'average':50},'smriti':{'total':165,"average':55},'subodh':{'total':198,'average':66}}
topper of the class:subodh
topper marks:66
        
