# TODO решить с помощью list comprehension и ра
from pprint import pprint
list = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]
pprint(list)





