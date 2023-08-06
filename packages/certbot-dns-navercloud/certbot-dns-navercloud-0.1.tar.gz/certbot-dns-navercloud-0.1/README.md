# certbot-dns-navercloud
NaverCloud DNS Authenticator plugin for Certbot

Create credentials ini file
```bash
$ nano ~/certbot-creds.ini
```

Set access key and secret key
```ini
dns_navercloud_access_key = <access_key>
dns_navercloud_secret_key = <secret_key>
```
Set appropriate permissions
```bash
$ chmod 600 ~/certbot-creds.ini
```
Retrieve the certificate
```bash
$ certbot certonly \
--authenticator 'dns-navercloud' \
--dns-navercloud-credentials '~/certbot-creds.ini' \
-d '*.example.com'
```
