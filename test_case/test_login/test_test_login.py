
import requests
import pytest
import allure
import json
import config.env_config as config
from hashlib import md5
from faker import Faker
from tools.report import log_tool

f = Faker(locale='zh_CN')



@pytest.mark.run(order=1)
@allure.epic('一级分类')
@allure.feature('二级分类')
@allure.story('三级分类')
def test_d1_admin( pub_data):

    with allure.step('第1步：准备请求报文'):
        log_tool.info('\n-----------------test_case/test_login/test_test_login.py::d1_admin-----------------')
        url = config.api_url+'/crmapi/user/login/admin'
        allure.attach(url, '请求地址', allure.attachment_type.TEXT)
        log_tool.info('\n请求地址：\n'+url)

        headers = {
    "addr": "上海市虹口区",
    "ip": "124.77.86.126",
    "Content-Type": "application/json;charset=UTF-8"
}
        allure.attach(json.dumps(headers, ensure_ascii=False, indent=4), '请求头', allure.attachment_type.TEXT)
        log_tool.info('\n请求头：\n'+json.dumps(headers, ensure_ascii=False, indent=4))
    
        headers['addr'] = '上海市虹口区'.encode('utf-8').decode('latin-1')
            
        req = {
    "username": "manager",
    "password": md5('123456&key=guoyasoft'.encode('utf8')).hexdigest()
}
        allure.attach(json.dumps(req, ensure_ascii=False, indent=4), '请求正文', allure.attachment_type.TEXT)
        log_tool.info('\n请求正文：\n'+json.dumps(req, ensure_ascii=False, indent=4))

    with allure.step('第2步：调用接口'):
        resp = requests.post(url, headers=headers ,json=req)

    with allure.step('第3步：接收响应'):
        data = resp.json()
        allure.attach(json.dumps(data, ensure_ascii=False, indent=4), '响应报文', allure.attachment_type.TEXT)
        log_tool.info('\n响应报文：\n'+json.dumps(data, ensure_ascii=False, indent=4))
    
    with allure.step('第4步：判断结果'):
        allure.attach("resp.status_code == 200", '断言条件', allure.attachment_type.TEXT)
        log_tool.info('\n断言条件：\n'+'resp.status_code == 200')
        assert data['code']==20000
    
    with allure.step('第5步：提取数据'):
        token=data['data']['token']
        pub_data['token']=token
        # pub_data['data_name']='data_value';
        allure.attach('token='+token, '提取数据列表',allure.attachment_type.TEXT)
        log_tool.info('\n提取数据列表：\n'+'token='+token)
        log_tool.info('\n\n\n')
    


@pytest.mark.run(order=2)
@allure.epic('一级分类')
@allure.feature('二级分类')
@allure.story('三级分类')
def test_d2_info( pub_data):

    with allure.step('第1步：准备请求报文'):
        log_tool.info('\n-----------------test_case/test_login/test_test_login.py::d2_info-----------------')
        url = config.api_url+'/crmapi/user/info?token=5954bc3637eb4ce8aefa71afbd9d3d72'
        allure.attach(url, '请求地址', allure.attachment_type.TEXT)
        log_tool.info('\n请求地址：\n'+url)

        headers = {
    "addr": "上海市虹口区",
    "UserID": "0",
    "ip": "124.77.86.126",
    "Token": "5954bc3637eb4ce8aefa71afbd9d3d72"
}
        allure.attach(json.dumps(headers, ensure_ascii=False, indent=4), '请求头', allure.attachment_type.TEXT)
        log_tool.info('\n请求头：\n'+json.dumps(headers, ensure_ascii=False, indent=4))
    
        headers['addr'] = '上海市虹口区'.encode('utf-8').decode('latin-1')
            
    with allure.step('第2步：调用接口'):
        resp = requests.get(url, headers=headers )

    with allure.step('第3步：接收响应'):
        data = resp.json()
        allure.attach(json.dumps(data, ensure_ascii=False, indent=4), '响应报文', allure.attachment_type.TEXT)
        log_tool.info('\n响应报文：\n'+json.dumps(data, ensure_ascii=False, indent=4))
    
    with allure.step('第4步：判断结果'):
        allure.attach("resp.status_code == 200", '断言条件', allure.attachment_type.TEXT)
        log_tool.info('\n断言条件：\n'+'resp.status_code == 200')
        assert data['code']==20000
    
    with allure.step('第5步：提取数据'):
        # pub_data['data_name']='data_value';
        allure.attach('无', '提取数据列表',allure.attachment_type.TEXT)
        log_tool.info('\n提取数据列表：\n'+'无')
        log_tool.info('\n\n\n')
    


