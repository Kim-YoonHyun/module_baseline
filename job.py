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


def job(root_path, cf, test, date_, now, out_var1, out_var2, log):
    start = time.time()

    _in_var1 = cf.get('InTemp', '_in_var1') # 기본 (str)
    in_var1 = cf['InTemp']['_in_var1'] # 기본 (str)

    _in_var2 = cf.getint('InTemp', '_in_var2') # int
    _in_var3 = cf.getfloat('InTemp', '_in_var3') # float
    _in_var4 = cf.getboolean('InTemp', '_in_var4') # bool type

    # custom path
    save_path = cf['Path']['save_path']
    root_data_path = cf['Path']['root_data_path']
    
    status, error_info, error_msg, result_dict = 1, '', '', {'result':None}
    # =========================================================================
    # 저장 경로 생성
    os.makedirs(save_path, exist_ok=True)

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
        result = f'외부 변수: {out_var1}, {out_var2}, 내부변수: {_in_var1}, {_in_var2}, {_in_var3}, {_in_var4}'
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '모듈 진행 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict
    
    # =========================================================================
    # 결과 기록
    try:
        pass
        # t = time.time() - start
        # hh, mm, ss = tiu.time_measure(t)
        # result_dict = {
        #     'result':result,
        #     '모듈 진행시간':f"{hh}시간 {mm}분 {ss}초"
        # }
        # with open(f'{save_path}/result_name.json', 'w', encoding='utf-8-sig') as f:
        #     json.dump(result_dict, f, indent='\t', ensure_ascii=False)
    except Exception:
        status = 2
        error_info = u.get_error_info()
        error_msg = '최종 결과 저장 중 에러가 발생하였습니다.'
        return status, error_info, error_msg, result_dict

    status = 3
    return status, error_info, error_msg, result_dict