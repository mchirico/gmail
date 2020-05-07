class Rejects:
    mylist = ['found', 'human', 'reject', '<>', 'deegit.com',
              'tech.com', 'mail.net', 'talent', 'solutions',
              'apolisrises.com', 'sparkpost.com', 'beyond.com', 'patel',
              'solutions.com', 'smtp.com', 'kumar', 'salesforce.com',
              'providers.com','spectrum.com','kodus.com']

    def returnpath(self, returnpath):
        for i in self.mylist:
            if i in str(returnpath).lower():
                return True
        return False
