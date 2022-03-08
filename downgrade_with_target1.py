import random
taken1, taken0 = [], []
tot1, tot0 = dt_1.shape[0], dt_0.shape[0]
data_train = pd.DataFrame()
bootstrap = True

#ratio of 1 to 0: 1 is 50%, max 99
#filter p
p = 1
maxp = round(tot0/tot1) - 1
if p > maxp:
    p = maxp
elif p <= 0:
    p = tot1/tot0
else:
    pass
print('Filtered percentage to take: ', p)

while len(taken1) <= tot1 and len(taken0) <= round(p*tot1):
    i, j = random.randrange(0, tot1, 1), random.randrange(0, tot0, 1)
    to_compute = tot1 + p*tot1
    if len(taken1) == 0:
        data_train = pd.concat([data_train, pd.DataFrame(dt_1.iloc[i, :]).T])
        taken1.append(i)
    if len(taken0) == 0:
        data_train = pd.concat([data_train, pd.DataFrame(dt_0.iloc[j, :]).T])
        taken0.append(j)
        
    inclusion_ratio = len(taken0) / len(taken1)
    
    if bootstrap == True:
        if inclusion_ratio >= p:
            data_train = pd.concat([data_train, pd.DataFrame(dt_1.iloc[i, :]).T])
            taken1.append(i)
        if inclusion_ratio <= p:
            data_train = pd.concat([data_train, pd.DataFrame(dt_0.iloc[j, :]).T])
            taken0.append(j)
    else:
        if i not in taken1 and inclusion_ratio <= 1:
            data_train = pd.concat([data_train, pd.DataFrame(dt_1.iloc[i, :]).T])
            taken1.append(i)
        if j not in taken0 and inclusion_ratio >= 1:
            data_train = pd.concat([data_train, pd.DataFrame(dt_0.iloc[j, :]).T])
            taken0.append(j)
    
    if to_compute/len(data_train) == 0.5:
        print('\n50% completed...')
    if to_compute/len(data_train) == 0.75:
        print('\n75% completed...')
    if to_compute/len(data_train) == 1:
        print('\n100% completed...')
        
  
print('\n100% completed...')
