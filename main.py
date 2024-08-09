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
