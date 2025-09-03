import sys
import os 
import time

from utilskit import timeutils as tiu
from utilskit import utils as u
import logie as lo

import job


def main(root_path, cf, test, out_var1, out_var2):
    # 로그 파일 생성
    log_path = os.path.join(root_path, 'log')
    log = lo.get_logger(
        log_path=log_path,
        log_name='analysis'
    )
    # 현재 시간
    date_ = tiu.get_now('년-월-일')
    now = tiu.get_now('시:분:초')

    '''
    status
    0: 대기중
    1: 진행중
    2: 에러
    3: 정상 완료
    '''
    try:
        whole_start = time.time() 

        # 실행
        # 그룹별 진행
        status, error_info, error_msg, result_dict = job.job(
            root_path=root_path,
            cf=cf,
            test=test,
            date_=date_,
            now=now,
            out_var1=out_var1,
            out_var2=out_var2,
            log=log
        )
        result_dict['status'] = status
        result_dict['error_info'] = error_info
        result_dict['error_msg'] = error_msg
        
        # 전체 시간 기록
        wh, wm, ws = tiu.time_measure(time.time() - whole_start)
        wh = str(wh).zfill(2)
        wm = str(wm).zfill(2)
        ws = str(ws).zfill(2)
        log.info(f'전체 소요시간: {wh}:{wm}:{ws}\n')
        result_dict['전체 소요시간'] = f'{wh}:{wm}:{ws}'
        return result_dict

    except Exception:
        result_dict = {
            'status':2,
            'error_msg':'의도치 않은 에러 발생',
            'error_info':u.get_error_info()
        }
    return result_dict