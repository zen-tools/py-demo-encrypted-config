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
$ head config-dev.ini
[main]
test = Hello, World!
$ ./app.py -c config-dev.ini
[2018-02-26 21:36:32,375] [INFO] main.test = Hello, World!

$ # Test application with encrypted config file
$ head config-prod.ini
[main]
private_key = -----BEGIN RSA PRIVATE KEY-----
	Proc-Type: 4,ENCRYPTED
	DEK-Info: DES-EDE3-CBC,55978926C6F361DB

	1t4F7M9zIhzbBlk6GswCj0snr7wwu7E0DWn3dIuhon3Xyx4cpjFlsxGFD9tjPo2m
	ez42s1bexWJyjI1FkG0v6J/kIY0GOBNSFrUoDrgqpGO2zoQkUbF3+ZizUL/3dTe+
	+ap7df4+Phhw3s4zUqGQoJOUFkUFE2vXqsbOjPt5sE8DU0bHJKmWvOoZYdqGdZ/m
	8GpRpSREXfM1fVkE2zrhtJjN5OOzZDBhkHFgW3kdrBY8ZZauTzQyVKLPArS2uRmP
	RgDsj4lF3/WT3p7OudWpvUiJ2VuoXtd8uXfchRNEa4CiOwP93QiruYDj4UFCeO//
(venv) zen@devel:~/Desktop/ssl-settings$ ./app.py -c config-prod.ini
Enter password:
[2018-02-26 21:36:51,235] [INFO] main.test = Hello, World!
```
