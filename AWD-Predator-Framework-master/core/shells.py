# -*- coding: utf-8 -*-
import pickle

# 导入 core.ip_list 模块
from core.ip_list import *

# 定义全局变量用于存储shell路径和密码
GET_eval_shells_path_pwd = {}
POST_eval_shells_path_pwd = {}
GET_exec_shells_path_pwd = {}
POST_exec_shells_path_pwd = {}


# 添加GET eval shell路径和密码
def GET_eval_shell_path_pwd(path, pwd):
    global GET_eval_shells_path_pwd
    GET_eval_shells_path_pwd[path] = pwd


# 添加POST eval shell路径和密码
def POST_eval_shell_path_pwd(path, pwd):
    global POST_eval_shells_path_pwd
    POST_eval_shells_path_pwd[path] = pwd


# 添加GET exec shell路径和密码
def GET_exec_shell_path_pwd(path, pwd):
    global GET_exec_shells_path_pwd
    GET_exec_shells_path_pwd[path] = pwd


# 添加POST exec shell路径和密码
def POST_exec_shell_path_pwd(path, pwd):
    global POST_exec_shells_path_pwd
    POST_exec_shells_path_pwd[path] = pwd


# 获取GET eval shell路径和密码
def Get_GET_eval_sap():
    return GET_eval_shells_path_pwd


# 获取POST eval shell路径和密码
def Get_Post_eval_sap():
    return POST_eval_shells_path_pwd


# 获取GET exec shell路径和密码
def Get_GET_exec_sap():
    return GET_exec_shells_path_pwd


# 获取POST exec shell路径和密码
def Get_POST_exec_sap():
    return POST_exec_shells_path_pwd


# 显示所有shell路径和密码
def show_sap():
    for i in GET_eval_shells_path_pwd:
        print(i + ':' + GET_eval_shells_path_pwd[i] + ' eval get')
    for i in POST_eval_shells_path_pwd:
        print(i + ':' + POST_eval_shells_path_pwd[i] + ' eval post')
    for i in GET_exec_shells_path_pwd:
        print(i + ':' + GET_exec_shells_path_pwd[i] + ' exec get')
    for i in POST_exec_shells_path_pwd:
        print(i + ':' + POST_exec_shells_path_pwd[i] + ' exec post')


# 保存shell路径和密码
def save_shell_path_pwd():
    with open('data/GET_eval.pickle', 'wb') as f:
        pickle.dump(GET_eval_shells_path_pwd, f)
    with open('data/POST_eval.pickle', 'wb') as y:
        pickle.dump(POST_eval_shells_path_pwd, y)
    with open('data/GET_exec.pickle', 'wb') as g:
        pickle.dump(GET_exec_shells_path_pwd, g)
    with open('data/POST_exec.pickle', 'wb') as u:
        pickle.dump(POST_exec_shells_path_pwd, u)
    target = open('auxi/webshell.txt', 'w')
    for i in ipList:
        print(i)
        for j in POST_eval_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(j)
            target.write(',')
            target.write('post')
            target.write(',')
            target.write(POST_eval_shells_path_pwd[j])
            target.write('\n')
        for k in GET_eval_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(k)
            target.write(',')
            target.write('get')
            target.write(',')
            target.write(GET_eval_shells_path_pwd[k])
            target.write('\n')
        """
        for m in GET_exec_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(m)
            target.write(',')
            target.write('get')
            target.write(',')
            target.write(GET_exec_shells_path_pwd[m])
            target.write('\n')
        for n in POST_exec_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(n)
            target.write(',')
            target.write('get')
            target.write(',')
            target.write(POST_exec_shells_path_pwd[n])
            target.write('\n')
        """
    target.close()
    print("save ok")


# 读取shell路径和密码
def load_shell_path_pwd():
    global GET_eval_shells_path_pwd, POST_eval_shells_path_pwd, GET_exec_shells_path_pwd, POST_exec_shells_path_pwd
    with open('data/GET_eval.pickle', 'rb') as f:
        a = pickle.load(f)
        GET_eval_shells_path_pwd = a
    with open('data/POST_eval.pickle', 'rb') as y:
        b = pickle.load(y)
        POST_eval_shells_path_pwd =在给定的代码中，有一些错误和问题。下面是修复后的代码，并添加了注释：

