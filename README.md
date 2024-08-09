# get-certificate-date-demo
Install requirements.
```
pip3 install pyOpenSSL
pip3 install pytz
```
Runing demo.
```
python3 main.py
```
result
```
root@Ubuntu:~/get-certificate-date-demo# cat main.py 
import ssl
from OpenSSL import crypto
from get_certificate_date import GetCertificateDate

def main():
    ###
    host = 'www.taobao.com'
    port = 443
    certificate = ssl.get_server_certificate((host, port))

    ###
    # cert_file = 'cert.crt'
    # certificate = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
    # certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, certificate)

    ###
    result = GetCertificateDate(certificate)

    ###
    print(f'证书创建时间：{result.get_begin_date()}')
    print(f'证书到期时间：{result.get_expire_date()}')
    print(f'证书是否过期：{result.has_expired()}')

if __name__ == '__main__':
    main()
root@Ubuntu:~/get-certificate-date-demo#
root@Ubuntu:~/get-certificate-date-demo# python3 main.py
证书创建时间：2024-06-19 17:06:02
证书到期时间：2025-07-21 17:06:01
证书是否过期：False
root@Ubuntu:~/get-certificate-date-demo#
```
cert file.
```
root@Ubuntu:~/get-certificate-date-demo# cat main.py 
import ssl
from OpenSSL import crypto
from get_certificate_date import GetCertificateDate

def main():
    ###
    # host = 'expired.badssl.com' # expired
    # port = 443
    # certificate = ssl.get_server_certificate((host, port))

    ###
    cert_file = '/etc/nginx/ssl/server.crt'
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
    certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, certificate)

    ###
    result = GetCertificateDate(certificate)

    ###
    print(f'证书创建时间：{result.get_begin_date()}')
    print(f'证书到期时间：{result.get_expire_date()}')
    print(f'证书是否过期：{result.has_expired()}')

if __name__ == '__main__':
    main()
root@Ubuntu:~/get-certificate-date-demo#

root@Ubuntu:~/get-certificate-date-demo# openssl x509 -noout -text -in /etc/nginx/ssl/server.crt | grep -A1 'Not Before'
            Not Before: Jul 23 03:34:51 2024 GMT
            Not After : Jul 21 03:34:51 2034 GMT
root@Ubuntu:~/get-certificate-date-demo#

root@Ubuntu:~/get-certificate-date-demo# python3 main.py
证书创建时间：2024-07-23 11:34:51
证书到期时间：2034-07-21 11:34:51
证书是否过期：False
root@Ubuntu:~/get-certificate-date-demo#
```

domain expired.
![image](https://github.com/user-attachments/assets/60e647ec-6ead-48dc-9bb4-487e03e66404)
```
root@Ubuntu:~/get-certificate-date-demo# cat main.py 
import ssl
from OpenSSL import crypto
from get_certificate_date import GetCertificateDate

def main():
    ###
    host = 'expired.badssl.com' # expired
    port = 443
    certificate = ssl.get_server_certificate((host, port))

    ###
    # cert_file = 'cert.crt'
    # certificate = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
    # certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, certificate)

    ###
    result = GetCertificateDate(certificate)

    ###
    print(f'证书创建时间：{result.get_begin_date()}')
    print(f'证书到期时间：{result.get_expire_date()}')
    print(f'证书是否过期：{result.has_expired()}')

if __name__ == '__main__':
    main()
root@Ubuntu:~/get-certificate-date-demo#

root@Ubuntu:~/get-certificate-date-demo# python3 main.py
证书创建时间：2015-04-09 08:00:00
证书到期时间：2015-04-13 07:59:59
证书是否过期：True
root@Ubuntu:~/get-certificate-date-demo#
```
