# 2025-11-14 ver 2.0
- module 개발 라이브러리 구조 대폭 변경
1. 일반, API, 스케줄러 3가지 방식 중 택1 하여 모듈을 돌리는 방식을 정하는 run.py
2. log 생성 및 job 에 필요한 args 를 구성하고 job 자체의 기동 및 결과를 리턴받는 container.py
3. 모듈의 실제 분석 작업을 진행하는 job.py
4. 결과에 대한 제어(기록, 저장 등)를 담당하는 resulting.py
5. 자체 모듈 코드를 두는 utils 폴더
6. resource 외에 임의로 필요한 데이터 모음 extra_data
7. 모듈의 버전을 명시하면서 동시에 manifest.json 을 통한 버전을 입력받는 \__version__.py 
8. \__init__.py 를 통한 모듈화 명시
9. requirements.txt
- 위의 구조는 system 의 src 폴더 내에 module 이 있는 것을 가정하여 만들어진 구조이다.
- 본 모듈은 기본적으로 자체 구축 패키지인 utilskit, logie 패키지를 사용하는 것을 전제로 한다.
- 모듈 실행 방법
```cmd
cd path/to/system/src
python -m module.run
```