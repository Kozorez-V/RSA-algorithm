def getDecryptedMessage(encryptedMessage, d, n):
    decryptedMessage = []
    for word in encryptedMessage:
        word = int(word)**d % n
        decryptedMessage.append(word)
    return decryptedMessage