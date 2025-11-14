import sys
import os 
sys.path.append(os.getcwd())
import warnings
warnings.filterwarnings('ignore')

import logie as lo



def main():
    # 실행
    lo.log_sort('/home/gj_anly/kimyh/bus_monitoring_module/log/normal/analysis')
    
    

if __name__ == "__main__":
    main()

