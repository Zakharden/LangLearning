"""Напишите класс, который будет принимать в себя IP-адрес и маску. Если что-то из этого введено неверно
(например, 381.192.10.0 или просто строка с набором букв), то должна выводиться ошибка.
У класса должен быть метод, выводящий адрес сети по IP-адресу и маске, метод,
выводящий эту же информацию в двоичном виде, а также метод, транслирующий все хранящиеся в классе данные."""

import ipaddress

class Network:
def __init__(self, ip_network):
self.ip_network = ipaddress.ip_network(ip_network)
self.ip, self.mask = self.ip_network.with_netmask.split('/')

def print(self):
print(self.ip_network)

def print_bin(self):
print('.'.join([bin(int(x)+256)[3: ] for x in self.ip.split('.')]),
'.'.join([bin(int(x)+256)[3: ] for x in self.mask.split('.')]), sep='/')

def print_all(self):
print(f'ip: {self.ip}\nmask: {self.mask}\nnetwork: {self.ip_network}')

def __str__(self):
return f'ip: {self.ip}\nmask: {self.mask}\nnetwork: {self.ip_network}'


def check_if_ip_is_network(ip_address):
try:
ipaddress.ip_network(ip_address)
return True
except ValueError:
return False

while True:
ip, mask = input().split()
ip_with_mask = "/".join([ip, mask])
if check_if_ip_is_network(ip_with_mask):
a = Network(ip_with_mask)
a.print()
a.print_bin()
a.print_all()
else:
print('Введены некорректные значения'


