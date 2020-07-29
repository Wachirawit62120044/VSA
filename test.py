import all

#resp = all.add_data("5f11d5290ca1d1000e154620","ข้าว3","test/test.jpg","ใบ")
#if resp.status_code != 201:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('Created data. ID: {}'.format(resp.json()["_id"]))

#resp = all.add_training("001","1200","image/image.jpg","10000","85","5efd7f1f8ffa26000e74eaa0")
#if resp.status_code != 201:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('Created data. ID: {}'.format(resp.json()["_id"]))

#resp = all.add_account("test","test","001")
#if resp.status_code != 201:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('Created data. ID: {}'.format(resp.json()["_id"]))

#resp = all.get_detect("5f1331569afe8e000ee96a65")
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print(resp.json())

#resp = all.get_all()
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print(resp.json())

#resp = all.delete_data("5f0300ee55e8e3000e87e33c")
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('deletedCount: {}'.format(resp.json()["deletedCount"]))

resp = all.get_imgAlluser()
if resp.status_code != 200:
    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
for item in resp.json():
    print(resp.json())
#    print(item['_id'])
#    print('ID:{} Image:{}'.format(item['_id'], item['report']['Image']))

#resp = all.get_imgOneuser("5f11d5290ca1d1000e154620")
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print('ID:{} Image:{}'.format(item['_id'], item['report']['Image']))

#resp = all.update_data("5f1331569afe8e000ee96a65","รา","admin",{"x":"3","sads":"sddsd"})
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#print('nModified: {}'.format(resp.json()["nModified"]))

#resp = all.login("test","test")
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print(resp.json())

#resp = all.detail("2019-06-11T00:00:00.000Z","2020-07-18T20:00:00.000Z")
#if resp.status_code != 200:
#    raise all.ApiError('{} {}'.format(resp.status_code,resp.json()))
#for item in resp.json():
#    print(resp.json())
