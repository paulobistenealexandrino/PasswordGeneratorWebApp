class Password:
    def __init__(self, length=0, has_lowercase=True, has_uppercase=True, has_numbers=True, has_special=True, content=''):
        MINIMAL_LENGTH = 12
        if length < MINIMAL_LENGTH:
            length = MINIMAL_LENGTH
        self.length = length
        self.has_lowercase = has_lowercase
        self.has_uppercase = has_uppercase
        self.has_numbers = has_numbers
        self.has_special = has_special
        self.content = content
    
    def generate(self):
        """Generate random password containing at least 12 characters, 1 lowercase, 1 uppercase, 1 numeral e 1 special.
    
            Key arguments:
            length -- password length
        """
        LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
        UPPERCASE = LOWERCASE.upper()
        NUMBERS = '0123456789'
        SPECIAL_CHARACTERS = '~!@#$%^&*()_+'
        all_characters = ''    

        password_list = []
        import random
        if self.has_lowercase:
            password_list.append(LOWERCASE[random.randint(0, len(LOWERCASE) - 1)])
            all_characters += LOWERCASE
        if self.has_uppercase:
            password_list.append(UPPERCASE[random.randint(0, len(UPPERCASE) - 1)])
            all_characters += UPPERCASE
        if self.has_numbers:
            password_list.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
            all_characters += NUMBERS
        if self.has_special:
            password_list.append(SPECIAL_CHARACTERS[random.randint(0, len(SPECIAL_CHARACTERS) - 1)])
            all_characters += SPECIAL_CHARACTERS
        for i in range(len(password_list), self.length):
            password_list.append(all_characters[random.randint(0, len(all_characters) - 1)])
        random.shuffle(password_list)

        self.content = ''.join(password_list)