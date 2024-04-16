import json

class EmailDataConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.cookie = ""
        self.numbers = []
        self.usernames = []
        self.messages = []
        self.attachments = []
        self.use_random_message = False
        self.random_message_length = 0

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            self.cookie = data.get('cookie', "")
            self.numbers = data.get('numbers', [])
            self.usernames = data.get('usernames', [])
            self.messages = data.get('messages', [])
            self.attachments = data.get('attachments', [])
            self.use_random_message = data.get('use_random_message', False)
            self.random_message_length = data.get('random_message_length', 0)

    def __repr__(self):
        return (f"EmailDataConfig(cookie={self.cookie}, numbers={self.numbers}, usernames={self.usernames}, "
                f"messages={self.messages}, attachments={self.attachments}, "
                f"use_random_message={self.use_random_message}, "
                f"random_message_length={self.random_message_length})")


class PayloadConfig:
    def __init__(self, pcap_file, target_ip=None, target_port=None):
        self.pcap_file = pcap_file
        self.target_ip = target_ip
        self.target_port = target_port


class TargetConfig:
    def __init__(self, ip, ports=None):
        self.ip = ip
        self.ports = ports if ports is not None else []


class LoadTestingConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.payloads = []
        self.targets = []

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            
            self.payloads = [PayloadConfig(**payload) for payload in data.get('payloads', [])]
            self.targets = [TargetConfig(**target) for target in data.get('targets', [])]


class ConfigMain:
    def __init__(self, config_file):
        self.config_file = config_file
        self.version = None
        self.description = None
        self.traffic_generator = None
        self.attack_address = None
        self.logging = None
        self.whatsapp_config = None
        self.http_config = None
        self.mail_config = None
        self.payload_config = None
        self.telegram_config = None
        self.yandex_disk_config = None

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            self.version = data.get('version')
            self.description = data.get('description')
            self.traffic_generator = data.get('traffic_generator')
            self.attack_address = data.get('attack_address')
            self.logging = data.get('logging')
            self.whatsapp_config = data.get('whatsapp_config')
            self.http_config = data.get('http_config')
            self.mail_config = data.get('mail_config')
            self.payload_config = data.get('payload_config')
            self.telegram_config = data.get('telegram_config')
            self.yandex_disk_config = data.get('yandex_disk_config')


class MailServerConfig:
    def __init__(self, imap_enable, pop3_enable, smtp_enable, imap_domainname, pop3_domainname, smtp_domainname, imap_port, pop3_port, smtp_port, users):
        self.imap_enable = imap_enable
        self.pop3_enable = pop3_enable
        self.smtp_enable = smtp_enable
        self.imap_domainname = imap_domainname
        self.pop3_domainname = pop3_domainname
        self.smtp_domainname = smtp_domainname
        self.imap_port = imap_port
        self.pop3_port = pop3_port
        self.smtp_port = smtp_port
        self.users = users

class EmailConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.servers = []
        self.subjects = []
        self.addresses = []
        self.messages = []
        self.use_random_subjects = False
        self.use_random_message = False
        self.random_message_length = 0

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            
            self.servers = [MailServerConfig(**server) for server in data.get('servers', [])]
            self.subjects = data.get('subjects', [])
            self.addresses = data.get('addresses', [])
            self.messages = data.get('messages', [])
            self.use_random_subjects = data.get('use_random_subjects', False)
            self.use_random_message = data.get('use_random_message', False)
            self.random_message_length = data.get('random_message_length', 0)


class HttpRequest:
    def __init__(self, method, url, http_version, data=None, headers=None):
        self.method = method
        self.url = url
        self.http_version = http_version
        self.data = data
        self.headers = headers

    def __repr__(self):
        return (f"HttpRequest(method={self.method}, url={self.url}, http_version={self.http_version}, "
                f"data={self.data}, headers={self.headers})")

class HttpRequestsCollection:
    def __init__(self, config_file):
        self.config_file = config_file
        self.requests = []

        self.load_requests()

    def load_requests(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            for request in data:
                http_request = HttpRequest(
                    method=request.get('method'),
                    url=request.get('url'),
                    http_version=request.get('http_version'),
                    data=request.get('data'),
                    headers=request.get('headers')
                )
                self.requests.append(http_request)


class TelegramDataConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.cookie = ""
        self.numbers = []
        self.usernames = []
        self.messages = []
        self.attachments = []
        self.use_random_message = False
        self.random_message_length = 0

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            self.cookie = data.get('cookie', "")
            self.numbers = data.get('numbers', [])
            self.usernames = data.get('usernames', [])
            self.messages = data.get('messages', [])
            self.attachments = data.get('attachments', [])
            self.use_random_message = data.get('use_random_message', False)
            self.random_message_length = data.get('random_message_length', 0)


class WhatsAppMessageConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.cookie = ""
        self.numbers = []
        self.messages = []
        self.attachments = []
        self.use_random_message = False
        self.random_message_length = 0

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            self.cookie = data.get('cookie', "")
            self.numbers = data.get('numbers', [])
            self.messages = data.get('messages', [])
            self.attachments = data.get('attachments', [])
            self.use_random_message = data.get('use_random_message', False)
            self.random_message_length = data.get('random_message_length', 0)


class YandexDiskConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.accounts = []
        self.files = []

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            self.accounts = data.get('account', [])
            self.files = data.get('files', [])

