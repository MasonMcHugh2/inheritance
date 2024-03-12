import g_PersonClass as p


def main():
    name = 'Mason'
    address = '10811 Meadow Lake Ln'
    number = '(832) 993-0440'
    cust_number = 1234
    mail_list = True

    person1 = p.Person(name,address,number)

    customer1 = p.Customer(name,address,number,cust_number,mail_list)

    print(person1.print_person())

    print()
    print()
    print()

    print(customer1.print_person())

main()