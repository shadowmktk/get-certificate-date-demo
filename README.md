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
