Presented by:

Python: Hash Tables
Week 6

Adrian Gould / Sander Huijsen

ICT40518 Certificate IV in ProgrammingICT50718 Diploma of Software Development

Hash Tables
Based on arrays (in Python: list)
Fast insertion and searching
Easy to program
Disadvantages:
based on arrays (hard to expand)
full table performs inefficiently
cannot be used to store or access items in order
Hash Tables
Based on arrays (in Python: list)
Convert key values to array index values:
hash function
For example:
employee database, key: employee ID
the hash function converts the employee ID into an array index
Hash Table: example
Consider all values 0 .. 199
could convert them into the range 0 .. 9
simple solution is to use modulo (remainder after division) of the value with 10:
key = value % 10

could also use this principle for an array index:
index = number % array_size

Hash Table: example
The last calculation can be used to implement the hash function.
The array into which data is inserted using a hash function is called a hash table.
Hashing
The process of generating a number or a string for a larger message (e.g., a string, a file, etc.)
hash should be unique, but fundamentally cannot be unique.
Think about the numbers example.
There must be a balance.
The original input cannot be calculated from the hash.
Hashing
Uses:
security, digital fingerprinting, cryptography;
convert key into index for lookup (hash tables);
compiler: keyword and value;
compiler: optimizing switch statements;
cache implementation on web browsers, OS, etc., and
many others.
Hashing algorithms
For example:
Bernstein hash;
additive hash;
XOR hash;
rotating hash;
many others.
Hashing: cryptography
Types:
MD5
DES
SHA
RSA
AES
…
Hashing: inserting (double hashing)
def insert(self, key, value):

“””A very naïve example

“””

hash1 = myhash1(key)

hash2 = myhash2(key)

while table[hash1] is not None:

hash1 = (hash1 + hash2) % TABLE_SIZE

table[hash1] = value

Hashing: ways to handle collisions
Linear probing
Upon collision, just find the next empty spot in the array
Chaining
Upon collision, just append the item to the end of that location’s list / linked list / …
Hashing: deletion
Obviously uses the hashing procedure for insertion