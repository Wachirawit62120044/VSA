import requests #npm install requests
import json

def _url(path):
    return 'https://test-o7f7gafj4q-uc.a.run.app/project1' + path

def get_all():
    return requests.get(_url('/findall/'))

def get_user(user):
    return requests.get(_url('/finduser/'), json = {"data": user})

def add_data_test(username, password, email):
    return requests.post(_url('/adddata/'), json = {"data":{
        "Username":username,
        "Password":password,
        "Email":email
        }})

def delete_test(_id):
    return requests.delete(_url('/delete/'), json = {"data": _id})

def update_data(_id, username, password, email):
    return requests.put(_url('/updatedata/'), json = {"id": _id, "data":{
        "Username":username,
        "Password":password,
        "Email":email
        }})

def add_account(username, password, siteid):
    return requests.post(_url('/addaccount/'), json = {"data":{
        "Username":username,
        "Password":password,
        "SiteID":siteid
        }})

def add_data(userid, planttype, image, location):
    return requests.post(_url('/adddata/'), json = {"data":{
        "UserID":userid,
        "plantType":planttype,
        "Image":image,
        "Location":location
        }})

def add_training(modelid, training, dataimage, loop, accuracy, userid):
    return requests.post(_url('/addtraining/'), json = {"data":{
        "ModelID":modelid,
        "Training":training,
        "DataImage":dataimage,
        "Loop":loop,
        "Accuracy":accuracy,
        "UserID":userid
        }})

def get_detect(_id):
    return requests.get(_url('/getdetect/'), params = {"data":_id})

def get_imgOneuser(user):
    return requests.get(_url('/getimgOneuser/'), params = {"data":user})

def get_imgAlluser():
    return requests.get(_url('/getimgAlluser/'))

def delete_data(_id):
    return requests.delete(_url('/deletedata/'), json = {"data": _id})

def update_data(_id, classname, whomark, roi):
    return requests.put(_url('/sentROI/'), json = {"id": _id, "data":{
        "ClassName":classname,
        "WhoMark":whomark,
        "ROI":roi
        }})

def login(username,password):
    return requests.get(_url('/login/'), params = {
        "Username":username,
        "Password":password
        })

def detail(start,end):
    return requests.get(_url('/getdetail/'), params = {
        "start":start,
        "end":end
        })

class ApiError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)

#resp = get_all()
#if resp.status_code != 200:
#    raise ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print('ID:{} Email:{}'.format(item['_id'], item['Email']))

#resp = get_user("1a234")
#if resp.status_code != 200:
#    raise ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print('Username:{} Email:{}'.format(item['Username'], item['Email']))


#resp = add_data("qwer","qwer","1234@1234.com")
#if resp.status_code != 201:
#    raise ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('Created data. ID: {}'.format(resp.json()["_id"]))

#resp = delete_data("5eef5ff69a29e414c0bfcb4f")
#if resp.status_code != 200:
#    raise ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('deletedCount: {}'.format(resp.json()["deletedCount"]))

#resp = update_data("5eee3d79d8837d332cfccc08","zxcv","zxcv","asdf@asdf.com")
#if resp.status_code != 200:
#    raise ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('nModified: {}'.format(resp.json()["nModified"]))
