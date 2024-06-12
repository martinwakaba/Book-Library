class User:
    def __init__(self, id, name, email, phone_number):
        self._id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string. ")
        if len(value) == 0:
            raise ValueError("Name cannot be empty!!!")
        
        self.name = value
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone_number(self):
        return self._phone_number