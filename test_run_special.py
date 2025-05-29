import logging

from module.crawling_target.get_special_fund import GetSpecialFund
from module.data_mining.data_mining import DataMining
from module.process_manager import TaskManager
from module.saving_result.save_result_2_file import SaveResult2CSV
from utils.constants import log_format

"""
爬取特定基金
"""
if __name__ == '__main__':
    # 日志级别
    logging.basicConfig(level=logging.INFO, format=log_format)

    TaskManager(GetSpecialFund()
                , DataMining()
                , SaveResult2CSV()).run()
