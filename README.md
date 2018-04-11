# NE_log_collector

## Description

Maintaining a proactive aproach is an integral part of network maintenance. One such approach is collecting information from logs of routers, switches or any networking equipment, analyzing the data and taking corrective actions to pre-empt outages.

footprint_log_collector is a python script which collects debug logs named "footprint0" from multiple network elements of a proprietary telecomunications networking vendor.

However, the same script logic with a few changes can be applied to any other device that supports ftp.

### Usage

1. Create a file named footprint_log_collector.py, copy the contents of the script and save it your Linux machine
2. Create a file containing IP addresses of all your network elements
```
user@Machine ~/Scripts > cat IP_file 
192.9.100.138
192.9.100.140
192.9.100.137

```

3. Run the script specifying the IP address file as the first argument
4. The output will be displayed for each IP mentioned in the input file. (If any of the device is unreachable, the ftp connection will timeout and move on to the next NE)

```
user@Machine ~/Scripts > ./footprint_log_collector.py IP_file 

***************** Starting for 192.9.100.138 **********************

*resp* '220 Welcome to (V1.2) FTP server'
*cmd* 'USER root'
*resp* '331 Password required'
*cmd* 'PASS ****'
*resp* '230 User logged in'
*cmd* 'TYPE A'
*resp* '200 Type set to A, ASCII mode'
*cmd* 'PASV'
*resp* '227 Entering Passive Mode (192,9,100,138,253,90)'
*cmd* 'LIST'
*resp* '150 Opening ASCII mode data connection'
01-01-01 01:01dAM       <DIR>          .
01-01-01 01:01dAM       <DIR>          ..
04-11-18 19:55AM                    3961 footprint0
04-11-18 18:56AM                    5611 footprint2
04-11-18 19:48AM                    165886 syslog.txt
04-11-18 19:48AM                    4881 footprint1
04-11-18 16:04AM                    49886 footprint4
04-11-18 18:48AM                    17532 footprint3
04-11-18 15:47AM                    37008 footprint5
04-11-18 19:51AM                    0 pdtrc.lo0
04-11-18 01:00AM                    265484 sdh_cfgdata
04-11-18 14:40AM                    41776 footprint6
04-11-18 13:59AM                    49931 footprint7
04-10-18 21:44AM                    28080 footprint8
04-10-18 20:58AM                    2013 footprint9
04-11-18 18:49AM       <DIR>          csa
04-11-18 18:49AM       <DIR>          csb
04-11-18 19:48AM                    35644 abo.log

*resp* '226 Transfer complete'
*cmd* 'TYPE I'
*resp* '200 Type set to I, binary mode'
*cmd* 'PASV'
*resp* '227 Entering Passive Mode (192,9,100,138,205,144)'
*cmd* 'RETR footprint0'
*resp* '150 Opening BINARY mode data connection'
*resp* '226 Transfer complete'
*cmd* 'QUIT'
*resp* '221 Bye...see you later'

***************** Finished successfully for 192.9.100.138 **********************


***************** Starting for 192.9.100.140 **********************

timed out

***************** Finished for 192.9.100.140 **********************


***************** Starting for 192.9.100.137 **********************

*resp* '220 Welcome to (V1.2) FTP server'
*cmd* 'USER root'
*resp* '331 Password required'
*cmd* 'PASS ****'
*resp* '230 User logged in'
*cmd* 'TYPE A'
*resp* '200 Type set to A, ASCII mode'
*cmd* 'PASV'
*resp* '227 Entering Passive Mode (192,9,100,137,225,72)'
*cmd* 'LIST'
*resp* '150 Opening ASCII mode data connection'
01-01-01 01:01dAM       <DIR>          .
01-01-01 01:01dAM       <DIR>          ..
04-11-18 19:57AM                    5423 footprint0
04-11-18 16:10AM                    49891 footprint3
04-11-18 19:49AM                    166906 syslog.txt
04-11-18 19:32AM                    8626 footprint1
04-11-18 19:18AM                    2410 footprint2
04-11-18 14:09AM                    47118 footprint5
04-11-18 19:51AM                    0 pdtrc.lo0
04-11-18 16:09AM                    49957 footprint4
04-11-18 01:00AM                    356061 sdh_cfgdata
04-11-18 14:09AM                    49883 footprint6
04-10-18 17:51AM                    49971 footprint7
04-10-18 04:21AM                    2013 footprint8
04-11-18 19:19AM       <DIR>          csa
04-11-18 19:19AM       <DIR>          csb
04-10-18 01:00AM                    30310 footprint9
04-11-18 19:49AM                    29599 abo.log

*resp* '226 Transfer complete'
*cmd* 'TYPE I'
*resp* '200 Type set to I, binary mode'
*cmd* 'PASV'
*resp* '227 Entering Passive Mode (192,9,100,137,219,186)'
*cmd* 'RETR footprint0'
*resp* '150 Opening BINARY mode data connection'
*resp* '226 Transfer complete'
*cmd* 'QUIT'
*resp* '221 Bye...see you later'

***************** Finished successfully for 192.9.100.137 **********************

user@Machine ~/Scripts > 
 ```
