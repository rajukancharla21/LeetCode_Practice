from collections import defaultdict
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        r=defaultdict(dict)
        maxP=0
        for i in zip(creators,ids,views):
            print(i)
            if i[0] not in r:
                r[i[0]]={
                    'popularty':i[2],
                    'id':i[1],
                    'maxV':i[2]
                }
            else:
                r[i[0]]['popularty']+=i[2]
                if i[2] > r[i[0]]['maxV']:
                    r[i[0]]['id'] = i[1]
                    r[i[0]]['maxV']=i[2]
                elif i[2] >= r[i[0]]['maxV'] and r[i[0]]['id'] > i[1]:
                    r[i[0]]['id'] = i[1]
            
            maxP=max(maxP,r[i[0]]['popularty'])
        # print(r)
        res=[]
        for k,v in r.items():
            if v['popularty']==maxP:
                res.append([k,v['id']])
        return res
                    
                
        