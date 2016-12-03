from fabric.api import *
env.hosts =['162.243.128.84']
env.user = 'root'
env.password ='1234pttk'

def deploy ():
	with cd ('/srv/Todo'):
		run ('git pull')
		sudo ('supervisorctl restart todo')
		sudo ('supervisorctl status')