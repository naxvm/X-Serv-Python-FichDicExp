#! /usr/bin/python3.5


file = open('/etc/passwd', 'r')

maquinas = file.readlines()

usuarios = {}


for maquina in maquinas:
	login = maquina.split(':')[0]
	shell = maquina.split(':')[-1]
	usuarios[login] = shell

login = input('Introduce un login: ')

while login!= "":

	try:
		print('\nShell de',login, '>>', usuarios[login])
		login = input('Introduce un login: ')


	except KeyError:
		print('Usuario', login, 'no encontrado\n')
		break


file.close()
