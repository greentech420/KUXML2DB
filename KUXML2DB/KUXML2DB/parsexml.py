import logutil
from datetime import datetime

class parsexml:
    # XMLファイルを解析してデータを抽出する関数
    def pathology_report(root):
        global xml_error
        try:
            report_data = []
            #print(root.findtext("./kmlBody/kml_Title"))
            kmlRepTBF_FileName =        root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_FileName") #ファイル名
            kmlCm_Id =                  root.findtext("./kmlBody/kmlPiT_PatientModule/kmlCm_Id") #患者ID
            kmlPiT_Category =           root.findtext("./kmlBody/kmlPiT_PatientModule/kmlPiT_Category") #多分入外区分
            kmlDp_Department_kmlCm_Id = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Department/kmlDp_Department/kmlCm_Id") #多分診療科コード
            kmlDp_Department_kmlDp_Name = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Department/kmlDp_Department/kmlDp_Name") #診療科名称
            kmlOrT_Doctor_kmlCm_Id =    root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Doctor/kmlCm_Id") #依頼医師コード
            kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Doctor/kmlNm_Name/kmlNm_FullName") #依頼医師
            kmlOrT_Category =           root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Category") #検査手法
            kmlRepTBF_Specimen =        root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_Specimen") #検体
            # specimens =                 root.findall("./kmlBody/kmlOrT_OrderModule/kmlOrT_Type") #検体
            # kmlOrT_Type = ""
            # for specimen in specimens:
            #     kmlOrT_Type = kmlOrT_Type + specimen.text + ","
            # kmlOrT_Type = kmlOrT_Type[:-1]
            kmlOrT_Disease =            root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Clinical/kmlOrT_Disease") #臨床診断
            kmlOrT_Remark =             root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Clinical/kmlOrT_Remark") #臨床所見
            kmlCom_Contents =           root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Diagnosis/kmlCom_Comment/kmlCom_Contents") #病理診断/所見
            kmlRepTBF_ReceivingDate =   root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_ReceivingDate/kmlDt_Date/kmlDt_System") #受付日
            kmlRepTBF_SamplingDate =    root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_SamplingDate/kmlDt_Date/kmlDt_System") #採取日
            kmlRepT_Reporter_kmlCm_Id =    root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Reporter/kmlCm_Id") #病理医コード
            kmlRepT_Reporter_kmlNm_Name_kmlNm_FullName =    root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Reporter/kmlNm_Name/kmlNm_FullName") #病理医
            kmlRepTBF_AppendReporter2 = root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_AppendReporter2") #診断責任者
            kmlRepTBF_Version =         root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_Version") #レポートバージョン
            kmlRepTBF_VersionName =     root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_VersionName") #改定理由？
            kmlRepTBF_Revision =        root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_Revision") #リビジョン？
            kmlRepTBF_PhaseCode =       root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_PhaseCode") #フェーズコード
            kmlRepTBF_PhaseName =       root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBF_Domain/kmlRepTBF_PhaseName") #フェーズ名
            '''
            logger.debug("ファイル名:"+ kmlRepTBF_FileName) 
            logger.debug("患者ID:"+ kmlCm_Id) 
            logger.debug("多分入外区分:"+ kmlPiT_Category) 
            logger.debug("多分診療科コード:"+ kmlDp_Department_kmlCm_Id) 
            logger.debug("診療科名称:"+ kmlDp_Department_kmlDp_Name) 
            logger.debug("依頼医師コード:"+ kmlOrT_Doctor_kmlCm_Id) 
            logger.debug("依頼医師:"+ kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName) 
            logger.debug("検査手法:"+ kmlOrT_Category) 
            logger.debug("検体:"+ kmlRepTBF_Specimen) 
            logger.debug("臨床診断:"+ kmlOrT_Disease) 
            logger.debug("臨床所見:"+ kmlOrT_Remark) 
            logger.debug("病理診断/所見:"+ kmlCom_Contents) 
            logger.debug("病理医コード:"+ kmlRepT_Reporter_kmlCm_Id) 
            logger.debug("病理医:"+ kmlRepT_Reporter_kmlNm_Name_kmlNm_FullName) 
            logger.debug("診断責任者:"+ kmlRepTBF_AppendReporter2) 
            logger.debug("受付日:"+ kmlRepTBF_ReceivingDate) 
            logger.debug("採取日:"+ kmlRepTBF_SamplingDate) 
            logger.debug("レポートバージョン:"+ kmlRepTBF_Version) 
            logger.debug("レポートバージョン名称:"+ kmlRepTBF_VersionName) 
            logger.debug("リビジョン:"+ kmlRepTBF_Revision) 
            logger.debug("フェーズコード:"+ kmlRepTBF_PhaseCode) 
            logger.debug("フェーズ名:"+ kmlRepTBF_PhaseName)
            '''
            dic = { 'ファイル名':kmlRepTBF_FileName
                    ,'患者ID':kmlCm_Id
                    ,'入外区分':kmlPiT_Category
                    ,'診療科コード':kmlDp_Department_kmlCm_Id
                    ,'診療科':kmlDp_Department_kmlDp_Name
                    ,'依頼医師コード':kmlOrT_Doctor_kmlCm_Id
                    ,'依頼医師':kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName
                    ,'検査手法':kmlOrT_Category
                    ,'検体':kmlRepTBF_Specimen
                    ,'臨床診断':kmlOrT_Disease
                    ,'臨床所見':kmlOrT_Remark
                    ,'病理診断/所見':kmlCom_Contents
                    ,'病理医コード':kmlRepT_Reporter_kmlCm_Id
                    ,'病理医':kmlRepT_Reporter_kmlNm_Name_kmlNm_FullName
                    ,'診断責任者':kmlRepTBF_AppendReporter2
                    ,'受付日':kmlRepTBF_ReceivingDate
                    ,'採取日':kmlRepTBF_SamplingDate
                    ,'レポートバージョン':kmlRepTBF_Version
                    ,'レポートバージョン名称':kmlRepTBF_VersionName
                    ,'リビジョン':kmlRepTBF_Revision
                    ,'フェーズコード':kmlRepTBF_PhaseCode
                    ,'フェーズ名':kmlRepTBF_PhaseName
            }
            return dic
        except Exception as e:
            global xml_error
            xml_error = False
            logutil.logger.error(f"Error parse_xml root:{root}")
