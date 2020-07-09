# naptr2ip
This script returns the IPv4 address of a SIP Registrar with the lowest prio, by performing a DNS NAPTR and DNS SRV query.
It helps you if the SIP server software does not support NAPTR queries.
The output of this script can be used as /etc/hosts entry and can be updated regularly with a CRON job for example.
So you can enter the registration address into the configuration of the SIP server and still get a matching IP

## Prerequisite:

- Python3
- pip3
  - $ sudo apt install python3-pip
- dnspython Library
  - $ pip3 install git+https://github.com/rthalley/dnspython.git
 
  
## Example:
    naptr2ip reg.sip-trunk.telekom.de
    
 
  
