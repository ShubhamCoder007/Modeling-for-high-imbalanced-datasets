import time
best_params = []
for k in range(50, 76):
    start = time.process_time()
    print('--------------------------------\nWith cluster: ',k)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x_train)
    labels = kmeans.labels_
    
    clusters = {i:0 for i in np.unique(labels)}
    per = {i:0 for i in np.unique(labels)}
    total = {i:0 for i in np.unique(labels)}
    
    index = 0
    for i in y_train:
        total[labels[index]] = total[labels[index]] + 1
        if i == 1:
            clusters[labels[index]] = clusters[labels[index]] + 1
        index = index + 1
    
    for i in per.keys():
        per[i] = (clusters[i]/target_count) * 100
        
    support = {k:clusters[k]/total[k] if total[k] != 0 else 0 for k in total.keys()}
    
    if len(best_params) == 0:
        best_params.append({'k':k, 'support':support, 'per':per, 'total':total})
        print(best_params[-1])
        continue
    
    if max(best_params[-1]['support'].values()) < max(support.values()):
        sorted_support = {k: v for k, v in sorted(support.items(), key=lambda item: item[1])}
        best_params.append({'k':k, 'support':sorted_support, 'per':per, 'total':total})
        print(best_params[-1])
    else:
        print('Parameters rejected ')
        
    print('Time taken: ',time.process_time() - start)
        
    
    
