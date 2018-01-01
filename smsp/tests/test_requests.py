import pytest
from smsp import smsp_requests

#Just testing building requests for now
#TODO - check the objects against the schemas?

class Test_verifyNHSNumberRequest:
    def test_all_params(self):
        smsp_requests.verifyNHSNumberRequest("12345","19770708","foo","bar")
    
    def test_min_params(self):
        smsp_requests.verifyNHSNumberRequest("12345","19770708")

class Test_getNHSNumberRequest:
    def test_all_params(self):
        smsp_requests.getNHSNumberRequest("19770708","2","foo","bar","BS1 1AA")
    
    def test_min_params(self):
        smsp_requests.getNHSNumberRequest("19770708","2","foo")

class Test_getPatientDetailsByNHSNumberRequest:
    def test_all_params(self):
        smsp_requests.getPatientDetailsByNHSNumberRequest("12345","19770708","foo","bar")
    
    def test_min_params(self):
        smsp_requests.getPatientDetailsByNHSNumberRequest("12345","19770708")

class Test_getPatientDetailsBySearchRequest:
    def test_all_params(self):
        smsp_requests.getPatientDetailsBySearchRequest("19770708","2","foo","bar","BS1 1AA")

    def test_min_params(self):
        smsp_requests.getPatientDetailsBySearchRequest("19770708","2","foo")
        
class Test_getPatientDetailsRequest:
    def test_all_params(self):
        smsp_requests.getPatientDetailsRequest("19770709","12345","2","foo","bar","BS1 1AA")

    def test_min_params_nhs(self):
        smsp_requests.getPatientDetailsRequest("19770709","12345")

    def test_min_paramS_no_nhs(self):
        smsp_requests.getPatientDetailsRequest("19770709",None,"2","foo","bar","BS1 1AA")
        
        
