class Rejects:
    mylist = ['found', 'human', 'reject','<>', 'deegit.com',
              'tech.com', 'mail.net', 'talent', 'solutions']

    def returnpath(self, returnpath):
        for i in self.mylist:
            if i in str(returnpath).lower():
                return True
        return False