```python
# -*- coding: utf-8 -*-
import pickle

# 导入 core.ip_list 模块
from core.ip_list import *

# 定义全局变量用于存储 shell 路径和密码
GET_eval_shells_path_pwd = {}
POST_eval_shells_path_pwd = {}
GET_exec_shells_path_pwd = {}
POST_exec_shells_path_pwd = {}


# 添加 GET eval shell 路径和密码
def GET_eval_shell_path_pwd(path, pwd):
    global GET_eval_shells_path_pwd
    GET_eval_shells_path_pwd[path] = pwd


# 添加 POST eval shell 路径和密码
def POST_eval_shell_path_pwd(path, pwd):
    global POST_eval_shells_path_pwd
    POST_eval_shells_path_pwd[path] = pwd


# 添加 GET exec shell 路径和密码
def GET_exec_shell_path_pwd(path, pwd):
    global GET_exec_shells_path_pwd
    GET_exec_shells_path_pwd[path] = pwd


# 添加 POST exec shell 路径和密码
def POST_exec_shell_path_pwd(path, pwd):
    global POST_exec_shells_path_pwd
    POST_exec_shells_path_pwd[path] = pwd


# 获取 GET eval shell 路径和密码
def Get_GET_eval_sap():
    return GET_eval_shells_path_pwd


# 获取 POST eval shell 路径和密码
def Get_Post_eval_sap():
    return POST_eval_shells_path_pwd


# 获取 GET exec shell 路径和密码
def Get_GET_exec_sap():
    return GET_exec_shells_path_pwd


# 获取 POST exec shell 路径和密码
def Get_POST_exec_sap():
    return POST_exec_shells_path_pwd


# 显示所有 shell 路径和密码
def show_sap():
    for i in GET_eval_shells_path_pwd:
        print(i + ':' + GET_eval_shells_path_pwd[i] + ' eval get')
    for i in POST_eval_shells_path_pwd:
        print(i + ':' + POST_eval_shells_path_pwd[i] + ' eval post')
    for i in GET_exec_shells_path_pwd:
        print(i + ':' + GET_exec_shells_path_pwd[i] + ' exec get')
    for i in POST_exec_shells_path_pwd:
        print(i + ':' + POST_exec_shells_path_pwd[i] + ' exec post')


# 保存 shell 路径和密码
def save_shell_path_pwd():
    with open('data/GET_eval.pickle', 'wb') as f:
        pickle.dump(GET_eval_shells_path_pwd, f)
    with open('data/POST_eval.pickle', 'wb') as y:
        pickle.dump(POST_eval_shells_path_pwd, y)
    with open('data/GET_exec.pickle', 'wb') as g:
        pickle.dump(GET_exec_shells_path_pwd, g)
    with open('data/POST_exec.pickle', 'wb') as u:
        pickle.dump(POST_exec_shells_path_pwd, u)
    target = open('auxi/webshell.txt', 'w')
    for i in ipList:
        print(i)
        for j in POST_eval_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(j)
            target.write(',')
            target.write('post')
            target.write(',')
            target.write(POST_eval_shells_path_pwd[j])
            target.write('\n')
        for k in GET_eval_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(k)
            target.write(',')
            target.write('get')
            target.write(',')
            target.write(GET_eval_shells_path_pwd[k])
            target.write('\n')
        """
        for m in GET_exec_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(m)
            target.write(',')
            target.write('get')
            target.write(',')
            target.write(GET_exec_shells_path_pwd[m])
            target.write('\n')
        for n in POST_exec_shells_path_pwd:
            target.write('http://')
            target.write(i)
            target.write(n)
            target.write(',')
            target.write('get')
            target.write(',')
            target.write(POST_exec_shells_path_pwd[n])
            target.write('\n')
        """
    target.close()
    print("save ok")


# 读取 shell 路径和密码
def load_shell_path_pwd():
    global GET_eval_shells_path_pwd, POST_eval_shells_path_pwd, GET_exec_shells_path_pwd, POST_exec_shells_path_pwd
    with open('data/GET_eval.pickle', 'rb') as f:
        GET_eval_shells_path_pwd = pickle.load(f)
    with open('data/
