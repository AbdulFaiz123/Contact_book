from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:

     contact_list = []
     @classmethod
     def addContact(cls):
        name = input("enter the name:")
        email = input("enter the email")
        mobile = input("enetr mobile num:")
        add = input("enetr address")
        cls.contact_list.append(Contact(name,email,mobile,add))
        print(f"contact is added successfully with name:{name}")
     @classmethod
     def deleteContact(cls):
         name = input("enter the name to delete")
         Contact= cls.get_contact_by_name(name)
         if Contact:
             cls.contact_list.remove(Contact)
             InMemoryImpl._paint(cls.contact_list)
         else:
            print(f" Contact with name:{name} is not found")
        

     @classmethod
     def viewContact(cls):
        InMemoryImpl._paint(cls.contact_list)

     @classmethod
     def search(cls):
        if len(cls.contact_list)>0:
            name = input("enetr the name to search")
            s_list = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))

            if len(s_list)>0:
                InMemoryImpl._paint(s_list)
            else:
                print(f"ther is no found with given search")
        else:
            print(f"contact book is empty!.....you can't saerch")

     @classmethod
     def updateContact(cls):
        name = input("enetr the name to update")
        Contact = cls.get_contact_by_name(name)
        if Contact:
            print("1.name 2.email 3.mobile 4.address")
            ch = int(input("enter the new names:"))
            if ch ==1:
                print(f"old names:{Contact.get__name()}")
                name = input("enter the new name:")
                if name:
                    Contact.set__name(name)
            elif ch ==2:
                print(f"old email:{Contact.get__email()}")
                email = input("enter the new email:")
                if email:
                    Contact.set__email(email)
            elif ch ==3:
                print(f"old mobile:{Contact.get__mobile()}")
                mobile = input("enter the new mobile num:")
                if mobile:
                    Contact.set__mobile(mobile) 
            elif ch ==4:
                print(f"old add:{Contact.get__add()}")
                add = input("enter the new address:")
                if add:
                    Contact.set__add(add) 
        else:
            print(f"not found")

    

     @staticmethod
     def _paint(lst):
         if len(lst) !=0:
             table = BeautifulTable()
             table.column_headers = ["name","email","mobile","address"]
             for c in lst:
                 table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__add()])
             print(table)
         else:
             print("contact book is empty")
     @classmethod
     def get_contact_by_name(cls,name):
         if len(cls.contact_list)>0:
             contact=list(filter(lambda x:x.get__name().lower()==name.lower(),cls.contact_list))
         return contact[0] if Contact  else None