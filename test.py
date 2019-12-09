import random
import string

ran = 8
letters = string.ascii_lowercase
pas = ''.join(random.choice(letters) for i in range(ran))
print(pas)