from modules import generatingPublicKey, generatingPrivateKey, encryption, decryption, source, converting

# get data

file = source.openFile()

# show original message

originalMessage = source.readMessage(file)
print("Original message:", originalMessage)

convertedMessage = converting.convertToUnicode(originalMessage)

# generating public key

p = generatingPublicKey.getFirstPrime()
q = generatingPublicKey.getSecondPrime(p)

print("p:", p, "\nq:", q)

n = generatingPublicKey.multiplication(p, q)

print("n:", n)

phi = generatingPublicKey.EulerFunction(p, q)
print("Phi:", phi)

e = generatingPublicKey.exponent(phi)
print("e:", e)

# generating private key

d = generatingPrivateKey.calculateD(phi, e)

print("d:", d)

# encryption

encryptedMessage = encryption.getEncryptedMessage(convertedMessage, e, n)
print("Encrypted message:", encryptedMessage)

# decryption

decryptedMessage = decryption.getDecryptedMessage(encryptedMessage, d, n)
print("Decrypted message:", decryptedMessage)

receivedMessage = converting.convertToCharachters(decryptedMessage)
print("Received message:", receivedMessage)