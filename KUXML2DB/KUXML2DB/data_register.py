import logutil
import traceback
from datetime import datetime

class data_register:
    # PostgreSQLにデータをdelete/insert
    def pathology_del_ins(report_url,report_data,conn,cursor):
 
        query = """
INSERT INTO public.pathology_report( 
    path                                        -- パス
    , kmlRepTBF_FileName                        -- ファイル名
    , kmlcm_id                                  -- 患者ID
    , kmlpit_category                           -- 入外区分
    , kmldp_department_kmlcm_id                 -- 診療科コード
    , kmldp_department_kmldp_name               -- 診療科
    , kmlort_doctor_kmlcm_id                    -- 依頼医師コード
    , kmlort_doctor_kmlnm_name_kmlnm_fullname   -- 依頼医師
    , kmlort_category                           -- 検査手法
    , kmlreptbf_specimen                        -- 検体
    , kmlort_disease                            -- 臨床診断
    , kmlort_remark                             -- 臨床所見
    , kmlcom_contents                           -- 病理診断/所見
    , kmlrept_reporter_kmlcm_id                 -- 病理医コード
    , kmlrept_reporter_kmlnm_name_kmlnm_fullname -- 病理医
    , kmlreptbf_appendreporter2                 -- 診断責任者
    , kmlreptbf_receivingdate                   -- 受付日
    , kmlreptbf_samplingdate                    -- 採取日
    , kmlreptbf_version                         -- レポートバージョン
    , kmlreptbf_versionname                     -- レポートバージョン名称
    , kmlreptbf_revision                        -- リビジョン
    , kmlreptbf_phasecode                       -- フェーズコード
    , kmlreptbf_phasename                       -- フェーズ名
) 
VALUES ( 
    %s   -- パス
    , %s -- ファイル名
    , %s -- 患者ID
    , %s -- 入外区分
    , %s -- 診療科コード
    , %s -- 診療科
    , %s -- 依頼医師コード
    , %s -- 依頼医師
    , %s -- 検査手法
    , %s -- 検体
    , %s -- 臨床診断
    , %s -- 臨床所見
    , %s -- 病理診断/所見
    , %s -- 病理医コード
    , %s -- 病理医
    , %s -- 診断責任者
    , %s -- 受付日
    , %s -- 採取日
    , %s -- レポートバージョン
    , %s -- レポートバージョン名称
    , %s -- リビジョン
    , %s -- フェーズコード
    , %s -- フェーズ名
)
        """

        try:
            #同じファイルパスで登録されたデータを削除
            cursor.execute("delete from public.pathology_report where path = %s ",(report_url,))
            logutil.logger.info(f"pathology_del_ins: delete by path :{report_url} deleted count :{cursor.rowcount}")
            #パス内にあるデータをINSERT
            err_cnt = 0
            cnt = 0
            for data in report_data:
                try:
                    cursor.execute(query, (
                        report_url,
                        data['ファイル名'],
                        data['患者ID'],
                        data['入外区分'],
                        data['診療科コード'],
                        data['診療科'],
                        data['依頼医師コード'],
                        data['依頼医師'],
                        data['検査手法'],
                        data['検体'],
                        data['臨床診断'],
                        data['臨床所見'],
                        data['病理診断/所見'],
                        data['病理医コード'],
                        data['病理医'],
                        data['診断責任者'],
                        data['受付日'],
                        data['採取日'],
                        data['レポートバージョン'],
                        data['レポートバージョン名称'],
                        data['リビジョン'],
                        data['フェーズコード'],
                        data['フェーズ名'],
                    ))

                    cnt += 1

                    #単体テスト用例外
                    #if cnt == 100 :
                    #    raise ("test")

                    logutil.logger.debug(f"Insert data {data}")
                    logutil.logger.debug(f"pathology_del_ins: inserted data {data['ファイル名']}")
                except Exception as e:
                    #なんかあったら
                    logutil.logger.error(e)
                    logutil.logger.error(traceback.format_exc())
                    err_cnt += 1
                    #ロールバックもしないし、例外は握りつぶして次のファイルを処理する。（エラーが出すぎる場合は別途検討）
                    #conn.rollback()
                    #raise e

            #すべて入れたらコミット
            conn.commit()
            logutil.logger.info(f"pathology_del_ins: inserted report data by path :{report_url} insert count :{cnt}")

            #でもエラーがある場合には異常終了させる
            if err_cnt > 0 :
                logutil.logger.error(f"###!!!There were { str(err_cnt) } errors when registering data. Please check the log.!!!###")
                raise "There was an error when registering data."

        except Exception as e:
            #全体的な例外は、そのまま丸投げ
            logutil.logger.error(f"pathology_del_ins: Error :{str(e)}")
            raise e


    # 放射線レポート　PostgreSQLにデータをdelete/insert
    def radiology_del_ins(report_url,report_data,conn,cursor):

        query = """
INSERT INTO public.radiology_report( 
    path                                        -- パス
    , filename                                  -- ファイル名
    , kmlcm_id                                  -- 患者ID
    , kmlpit_category                           -- 入外区分
    , kmldp_department_kmlcm_id                 -- 診療科コード
    , kmldp_department_kmldp_name               -- 診療科
    , kmlort_doctor_kmlcm_id                    -- 依頼医師コード
    , kmlort_doctor_kmlnm_name_kmlnm_fullname   -- 依頼医師
    , kmldt_system                              -- 検査実施日時
    , kmlort_category                           -- 目的臓器
    , kmlort_type                               -- 検査術式
    , kmlort_testsite_kmlort_name               -- 検査部位
    , kmlort_clinical_kmlort_disease            -- 臨床病名
    , kmlort_clinical_kmlort_purpose            -- 目的
    , kmlort_clinical_kmlort_remark             -- 臨床経過
    , kmlrept_remark_kmlcom_contents            -- 所見
    , kmlreptbg_riauthor                        -- 報告医
    , kmlrept_status                            -- レポートステータス
    , kmlrept_status_cd                         -- レポートステータスCD
) 
VALUES ( 
    %s    -- パス
    , %s  -- ファイル名
    , %s  -- 患者ID
    , %s  -- 入外区分
    , %s  -- 診療科コード
    , %s  -- 診療科
    , %s  -- 依頼医師コード
    , %s  -- 依頼医師
    , %s  -- 検査実施日時
    , %s  -- 目的臓器
    , %s  -- 検査術式
    , %s  -- 検査部位
    , %s  -- 臨床病名
    , %s  -- 目的
    , %s  -- 臨床経過
    , %s  -- 所見
    , %s  -- 報告医
    , %s  -- レポートステータス
    , %s  -- レポートステータスCD
)
        """

        try:
            #同じファイルパスで登録されたデータを削除
            cursor.execute("delete from public.radiology_report where path = %s ",(report_url,))
            logutil.logger.info(f"radiology_del_ins: delete by path :{report_url} deleted count :{cursor.rowcount}")
            #パス内にあるデータをINSERT
            err_cnt = 0
            cnt = 0
            for data in report_data:
                try:
                    cursor.execute(query, (
                        report_url,
                        data['ファイル名'],
                        data['患者ID'],
                        data['入外区分'],
                        data['診療科コード'],
                        data['診療科'],
                        data['依頼医師コード'],
                        data['依頼医師'],
                        data['検査実施日時'],
                        data['目的臓器'],
                        data['検査術式'],
                        data['検査部位'],
                        data['臨床病名'],
                        data['目的'],
                        data['臨床経過'],
                        data['所見'],
                        data['報告医'],
                        data['レポートステータス'],
                        data['レポートステータスCD'],
                    ))

                    cnt += 1

                    #単体テスト用例外
                    #if cnt == 100 :
                    #    raise ("test")

                    logutil.logger.debug(f"Insert data {data}")
                    logutil.logger.debug(f"radiology_del_ins: inserted data {data['ファイル名']}")
                except Exception as e:
                    #なんかあったら
                    logutil.logger.error(e)
                    logutil.logger.error(traceback.format_exc())
                    err_cnt += 1
                    #ロールバックもしないし、例外は握りつぶして次のファイルを処理する。（エラーが出すぎる場合は別途検討）
                    #conn.rollback()
                    #raise e

            #すべて入れたらコミット
            conn.commit()
            logutil.logger.info(f"radiology_del_ins: inserted report data by path :{report_url} insert count :{cnt}")

            #でもエラーがある場合には異常終了させる
            if err_cnt > 0 :
                logutil.logger.error(f"###!!!There were { str(err_cnt) } errors when registering data. Please check the log.!!!###")
                raise "There was an error when registering data."

        except Exception as e:
            #全体的な例外は、そのまま丸投げ
            logutil.logger.error(f"radiology_del_ins: Error :{str(e)}")
            raise e
