import base_class
import requests
class client_class(base_class.BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = None
    def get_json(self, r):
        return r.json()
    def get_params(self, i, param):
        meth = None
        param_name = None
        if i == 1:
            meth = "users.get"
            param_name = "user_ids=" + param
        if i == 2:
            meth = "friends.get"
            param_name = "user_id={0}&fields=bdate".format(param)
        self.method = meth + '?' + param_name
        return
    http_method = None
    def _get_data(self, method, http_method):
        response = requests.get(url=http_method)
        return  self.response_handler(response)
    def response_handler(self, r):
        if r.status_code != 200:
            print("Ошибка в ответе на запрос. Возможно неправильный username, или проблемы с интернетом")
            return 0
        temp = r.json()
        if "users.get" in self.method:
            id = temp['response']
            id2 = id[0]
            print ("Фамилия: " + id2['last_name'] + "   Имя: " + id2['first_name'])
            id = id2['uid']
            return id
        if "friends.get" in self.method:
            bdates = []
            dates = temp['response']
            for i in dates:
                if i.get('bdate') != None:
                    bdates.append(i['bdate'])
            return bdates

