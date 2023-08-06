import everapi


class Client(everapi.Client):
    def __init__(self, api_key, base='https://api.emailvalidation.io/v1'):
        super(Client, self).__init__(base, api_key)

    def status(self):
        return self._request('/status')

    def validate(self, email, catch_all=0):
        return self._request(f'/info', params={
            'email': email,
            'catch_all': catch_all
        })
