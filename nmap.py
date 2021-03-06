"""python nmap code for extraction of data(fqdn, mac address) from servers to be utilized by front end tools"""

import nmap

def get_mac(ip):
	nm = nmap.PortScanner()
	host = (ip)

	a=nm.scan(hosts=host, arguments='-sP')

	for k,v in a['scan'].iteritems():
    		if str(v['status']['state']) == 'up':
        		print str(v)
        		try:    print str(v['addresses']['ipv4']) + ' => ' + str(v['addresses']['mac'])
        		except: print str(v['addresses']['ipv4'])
get_mac(ip=<target>)
	


def get_fqdn(ip):
    	nm = nmap.PortScanner()
    	host = (ip)

    	a=nm.scan(hosts=host, arguments='-sP')

    	for k,v in a['scan'].iteritems():
        	if str(v['status']['state']) == 'up':
            		print str(v)
            		try:    print str(v['addresses']['ipv4']) + ' => ' + str(v['hostnames'][0]['name'])
            		except: print str(v['addresses']['ipv4'])
get_fqdn(ip=<target>)
