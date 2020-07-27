
import subprocess

serverInfo = {}

with open('server.txt') as fh:

  val =1
  for line in fh:
    
    host,user,port,password = line.strip().split(':')
    
    serverInfo[val] = {'host':host, 'user':user , 'port':port , 'password':password}
    val += 1
    
while True:


  for item in serverInfo:

    
    print('{} - {}'.format(item,serverInfo[item]['host']))
    
 
  selection = int(input('Select Your Host  (press 0 to quit ): '))
  
  if selection == 0:
    
    break
    
  if int(selection) in serverInfo:
  
    port = serverInfo[selection]['port']
    user = serverInfo[selection]['user']
  
    cmd = 'ssh -p {} {}@{}'.format(port,user,selection)
  
    subprocess.call(cmd,shell=True)
  else:
    print(selection)
    input('{} In valid Host'.format(selection))
