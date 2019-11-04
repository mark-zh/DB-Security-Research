import MySQLdb
	 	
def coon(host):
	username = 'root'
	password = 'pass'
	port = '3306'
	try:
		result = MySQLdb.connect(host,username,password)
	except Exception as e:
		if e[0] ==1045 :
			print 'success',host
		if e[0] == 1130:
			print 'failed'
		else:
			pass

def main():
	with open('','r') as hosts:
		h = hosts.readlines()
		for host in h:
			host = host.strip('\n')
			coon(host)	

if __name__ == '__main__':
	main()