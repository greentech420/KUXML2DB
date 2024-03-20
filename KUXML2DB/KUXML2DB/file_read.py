import xml.etree.ElementTree as ET
import logutil
from datetime import datetime

class readfile:
    # XMLファイルを読み込む関数
    def read_xml(file_path):
        try:
            with open(file_path, encoding="cp932") as file:
                xml = file.read()
                
            root = ET.fromstring(xml)
            return root
        except Exception as e:
            global xml_error
            xml_error = False
            logutil.logger.error(f"Error read_xml file_path {file_path} : {str(e)}")
            #raise e パース失敗はエラーフラグ立てて握りつぶす