#            raise e パースエラーのログのみ出力してスキップ

    def radiology_report(root,filename):
        global xml_error
        try:
            report_data = []
            #print(root.findtext("./kmlBody/kml_Title"))
            FileName =                  filename #ファイル名
            kmlCm_Id =                  root.findtext("./kmlBody/kmlPiT_PatientModule/kmlCm_Id") #患者ID
            kmlPiT_Category =           root.findtext("./kmlBody/kmlPiT_PatientModule/kmlPiT_Category") #多分入外区分
            kmlDp_Department_kmlCm_Id = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Department/kmlDp_Department/kmlCm_Id") #多分診療科コード
            kmlDp_Department_kmlDp_Name = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Department/kmlDp_Department/kmlDp_Name") #診療科名称
            kmlOrT_Doctor_kmlCm_Id =    root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Doctor/kmlCm_Id") #依頼医師コード
            kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Source/kmlOrT_Doctor/kmlNm_Name/kmlNm_FullName") #依頼医師
            kmlDt_System =              root.findtext("./kmlBody/kmlOpeT_OperationModule/kmlDt_Date/kmlDt_System") #検査実施日時
            kmlOrT_Category =           root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Category") #目的臓器
            kmlOrT_Type =               root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Type") #検査術式?
            kmlOrT_TestSite_kmlOrT_Name = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_TestSite/kmlOrT_Name") #検査部位
            kmlOrT_Clinical_kmlOrT_Disease = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Clinical/kmlOrT_Disease") #臨床病名
            kmlOrT_Clinical_kmlOrT_Purpose = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Clinical/kmlOrT_Purpose") #目的
            kmlOrT_Clinical_kmlOrT_Remark = root.findtext("./kmlBody/kmlOrT_OrderModule/kmlOrT_Clinical/kmlOrT_Remark")#臨床経過
            kmlRepT_Remark_kmlCom_Contents = root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Remark/kmlCom_Comment/kmlCom_Contents") #所見
            kmlRepT_Diagnosis_kmlCom_Contents = root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Diagnosis/kmlCom_Comment/kmlCom_Contents") #要約
            kmlRepTBG_RIAuthor = root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepTBG_RIAuthor") #報告医
            kmlRepT_Status = root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Status/kmlRepT_Display") #ステータス
            kmlRepT_Status_CD = root.findtext("./kmlBody/kmlRepT_ReportModule/kmlRepT_Status/kmlRepT_Data") #ステータス

            dic = { 'ファイル名':FileName
                    ,'患者ID':kmlCm_Id
                    ,'入外区分':kmlPiT_Category
                    ,'診療科コード':kmlDp_Department_kmlCm_Id
                    ,'診療科':kmlDp_Department_kmlDp_Name
                    ,'依頼医師コード':kmlOrT_Doctor_kmlCm_Id
                    ,'依頼医師':kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName
                    ,'検査実施日時':kmlDt_System
                    ,'目的臓器':kmlOrT_Category
                    ,'検査術式':kmlOrT_Type
                    ,'検査部位':kmlOrT_TestSite_kmlOrT_Name
                    ,'臨床病名':kmlOrT_Clinical_kmlOrT_Disease
                    ,'目的':kmlOrT_Clinical_kmlOrT_Purpose
                    ,'臨床経過':kmlOrT_Clinical_kmlOrT_Remark
                    ,'所見':kmlRepT_Remark_kmlCom_Contents
                    ,'報告医':kmlRepTBG_RIAuthor
                    ,'レポートステータス':kmlRepT_Status
                    ,'レポートステータスCD':kmlRepT_Status_CD
            }
            logutil.logger.debug(f"Dic:{dic}")
            return dic
        except Exception as e:
            global xml_error
            xml_error = False
            logutil.logger.error(f"Error parse_xml root:{root}")

