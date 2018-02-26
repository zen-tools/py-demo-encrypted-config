# **py-demo-encrypted-config**

## **Description**
The purpose of this project is to illustrate how-to load encrypted config files at runtime.

## **Example**
```
$ # Generate RSA key
$ ./tools/generate_key.py -k mykey.pem -p 12345

$ # Encrypt config file
$ ./tools/encrypt_config.py -s config-dev.ini -o config-prod.ini -k mykey.pem -p 12345

$ # Test application with non encrypted config file
$ cat config-dev.ini
[main]
test = Hello, World!
$ ./app.py -c config-dev.ini
[2018-02-26 21:36:32,375] [INFO] main.test = Hello, World!

$ # Test application with encrypted config file
$ cat config-prod.ini
[main]
private_key = -----BEGIN RSA PRIVATE KEY-----
	Proc-Type: 4,ENCRYPTED
	DEK-Info: DES-EDE3-CBC,55978926C6F361DB

	1t4F7M9zIhzbBlk6GswCj0snr7wwu7E0DWn3dIuhon3Xyx4cpjFlsxGFD9tjPo2m
	ez42s1bexWJyjI1FkG0v6J/kIY0GOBNSFrUoDrgqpGO2zoQkUbF3+ZizUL/3dTe+
	+ap7df4+Phhw3s4zUqGQoJOUFkUFE2vXqsbOjPt5sE8DU0bHJKmWvOoZYdqGdZ/m
	8GpRpSREXfM1fVkE2zrhtJjN5OOzZDBhkHFgW3kdrBY8ZZauTzQyVKLPArS2uRmP
	RgDsj4lF3/WT3p7OudWpvUiJ2VuoXtd8uXfchRNEa4CiOwP93QiruYDj4UFCeO//
	ufU/twaSz6h6UYNNtIrRq3v+ar/n0mZagIYQLqitTXxt70nirO6OS6HRADg9AJiC
	zeRCBkTTc/JlbsNgI6ZdUbNT8Wpmf8yBLDdVBayAgnphch9t0Dpbnp/qm3QCh8hV
	YFjzQe45yzoBQr8j5A0QkZ/2dey45MLtN8XS5hJS9UtO2zcd808Ga2TKMo3b/sFu
	QpCf/cEA/PRPzC8cAxtR2B5D2eRZoVFAtnZMwFBwx51K+Bb5BdMUN/mGyLeHnWuV
	S6XdScoB3intJLyX3NoWJKkzgADmCZnRzP8MOaNkZpa2XwZANma27PkAxQP7H37P
	kz6UKgezF7PMEBtJyEE0zcE4j9KWKZKoUFRb9OGTDmD0q/hlX3imMBisroWdZgil
	SCLrD0lKuDAP3wv4V1MWhOKlpsBSiWXXjJl8GFDpvHZjlsOHXP8noflll2hCgUlm
	znnKm3Ha9gkJ9L/Q/iqwLoVC1/CGAkvY6wRKtDaM/110pDmtOeWfkryljQCVHlko
	2BT3QG4ysP3MfV0apTJp+HEq7JMFaNbHyNKjSbZE5QZaYh7msWu+kCsvbNw01bJM
	yzPSoVNlV5iiC06BIgHUCaMZm0FH4av3R73jkiB6fDTuqiHtcUKENuJULpRYcohD
	mpAHIDJ02+cHBpWE+JZR3tKelX0D1bOgTT7s8uUjUE7ag2Wx/CwUsmTOIueASTVH
	vhlenNLsOAltKQJkoYpzock9Jlzy2tPvODA+xmQ5U4Px26gNteUFgtwWU3qBFlAs
	Yvs9F8LAouZUyIzPc8pzGtXXliXd2Xc4eE/prXZj/ErEwl8tGaWc6bnfH0UotJDH
	S7OocWKnEkLj0opi7Jgb/PRHNsj7zxcr2ZUzu36cw6sJSw1/irKfIAPw3/Lsx2QN
	ZbDBoX+kTcAk5WB9P++lqKq78n+bIYwLuz+iuf2zjej9pj+Lec/G9NgiyevQqADl
	nZTGNqPeBxlswpa9OWjdHrevqZzTUEXmWzGdETeoCN/S4sDcyS4z5MwyNBcPJFHJ
	f+JCOsD/WIOYaiPrMkyCwCMxyaoKmxP1d4oXiY3BjjauTTCqw+0pavguyeJIdEqv
	h4ZR//yFL+CFYeKgDrz8I+Job+1iCzZA/DkPIiXUlzlb/vaNkDTKAhY2OtYgsLcg
	butYewY1fyeE2+uZd1mZrm7IR/pyeH+8OKXLPbFS1dYNhAdPS2mrV1INFVQkI2uV
	yHT4I3noMJ+G0WuJF1OqgyYyabTuSuBgrU4+BkHxt8GpR8fk5cpV9Totqdc76y7o
	-----END RSA PRIVATE KEY-----
test = sSXy7JVMDHOrJBgMq/V+oxSjUAaDNw4F/E5Yye3RrROAiKOxEwdlZegye/axotgntK2QV4kvE3Kp
	zJxQkCaKRVPD1qvAsuD7+/j2BVKpHPX0WnIaA2AFiLYoGom85cQK/0f83C+OccPHRpTe0t/rLoPe
	ntfPtI3hTou4Fzb7wCx2ynB2DmhlUyaEaTaVnE0XA7B4EiP/mjYzDw9TcSZWwCEmHaeQMCMuZsFj
	Kviz+9SI+yieF3IrnhZRR5k0FYS74NcAyMV+DWUA1Ht13X5EcqNqEQybqb6BDkPmWdvkumE1ax/w
	0+G0gOgq56NrztnPWS8+t+wcadG8bXr73oHuCw==
(venv) zen@devel:~/Desktop/ssl-settings$ ./app.py -c config-prod.ini
Enter password:
[2018-02-26 21:36:51,235] [INFO] main.test = Hello, World!
```
