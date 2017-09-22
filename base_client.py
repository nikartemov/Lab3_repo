class BaseClient:
    # URL vk api
    BASE_URL = None
    # metod vk api
    method = None
    # GET, POST, ...
    http_method = None

    # poluchenie GET parametrov zaprosa
    def get_params(self):
        return None

    # poluchenie dannih POST zaprosa
    def get_json(self):
        return None

    # poluchenie HTTP zagolovkov
    def get_headers(self):
        return None

    # skleyka url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # otpravka zaprosa k VK API
    def _get_data(self, method, http_method):
        response = None

        #todo vipolnit zapros

        return self.response_handler(response)

    # obrabotka otveta ot VK API
    def response_handler(self, response):
        return response

    # zapusk klienta
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )