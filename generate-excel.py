import xlsxwriter
import time
from random import randint
from random import random
from faker import Faker

def get_user():
  total_records = input('How many records would you like to generate?: ')
  users = []
  fake = Faker(['es'])
  for i in range(int(total_records)):
    users.append({
      'first_name': fake.name(),
      'last_name': fake.last_name(),
      'email': fake.email(),
      'address': fake.address(),
      'phone': str(31) + str(randint(10000000, 99999999))
    })
  return users


def generate_file(): 
  users = get_user()
  random_name = str(time.strftime("%H:%M:%S", time.localtime())).replace(':', '-', 3)
  workbook = xlsxwriter.Workbook('users-' + random_name + '.xlsx')
  worksheet = workbook.add_worksheet()
  headers = ['Nombres', 'Apellidos', 'Dirección', 'Correo', 'Celular']
  coordinates = ['A', 'B', 'C', 'D', 'E']
  # write headers
  z = 0
  for coordinate in coordinates:
    worksheet.write(coordinate + str(1) , headers[z])
    z += 1

  row = 2
  for user in users:
    worksheet.write('A' + str(row) , user['first_name'])
    worksheet.write('B' + str(row) , user['last_name'])
    worksheet.write('C' + str(row) , user['address'])
    worksheet.write('D' + str(row) , user['email'])
    worksheet.write('E' + str(row) , user['phone'])
    row += 1
    
  workbook.close()

if __name__ == '__main__':
  generate_file()