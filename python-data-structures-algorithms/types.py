"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset ()
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	None

* There is no char type, you can use str with single or double quotes


* A set is a mutable data type
* A frozenset is an immutable data type
    mutable, unordered, use {}, unique elements

* tuple is an ordered and immutable collection of items. 
    -(no modifications, change values, add or remove)
    -elements within parentheses ()


"""

x1 = "Hello World"		
x2 = 20		
x3 = 20.5		
x4 = 1j	
x5 = ["apple", "banana", "cherry"]		
x6 = ("apple", "banana", "cherry")	
x7 = range(6)	
x8 = {"name" : "John", "age" : 36}	
x9 = {"apple", "banana", "cherry"}	
x10 = frozenset({"apple", "banana", "cherry"})	
x11 = True	
x12 = b"Hello"		
x14 = bytearray(5)	
x15 = memoryview(bytes(5))	
x16 = None