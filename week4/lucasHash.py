from week4.test_assertion import key


arraySize = 25

def lucasHash(data: str, size:int = arraySize):
    sumDigit = 0
    for c in data:
        sumDigit = sumDigit + ord(c)
        return sumDigit % size
    
array = [None] * arraySize
myDic = {'110':'John', '151':'Tanmay', '203':'Raj'}

for k,v in myDic.items():
    array[lucasHash(k)] = v
    print(lucasHash(v) f" lucasHash(k) = {array.key}")