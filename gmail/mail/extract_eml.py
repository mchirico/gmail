def cleanBinaryEmail(data):
    email = data[2:-1].replace('\\r\\n', '\n').replace('\\\\', '\\')
    return email
