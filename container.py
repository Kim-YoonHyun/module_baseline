import sys
import os 
import json
import time
from datetime import datetime, timedelta

from module import job
from module import resulting as res

from utilskit import timeutils as tiu
from utilskit import utils as u
import logie as lo


def main(run_mode, module_path, src_path, system_path, cf, test, out_var1, out_var2):
    # run 변수

    # 로그 파일 생성
    log_path = os.path.join(module_path, 'log', f'{run_mode}', 'module')
    log = lo.get_logger(
        log_id='module',
        log_path=log_path,
        log_name='total'
    )
    # 현재 시간 기록
    date_now = tiu.get_now('년-월-일 시:분:초')
    date_ = date_now.split(' ')[0]
    now = date_now.split(' ')[1]

    # 테스트용 임의지정
    # date_ = '2025-11-11'
    # now = '13:32:03'

    '''
    status
    0: 대기중
    1: 진행중
    2: 에러
    3: 정상 완료
    '''
    # =========================================================================
    try:
        whole_start = time.time() 
        log.info(f'{date_} {now} 분석 시작')

        # ================================================================
        # 입력 변수 세팅
        args = [
            module_path, src_path, system_path,
            test, date_, now, log
        ]

        # ================================================================
        # 분석 시작
        job_start = time.time()
        status, error_info, error_msg, result_dict = job.job(*args)

        # ================================================================
        # 분석중 에러가 발생한 경우
        if status == 2:
            print(error_info)
            log.error(error_msg)
            log.error(error_info)
            print('wait 5 seconds...')
            time.sleep(5)

        # ================================================================
        # 결과 제어
        log_msg = result_dict['log_msg']
        res.main(
            date_, result_dict,
        )
        
        # ================================================================
        # 분석 중간에 넘어간 경우
        if status == 1:
            log.info(log_msg)

        # ================================================================
        # 분석 종료
        jh, jm, js = tiu.time_measure(time.time() - job_start)
        jhh = str(jh).zfill(2)
        jmm = str(jm).zfill(2)
        jss = str(js).zfill(2)
        log.info(f'분석 종료. 소요시간 = {jhh}시간 {jmm}분 {jss}초')

        # ================================================================
        # 전체 시간 기록
        wh, wm, ws = tiu.time_measure(time.time() - whole_start)
        wh = str(wh).zfill(2)
        wm = str(wm).zfill(2)
        ws = str(ws).zfill(2)
        log.info(f'전체 소요시간: {wh}:{wm}:{ws}\n')
    except Exception:
        print('구역 에러')
        print(u.get_error_info())
        print(error_msg)
        print('실제 에러')
        print(error_info)
        print('비정상 에러 발생')
        