import random
import time
taken1, taken0 = [], []
#dt_1 = data[data['gtl_target'] == 1]
#dt_0 = data[data['gtl_target'] == 0]
tot1, tot0 = dt_1.shape[0], dt_0.shape[0]
data_train = pd.DataFrame()
#SET false if not required
bootstrap = True

#ratio of 1 to 0: 1 is 50%, max 99
#filter p - SET p
p = 10
maxp = round(tot0/tot1) - 1
if p > maxp:
    p = maxp
elif p <= 0:
    p = tot1/tot0
else:
    pass
to_compute = round(tot1 + p*tot1)
print('Filtered p: ', p, '\nTarget-0 to be sampled ',p,'x times target-1')
print('\nTotal data to be sampled: ',to_compute, '\n')

start = time.process_time()
#while len(taken1) <= tot1 and len(taken0) <= round(p*tot1):
while len(data_train) <= to_compute:
    i, j = random.randrange(0, tot1, 1), random.randrange(0, tot0, 1)
    if len(taken1) == 0:
        data_train = pd.concat([data_train, pd.DataFrame(dt_1.iloc[i, :])])
        taken1.append(i)
    if len(taken0) == 0:
        data_train = pd.concat([data_train, pd.DataFrame(dt_0.iloc[j, :])])
        taken0.append(j)
        
    inclusion_ratio = len(taken0) / len(taken1)
    
    if bootstrap == True:
        if inclusion_ratio >= p:
            if i+20 < tot1:
                data_train = pd.concat([data_train, pd.DataFrame(dt_1.iloc[i:20+i, :])])
                taken1.append(x for x in range(i,i+20))
            else: 
                data_train = pd.concat([data_train, pd.DataFrame(dt_1.iloc[i, :])])
                taken1.append(i)
        if inclusion_ratio <= p:
            if j+20 < tot0:
                data_train = pd.concat([data_train, pd.DataFrame(dt_0.iloc[j:20+j, :])])
                taken0.append(x for x in range(j,j+20))
            else:
                data_train = pd.concat([data_train, pd.DataFrame(dt_0.iloc[j, :])])
                taken0.append(j)
    else:
        if i not in taken1 and inclusion_ratio <= p:
            data_train = pd.concat([data_train, dt_1.iloc[i:i+1, :]])
            taken1.append(i)
        if j not in taken0 and inclusion_ratio >= p:
            data_train = pd.concat([data_train, dt_0.iloc[j:j+1, :]])
            taken0.append(j)
    
    if len(data_train) == round(to_compute*0.5):
        print('\n50% completed...')
    if len(data_train) == round(to_compute*0.75):
        print('\n75% completed...')
    if len(data_train) == round(to_compute):
        print('\n100% completed...')
        
    if len(data_train) % 100 == 0:
        print('Prepared sample: ',data_train.shape)
        
  
print('\n100% completed. \nTime taken: ', time.process_time() - start)
if bootstrap == True:
    print('Data sampled using bootstrap.')
