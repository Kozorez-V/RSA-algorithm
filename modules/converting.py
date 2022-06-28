def convertToUnicode(message):
    convertedMessage = []
    for word in message:
        word = ord(word)
        convertedMessage.append(word)
    return convertedMessage

def convertToCharachters(decryptedMessage):
    convertedMessage = []
    for number in decryptedMessage:
        number = chr(number)
        convertedMessage.append(number)
    return ''.join(convertedMessage)