s=input('enter any string:')
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
    print('count of all character is:',freq)
    for k,v in freq.items():
        print(k,'.',end='')
        for i in range(0,v):
            print('*',end='')
        print()
output:
enter any string:Ashish Samant
count of all character is:{'A':1,'s':2,'h':2,'i':1,'':1,'S':1,'a':2,'m':1,'n':1,'t':1}
A:*
s:**
h:**
i:*
:*
S:*
a:*
m:*
n:*
t:*
