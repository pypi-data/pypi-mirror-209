# coding: utf-8
import re
import os
import platform
from http import server
from pathlib import Path


class Server:
    def __init__(self, server_name, server_port, logfile, configs):
        self.name: tuple = server_name
        self.port = server_port
        self.logfile = logfile
        self.configs = configs

    def eq_name(self, server_name):
        pattern = server_name.replace(".", "\.").replace("*", ".*?") if server_name is not None else None
        if server_name is None:
            return True
        for _ in self.name:
            if re.match(pattern, _) is not None:
                return True

        return False

    @classmethod
    def create(cls, server, nginx_path):
        _server_name = server['server_name']
        _logfile = server['logfile']
        _configs = server['configs']
        _server_port = server['port']
        logfile = Path(_logfile)
        # 判断路径是否为绝对路径
        _logfile = logfile if logfile.is_absolute() else Path(nginx_path).parent / logfile

        return cls(_server_name, _server_port, _logfile, _configs)


class NginxException(Exception):
    pass


class Nginx:

    def __init__(self, nginx_path=None):
        self.nginx_conf = None
        self.nginx_path = nginx_path
        self.backend = list()  # 保存后端ip和pool name
        self.serverBlock = list()  # 保存解析后端每个server块
        self.servers = list()
        self.load_nginx_config()
        self.parse_backend_ip()
        self.parse_server_block()

    def load_nginx_config(self):
        # 判断平台
        if platform.system() == 'Windows':
            self.nginx_path = self.get_nginx_path_win(self.nginx_path)
            self.nginx_conf = os.popen(f"cd /d {Path(self.nginx_path).parent} && nginx -T").read()
        else:
            self.nginx_path = self.get_nginx_path_linux(self.nginx_path)
            self.nginx_conf = os.popen(f"{self.nginx_path} -T").read()

    #############################################################################
    #####Parse Nginx Config######################################################
    def get_nginx_path_win(self, nginx_path):
        os.popen(f"chcp 65001")
        if nginx_path is not None and nginx_path.exists():
            return nginx_path

        nginx_paths = os.popen(f"where nginx").readlines()

        if not nginx_paths:
            raise NginxException('请将[nginx.exe]配置到环境变量中')

        for path in nginx_paths:
            path = path.strip()
            if os.path.exists(path):
                return path

    def get_nginx_path_linux(self, nginx_path):
        if nginx_path is not None and nginx_path.exists():
            return nginx_path

        nginx_paths = os.popen(f"which nginx").readlines()

        if not nginx_paths:
            raise NginxException('请将[nginx]配置到环境变量中')

        for path in nginx_paths:
            path = path.strip()
            if os.path.exists(path):
                return path

    def parse_backend_ip(self):
        # 获取每个upstream块
        regex_1 = 'upstream\s+([^{ ]+)\s*{([^}]*)}'
        upstreams = re.findall(regex_1, self.nginx_conf)

        for up in upstreams:
            # 获取后端的ip
            regex_2 = 'server\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?::\d{2,5})?)'
            backend = re.findall(regex_2, up[1])
            # 判断是否有后端的ip设置
            if len(backend) > 0:
                pool_and_ip = {'poolname': up[0], 'ip': ' '.join(backend)}
                self.backend.append(pool_and_ip)

    def parse_server_block(self):
        flag = False
        serverblock = ''
        num_of_quote = 0

        for line in self.nginx_conf.splitlines():
            x = line.replace(' ', '')
            if x.startswith('server{'):
                num_of_quote += 1
                flag = True
                serverblock += line
                continue
            # 发现{，计数加1。发现}，计数减1，直到计数为0
            if flag and '{' in line:
                num_of_quote += 1

            # 将proxy_pass的别名换成ip
            if flag and 'proxy_pass' in line:
                r = re.findall('proxy_pass\s+https?://([^;/]*)[^;]*;', line)
                if len(r) > 0:
                    for pool in self.backend:
                        if r[0] == pool['poolname']:
                            line = line.replace(r[0], pool['ip'])

            if flag and num_of_quote != 0:
                serverblock += line

            if flag and '}' in line:
                num_of_quote -= 1

            if flag and num_of_quote == 0:
                self.serverBlock.append(serverblock)
                flag = False
                serverblock = ''
                num_of_quote = 0

        for singleServer in self.serverBlock:
            port = re.findall('listen\s*((?:\d|\s)*)[^;]*;', singleServer)[0]  # port只有一个

            r = re.findall('server_name\s+([^;]*);', singleServer)  # server_name只有一个

            # 可能存在没有server_name的情况
            if len(r) > 0:
                servername = r[0]
            else:
                continue

            # 判断servername是否有ip，有ip就不存。比如servername 127.0.0.1这样的配置
            if len(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', servername)) > 0:
                continue

            servername = tuple(r[0].split())

            include = ' '.join(re.findall('include\s+([^;]*);', singleServer))  # include不止一个
            # location可能不止一个
            locations = re.findall('location\s*[\^~\*=]{0,3}\s*([^{ ]*)\s*\{[^}]*proxy_pass\s+https?://([^;/]*)[^;]*;',
                                   singleServer)

            backend_list = list()
            backend_ip = ''

            # 可能存在多个location
            if len(locations) > 0:
                for location in locations:
                    backend_path = location[0]
                    poolname = location[1]
                    # 如果不是ip的pool name，就取出后端对应的ip
                    if len(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', poolname)) == 0:
                        for backend in self.backend:
                            if poolname == backend['poolname']:
                                backend_ip = backend['ip']
                                break
                    else:
                        backend_ip = poolname

                    backend_list.append({"backend_path": backend_path, "backend_ip": backend_ip})

            # 匹配到;或者\n为止
            access_logs = re.findall('access_log\s+([^;]*)[;\n]', singleServer)
            logfile = ''
            configs = []
            if len(access_logs) > 0:
                for _access_log in access_logs:
                    _logfile, configs = _access_log.split(' ', 1)
                    if 'salesea' in configs:
                        logfile = _logfile
                        break

            if not logfile:
                continue

            server = Server.create(
                {
                    'port': port,
                    'server_name': servername,
                    'include': include,
                    'backend': backend_list,
                    'logfile': logfile,
                    'configs': configs
                },
                self.nginx_path
            )

            self.servers.append(server)
