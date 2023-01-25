import pickle
from hashlib import sha256

f = open('login.bin', 'wb')
data = sha256(input('enter the root password : ').encode()).hexdigest()
pickle.dump(data, f)
f.close()

f = open("data.csv", "w")
f.close()
