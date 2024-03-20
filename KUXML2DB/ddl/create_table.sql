DROP TABLE IF EXISTS pathology_report;
CREATE TABLE pathology_report (
  id  SERIAL PRIMARY KEY , 
  path text ,                       --パス
  kmlRepTBF_FileName text ,         --ファイル名
  kmlCm_Id text ,                   --患者ID
  kmlPiT_Category text ,            --入外区分
  kmlDp_Department_kmlCm_Id text ,  --診療科コード
  kmlDp_Department_kmlDp_Name text ,--診療科
  kmlOrT_Doctor_kmlCm_Id text ,     --依頼医師コード
  kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName text , --依頼医師
  kmlOrT_Category text ,            --検査手法
  kmlRepTBF_Specimen text ,         --検体
  kmlOrT_Disease text ,             --臨床診断
  kmlOrT_Remark text ,              --臨床所見
  kmlCom_Contents text ,            --病理診断/所見
  kmlRepT_Reporter_kmlCm_Id text ,  --病理医コード
  kmlRepT_Reporter_kmlNm_Name_kmlNm_FullName text , --病理医
  kmlRepTBF_AppendReporter2 text ,  --診断責任者
  kmlRepTBF_ReceivingDate text ,    --受付日
  kmlRepTBF_SamplingDate text ,     --採取日
  kmlRepTBF_Version text ,          --レポートバージョン
  kmlRepTBF_VersionName text ,      --レポートバージョン名称
  kmlRepTBF_Revision text ,         --リビジョン
  kmlRepTBF_PhaseCode text ,        --フェーズコード
  kmlRepTBF_PhaseName text ,        --フェーズ名
  create_timestamp timestamp default CURRENT_TIMESTAMP 
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
COMMENT ON COLUMN pathology_report.path IS 'パス';
COMMENT ON COLUMN pathology_report.kmlRepTBF_FileName IS 'ファイル名';
COMMENT ON COLUMN pathology_report.kmlCm_Id IS '患者ID';
COMMENT ON COLUMN pathology_report.kmlPiT_Category IS '入外区分';
COMMENT ON COLUMN pathology_report.kmlDp_Department_kmlCm_Id IS '診療科コード';
COMMENT ON COLUMN pathology_report.kmlDp_Department_kmlDp_Name IS '診療科';
COMMENT ON COLUMN pathology_report.kmlOrT_Doctor_kmlCm_Id IS '依頼医師コード';
COMMENT ON COLUMN pathology_report.kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName IS '依頼医師';
COMMENT ON COLUMN pathology_report.kmlOrT_Category IS '検査手法';
COMMENT ON COLUMN pathology_report.kmlRepTBF_Specimen IS '検体';
COMMENT ON COLUMN pathology_report.kmlOrT_Disease IS '臨床診断';
COMMENT ON COLUMN pathology_report.kmlOrT_Remark IS '臨床所見';
COMMENT ON COLUMN pathology_report.kmlCom_Contents IS '病理診断/所見';
COMMENT ON COLUMN pathology_report.kmlRepT_Reporter_kmlCm_Id IS '病理医コード';
COMMENT ON COLUMN pathology_report.kmlRepT_Reporter_kmlNm_Name_kmlNm_FullName IS '病理医';
COMMENT ON COLUMN pathology_report.kmlRepTBF_AppendReporter2 IS '診断責任者';
COMMENT ON COLUMN pathology_report.kmlRepTBF_ReceivingDate IS '受付日';
COMMENT ON COLUMN pathology_report.kmlRepTBF_SamplingDate IS '採取日';
COMMENT ON COLUMN pathology_report.kmlRepTBF_Version IS 'レポートバージョン';
COMMENT ON COLUMN pathology_report.kmlRepTBF_VersionName IS 'レポートバージョン名称';
COMMENT ON COLUMN pathology_report.kmlRepTBF_Revision IS 'リビジョン';
COMMENT ON COLUMN pathology_report.kmlRepTBF_PhaseCode IS 'フェーズコード';
COMMENT ON COLUMN pathology_report.kmlRepTBF_PhaseName IS 'フェーズ名';

DROP TABLE IF EXISTS radiology_report;
CREATE TABLE radiology_report (
  id  SERIAL PRIMARY KEY , 
  path text ,                       --パス
  fileName text ,                   --ファイル名
  kmlCm_Id text ,                   --患者ID
  kmlPiT_Category text ,            --入外区分
  kmlDp_Department_kmlCm_Id text ,  --診療科コード
  kmlDp_Department_kmlDp_Name text ,--診療科
  kmlOrT_Doctor_kmlCm_Id text ,     --依頼医師コード
  kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName text , --依頼医師
  kmlDt_System text ,               --検査実施日時
  kmlOrT_Category text ,            --目的臓器
  kmlOrT_Type text ,                --検査術式
  kmlOrT_TestSite_kmlOrT_Name text ,--検査部位
  kmlOrT_Clinical_kmlOrT_Disease text , --臨床病名
  kmlOrT_Clinical_kmlOrT_Purpose text , --目的
  kmlOrT_Clinical_kmlOrT_Remark text ,  --臨床経過
  kmlRepT_Remark_kmlCom_Contents text , --所見
  kmlRepTBG_RIAuthor text ,         --報告医
  kmlRepT_Status text ,             --レポートステータス
  kmlRepT_Status_CD text ,          --レポートステータスCD
  create_timestamp timestamp default CURRENT_TIMESTAMP 
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

COMMENT ON COLUMN radiology_report.path IS 'パス';
COMMENT ON COLUMN radiology_report.FileName IS 'ファイル名';
COMMENT ON COLUMN radiology_report.kmlCm_Id IS '患者ID';
COMMENT ON COLUMN radiology_report.kmlPiT_Category IS '入外区分';
COMMENT ON COLUMN radiology_report.kmlDp_Department_kmlCm_Id IS '診療科コード';
COMMENT ON COLUMN radiology_report.kmlDp_Department_kmlDp_Name IS '診療科';
COMMENT ON COLUMN radiology_report.kmlOrT_Doctor_kmlCm_Id IS '依頼医師コード';
COMMENT ON COLUMN radiology_report.kmlOrT_Doctor_kmlNm_Name_kmlNm_FullName IS '依頼医師';
COMMENT ON COLUMN radiology_report.kmlDt_System IS '検査実施日時';
COMMENT ON COLUMN radiology_report.kmlOrT_Category IS '目的臓器';
COMMENT ON COLUMN radiology_report.kmlOrT_Type IS '検査術式';
COMMENT ON COLUMN radiology_report.kmlOrT_TestSite_kmlOrT_Name IS '検査部位';
COMMENT ON COLUMN radiology_report.kmlOrT_Clinical_kmlOrT_Disease IS '臨床病名';
COMMENT ON COLUMN radiology_report.kmlOrT_Clinical_kmlOrT_Purpose IS '目的';
COMMENT ON COLUMN radiology_report.kmlOrT_Clinical_kmlOrT_Remark IS '臨床経過';
COMMENT ON COLUMN radiology_report.kmlRepT_Remark_kmlCom_Contents IS '所見';
COMMENT ON COLUMN radiology_report.kmlRepTBG_RIAuthor IS '報告医';
COMMENT ON COLUMN radiology_report.kmlRepT_Status IS 'レポートステータス';
COMMENT ON COLUMN radiology_report.kmlRepT_Status_CD IS 'レポートステータスCD';
