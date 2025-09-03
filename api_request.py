import sys
import os
import json
import ssl
import json
import requests

def main():
    data = {
        "out_var1":111,
        "out_var2":222
    }

    url = "http://localhost:7030/temp"
    # url = "http://localhost:7000/minus"
    # url = "http://localhost:7000/plus"
    # url = "http://211.228.178.190:7000/check"
    
    
    # json_data = json.dumps(data)
    json_data = data
    res = requests.post(url, json=json_data)#, headers=header)
    result_dict = json.loads(res.text)

    status = result_dict['status']
    error_msg = result_dict['error_msg']
    error_info = result_dict['error_info']

    if status == 2:
        print(error_info)
        print(error_msg)
    else:
        result = result_dict['result']
        whole_time = result_dict['전체 소요시간']
        print('---------------------------------')
        print(result)
        print('---------------------------------')
        print(f'전체 소요 시간: {whole_time}')
        print('---------------------------------')
    
    


if __name__ == "__main__":
    print(ssl.OPENSSL_VERSION)
    main()
    
    # =========================================================================
    # datom
    # url = 'https://www.datom.co.kr:8000/refine/execute'
    # url = 'https://www.datom.co.kr:8070/eda/execute'
    # data = {"sn":718}
    
    # =========================================================================
    # smartfarm
    # url = 'http://localhost:7000/sss'
    # url = 'http://59.25.177.42:7070/sssb'
    
    # =========================================================================
    # dataflagship 211.195.9.226
    # url = 'http://localhost:8080/test'
    # data = {"reg_idx":19}
    
    # url = 'http://localhost:8080/retrain'
    # url = 'http://211.195.9.226:7000/retrain'
    # data = {"id":74}
    
    # =========================================================================
    url = "http://10.182.53.73:43401/api/search/searchdslist"
    # curl -X POST "http://10.182.53.73:43401/api/search/searchdslist" 
    # -H "accept: application/json" 
    # -H "Content-Type: application/x-www-form-urlencoded" 
    # -d "{\"resultParam\":{\"dfpt\":[{\"diffi_16\":\"Y\",\"diffi_17\":\"Y\"}],\"pttn\":[{\"normal_37\":\"Y\",\"normal_38\":\"Y\"}],\"prpl\":[{}],\"organ\":[{}],\"twitter\":[{}],\"saeol\":[{\"saeol_1\":\"%EC%83%88%EC%98%AC%EC%8B%9C%EC%8A%A4%ED%85%9C_%EC%8B%9C%EB%8F%84%EC%8B%9C%EC%8A%A4%ED%85%9C_%EC%9D%91%EB%8B%B5%EC%86%8C_%EA%B8%B0%ED%83%80\"}]},\"requestId\":\"\",\"target\":\"pttn%2Cdfpt%2Csaeol\",\"targetCnt\":\"pttn%2Cdfpt%2Csaeol\",\"targetOri\":\"pttn%2Cdfpt%2Csaeol\",\"classification\":\"\",\"userAncCode\":\"\",\"taskId\":\"\",\"petiType\":\"\",\"cvplSe\":\"\",\"rcvPath\":\"\",\"brtcCodeA\":\"\",\"brtcCodeO\":\"\",\"brtcNameAKeyword\":\"\",\"age\":\"\",\"sex\":\"\",\"addr\":\"\",\"petiStatus\":\"\",\"dateKind\":\"\",\"sort\":\"\",\"ancCode\":\"\",\"mainSubCd\":\"\",\"mngAncCd\":\"\",\"mngPcdAncCd\":\"\",\"searchOption\":\"B0060005\",\"pageNo\":1,\"pageUnit\":100,\"pageSize\":10,\"firstIndex\":1,\"lastIndex\":1,\"excelHeaderInfo\":\"\",\"cnrsYn\":\"\",\"schCndDcrt\":\"\",\"id\":\"\",\"contents\":\"\",\"pttnList\":\"\",\"schCond\":\"\",\"schDtKind\":\"\",\"schDtFrom\":\"\",\"schDtTo\":\"\",\"schObj\":\"\",\"pttnClsfKeyword\":\"\",\"pttnClsfCd\":\"\",\"relmCdKeyword\":\"\",\"ocrnCausTyCd\":\"\",\"relmCdL\":\"\",\"relmCdM\":\"\",\"relmCdS\":\"\",\"relmCd\":\"\",\"pttnKind\":\"\",\"pttnClsfKind\":\"\",\"cmitRslnPrcsSctnCd\":\"\",\"partPrcsSctnCd\":\"\",\"stsfdCd\":\"\",\"pttnDeptPrcsSttsCd\":\"\",\"pttnRqstPrcsTyDtlCd\":\"\",\"pttnRqstNo\":\"\",\"pttnRqstPrcsSttsCd\":\"\",\"pttnRqstTitl\":\"\",\"pttnDutySctnCd\":\"\",\"safeYn\":\"\",\"pbstYn\":\"\",\"avoidYn\":\"\",\"mlnpPttnYn\":\"\",\"sctyEntrSctnCd\":\"\",\"mrgYn\":\"\",\"helpYn\":\"\",\"acfrMsnfYn\":\"\",\"wdrwYn\":\"\",\"lwrdNm\":\"\",\"lwrdId\":\"\",\"mmsnfYn\":\"\",\"mmsnfRpsnInstYn\":\"\",\"stsfdCdYn\":\"\",\"stsfdCnfmYn\":\"\",\"addAnswYn\":\"\",\"firStsfdCd\":\"\",\"firMrwdCnfmYn\":\"\",\"firStsfdSltnSttsCd\":\"\",\"lastStsfdCd\":\"\",\"lastMrwdCnfmYn\":\"\",\"lastStsfdSltnSttsCd\":\"\",\"ablYnKeyword\":\"\",\"hqCplnChk\":\"\",\"instCdKind\":\"\",\"deptCdKind\":\"\",\"deptCdKeyword\":\"\",\"pttnRqstPathSctnCd\":\"\",\"epDtlDutySctnCd\":\"\",\"prplPrcsSttsSmryCd\":\"\",\"noKind\":\"\",\"schNo\":\"\",\"prctSttsSctnCd\":\"\",\"prplOrgnSctnCd\":\"\",\"mrgPrplSctnCd\":\"\",\"prplWdrwYn\":\"\",\"prplHelpYn\":\"\",\"prplAcfrMsnfYn\":\"\",\"prplMmsnfYn\":\"\",\"prplMmsnfRpsnInstYn\":\"\",\"sctyPrplYn\":\"\",\"rwrd\":\"\",\"stsfdSltnSttsCd\":\"\",\"stsfdDsctRsnCd\":\"\",\"mrwdCntnCl\":\"\",\"prplRqstNo\":\"\",\"instRcptNo\":\"\",\"rwrdYn\":\"\",\"tmdlExcplRcmnYn\":\"\",\"prcsDeptCdKind\":\"\",\"prcsInstCdKeyword\":\"\",\"prcsInstCdSchKeyword\":\"\",\"prcsPttnRqstPathSctnCd\":\"\",\"instCd\":\"\",\"instBbsKeyword\":\"\",\"pttnRqstPrcsTyCd\":\"\",\"prcsInstNm\":\"\",\"prcsInstCd\":\"\",\"mngInstCdNm\":\"\",\"mngInstCd\":\"\",\"depCodePath\":\"\",\"depCode\":\"\",\"mainSubCodePath\":\"\",\"mainSubCdPath\":\"\",\"docId\":\"\",\"docCnt\":\"\",\"schSctnCd\":\"\",\"schCndNo\":0,\"atchFileSn\":0,\"xlsDwldSctnCd\":\"\",\"atchFileNm\":\"\",\"dplcPttnYn\":\"\",\"collectCd\":\"\",\"classificationMulti\":\"\",\"instPrcsInstCd\":\"\",\"instMngInstCd\":\"\",\"instInstCd\":\"\",\"changeStartPos\":\"\",\"sentiment\":\"\",\"allCheck\":\"\",\"gubun\":\"\",\"kwrdNm\":\"\",\"clstKwrdTitl\":\"\",\"clstKwrdCntn\":\"\",\"asctCnt\":\"\",\"mainSubName\":\"\",\"rsnYn\":\"N\",\"dwldRsn\":\"\",\"userId\":\"\",\"frstRegrId\":\"\",\"lastModrId\":\"\",\"ageParam\":\"\",\"sexParam\":\"\",\"addrParam\":\"\",\"andSearch\":\"\",\"_id\":\"\",\"bmctId\":\"\",\"bcmtText\":\"\",\"dupInfoList\":\"\",\"dupInfoType\":\"\",\"contentLength\":\"\",\"topnKeyword\":\"\",\"documentCnt\":0,\"contentLimit\":0,\"overCount\":0,\"itrsPttnNo\":\"\",\"classificationMainYn\":\"N\",\"flag\":\"\",\"listCount\":0,\"searchword\":\"\",\"searchColumn\":\"_search%2Fuser_id\",\"returnFields\":\"doc_id%2Fcreate_date%2Fclassification_search%2Findex_type%2Fmain_sub_name%2Fmng_anc_name%2Fage%2Fsex%2Fdep_code_path%2Fmain_sub_code_path%2Fgubun%2Fmain_sub_type_name%2Ftitle%2F_search%2Fcontent%2Fanc_reg_date%2Fprcs_stts_nm%2Fnser_name%2Fpttn_ofwk_cd%2Fprcs_cntn%2Fprcs_smry%2Fotln_smry%2Faddr%2Fevent_lat%2Fevent_lon%2Fpttn_rqst_path_cd%2Fprcs_type_cd\",\"omitDuplicate\":\"false\",\"omitSimilar\":\"false\",\"highlightHead\":\"%3Cb%3E\",\"highlightTail\":\"%3C%2Fb%3E\",\"startPos\":1,\"retCount\":10,\"testMode\":\"false\",\"topN\":10000,\"sortBy\":\"\",\"sortOrder\":\"\",\"period\":\"\",\"dateType\":\"C\",\"dateFrom\":\"20221123\",\"dateTo\":\"20221123\",\"rtrnTrg\":\"\"}"
    header = {"Content-Type": 'application/x-www-form-urlencoded'}
    
    
    # # 108
    # url = 'http://59.23.150.172:7000/sss'
    # url = 'http://localhost:7000/sss'
    
    
    
    
