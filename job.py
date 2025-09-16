import sys
import os
import json
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

from utilskit import utils as u
from utilskit import timeutils as tiu
from utilskit import dataframeutils as dfu
from utilskit import dbutils as dbu


def job(*args):
    # 결과용 변수 최초 세팅
    status, error_info, error_msg = 1, '', ''
    result_dict = {
        'analy_start':None,
        'time_start':None,
        'log_msg':'',
    }
    # =========================================================================
    # 0. 일반 변수 세팅 및 결과 변수 생성
    try:
        root_path, test, date_, now, log, push_example = args[0:6]
        job_result_dict = {}
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = f'존재하지 않는 데이터입니다. 입력변수를 확인부탁드립니다.'
        return status, error_info, error_msg, result_dict


    # =========================================================================
    try:
        # 데이터 불러오기
        '''
        dataset code
        '''
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = f'존재하지 않는 데이터입니다. 입력변수를 확인부탁드립니다.'
        return status, error_info, error_msg, result_dict

    # =========================================================================
    # 모듈 진행1
    try:
        '''
        module code1
        '''
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '모듈 진행 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    
    # =========================================================================
    # 모듈 진행2
    try:
        '''
        module code2
        '''
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '모듈 진행 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    
    # =========================================================================
    # 결과 산출
    try:
        pass
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '모듈 진행 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    
    # =========================================================================
    # 결과 기록
    try:
        pass
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '최종 결과 저장 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict

    status = 3
    return status, error_info, error_msg, result_dict