@pytest.mark.run(order=3)
@allure.epic('一级分类')
@allure.feature('二级分类')
@allure.story('三级分类')
def test_d3_addTeacher( pub_data):

    with allure.step('第1步：准备请求报文'):
        log_tool.info('\n-----------------test_case/test_login/test_test_login.py::d3_addTeacher-----------------')
        url = config.api_url+'/crmapi/admin/addTeacher'
        allure.attach(url, '请求地址', allure.attachment_type.TEXT)
        log_tool.info('\n请求地址：\n'+url)

        headers = {
    "addr": "上海市虹口区",
    "UserID": "0",
    "ip": "124.77.86.126",
    "Token": "5954bc3637eb4ce8aefa71afbd9d3d72",
    "Content-Type": "application/json;charset=UTF-8"
}
        allure.attach(json.dumps(headers, ensure_ascii=False, indent=4), '请求头', allure.attachment_type.TEXT)
        log_tool.info('\n请求头：\n'+json.dumps(headers, ensure_ascii=False, indent=4))
    
        headers['addr'] = '上海市虹口区'.encode('utf-8').decode('latin-1')
            
        req = {
    "name": f.name(),
    "username": f.user_name(),
    "paaword": "7a64d3bd06bc8e17d2100f846e719fd6",
    "rule": [
        "teacher"
    ]
}
        allure.attach(json.dumps(req, ensure_ascii=False, indent=4), '请求正文', allure.attachment_type.TEXT)
        log_tool.info('\n请求正文：\n'+json.dumps(req, ensure_ascii=False, indent=4))

    with allure.step('第2步：调用接口'):
        resp = requests.post(url, headers=headers ,json=req)

    with allure.step('第3步：接收响应'):
        data = resp.json()
        allure.attach(json.dumps(data, ensure_ascii=False, indent=4), '响应报文', allure.attachment_type.TEXT)
        log_tool.info('\n响应报文：\n'+json.dumps(data, ensure_ascii=False, indent=4))
    
    with allure.step('第4步：判断结果'):
        allure.attach("resp.status_code == 200", '断言条件', allure.attachment_type.TEXT)
        log_tool.info('\n断言条件：\n'+'resp.status_code == 200')
        assert data['code']==20000
    
    with allure.step('第5步：提取数据'):
        # pub_data['data_name']='data_value';
        allure.attach('无', '提取数据列表',allure.attachment_type.TEXT)
        log_tool.info('\n提取数据列表：\n'+'无')
        log_tool.info('\n\n\n')
    


