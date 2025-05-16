
#Jai shree Ram
#usinng enumm
from enum import Enum
from fastapi import FastAPI
app = FastAPI()
@app.get('/{no}')
async def random(no: int): #path operator
    if type(no) != int:
        return{'Kya enter kar rha hai bkl, number daal'}
    else:
        return{"message": 'Let\'s see if this works,', 'key':no}
#don't pass read_item(56), because it is fast api's duty to run the func when you send a request
#query parameters
#pydantic can be convereted into dictionaries--use .dict 
