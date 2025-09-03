import sys
import os 
import configparser
import warnings
warnings.filterwarnings('ignore')

import container

DEVELOP = True

'''
스케줄러, API 등의 단순 return 이 불가능한 경우
return 값을 받고 출력하기 위한 함수
'''
def wrapper(*args, **kwargs):
    result_dict = container.main(*args, **kwargs)
    status = result_dict['status']
    error_msg = result_dict['error_msg']
    error_info = result_dict['error_info']

    if status == 2:
        print(error_info)
        print(error_msg)
    else:
        print('분석 완료')


def main():
    # root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_path = os.path.dirname(os.path.abspath(__file__))
    
    config = configparser.ConfigParser()
    if DEVELOP:
        config.read(os.path.join(root_path, 'develop_config.ini'))
    else:
        config.read(os.path.join(root_path, 'config.ini'))
    
    run_mode = config.get('Run', 'run_mode')
    test = config.getboolean('Run', 'test')
    out_var1 = 111
    out_var2 = 222

    # 스케줄러 방식 실행
    if run_mode == 'schedule':
        from apscheduler.schedulers.background import BlockingScheduler

        sched_mode = config.get('Run', 'sched_mode')
        if sched_mode == 'interval':
            sched = BlockingScheduler(timezone='Asia/Seoul')
            # sched.add_job(job_wrapper, 'interval', minutes=5, id='test_1', 
            #               args=[ROOT_PATH, schedule, test, config, fuel_type, mode, clu_vector_db_name, man_vector_db_name, bus])
            sched.add_job(wrapper, 'interval', seconds=5, id='inter_0', 
                          args=[root_path, config, test, out_var1, out_var2])
        elif sched_mode == 'cron':
            hh = config.get('Run', 'hh')
            mm = config.get('Run', 'mm')
            ss = config.get('Run', 'ss')
            sched.add_job(wrapper, 'cron', hour=hh, minute=mm, second=ss, id='cron_0', 
                          args=[root_path, config, test, out_var1, out_var2])
        else:
            raise ValueError('스케줄 모드 설정 에러')
        sched.start()
    # Api 방식 실행
    elif run_mode == 'api':
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        from fastapi.responses import JSONResponse
        from pydantic import BaseModel
        import uvicorn
        app = FastAPI(
            title="API title",
            version="0.1.0",
            # root_path='/path',
            description="""Markdown 문법 내용"""
        )
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        class Item(BaseModel):
            out_var1:int
            out_var2:int

        @app.post("/temp")
        async def run_api(item: Item):
            out_var1 = item.out_var1
            out_var2 = item.out_var2

            result_dict = wrapper(
                root_path=root_path,
                cf=config,
                out_var1=out_var1,
                out_var2=out_var2
            )
            return JSONResponse(content=result_dict)
        
        host = config.get('Run', 'api_host')
        port = config.getint('Run', 'api_port')
        uvicorn.run("run_api:app", host=host, port=port, reload=False)
    # 일반 실행
    else:
        wrapper(
            root_path=root_path,
            cf=config, 
            test=test,
            out_var1=out_var1,
            out_var2=out_var2
        )

   
if __name__ == "__main__":
    main()