from smsp import common_itk
from io import StringIO

def object_to_xml(obj):
    output = StringIO()
    obj.export(output,0)
    xml = output.getvalue()
    output.close()
    return xml

def build_semantic_text(text):
    o = common_itk.MixedContainer(common_itk.MixedContainer.CategoryText,common_itk.MixedContainer.TypeNone,'',text)
    st = common_itk.ST.factory(valueOf_=text,content_=[o,])
    return st

def build_person_dob(dob):
    if dob==None:
        return None
    ts = common_itk.TS_NHS_TimestampType4(dob)
    st = build_semantic_text("Person.DateOfBirth")
    return common_itk.Person_DateOfBirth(value=ts,semanticsText=st)

def build_person_gender(gender):
    if gender==None:
        return None
    st = build_semantic_text("Person.Gender")
    gender_type = common_itk.CV_NHS_CodedValueType1(code=gender,codeSystem="2.16.840.1.113883.2.1.3.2.4.16.25")
    return common_itk.Person_Gender(value=gender_type,semanticsText=st)

def build_person_name(given_name,family_name):
    if given_name==None and family_name==None:
        return None
    
    st = build_semantic_text("Person.Name")
    if given_name:
        given = common_itk.en_given.factory(valueOf_=given_name)
        given.original_tagname_ = "given"
    else:
        given = None
    if family_name:
        family = common_itk.en_family.factory(valueOf_=family_name)
        family.original_tagname_ = "family"
    else:
        family = None
    person_name_3 = common_itk.PN_NHS_PersonNameType3.factory(given=given,family=family)
    return common_itk.Person_Name(value=person_name_3,semanticsText=st)

def build_person_postcode(postcode):
    if postcode==None:
        return None
    st = build_semantic_text("Person.Postcode")
    o = common_itk.MixedContainer(common_itk.MixedContainer.CategoryText,common_itk.MixedContainer.TypeNone,'',postcode)
    postcode = common_itk.ADXP.factory(valueOf_=postcode,content_=[o,])
    postcode = common_itk.AD_NHS_AddressType1.factory(postalCode=postcode)
    return common_itk.Person_Postcode(value=postcode,semanticsText=st)

def build_person_nhsnumber(nhs_number):
    if nhs_number==None:
        return None
    st = build_semantic_text("Person.NHSNumber")
    nnn = common_itk.II_NHS_IdentifierType1.factory(root="2.16.840.1.113883.2.1.4.1",extension=nhs_number)
    nnn = common_itk.Person_NHSNumber(value=nnn,semanticsText=st)
    return nnn

def build_coded_value(code,code_system):
    common_itk.CV_NHS_CodedValueType1.factory(
        code=code,
        codeSystem=code_system)

def build_id(root):
    return common_itk.II_NHS_IdentifierType2.factory(root=root)
