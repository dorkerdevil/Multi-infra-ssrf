# Header Abuse external/internal SSRF and AC bypass.

This is totally random - This script does quick check for the external ssrf using multiple headers , you can also abuse this to send thousands of requests against random servers in the infra either external or internal (depends) as well as AC bypasses.

Note - "I know there is plugin like this in for burp but this randomized uniq id in burp collab to avoid any issues and keep sending and hitting the target(s)".

Note - you can also use 127.0.0.1 in place of id.collab.net to check for AC bypass.

## Usage  
```bash
python3 random_ssrf.py http://target id.collab.net '/endpoint'
```

#update - added more headers to rotate in order to detect dns/http interactions .

## Authors
• [D0rkerDevil](https://twitter.com/D0rkerDevil) 

 This is for educational purposes, Authors are not responsible for any damages.
