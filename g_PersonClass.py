class Person:
    def __init__(self,name,address,number):
        self.__name = name
        self.__address = address
        self.__num = number

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_number(self):
        return self.__num

    def print_person(self):
        print('Name: ', self.__name)
        print('Addr: ', self.__address)
        print('Phone: ', self.__num)
    

class Customer(Person):
    def __init__(self,name,address,number,cust_number,mail_list):
        Person.__init__(self,name,address,number)

        self.__number = cust_number
        self.__list = mail_list

    def print_person(self):
        Person.print_person(self)
        
        print('Customer Number: ', self.__number)

        if self.__list:
            print('On list')
        else:
            print('Not on list')