import sys
import os
import setting
import logutil 
import psycopg2
import traceback
from datetime import datetime
from file_read import readfile
from parsexml import parsexml
from data_register import data_register

# データベース接続パラメータ
db_params = {
    'host': setting.set_host,
    'database': setting.set_database,
    'user': setting.set_user,
    'password': setting.set_pass,
}

mode_pathology = "PATHOLOGY"
mode_radiology = "RADIOLOGY"
xml_error = False

#メイン処理
def main(report_url):

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    try:
        data = []
        for filename in os.listdir(report_url):
            if filename.endswith('.xml'):
                
                file_path = os.path.join(report_url, filename)

                logutil.logger.info('read:' + file_path)

                #xml読み込み
                root = readfile.read_xml(file_path)

                #xml解析
                report_data = None

                if mode == mode_pathology:
                    report_data = parsexml.pathology_report(root)
                elif mode == mode_radiology:
                    report_data = parsexml.radiology_report(root,filename)
                else:
                    raise "Not implement" # ここには来ないはず
                #logutil.logger.debug(report_data)
                data.append(report_data)
        
        #delete inssert
        if mode == mode_pathology:
            data_register.pathology_del_ins(report_url,data,conn,cursor)
        elif mode == mode_radiology:
            data_register.radiology_del_ins(report_url,data,conn,cursor)
        else:
            raise "Not implement" # ここには来ないはず

    finally:
        #カーソルとコネクションはclose
        cursor.close()
        conn.close()

#初期処理
if __name__ == "__main__":

    
    try:
        # 病理か放射線か？
        mode = sys.argv[1].upper()
        if not ( mode == mode_pathology or mode == mode_radiology ) :
            raise "第一引数は、PATHOLOGYかRADIOLOGYを指定してください"
        # XMLのパス読み込み
        report_url = sys.argv[2]

        logutil.set_logger("xml2db" , mode , os.path.basename(report_url))

        #起動メッセージ
        logutil.logger.info( f"START mode : {mode} path : { report_url }" )

        #メイン呼び出し
        main(report_url)

        #Parseでエラーがあった場合には完走後にraise
        if xml_error == True:
            raise "xml parse error"
        
        #終了メッセージ
        logutil.logger.info( f"END mode : {mode} path : { report_url }" )

    except Exception as e:
        logutil.logger.error(e)
        logutil.logger.error(traceback.format_exc())

        print("USAGE:")
        print("コマンド例.病理レポートの場合")
        print("> python C:\\\\KUXML2DB\\\\KUXML2DB\\\\xml2dbl.py PATHOLOGY C:\\\\iqvia\\\\xmldevfiles\\\\20231220")
        print("")
        print("コマンド例.放射線レポートの場合")
        print("> python C:\\\\KUXML2DB\\\\KUXML2DB\\\\xml2dbl.py RADIOLOGY C:\\\\iqvia\\\\xmldevfiles\\\\20231220")

        sys.exit(1)