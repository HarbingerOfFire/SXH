#SXH: SIMPLE XOR HASHING ALGORITHM

#PROCESS:
  1. Increase size by a factor of a rounded value (100 for 128, 200 for 256, and 500 for 512)
  2. Block into appropriate bit size
  3. XOR each character in each block by the next character in the respective block.
  4. XOR each block by the next.

The result is a simple hash, given in hexadecimal.
