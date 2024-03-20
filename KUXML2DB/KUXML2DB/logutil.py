import sys
import os
import logging
import setting



def set_logger(name=None ,mode = 'MODE', yyyymmdd='yyyymmdd'):
    setting.log_path = setting.log_path.replace('yyyymmdd',yyyymmdd)
    setting.log_path = setting.log_path.replace('MODE',mode)
    #ログの構成
    logging.basicConfig(filename=setting.log_path,level=setting.loglevel, encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

    # INFO以下のログを標準出力する
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setLevel(setting.loglevel) #標準出力にはDEBUG
    stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING) #ワーニング以上は標準出力には出さない

    # WARNING以上のログを標準エラー出力する
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    stderr_handler.setLevel(logging.WARNING) #標準エラー出力はWARN以上

    # ロガーにハンドラを設定する
    global logger
    logger = logging.getLogger(name)
    logger.setLevel(setting.loglevel) #ログレベルはDEBUG
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
