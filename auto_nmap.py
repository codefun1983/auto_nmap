import random
import os
import commands as cds

print(cds.getoutput('figlet Taiwan'))
print('Linux support only!\n')
print('using info:')
print('             host : a.b.c.d , alphabet is a range')
print('             one range input two numbers!')
print('             ex : input(1-255) , set alphabet range(1,256) \n')
print('result is saved in ip.txt!\n\n\n\n\n')
li_num = range(0,256)
proceed = raw_input('this tool is slow but automatically using nmap scan , if you want to proceed input \'yes\' :')
if proceed.lower() == 'yes':
	print(cds.getoutput('clear'))
else:
	exit(0)
previous_param = raw_input('please enter nmap previous_param: like -sP -sY :')
suffix_param = raw_input('please enter nmap suffix_param : like -p1-255 :')
first = raw_input('input first number of adress : ').split('-')
second = raw_input('input second number of adress : ').split('-')
third = raw_input('input third number of adress : ').split('-')
forth = raw_input('input forth number of adress : ').split('-')
input_params= [first,second,third,forth]
def sort_num(cc):
	f = lambda a1,a2:a1 if a1>a2 else a2
	y=f(int('%s'%cc[0]),int('%s'%cc[1]))
	if cc.index(str(y))==0:
		i = cc[0]
		cc[0]=cc[1]
		cc[1]=i
cal = 1
for param in input_params:
	if param == [''] or param == None:
		exit('param must be two numbers, 1-255')
	sort_num(param)
	param_cal = (int(param[1])-int(param[0]))+1
	cal *= param_cal

for i in range(0,2):
	if int(first[i]) not in li_num or int(first[i]) is int(0) or first[i]==['']:
		exit('your first num error, please input \"1-255\" , begin_num-end_num')
	elif int(second[i]) not in li_num:
		exit('your second num error, please input \"0-255\"')
	elif int(third[i]) not in li_num:
		exit('your third num error, please input \"0-255\"')
	elif int(forth[i]) not in li_num:
		exit('your forth num error, please input \"0-255\"')

	else:
		print(cds.getoutput('clear'))
		l_save=[]
		while len(l_save)!=cal:
			a = str(random.randint(int(first[0]),int(first[1])))
			b = str(random.randint(int(second[0]),int(second[1])))
			c = str(random.randint(int(third[0]),int(third[1])))
			d = str(random.randint(int(forth[0]),int(forth[1])))
			ip = '%s.%s.%s.%s'%(a,b,c,d)
			if ip not in l_save:
				l_save.append(ip)
				os.system('touch ip.txt')
				print('now is scanning : %s'%ip)
				check = cds.getoutput('nmap %s %s %s'%(previous_param,ip,suffix_param))
				checkip = check.find('0 hosts up')
				if checkip == -1:
					path = os.getcwd()
					location = os.path.join(path,'ip.txt')
					os.system('echo \'%s\' >> %s'%(check,location))
#					print('host is up!')
#				else:
#					print('host already down! %s'%ip)
				l_save.sort()
				print('ip saved! %s'%ip)
			else:
				print('ip already exist!')
		print('already scan :\n%s'%l_save)
		print('scan count : %s'%(len(l_save)))
		exit(0)
