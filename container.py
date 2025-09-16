import sys
import os 
import time
from datetime import datetime, timedelta

from utilskit import timeutils as tiu
from utilskit import utils as u
import logie as lo


import job


def main(run_mode, root_path, cf, test, out_var1, out_var2):
    # run
    push_example = cf.getboolean('Run', 'push_example')

    _in_var1 = cf.get('InTemp', '_in_var1') # 기본 (str)
    _in_var1 = cf['InTemp']['_in_var1'] # 기본 (str)
    _in_var2 = cf.getint('InTemp', '_in_var2') # int
    _in_var3 = cf.getfloat('InTemp', '_in_var3') # float
    _in_var4 = cf.getboolean('InTemp', '_in_var4') # bool type

    # 로그 파일 생성
    log_path = os.path.join(root_path, 'log', f'{run_mode}', 'module_baseline')
    log = lo.get_logger(
        log_id='baseline',
        log_path=log_path,
        log_name='total'
    )
    # 현재 시간
    date_ = tiu.get_now('년-월-일')
    now = tiu.get_now('시:분:초')

    # 진행 시간 리스트화
    if not push_example:
        now_list = [now]
    else:
        #==
        # date_ = '2025-09-09'
        # now = '08:24:01'
        now = '08:31:01'
        now_list = []
        while True:
            if int(now.replace(':', '')) > 90000:
            # if int(now.replace(':', '')) > 201106:
            # if int(now.replace(':', '')) > 174106:
                break
            now_list.append(now)
            s_time = f'{date_} {now}'
            s_time = datetime.strptime(s_time, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=5)
            s_time = datetime.strftime(s_time, '%Y-%m-%d %H:%M:%S')
            now = s_time.split(' ')[1]
    
    '''
    status
    0: 대기중
    1: 진행중
    2: 에러
    3: 정상 완료
    '''
    try:
        for now in now_list:
            whole_start = time.time() 
            log.info(f'{date_} {now} 분석 시작')

            # 테스트 설정
            if test:
                pass
            else:
                pass

            # 입력 변수 세팅
            args = [
                root_path, test, date_, now, log, push_example
            ]

            # ================================================================
            # 분석 시작
            job_start = time.time()
            status, error_info, error_msg, result_dict = job.job(*args)

            # ================================================================
            # 결과 처리
            log_msg = result_dict['log_msg']
            '''
            code
            '''

            # ================================================================
            # 분석 중간에 넘어간 경우
            if status == 1:
                log.info(f'<로그내용> --> {log_msg}')
                continue

            # ================================================================
            # 분석중 에러가 발생한 경우
            if status == 2:
                print(error_info)
                log.error(f'<로그내옹> --> {error_msg}')
                print('wait 5 seconds...')
                time.sleep(5)
                continue

            # ===============================================================
            # 분석 종료
            jh, jm, js = tiu.time_measure(time.time() - job_start)
            jhh = str(jh).zfill(2)
            jmm = str(jm).zfill(2)
            jss = str(js).zfill(2)
            log.info(f'분석 종료. 소요시간 = {jhh}시간 {jmm}분 {jss}초')

        # ===============================================================
        # 전체 시간 기록
        wh, wm, ws = tiu.time_measure(time.time() - whole_start)
        wh = str(wh).zfill(2)
        wm = str(wm).zfill(2)
        ws = str(ws).zfill(2)
        log.info(f'전체 소요시간: {wh}:{wm}:{ws}\n')

    except Exception:
        print(u.get_error_info())
        print('비정상 에러 발생')