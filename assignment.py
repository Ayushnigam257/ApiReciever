#importing modues
import requests
import asyncio
import json
import random
import pymongo
#creating local host server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#database name : mydatabase
#table name : data
mydb = myclient["mydatabase"]
mycol = mydb["customer"]
#initializing a queue
queue=[]

#fetchng data from queue to mongodb database
def fetch():
    while(True):
        if (len(queue) == 0):
            break
        #here pop function remove the first element and return the data in to j(local variable)
        j = json.loads(queue.pop(0))
        #taking data into database one by one
        x = mycol.insert_one(j)

#creating a async function
async def main():
    lst = ['https://www.thecocktaildb.com/api/json/v1/1/random.php','https://randomuser.me/api/']
    for i in range(20):
        #collecting info from Api using get method
        data=requests.get(random.choice(lst))
        #appending data to queue
        queue.append(data.text)
        #sleeps between 1-5 seconds randomly
        await asyncio.sleep(random.randint(1,5))


#calling asyncio function
asyncio.run(main())
fetch()
print("data entry successfully")
