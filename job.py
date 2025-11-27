import sys
import os
import json
import copy
import random
import time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

from utilskit import utils as u

from module.parameters import Params


def job(p: Params):
# def job(*args):
    # 결과용 변수 최초 세팅
    status, error_info, error_msg = 1, '', ''
    result_dict = {
        'analy_start':None,
        'log_msg':''
    }

    # =========================================================================
    # 0. 일반변수 세팅 및 결과 변수 생성
    try:
        module_path, src_path, system_path = p.path.module_path, p.path.src_path, p.path.system_path
        test = p.run.test
        date_, now = p.common.date_, p.common.now

        # 분석시작 시간 설정 - 기본: 현재 기준 3분 이전
        analy_start = datetime.strptime(f'{date_} {now}', '%Y-%m-%d %H:%M:%S') - timedelta(minutes=3)
        analy_start = datetime.strftime(analy_start, '%Y-%m-%d %H:%M:%S')

        # 결과 추가
        result_dict['analy_start'] = analy_start
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '일반&결과 변수 세팅 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    
    # =========================================================================
    # 메인 코드1
    try:
        '''
        code
        '''
        if True:
            result_dict['log_msg'] = '분석 진행 도중 예외 문구 입력 가능'
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '전처리 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict

    # =========================================================================
    # 메인 코드2
    try:
        '''
        code
        '''
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '모듈 진행 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    
    # =========================================================================
    # 메인 코드3
    try:
        '''
        code
        '''
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '모듈 결과 생성 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    status = 3
    return status, error_info, error_msg, result_dict