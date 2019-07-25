class Contact:
    def __init__(self,name,email,mobile,add):
        self._name = name
        self._email = email
        self._mobile = mobile
        self._add = add

    def get__name(self):
        return self._name

    def set__name(self, _name) :
        self._name = _name

    def get__email(self):
        return self._email
    
    def set__email(self, _email) :
        self._email = _email

    def get__mobile(self):
        return self._mobile
    
    def set__mobile(self, _mobile) :
        self._mobile = _mobile

    def get__add(self):
        return self._add
    
    def set__add(self, _add) :
        self._add = _add

