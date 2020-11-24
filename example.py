import encryption

class Privnote:
    def __init__(self):
        self.ENDPOINT = 'https://privnote.com/'
        self._password = encryption.Encryption().gen_password()

    @property
    def password(self) -> None:
        return self._password.decode()

    def format_url(self, resp) -> str:
        return resp['note_link'] + '#' + self.password
        
    def encrypt(self, data: str):
        return encryption.Encryption().encrypt(data, self._password).decode()

    def format_data(self, data) -> dict:
        return {'data': data,
        'has_manual_pass': 'false',
        'duration_hours': '0',
        'dont_ask': 'false',
        'data_type': 'T',
        'notify_email': '',
        'notify_ref': ''}