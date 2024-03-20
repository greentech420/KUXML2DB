#使い方
# 以下のような感じでFROMとTOをYYYYMMDDで指定するとその対象のXMLファイルをパースしてDBにDELETE/INSERTします。
# 同じ
# PS C:\KUXML2DB> .\bat\getReport.ps1 20231001 20231231

#引数を変数に格納
$formYYYYMMDD = $Args[0]
$toYYYYMMDD = $Args[1]

#引数を日付に変換
$dt1 = [DateTime]::ParseExact($formYYYYMMDD,"yyyyMMdd", $null);
#echo $dt1
$dt2 = [DateTime]::ParseExact($toYYYYMMDD,"yyyyMMdd", $null);
#echo $dt2
# 2つの日付の差の日数を計算（TimeSpanが返される）
$dt3 = $dt2 - $dt1;
$days = $dt3.Days; 

echo $days

# 開始から終了まで日数でloop
for( $i = 0; $i -le $days; $i++ )
{
    $Date = $dt1.AddDays($i).Date
    $yyyymmdd = (Get-Date $Date -Format "yyyyMMdd")
    python C:\\KUXML2DB\\KUXML2DB\\xml2dbl.py PATHOLOGY \\k7vciswebrpt1\\BF\\$yyyymmdd
    python C:\\KUXML2DB\\KUXML2DB\\xml2dbl.py RADIOLOGY \\k7vciswebrpt1\\BG\\$yyyymmdd
}
