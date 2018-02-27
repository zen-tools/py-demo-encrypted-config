# **py-demo-encrypted-config**

## **Description**
The purpose of this project is to illustrate how-to load encrypted config files at runtime.

## **Example**
```
$ # Generate RSA key
$ ./tools/generate_key.py -k mykey.pem -p 12345

$ # Encrypt config file
$ ./tools/encrypt_config.py -i config-dev.ini -o config-prod.ini -k mykey.pem -p 12345

$ # Test application with non encrypted config file
$ cat config-dev.ini
[main]
test = Hello, World!
$ ./app.py -c config-dev.ini
[2018-02-26 21:36:32,375] [INFO] main.test = Hello, World!

$ # Test application with encrypted config file
$ cat config-prod.ini
[main]
private_key = ./mykey.pem
test = sSXy7JVMDHOrJBgMq/V+oxSjUAaDNw4F/E5Yye3RrROAiKOxEwdlZegye/axotgntK2QV4kvE3Kp
	zJxQkCaKRVPD1qvAsuD7+/j2BVKpHPX0WnIaA2AFiLYoGom85cQK/0f83C+OccPHRpTe0t/rLoPe
	ntfPtI3hTou4Fzb7wCx2ynB2DmhlUyaEaTaVnE0XA7B4EiP/mjYzDw9TcSZWwCEmHaeQMCMuZsFj
	Kviz+9SI+yieF3IrnhZRR5k0FYS74NcAyMV+DWUA1Ht13X5EcqNqEQybqb6BDkPmWdvkumE1ax/w
	0+G0gOgq56NrztnPWS8+t+wcadG8bXr73oHuCw==
$ ./app.py -c config-prod.ini
Enter password:
[2018-02-26 21:36:51,235] [INFO] main.test = Hello, World!
```
