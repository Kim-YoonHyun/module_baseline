import sys
import os 
import configparser
import warnings
warnings.filterwarnings('ignore')

from analy_module import container

DEVELOP = True


def main():
    # root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # root_path = os.path.dirname(os.path.abspath(__file__))
    
    # config 읽기
    config = configparser.ConfigParser()
    # 개발 설정
    if DEVELOP:
        config.read(os.path.join(root_path, 'develop_config.ini'))
    # 운영 설정
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
            sched.add_job(container.main, 'interval', minutes=5, id='inter_0', 
            # sched.add_job(container.main, 'interval', seconds=5, id='inter_0', 
                          args=[run_mode, root_path, config, test, out_var1, out_var2])
        elif sched_mode == 'cron':
            hh = config.get('Run', 'hh')
            mm = config.get('Run', 'mm')
            ss = config.get('Run', 'ss')
            sched.add_job(container.main, 'cron', hour=hh, minute=mm, second=ss, id='cron_0', 
                          args=[run_mode, root_path, config, test, out_var1, out_var2])
        else:
            print(f"Schedule mode '{sched_mode}' does not exist. Please choose one of: interval, cron")
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

            result_dict = container.main(
                run_mode=run_mode,
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
    elif run_mode == 'normal':
        container.main(
            run_mode=run_mode,
            root_path=root_path,
            cf=config, 
            test=test,
            out_var1=out_var1,
            out_var2=out_var2
        )
    else:
        print(f"Run mode '{run_mode}' does not exist. Please choose one of: schedule, api, or normal")
        raise ValueError('실행 모드 설정 에러')

   
if __name__ == "__main__":
    main()