# Data Acquisition Tools from DHMS Server
# Author: Daijie Bao 
# Date: 2023-04-13
# Belongs to: DHMS AI Team 

# Import the necessary libraries
import wget
import json
import traceback
import requests
import os
from os import path


headers = {
    'X-Forwarded-Uid': "1",
    'Content-Type': 'application/json'
}

# Create a directory to store the downloaded data
def get_sources(de_id, metric_no, start, end, downsample, baseurl=None, session=None) -> dict:
    """
    获取tsdb_query的sources
    :param de_id: device id
    :param metric_no: metric no
    :param start: start time
    :param end: end time
    :param downsample: downsample
    :param baseurl: baseurl
    :param session: session
    :return: sources
    """
    tsdb_query_rsp = get_tsdb_query(de_id, metric_no, start, end, downsample, baseurl=baseurl, session=session)
    if tsdb_query_rsp.status_code != 200:
        raise Exception("tsdb_query获取不成功")
    sources = json.loads(tsdb_query_rsp.content)["data"][0]["sources"]
    return sources

# Create a function to get tsdb_query response
def get_tsdb_query(device_id, metric, start_time, end_time, downsample,  baseurl=None, session=None) -> requests.models.Response:
    """
    获取tsdb_query的response
    :param device_id: device id
    :param metric: metric no
    :param start_time: start time
    :param end_time: end time
    :param downsample: downsample
    :param baseurl: baseurl
    :param session: session
    :return: tsdb_query的response
    """
    if isinstance(metric, str):
        queries = [{"metric": metric, "downsample": downsample,
                    "filters": [{"tagk": "deviceid", "filter": str(device_id), "type": "literal_or"}]}]
    elif isinstance(metric, list):
        queries = [{"metric": item, "downsample": downsample,
                    "filters": [{"tagk": "deviceid", "filter": str(device_id), "type": "literal_or"}]}
                   for item in metric]
    else:
        raise TypeError("the metric of tsdb query payload must be a str like m.1111 or a list like [m.1111, m.2222]")
    req_body = {
        "start": start_time,
        "end": end_time,
        "queries": queries
    }
    if baseurl and session:
        rsp = session.post(baseurl + "/api/tsdb/v1/query", data=json.dumps(req_body))
    else:
        rsp = requests.post("http://tsdbvendorsvc/tsdb/v1/query", data=json.dumps(req_body), headers=headers)
    return rsp


def get_session(baseurl="http://192.168.1.89:8000", username="13199999999", password="123456") -> requests.Session:
    """
    获取session
    :param baseurl: baseurl
    :param username: username
    :param password: password
    :return: session
    """
    env = {"baseurl": baseurl, "username": username, "password": password}
    session = req_session(env)
    return session


def login(env, session) -> requests.models.Response:
    """
    登录
    :param env: 环境
    :param session: session
    :return: 登录的response
    """
    url = env['baseurl'] + '/api/user/v1/login'
    headers = {
        'Content-Type': 'application/json',
        'X-Request-Id': '-0e5757e6-ab1e-4c64-aaf3-72856fe8c7da',
        'X-Auth-Tkn': 'dhms'
    }
    payload = {
        'username': env["username"],
        'password': env['password'],
        'prvset_name': 'dhms',
        'project_name': 'supervisor,consumer',
        'platform': 'WEB'
    }
    try:
        res = session.post(url, headers=headers, json=payload, timeout=20)
        return res
    except Exception as e:
        print(e)
        traceback.print_exc()


def req_session(env) -> requests.Session:
    """
    获取session
    :param env: 环境
    :return: session
    """
    session = requests.Session()
    session.headers.update({'X-Forwarded-PrId': '-1'})
    session.headers.update({'X-Request-Id': '-fc25f820-9ede-4a55-82d0-c551246e3dc5'})
    session.headers.update({'Content-Type': 'application/json'})
    login_res = login(env, session)
    token = login_res.headers['X-Auth-Tkn']
    cu_id = json.loads(login_res.text)['data']['cu_id']
    orgset = str(1000000000000000 + cu_id)
    session.headers.update({'X-Auth-Tkn': token})
    session.headers.update({'X-Forwarded-OrgSet': orgset})
    return session


# Create a function to download real time sensor data from DHMS server 
def download_data_from_DHMS_Server(de_id, metric_no, start, end, downsample, baseurl, username, password)-> None:
    """
    Download data from DHMS Server
    :param de_id: device id
    :param metric_no: metric no
    :param start: start time
    :param end: end time
    :param downsample: downsample
    :param baseurl: baseurl
    :param username: username
    :param password: password
    :return: None
    """
    print('Starting the download data from DHMS Server')
    print('\n')
    save_path = path.join(path.dirname(path.abspath(__file__)), 'Data_{}_{}'.format(de_id, metric_no))
    if not path.exists(save_path):
        os.makedirs(save_path)
    session = get_session(baseurl=baseurl, username=username, password=password)
    sources = get_sources(de_id, metric_no, start, end, downsample, baseurl=baseurl, session=session)
    for i, (k, v) in enumerate(sources.items()):
        try:
            print(i+1)
            if not v["file"]:
                continue
            else:
                file = baseurl + v["file"]
            wget.download(file, save_path)
        except Exception as e:
            print(e)
    print('\nDownload Process Finished!')