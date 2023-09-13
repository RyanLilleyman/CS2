import info1

def main():
  my_info = info1.Information('Wassnaa', '2222 my address', 23, '444444-44')
  your_info = info1.Information('Li', '3333 your address', 20, '66666-66')
  sis_info = info1.Information ('Maia', '6666 sis address', 19, '888888-88')

  print("Display my sister information: ")
  display(sis_info)
  print()
  print("Display your information: ")
  display(your_info)
  print()
  print("Display my information: ")
  display(my_info)


def display(info):
    print('Name: ', info.get_name())
    print('address: ', info.get_address())
    print('age: ', info.get_age())
    print('phone_no: ', info.get_phone_no())



main()