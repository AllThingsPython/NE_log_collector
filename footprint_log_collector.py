#! /usr/bin/env python

import ftplib,os,sys

ip_file = open(sys.argv[1], 'r')

for ip in ip_file:

        print "\n***************** Starting for {0} **********************\n".format(ip.rstrip())
        i = ip.rstrip()
        new_file = open('{0}_footprint0'.format(i), 'wb')
	try:
		ftp = ftplib.FTP()
		ftp.set_debuglevel(1)
		ftp.connect(ip.rstrip(),'21',5)
		ftp.login('root','root')
		ftp.retrlines('LIST')
		ftp.retrbinary('RETR footprint0', new_file.write)
		new_file.close()
		ftp.quit()
		print "\n***************** Finished successfully for {0} **********************\n".format(ip.rstrip())
	
	except ftplib.all_errors as e:
		print e
		os.remove('{0}_footprint0'.format(i))
		print "\n***************** Finished for {0} **********************\n".format(ip.rstrip())

ip_file.close()
