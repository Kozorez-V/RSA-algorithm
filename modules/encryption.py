def getEncryptedMessage(message, e, n):
    encryptedMessage = []
    for letter in message:
        letter = int(letter)**e % n
        encryptedMessage.append(letter)
    return encryptedMessage
