#extracting the data from json file

'''import json
file="data.json"
with open (file,"r") as json_file:
    data=json.load(json_file)
print(data)    
new=(data["names"])
for i in new:
    name=(i["firstname"])
    age=(i["age"])
    print(f"age of {name} is {age}")
    
#updating the data in jsonfile

import json
file="data.json"
def new_file(data, filename="newdatafile"):
    with open(filename,"w") as f:
        json.dump(data,f,indent=8)

with open(file,"r") as json_file:
    data=json.load(json_file) 
    new_file(data)       
'''

    
