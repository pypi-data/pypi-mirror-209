# 解析Nginx日志, 根据开始时间进行筛选
import asyncio
import itertools
import json
import os
import re
import aiohttp as aiohttp
from pathlib import Path

from .nginx import Nginx, NginxException
from .log import logger
from .solution import print_solution

def launch():
    # 将PID写入文件
    pid = os.getpid()
    with open("salesea.pid", "w") as f:
        f.write(str(pid))
    #############################################################################
    #####Global Variable#########################################################
    datetime_format = "%Y-%m-%d %H:%M:%S %z"  # 时间格式
    nginx = None

    #############################################################################
    #####Get Access Servers######################################################

    def get_access_servers(server_name=None):
        nginx_path = nginx.nginx_path
        pattern = server_name.replace(".", "\.").replace("*", ".*?") if server_name is not None else None
        servers = []
        logger.debug(f"nginx_path: {nginx_path}")
        for server in nginx.servers:
            if server.logfile is not None:
                match = server_name is None or re.match(pattern, server.name)
                logger.debug(f"server_name: {server.name} {'匹配' if match else '不匹配'}")
                if match:
                    servers.append(server)
        return servers

    #############################################################################
    #####Parse Nginx Log########################################################
    def parse_nginx_log(logfile: Path, pattern):
        if not logfile.exists():
            logger.error(f"日志文件不存在: {str(logfile)}")
        else:
            offset = 0
            with open(logfile, mode="r+", encoding="utf-8") as fobj:
                while True:
                    line = fobj.readline().strip()
                    if line:
                        try:
                            row = re.match(pattern, line)
                            data = row.groupdict()
                            yield data
                        except Exception as e:
                            logger.error(f"解析日志错误: {e}")
                            logger.info(f"解析日志错误: {line}")
                    else:
                        # 获取当前偏移量
                        offset = fobj.tell()
                        # 定位文件指针
                        fobj.seek(offset)
                        # 清除0到偏移量之间的内容
                        fobj.truncate(0)
                        break

    #############################################################################
    #####Scheduler##############################################################
    # 使用asyncio实现定时任务
    def scheduler(interval):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                while True:
                    await func(*args, **kwargs)
                    await asyncio.sleep(interval)

            return wrapper

        return decorator

    #############################################################################
    #####Utils###################################################################
    # 迭代器切割
    def chunked(iterable, n):
        for i in range(0, len(iterable), n):
            yield iterable[i:i + n]

    #############################################################################
    #####Main###################################################################
    async def main():
        logfile = "./access.log"
        # 替换所有的$符号为(.*?)，并且将$符号后面的字符串作为分组名
        log_pattern = re.sub(r"\$[a-zA-Z_]\w*", r"(?P<\g<0>>.*?)", LOG_FORMAT)
        log_pattern = log_pattern.replace('$', '').replace('[', '\[').replace(']', '\]')
        servers = get_access_servers(SERVER_NAME)

        if servers:
            [logger.info(f'解析到配置：{server.name}:{server.port} >> {server.logfile}') for server in servers]
        else:
            logger.error('未解析到指定的Nginx服务器\n')
            print_solution()
            exit(1)

        @scheduler(CHECK_INTERVAL)
        async def task():
            # logger.debug(f"开始扫描日志文件：{[str(server.logfile) for p in servers]}")
            count = 0
            async with aiohttp.ClientSession(headers={
                'Content-Type': 'application/json'
            }) as session:
                for server in servers:
                    nginx_log_iter = parse_nginx_log(server.logfile, log_pattern)
                    tasks = []
                    while True:
                        datas = itertools.islice(nginx_log_iter, REQUEST_CONCURRENCY)
                        try:
                            for data in datas:
                                # 使用并发请求
                                d = re.match(r"[a-zA-Z]+\s(?P<path>/.*?)(?P<query>\?.*?)?\s",
                                             data['request']).groupdict()
                                tasks.append(session.post('https://salesea.cn/api/visit', data=json.dumps({
                                    'visitApiKey': VISIT_APIKEY,
                                    'domain': server.name or SERVER_NAME or 'localhost',
                                    'path': d.get('path'),
                                    'query': d.get('query'),
                                    'referrer': data['http_referer'],
                                    'user_agent': data['http_user_agent'],
                                    'ip': data['remote_addr'],
                                })))
                                count += 1
                            if not tasks:
                                break
                            results = await asyncio.gather(*tasks)
                            for result in results:
                                text = await result.text()
                                logger.debug(f"请求结果: {text}")
                            tasks.clear()
                        except Exception as e:
                            logger.error(f"请求错误: {e}")
                            logger.info(f"请求错误: {data}")

            logger.__getattribute__('info' if count else 'debug')(f"解析到[{count}]条日志")

        await task()

    try:
        from .config import NGINX_PATH, SERVER_NAME, CHECK_INTERVAL, REQUEST_CONCURRENCY, VISIT_APIKEY, LOG_FORMAT

        try:
            nginx = Nginx(Path(NGINX_PATH) if NGINX_PATH else None)
        except NginxException as e:
            logger.error(f"[nginx] {e}")
            exit(1)

        #############################################################################
        #####Print Config############################################################
        logger.debug(f"#" * 65)
        logger.debug(f"# nginx_path: {nginx.nginx_path}")
        logger.debug(f"# server_name: {SERVER_NAME}")
        logger.debug(f"# check_interval: {CHECK_INTERVAL}")
        logger.debug(f"# request_concurrency: {REQUEST_CONCURRENCY}")
        logger.debug(f"# visit_apikey: {'*' * 8} ({len(VISIT_APIKEY or '')})")
        logger.debug(f"#" * 65)

        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("用户终止程序")
