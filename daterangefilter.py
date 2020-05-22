import os
import json

g = open('filteredlog.txt', 'w')
for filename in os.listdir('.'):
    if 'cdlog' in filename:
        f = open(str(filename), 'r')
        for row in f:
            rowdata = json.loads(row)
            payload =  json.loads(rowdata['payload'])
            datetime = payload['received']
            datetime2 = datetime.replace('-','')
            datetime3 = datetime2.replace('T','')
            datetime4 = datetime3.replace(':','')
            date = datetime4[0:8]
            if 20190101 <= int(date) <= 20190102:
                g.write(json.dumps(rowdata)+'\n')
        f.close()
g.close()
print '\nQuery completed'