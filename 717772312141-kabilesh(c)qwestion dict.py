#dictionary operation
portfolio={
    'account':['SBI','IOB'],
    'shares':['HDFC','ICICI','TM','TCS'],
    'ornaments':['10gm gold','1kg silver']
    }
portfolio['MF']=['Reliance','ABSL']
print(portfolio)
portfolio['account']=['Axis','BOB']
print(portfolio)
lst=portfolio['shares']
portfolio['shares']=sorted(lst)
print(portfolio)
del(portfolio['ornaments'])
print(portfolio)
outout:
{'account': ['SBI', 'IOB'], 'shares': ['HDFC', 'ICICI', 'TM', 'TCS'], 'ornaments': ['10gm gold', '1kg silver'], 'MF': ['Reliance', 'ABSL']}
{'account': ['Axis', 'BOB'], 'shares': ['HDFC', 'ICICI', 'TM', 'TCS'], 'ornaments': ['10gm gold', '1kg silver'], 'MF': ['Reliance', 'ABSL']}
{'account': ['Axis', 'BOB'], 'shares': ['HDFC', 'ICICI', 'TCS', 'TM'], 'ornaments': ['10gm gold', '1kg silver'], 'MF': ['Reliance', 'ABSL']}
{'account': ['Axis', 'BOB'], 'shares': ['HDFC', 'ICICI', 'TCS', 'TM'], 'MF': ['Reliance', 'ABSL']}
