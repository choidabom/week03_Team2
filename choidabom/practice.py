from collections import defaultdict
name_list = [('kim', 'yuna'), ('kang', 'hodong'), ('park', 'jisung'), ('kim', 'yujin'), ('park', 'chanho')]
ndict = defaultdict(list)
for k, v in name_list: # 리스트의 요소가 튜플이기 때문에 k, v 값으로 할당
    ndict[k].append(v)  # 값이 리스트이기 때문에 append()를 이용해서 항목추가
print(ndict)