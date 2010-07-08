import time
import os
import ConfigParser

if not os.path.isdir('.pymatic'):
    print 'Please execute `pymatic init` before deploy'
    exit()

config = ConfigParser.RawConfigParser()
config.read('.pymatic/config')

try:

   name     = config.get('main', 'name')
   machines = config.get('main', 'machines')
   local_backup = config.get('main', 'local_backup')
   filename = '%s-%s.tar.gz' % (name, time.strftime('%Y%m%d%H%M%S'))
   
   os.system('tar --exclude %s --exclude %s -cf %s .' % (filename, local_backup, filename))
   os.system('mkdir -p %s' % local_backup)
   os.system('mv %s %s/%s' % (filename, local_backup, filename))

   for machine in machines.split(','):
      section = 'machine %s' % machine
      user = config.get(section, 'user')
      passwd = config.get(section, 'password')
      host = config.get(section, 'host')
      remote_backup = config.get(section, 'remote_backup')

      os.system('ssh %s@%s mkdir -p %s' % (user, host, remote_backup))
      os.system('scp %s/%s %s@%s:%s/%s' % (local_backup, filename, user, host, remote_backup, filename))

except ConfigParser.NoOptionError, e:

   print "Config error in .pymatic/config: " + str(e)


