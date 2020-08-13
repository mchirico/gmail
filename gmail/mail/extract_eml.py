def extract(data, eml_file='junk.eml'):
    email = data[2:-1].replace('\\r\\n', '\n').replace('\\\\', '\\')
    f = open(eml_file, 'w')
    f.write(email)
    f.close()
    return email
