class Password:
    def __init__(self, content=''):
        self.content = content
    
    def generate(self, length=12):
        """Generate random password containing at least 12 characters, 1 lowercase, 1 uppercase, 1 numeral e 1 special.
    
            Key arguments:
            length -- password length
        """
        import random
        if length < 12:
            length = 12       

        LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
        UPPERCASE = LOWERCASE.upper()
        NUMBERS = '0123456789'
        SPECIAL_CHARACTERS = '~!@#$%^&*()_+'
        ALL_CHARACTERS = LOWERCASE + UPPERCASE + NUMBERS + SPECIAL_CHARACTERS    

        password_list = []
        password_list.append(LOWERCASE[random.randint(0, len(LOWERCASE) - 1)])
        password_list.append(UPPERCASE[random.randint(0, len(UPPERCASE) - 1)])
        password_list.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
        password_list.append(SPECIAL_CHARACTERS[random.randint(0, len(SPECIAL_CHARACTERS) - 1)])
        for i in range(4, length):
            password_list.append(ALL_CHARACTERS[random.randint(0, len(ALL_CHARACTERS) - 1)])

        random.shuffle(password_list)
        self.content = ''.join(password_list)