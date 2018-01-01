from smsp import smsp_itk
from smsp import smsp_utils
from smsp import common_itk

def verifyNHSNumberRequest(nhs_number,dob,family_name=None,given_name=None):
    dob = smsp_utils.build_person_dob(dob)
    person_name = smsp_utils.build_person_name(given_name,family_name)
    nnn = smsp_utils.build_person_nhsnumber(nhs_number)
    
    queryEvent = smsp_itk.verifyNHSNumberRequest_v1_0Grouper.factory(
        Person_NHSNumber=nnn,
        Person_DateOfBirth=dob,
        Person_Name=person_name)
    id_ = smsp_utils.build_id("3E25ACE2-23F8-4A37-B446-6A37F31BF77C")
    code = smsp_utils.build_coded_value("verifyNHSNumberRequest-v1-0","2.16.840.1.113883.2.1.3.2.4.17.284")
    
    verify_nhs_number_request = smsp_itk.verifyNHSNumberRequest_v1_0.factory(
        queryEvent=queryEvent,
        moodCode="EVN",
        classCode="CACT",
        id=id_,
        code=code)
    verify_nhs_number_request.original_tagname_="verifyNHSNumberRequest-v1-0"

    return smsp_utils.object_to_xml(verify_nhs_number_request)

def getNHSNumberRequest(dob,gender,family_name,given_name=None,postcode=None):
    dob = smsp_utils.build_person_dob(dob)
    gender = smsp_utils.build_person_gender(gender)
    person_name = smsp_utils.build_person_name(given_name,family_name)
    postcode = smsp_utils.build_person_postcode(postcode)

    queryEvent = smsp_itk.getNHSNumberRequest_v1_0Grouper.factory(
        Person_DateOfBirth=dob,
        Person_Gender=gender,
        Person_Name=person_name,
        Person_Postcode=postcode)

    id_ = smsp_utils.build_id("3E25ACE2-23F8-4A37-B446-6A37F31BF77C")
    code = smsp_utils.build_coded_value("getNHSNumberRequest-v1-0","2.16.840.1.113883.2.1.3.2.4.17.284")
    
    get_nhs_number_request = smsp_itk.getNHSNumberRequest_v1_0.factory(
        queryEvent=queryEvent,
        moodCode="EVN",
        classCode="CACT",
        id=id_,
        code=code)
    get_nhs_number_request.original_tagname_="getNHSNumberRequest-v1-0"

    return smsp_utils.object_to_xml(get_nhs_number_request)

def getPatientDetailsByNHSNumberRequest(nhs_number,dob,family_name=None,given_name=None):
    dob = smsp_utils.build_person_dob(dob)
    person_name = smsp_utils.build_person_name(given_name,family_name)
    nnn = smsp_utils.build_person_nhsnumber(nhs_number)
    
    queryEvent = smsp_itk.getPatientDetailsByNHSNumberRequest_v1_0Grouper.factory(
        Person_NHSNumber=nnn,
        Person_DateOfBirth=dob,
        Person_Name=person_name)
    id_ = smsp_utils.build_id("3E25ACE2-23F8-4A37-B446-6A37F31BF77C")
    code = smsp_utils.build_coded_value("getPatientDetailsByNHSNumberRequest-v1-0","2.16.840.1.113883.2.1.3.2.4.17.284")
    
    get_details_by_nhs_number_request = smsp_itk.getPatientDetailsByNHSNumberRequest_v1_0.factory(
        queryEvent=queryEvent,
        moodCode="EVN",
        classCode="CACT",
        id=id_,
        code=code)
    get_details_by_nhs_number_request.original_tagname_="getPatientDetailsByNHSNumberRequest-v1-0"

    return smsp_utils.object_to_xml(get_details_by_nhs_number_request)

def getPatientDetailsBySearchRequest(dob,gender,family_name,given_name=None,postcode=None):
    dob = smsp_utils.build_person_dob(dob)
    gender = smsp_utils.build_person_gender(gender)
    person_name = smsp_utils.build_person_name(given_name,family_name)
    postcode = smsp_utils.build_person_postcode(postcode)

    queryEvent = smsp_itk.getPatientDetailsBySearchRequest_v1_0Grouper.factory(
        Person_DateOfBirth=dob,
        Person_Gender=gender,
        Person_Name=person_name,
        Person_Postcode=postcode)

    id_ = smsp_utils.build_id("3E25ACE2-23F8-4A37-B446-6A37F31BF77C")
    code = smsp_utils.build_coded_value("getPatientDetailsBySearchRequest-v1-0","2.16.840.1.113883.2.1.3.2.4.17.284")
    
    get_nhs_number_request = smsp_itk.getPatientDetailsBySearchRequest_v1_0.factory(
        queryEvent=queryEvent,
        moodCode="EVN",
        classCode="CACT",
        id=id_,
        code=code)
    get_nhs_number_request.original_tagname_="getPatientDetailsbySearchRequest-v1-0"

    return smsp_utils.object_to_xml(get_nhs_number_request)
"""
#getPatientDetails
dob
[forename] (req without nnn)
[gender] (req without nnn)
[nhs number]
[surname] (req without nnn)
[postcode]
"""
def getPatientDetailsRequest(dob,nhs_number=None,gender=None,family_name=None,given_name=None,postcode=None):
    if nhs_number==None:
        if family_name==None or given_name==None or gender==None:
            raise TypeError("Family name,Given name and Gender must be specfified when NHS Number is None")
        
    dob = smsp_utils.build_person_dob(dob)
    nnn = smsp_utils.build_person_nhsnumber(nhs_number)
    gender = smsp_utils.build_person_gender(gender)
    person_name = smsp_utils.build_person_name(given_name,family_name)
    postcode = smsp_utils.build_person_postcode(postcode)

    queryEvent = smsp_itk.getPatientDetailsRequest_v1_0Grouper.factory(
        Person_DateOfBirth=dob,
        Person_Gender=gender,
        Person_Name=person_name,
        Person_Postcode=postcode,
        Person_NHSNumber=nnn,
    )

    id_ = smsp_utils.build_id("3E25ACE2-23F8-4A37-B446-6A37F31BF77C")
    code = smsp_utils.build_coded_value("getPatientDetailsRequest-v1-0","2.16.840.1.113883.2.1.3.2.4.17.284")
    
    get_details_request = smsp_itk.getPatientDetails_v1_0.factory(
        queryEvent=queryEvent,
        moodCode="EVN",
        classCode="CACT",
        id=id_,
        code=code)
    get_details_request.original_tagname_="getPatientDetailsRequest-v1-0"

    return smsp_utils.object_to_xml(get_details_request)
