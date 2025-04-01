
# RSA Encryption and Decryption (Interactive)

## Overview:
This Python program performs **RSA encryption and decryption** using an interactive approach. The user is prompted to input values for two prime numbers (p and q), the public exponent (e), and the message (M) to be encrypted. Based on these inputs, the program calculates the following:
- n = p * q
- φ(n) = (p - 1)(q - 1)
- The private key d by calculating the modular inverse of e modulo φ(n)
- Encrypts the message M to produce ciphertext C
- Decrypts the ciphertext C to retrieve the original message M'

The program also checks if the decrypted message M' is the same as the original message M, to verify the correctness of the encryption and decryption process.

The other file 'time.py' calculates the time it would take to test exhaustively the given passwords - it is question specific.

## Steps in the Program:
1. **User Input**: The user is asked to input the following:
   - p (first prime number)
   - q (second prime number)
   - e (public exponent)
   - M (message to be encrypted)
   
2. **RSA Calculations**:
   - **Step 1**: Compute n = p * q
   - **Step 2**: Compute φ(n) = (p - 1)(q - 1)
   - **Step 3**: Compute the private key d by finding the modular inverse of e modulo φ(n)
   - **Step 4**: Encrypt the message using the formula:  
     C = M^e mod n
   - **Step 5**: Decrypt the ciphertext using the formula:  
     M' = C^d mod n
   - **Step 6**: Check if the decrypted message M' is the same as the original message M.

3. **Output**:
   - The program displays:
     - The calculated values for n, φ(n), and d
     - The ciphertext C
     - The decrypted message M'
     - A check to verify if M' = M

## Features:
- **Interactive**: The user can input values dynamically for prime numbers p, q, the public exponent e, and the message M.
- **Modular Inverse Calculation**: The program uses the **Extended Euclidean Algorithm** to calculate the modular inverse of e modulo φ(n), which is crucial to determining the private key d.
- **Verification**: After decryption, the program checks if the decrypted message matches the original message, providing assurance that the encryption and decryption process works correctly.
"""


