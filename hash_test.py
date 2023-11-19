import hashlib

iString = b"backpack"

oString = hashlib.sha256(iString)
print(oString.hexdigest())

iString = b"Backpack"

oString = hashlib.sha256(iString)
print(oString.hexdigest())
 
 
iString = b"backpacq"

oString = hashlib.sha256(iString)
print(oString.hexdigest())
