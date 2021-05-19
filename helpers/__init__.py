from helpers.manager import Resources
import json


class SuiteTestData:
    login_url = None
    login_user = None
    login_password = None
    api_url = None
    query_params = None

    def __init__(self):
        loaded = self.__load()
        assert loaded is True, f'Error while loading {Resources.get_resource("testData.json")}'

    def __load(self):
        try:
            with open(Resources.get_resource('testData.json'), 'r') as f:
                data = json.load(f)
            if not data:
                return False
            if 'login_url' in data:
                self.login_url = data['login_url']
            if 'login_user' in data:
                self.login_user = data['login_user']
            if 'login_password' in data:
                self.login_password = data['login_password']
            if 'api_url' in data:
                self.api_url = data['api_url']
            if 'query_params' in data:
                self.query_params = data['query_params']
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    std = SuiteTestData()
    print(std)