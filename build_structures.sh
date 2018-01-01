#!/bin/bash
download=0
tidy=1
removepack=0
while [ "$1" != "" ]; do
    case $1 in
        -d | --download )       download=1
                                ;;
        -t | --donttidy )       tidy=0
                                ;;
	-p | --removepack )      removepack=1
    esac
    shift
done
if [ "$download" = "1" ]; then
    wget https://developer.nhs.uk/wp-content/uploads/2017/06/Requirements-Pack-4.zip -O requirementspack.zip
    unzip requirementspack.zip
    unzip ./Requirements\ Pack/PDSMiniServices.zip -d ./Requirements\ Pack
    if [ "$tidy" = "1" ];then
	rm requirementspack.zip
    fi
fi
generateDS -f -o getPatientDetailsReq.py -f  --cleanup-name-list="[('[-:.]', '_'),('QUPA_MT000005GB01_','')]" ./Requirements\ Pack/PDSMiniServices/Schemas/QUPA_MT000005GB01.xsd
generateDS -f -o getPatientDetailsBySearchReq.py  --cleanup-name-list="[('[-:.]', '_'),('QUPA_MT000004GB01_','')]" -f ./Requirements\ Pack/PDSMiniServices/Schemas/QUPA_MT000004GB01.xsd
generateDS -f -o getPatientDetailsByNHSNumberReq.py --cleanup-name-list="[('[-:.]', '_'),('QUPA_MT000003GB01_','')]"  -f ./Requirements\ Pack/PDSMiniServices/Schemas/QUPA_MT000003GB01.xsd
generateDS -f -o getNHSNumberReq.py --cleanup-name-list="[('[-:.]', '_'),('QUPA_MT000002GB01_','')]" -f ./Requirements\ Pack/PDSMiniServices/Schemas/QUPA_MT000002GB01.xsd
generateDS -f -o verifyNHSNumberReq.py  --cleanup-name-list="[('[-:.]', '_'),('QUPA_MT000001GB01_','')]" -f ./Requirements\ Pack/PDSMiniServices/Schemas/QUPA_MT000001GB01.xsd
generateDS -f -o verifyNHSNumberResp.py  --cleanup-name-list="[('[-:.]', '_'),('COMT_MT000013GB01_','')]" -f ./Requirements\ Pack/PDSMiniServices/Schemas/COMT_MT000013GB01.xsd
generateDS -f -o getNHSNumberResp.py  --cleanup-name-list="[('[-:.]', '_'),('COMT_MT000014GB01_','')]" -f ./Requirements\ Pack/PDSMiniServices/Schemas/COMT_MT000014GB01.xsd
generateDS -f -o getPatientDetailsResp.py  --cleanup-name-list="[('[-:.]', '_'),('COMT_MT000016GB01_','')]" -f ./Requirements\ Pack/PDSMiniServices/Schemas/COMT_MT000016GB01.xsd
mkdir built
python cleanup.py
cp built/common_itk.py ./smsp
cp built/smsp_itk.py ./smsp
if [ "$tidy" = "1" ];then
    rm getPatientDetailsReq.py
    rm getPatientDetailsBySearchReq.py
    rm getPatientDetailsByNHSNumberReq.py
    rm getNHSNumberReq.py
    rm verifyNHSNumberReq.py
    rm verifyNHSNumberResp.py
    rm getNHSNumberResp.py
    rm getPatientDetailsResp.py
    rm -f -r built
fi
if [ "$removepack" = "1" ];then
    rm -r ./Requirements\ Pack
fi

