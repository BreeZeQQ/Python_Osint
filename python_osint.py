import osint_module
import os
import threading
import argparse


ap = argparse.ArgumentParser()
ap.add_argument( "--host", required=True,	help="Enter a hostname")
args = vars(ap.parse_args())
host=args["host"]

api='https://api.hackertarget.com'
subdomain_query=api+'/hostsearch/?q='+host
dnslookup_query=api+'/dnslookup/?q='+host
reversedns_query=api+'/reversedns/?q='+host
zonetransfer_query=api+'/zonetransfer/?q='+host
reverseip_query=api+'/hostreverseiplookup/?q='+host



threading.Thread(osint_module.dnslookup(dnslookup_query)).start()
threading.Thread(osint_module.subdomain(subdomain_query)).start()
threading.Thread(osint_module.reversedns(reversedns_query)).start()
threading.Thread(osint_module.zonetransfer(zonetransfer_query)).start()
#threading.Thread(osint_module.reverseip(reverseip_query)).start()
