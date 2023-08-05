import logging

#############################################################################
#####Logger Handler##########################################################
logger = logging.getLogger(__name__)  # 日志对象
logger.level = logging.INFO  # 日志级别
handler = logging.StreamHandler()  # 日志处理器
handler.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")  # 日志格式
logger.addHandler(handler)  # 添加日志处理器
fh = logging.FileHandler("salesea.log", encoding="utf-8")  # 日志文件处理器
fh.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")  # 日志格式
logger.addHandler(fh)  # 添加日志文件处理器