@pytest.mark.run(order=4)
@allure.epic('一级分类')
@allure.feature('二级分类')
@allure.story('三级分类')
def test_d4_getClassForView( pub_data):

    with allure.step('第1步：准备请求报文'):
        log_tool.info('\n-----------------test_case/test_login/test_test_login.py::d4_getClassForView-----------------')
        url = config.api_url+'/crmapi/admin/getClassForView?pageNum=1&pageSize=100'
        allure.attach(url, '请求地址', allure.attachment_type.TEXT)
        log_tool.info('\n请求地址：\n'+url)

        headers = {
    "addr": "上海市虹口区",
    "UserID": "0",
    "ip": "124.77.86.126",
    "Token": "5954bc3637eb4ce8aefa71afbd9d3d72"
}
        allure.attach(json.dumps(headers, ensure_ascii=False, indent=4), '请求头', allure.attachment_type.TEXT)
        log_tool.info('\n请求头：\n'+json.dumps(headers, ensure_ascii=False, indent=4))
    
        headers['addr'] = '上海市虹口区'.encode('utf-8').decode('latin-1')
            
    with allure.step('第2步：调用接口'):
        resp = requests.get(url, headers=headers )

    with allure.step('第3步：接收响应'):
        data = resp.json()
        allure.attach(json.dumps(data, ensure_ascii=False, indent=4), '响应报文', allure.attachment_type.TEXT)
        log_tool.info('\n响应报文：\n'+json.dumps(data, ensure_ascii=False, indent=4))
    
    with allure.step('第4步：判断结果'):
        allure.attach("resp.status_code == 200", '断言条件', allure.attachment_type.TEXT)
        log_tool.info('\n断言条件：\n'+'resp.status_code == 200')
        assert data['code']==20000
    
    with allure.step('第5步：提取数据'):
        # pub_data['data_name']='data_value';
        allure.attach('无', '提取数据列表',allure.attachment_type.TEXT)
        log_tool.info('\n提取数据列表：\n'+'无')
        log_tool.info('\n\n\n')
    


@pytest.mark.run(order=5)
@allure.epic('一级分类')
@allure.feature('二级分类')
@allure.story('三级分类')
def test_d5_queryStuList( pub_data):

    with allure.step('第1步：准备请求报文'):
        log_tool.info('\n-----------------test_case/test_login/test_test_login.py::d5_queryStuList-----------------')
        url = config.api_url+'/crmapi/admin/stu/queryStuList?pageNum=1&pageSize=10'
        allure.attach(url, '请求地址', allure.attachment_type.TEXT)
        log_tool.info('\n请求地址：\n'+url)

        headers = {
    "addr": "上海市虹口区",
    "UserID": "0",
    "ip": "124.77.86.126",
    "Token": "5954bc3637eb4ce8aefa71afbd9d3d72",
    "Content-Type": "application/json;charset=UTF-8"
}
        allure.attach(json.dumps(headers, ensure_ascii=False, indent=4), '请求头', allure.attachment_type.TEXT)
        log_tool.info('\n请求头：\n'+json.dumps(headers, ensure_ascii=False, indent=4))
    
        headers['addr'] = '上海市虹口区'.encode('utf-8').decode('latin-1')
            
        req = {
    "className": "",
    "classId": 0,
    "stuId": 0,
    "stuName": "",
    "age1": 0,
    "age2": 0,
    "cert": "",
    "province": "",
    "city": "",
    "education": "",
    "feeUnpayed": 0,
    "feePayed": 0,
    "badDebt": 0,
    "discountsName": "",
    "phone": "",
    "discountsAmount": 0,
    "employmentType": "",
    "homeAddr": "",
    "comAddr": ""
}
        allure.attach(json.dumps(req, ensure_ascii=False, indent=4), '请求正文', allure.attachment_type.TEXT)
        log_tool.info('\n请求正文：\n'+json.dumps(req, ensure_ascii=False, indent=4))

    with allure.step('第2步：调用接口'):
        resp = requests.post(url, headers=headers ,json=req)

    with allure.step('第3步：接收响应'):
        data = resp.json()
        allure.attach(json.dumps(data, ensure_ascii=False, indent=4), '响应报文', allure.attachment_type.TEXT)
        log_tool.info('\n响应报文：\n'+json.dumps(data, ensure_ascii=False, indent=4))
    
    with allure.step('第4步：判断结果'):
        allure.attach("resp.status_code == 200", '断言条件', allure.attachment_type.TEXT)
        log_tool.info('\n断言条件：\n'+'resp.status_code == 200')
        assert data['code']==20000
    
    with allure.step('第5步：提取数据'):
        # pub_data['data_name']='data_value';
        allure.attach('无', '提取数据列表',allure.attachment_type.TEXT)
        log_tool.info('\n提取数据列表：\n'+'无')
        log_tool.info('\n\n\n')
    