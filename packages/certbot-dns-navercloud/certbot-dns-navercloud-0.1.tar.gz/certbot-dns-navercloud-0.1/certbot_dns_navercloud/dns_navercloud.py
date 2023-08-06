import base64
import hashlib
import hmac
import logging
import time
from urllib.parse import urlencode

import requests
from certbot import errors
from certbot.plugins import dns_common

logger = logging.getLogger(__name__)


class Authenticator(dns_common.DNSAuthenticator):
    description = 'Obtain certificates using a DNS TXT record (if you are using NaverCloud for DNS).'
    ttl = 30

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add, default_propagation_seconds=15):
        super().add_parser_arguments(add, default_propagation_seconds)
        add('credentials', help='NaverCloud credentials INI file.')

    def more_info(self):
        return 'This plugin configures a DNS TXT record to respond to a dns-01 challenge using the NaverCloud API.'

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'NaverCloud credentials INI file',
            {
                'access_key': 'Access Key for NaverCloud API',
                'secret_key': 'Secret Key for NaverCloud API'
            }
        )

    def _perform(self, domain: str, validation_name: str, validation: str):
        print(domain, validation_name, validation)
        client = self._get_navercloud_client()
        domain, validation_name = client.get_domain_and_host(domain, validation_name)
        client.add_record(domain, validation_name, validation, self.ttl)

    def _cleanup(self, domain: str, validation_name: str, validation: str):
        print(domain, validation_name, validation)

        client = self._get_navercloud_client()
        domain, validation_name = client.get_domain_and_host(domain, validation_name)
        client.remove_records(domain, validation_name, validation)

    def _get_navercloud_client(self):
        if not self.credentials:
            raise errors.Error('Plugin has not been prepared.')

        return _NaverCloudClient(
            self.credentials.conf('access_key'),
            self.credentials.conf('secret_key')
        )


class _NaverCloudClient:
    base_url = 'https://globaldns.apigw.ntruss.com/dns/v1'
    access_key = None
    secret_key = None
    domain_ids = {}

    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def request(self, method, uri, params=None, body=None):
        timestamp = str(int(time.time() * 1000))
        headers = {
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': self.access_key,
            'x-ncp-apigw-signature-v2': self.make_signature(method, uri, params, timestamp)
        }
        url = self.base_url + uri
        if method == 'GET':
            return requests.get(url, params=params, headers=headers)
        elif method == 'POST':
            return requests.post(url, params=params, json=body, headers=headers)
        elif method == 'PUT':
            return requests.put(url, params=params, json=body, headers=headers)
        elif method == 'DELETE':
            return requests.delete(url, params=params, json=body, headers=headers)

    def make_signature(self, method, uri, params, timestamp):
        uri = '/' + self.base_url.split('/', 3)[3] + uri
        if params:
            uri += '?' + urlencode(params)
        secret_key = bytes(self.secret_key, 'utf-8')
        message = bytes(f'{method} {uri}\n{timestamp}\n{self.access_key}', 'utf-8')
        return base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    def get_domain_and_host(self, domain, name):
        try:
            self.get_domain_id(domain)
            return domain, name.removesuffix('.' + domain)
        except AssertionError:
            subdomains = domain.split('.', 1)
            return self.get_domain_and_host(subdomains[1], name)

    def get_domain_id(self, domain):
        domain_id = self.domain_ids.get(domain)
        if domain_id:
            return domain_id

        params = {
            'page': 0,
            'size': 20,
            'domainName': domain
        }
        response = self.request('GET', '/ncpdns/domain', params=params)
        if response.status_code == 200:
            domain_ids = [d['id'] for d in response.json()['content'] if d['name'] == domain]
            assert len(domain_ids) == 1
            domain_id = domain_ids[0]
            self.domain_ids[domain] = domain_id
            return domain_id
        else:
            raise Exception('Failed to get domain id')

    def get_record_ids(self, domain, name, content):
        domain_id = self.get_domain_id(domain)
        params = {
            'page': 0,
            'size': 20,
            'recordType': 'TXT',
            'searchContent': name
        }
        response = self.request('GET', f'/ncpdns/record/{domain_id}', params=params)
        if response.status_code == 200:
            records = response.json()['content']
            return [
                record['id'] for record in records
                if record['host'] == name and record['content'] == f'"{content}"'
            ]
        else:
            raise Exception('Failed to get record ids')

    def add_record(self, domain, name, content, ttl):
        self.rollback(domain)
        domain_id = self.get_domain_id(domain)
        body = [
            {
                'host': name,
                'type': 'TXT',
                'content': content,
                'ttl': ttl,
                'aliasId': None,
                'lbId': None
            }
        ]
        response = self.request('POST', f'/ncpdns/record/{domain_id}', body=body)
        if response.ok:
            self.apply(domain)
        else:
            raise Exception('Failed to add record')

    def remove_records(self, domain, name, content):
        self.rollback(domain)
        domain_id = self.get_domain_id(domain)
        body = self.get_record_ids(domain, name, content)
        response = self.request('DELETE', f'/ncpdns/record/{domain_id}', body=body)
        if response.ok:
            self.apply(domain)
        else:
            raise Exception('Failed to remove records')

    def apply(self, domain):
        domain_id = self.get_domain_id(domain)
        return self.request('PUT', f'/ncpdns/record/apply/{domain_id}')

    def rollback(self, domain):
        domain_id = self.get_domain_id(domain)
        return self.request('PUT', f'/ncpdns/record/rollback/{domain_id}')
