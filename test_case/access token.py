from requests import request
from faker import Faker,Factory


class Mydata:
    Token=None
    Ip='https://xxxhht'


class Test():
    def __init__(self):
        self.ip = getattr(Mydata, 'Ip')

    #  获取Access Token
    def token(self):
        url=self.ip+ '/api/interface/oauth/token'
        data={
            'grant_type':'password',
            'username':'admin',
            'password':'admin'
        }
        head={
            'Authorization':'Basic 46Y3JpdXNhZG1pbg=='
        }
        response=request(method='post',url=url,data=data,headers=head,verify=False).json()
        token=response['access_token']
        setattr(Mydata,'Token',token)
        return getattr(Mydata,'Token')


    def register_member(self):
        faker = Faker(locale='zh_CN')
        mobile = faker.phone_number()
        url=self.ip+'/api/interface/third/member/register'
        token=self.token()
        name=faker.name()
        mobile=faker.phone_number()
        head = {
        'Authorization': 'Bearer '+ token,
        'Content-Type': 'application/json'
        }
        data={
        "brand_code":"lae",
        "program_code":"lae",
        "mobile":mobile,
        "name":name,
        "gender":"M",
        "birthday":"1998-06-05",
        "chanel_code":"store",
        "consentStatus":"1",
        "consentTime":"2019-07-25 13:00:00",
        "store_code":"010"
    }
        response = request(method='post', url=url, data=data, headers=head,verify=False).json()
        return response['data']['union_code']



if __name__=="__main__":
    a=Test().token()
    print(a)





