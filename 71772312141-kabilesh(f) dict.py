users={
    'Sanjay':'ceftum1250','Rahul':'Crocin100',
    'Sanket':'metrogy150','Shyam':'Miopass10',
    'Sathish':'mvpxx_9000','Srishti':'Relaxo',
    'Smriti':'newyear200','Sakhi':'Bday1711',
    'Raakhi':'jaiiosh200','Rahika':'Ultu1900'
    }
userid=input('Enter username:')
password=input('Enter password:')
for k,v in users.items():
    if k==userid and v==password:
        print('valid username and password')
        exit()
print('Invalid  username and password')
