
from smsp.schema_utils import *
from smsp.schema_utils import _cast
from smsp.common_itk import *

class getNHSNumberRequest_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, queryEvent=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.queryEvent = queryEvent
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getNHSNumberRequest_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getNHSNumberRequest_v1_0.subclass:
            return getNHSNumberRequest_v1_0.subclass(*args_, **kwargs_)
        else:
            return getNHSNumberRequest_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_queryEvent(self): return self.queryEvent
    def set_queryEvent(self, queryEvent): self.queryEvent = queryEvent
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.queryEvent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000002GB01.getNHSNumberRequest-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.queryEvent is not None:
            self.queryEvent.export(outfile, level, namespace_, name_='queryEvent', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'queryEvent':
            obj_ = getNHSNumberRequest_v1_0Grouper.factory()
            obj_.build(child_)
            self.queryEvent = obj_
            obj_.original_tagname_ = 'queryEvent'


class getNHSNumberRequest_v1_0Grouper(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, Person_DateOfBirth=None, Person_Gender=None, Person_LocalIdentifier=None, Person_Name=None, Person_Postcode=None):
        self.original_tagname_ = None
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.Person_DateOfBirth = Person_DateOfBirth
        self.Person_Gender = Person_Gender
        self.Person_LocalIdentifier = Person_LocalIdentifier
        self.Person_Name = Person_Name
        self.Person_Postcode = Person_Postcode
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getNHSNumberRequest_v1_0Grouper)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getNHSNumberRequest_v1_0Grouper.subclass:
            return getNHSNumberRequest_v1_0Grouper.subclass(*args_, **kwargs_)
        else:
            return getNHSNumberRequest_v1_0Grouper(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_Person_DateOfBirth(self): return self.Person_DateOfBirth
    def set_Person_DateOfBirth(self, Person_DateOfBirth): self.Person_DateOfBirth = Person_DateOfBirth
    def get_Person_Gender(self): return self.Person_Gender
    def set_Person_Gender(self, Person_Gender): self.Person_Gender = Person_Gender
    def get_Person_LocalIdentifier(self): return self.Person_LocalIdentifier
    def set_Person_LocalIdentifier(self, Person_LocalIdentifier): self.Person_LocalIdentifier = Person_LocalIdentifier
    def get_Person_Name(self): return self.Person_Name
    def set_Person_Name(self, Person_Name): self.Person_Name = Person_Name
    def get_Person_Postcode(self): return self.Person_Postcode
    def set_Person_Postcode(self, Person_Postcode): self.Person_Postcode = Person_Postcode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.Person_DateOfBirth is not None or
            self.Person_Gender is not None or
            self.Person_LocalIdentifier is not None or
            self.Person_Name is not None or
            self.Person_Postcode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0Grouper', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000002GB01.getNHSNumberRequest-v1-0Grouper')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0Grouper')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0Grouper', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0Grouper'):
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000002GB01.getNHSNumberRequest-v1-0Grouper', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.Person_DateOfBirth is not None:
            self.Person_DateOfBirth.export(outfile, level, namespace_, name_='Person.DateOfBirth', pretty_print=pretty_print)
        if self.Person_Gender is not None:
            self.Person_Gender.export(outfile, level, namespace_, name_='Person.Gender', pretty_print=pretty_print)
        if self.Person_LocalIdentifier is not None:
            self.Person_LocalIdentifier.export(outfile, level, namespace_, name_='Person.LocalIdentifier', pretty_print=pretty_print)
        if self.Person_Name is not None:
            self.Person_Name.export(outfile, level, namespace_, name_='Person.Name', pretty_print=pretty_print)
        if self.Person_Postcode is not None:
            self.Person_Postcode.export(outfile, level, namespace_, name_='Person.Postcode', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'Person.DateOfBirth':
            obj_ = Person_DateOfBirth.factory()
            obj_.build(child_)
            self.Person_DateOfBirth = obj_
            obj_.original_tagname_ = 'Person.DateOfBirth'
        elif nodeName_ == 'Person.Gender':
            obj_ = Person_Gender.factory()
            obj_.build(child_)
            self.Person_Gender = obj_
            obj_.original_tagname_ = 'Person.Gender'
        elif nodeName_ == 'Person.LocalIdentifier':
            obj_ = Person_LocalIdentifier.factory()
            obj_.build(child_)
            self.Person_LocalIdentifier = obj_
            obj_.original_tagname_ = 'Person.LocalIdentifier'
        elif nodeName_ == 'Person.Name':
            obj_ = Person_Name.factory()
            obj_.build(child_)
            self.Person_Name = obj_
            obj_.original_tagname_ = 'Person.Name'
        elif nodeName_ == 'Person.Postcode':
            obj_ = Person_Postcode.factory()
            obj_.build(child_)
            self.Person_Postcode = obj_
            obj_.original_tagname_ = 'Person.Postcode'


class getNHSNumberResponse_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, value=None, subject=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.value = value
        self.subject = subject
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getNHSNumberResponse_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getNHSNumberResponse_v1_0.subclass:
            return getNHSNumberResponse_v1_0.subclass(*args_, **kwargs_)
        else:
            return getNHSNumberResponse_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.value is not None or
            self.subject is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='COMT_MT000014GB01.getNHSNumberResponse-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('COMT_MT000014GB01.getNHSNumberResponse-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='COMT_MT000014GB01.getNHSNumberResponse-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='COMT_MT000014GB01.getNHSNumberResponse-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='COMT_MT000014GB01.getNHSNumberResponse-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='COMT_MT000014GB01.getNHSNumberResponse-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'value':
            obj_ = valueType.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'subject':
            obj_ = Subject.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'


class getPatientDetailsByNHSNumberRequest_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, queryEvent=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.queryEvent = queryEvent
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getPatientDetailsByNHSNumberRequest_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getPatientDetailsByNHSNumberRequest_v1_0.subclass:
            return getPatientDetailsByNHSNumberRequest_v1_0.subclass(*args_, **kwargs_)
        else:
            return getPatientDetailsByNHSNumberRequest_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_queryEvent(self): return self.queryEvent
    def set_queryEvent(self, queryEvent): self.queryEvent = queryEvent
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.queryEvent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.queryEvent is not None:
            self.queryEvent.export(outfile, level, namespace_, name_='queryEvent', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'queryEvent':
            obj_ = getPatientDetailsByNHSNumberRequest_v1_0Grouper.factory()
            obj_.build(child_)
            self.queryEvent = obj_
            obj_.original_tagname_ = 'queryEvent'


class getPatientDetailsByNHSNumberRequest_v1_0Grouper(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, Person_DateOfBirth=None, Person_LocalIdentifier=None, Person_NHSNumber=None, Person_Name=None):
        self.original_tagname_ = None
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.Person_DateOfBirth = Person_DateOfBirth
        self.Person_LocalIdentifier = Person_LocalIdentifier
        self.Person_NHSNumber = Person_NHSNumber
        self.Person_Name = Person_Name
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getPatientDetailsByNHSNumberRequest_v1_0Grouper)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getPatientDetailsByNHSNumberRequest_v1_0Grouper.subclass:
            return getPatientDetailsByNHSNumberRequest_v1_0Grouper.subclass(*args_, **kwargs_)
        else:
            return getPatientDetailsByNHSNumberRequest_v1_0Grouper(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_Person_DateOfBirth(self): return self.Person_DateOfBirth
    def set_Person_DateOfBirth(self, Person_DateOfBirth): self.Person_DateOfBirth = Person_DateOfBirth
    def get_Person_LocalIdentifier(self): return self.Person_LocalIdentifier
    def set_Person_LocalIdentifier(self, Person_LocalIdentifier): self.Person_LocalIdentifier = Person_LocalIdentifier
    def get_Person_NHSNumber(self): return self.Person_NHSNumber
    def set_Person_NHSNumber(self, Person_NHSNumber): self.Person_NHSNumber = Person_NHSNumber
    def get_Person_Name(self): return self.Person_Name
    def set_Person_Name(self, Person_Name): self.Person_Name = Person_Name
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.Person_DateOfBirth is not None or
            self.Person_LocalIdentifier is not None or
            self.Person_NHSNumber is not None or
            self.Person_Name is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0Grouper', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0Grouper')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0Grouper')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0Grouper', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0Grouper'):
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000003GB01.getPatientDetailsByNHSNumberRequest-v1-0Grouper', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.Person_DateOfBirth is not None:
            self.Person_DateOfBirth.export(outfile, level, namespace_, name_='Person.DateOfBirth', pretty_print=pretty_print)
        if self.Person_LocalIdentifier is not None:
            self.Person_LocalIdentifier.export(outfile, level, namespace_, name_='Person.LocalIdentifier', pretty_print=pretty_print)
        if self.Person_NHSNumber is not None:
            self.Person_NHSNumber.export(outfile, level, namespace_, name_='Person.NHSNumber', pretty_print=pretty_print)
        if self.Person_Name is not None:
            self.Person_Name.export(outfile, level, namespace_, name_='Person.Name', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'Person.DateOfBirth':
            obj_ = Person_DateOfBirth.factory()
            obj_.build(child_)
            self.Person_DateOfBirth = obj_
            obj_.original_tagname_ = 'Person.DateOfBirth'
        elif nodeName_ == 'Person.LocalIdentifier':
            obj_ = Person_LocalIdentifier.factory()
            obj_.build(child_)
            self.Person_LocalIdentifier = obj_
            obj_.original_tagname_ = 'Person.LocalIdentifier'
        elif nodeName_ == 'Person.NHSNumber':
            obj_ = Person_NHSNumber.factory()
            obj_.build(child_)
            self.Person_NHSNumber = obj_
            obj_.original_tagname_ = 'Person.NHSNumber'
        elif nodeName_ == 'Person.Name':
            obj_ = Person_Name.factory()
            obj_.build(child_)
            self.Person_Name = obj_
            obj_.original_tagname_ = 'Person.Name'


class getPatientDetailsBySearchRequest_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, queryEvent=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.queryEvent = queryEvent
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getPatientDetailsBySearchRequest_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getPatientDetailsBySearchRequest_v1_0.subclass:
            return getPatientDetailsBySearchRequest_v1_0.subclass(*args_, **kwargs_)
        else:
            return getPatientDetailsBySearchRequest_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_queryEvent(self): return self.queryEvent
    def set_queryEvent(self, queryEvent): self.queryEvent = queryEvent
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.queryEvent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.queryEvent is not None:
            self.queryEvent.export(outfile, level, namespace_, name_='queryEvent', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'queryEvent':
            obj_ = getPatientDetailsBySearchRequest_v1_0Grouper.factory()
            obj_.build(child_)
            self.queryEvent = obj_
            obj_.original_tagname_ = 'queryEvent'


class getPatientDetailsBySearchRequest_v1_0Grouper(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, Person_DateOfBirth=None, Person_Gender=None, Person_LocalIdentifier=None, Person_Name=None, Person_Postcode=None):
        self.original_tagname_ = None
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.Person_DateOfBirth = Person_DateOfBirth
        self.Person_Gender = Person_Gender
        self.Person_LocalIdentifier = Person_LocalIdentifier
        self.Person_Name = Person_Name
        self.Person_Postcode = Person_Postcode
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getPatientDetailsBySearchRequest_v1_0Grouper)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getPatientDetailsBySearchRequest_v1_0Grouper.subclass:
            return getPatientDetailsBySearchRequest_v1_0Grouper.subclass(*args_, **kwargs_)
        else:
            return getPatientDetailsBySearchRequest_v1_0Grouper(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_Person_DateOfBirth(self): return self.Person_DateOfBirth
    def set_Person_DateOfBirth(self, Person_DateOfBirth): self.Person_DateOfBirth = Person_DateOfBirth
    def get_Person_Gender(self): return self.Person_Gender
    def set_Person_Gender(self, Person_Gender): self.Person_Gender = Person_Gender
    def get_Person_LocalIdentifier(self): return self.Person_LocalIdentifier
    def set_Person_LocalIdentifier(self, Person_LocalIdentifier): self.Person_LocalIdentifier = Person_LocalIdentifier
    def get_Person_Name(self): return self.Person_Name
    def set_Person_Name(self, Person_Name): self.Person_Name = Person_Name
    def get_Person_Postcode(self): return self.Person_Postcode
    def set_Person_Postcode(self, Person_Postcode): self.Person_Postcode = Person_Postcode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.Person_DateOfBirth is not None or
            self.Person_Gender is not None or
            self.Person_LocalIdentifier is not None or
            self.Person_Name is not None or
            self.Person_Postcode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0Grouper', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0Grouper')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0Grouper')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0Grouper', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0Grouper'):
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000004GB01.getPatientDetailsBySearchRequest-v1-0Grouper', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.Person_DateOfBirth is not None:
            self.Person_DateOfBirth.export(outfile, level, namespace_, name_='Person.DateOfBirth', pretty_print=pretty_print)
        if self.Person_Gender is not None:
            self.Person_Gender.export(outfile, level, namespace_, name_='Person.Gender', pretty_print=pretty_print)
        if self.Person_LocalIdentifier is not None:
            self.Person_LocalIdentifier.export(outfile, level, namespace_, name_='Person.LocalIdentifier', pretty_print=pretty_print)
        if self.Person_Name is not None:
            self.Person_Name.export(outfile, level, namespace_, name_='Person.Name', pretty_print=pretty_print)
        if self.Person_Postcode is not None:
            self.Person_Postcode.export(outfile, level, namespace_, name_='Person.Postcode', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'Person.DateOfBirth':
            obj_ = Person_DateOfBirth.factory()
            obj_.build(child_)
            self.Person_DateOfBirth = obj_
            obj_.original_tagname_ = 'Person.DateOfBirth'
        elif nodeName_ == 'Person.Gender':
            obj_ = Person_Gender.factory()
            obj_.build(child_)
            self.Person_Gender = obj_
            obj_.original_tagname_ = 'Person.Gender'
        elif nodeName_ == 'Person.LocalIdentifier':
            obj_ = Person_LocalIdentifier.factory()
            obj_.build(child_)
            self.Person_LocalIdentifier = obj_
            obj_.original_tagname_ = 'Person.LocalIdentifier'
        elif nodeName_ == 'Person.Name':
            obj_ = Person_Name.factory()
            obj_.build(child_)
            self.Person_Name = obj_
            obj_.original_tagname_ = 'Person.Name'
        elif nodeName_ == 'Person.Postcode':
            obj_ = Person_Postcode.factory()
            obj_.build(child_)
            self.Person_Postcode = obj_
            obj_.original_tagname_ = 'Person.Postcode'


class getPatientDetailsRequest_v1_0Grouper(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, Person_DateOfBirth=None, Person_Gender=None, Person_LocalIdentifier=None, Person_NHSNumber=None, Person_Name=None, Person_Postcode=None):
        self.original_tagname_ = None
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.Person_DateOfBirth = Person_DateOfBirth
        self.Person_Gender = Person_Gender
        self.Person_LocalIdentifier = Person_LocalIdentifier
        self.Person_NHSNumber = Person_NHSNumber
        self.Person_Name = Person_Name
        self.Person_Postcode = Person_Postcode
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getPatientDetailsRequest_v1_0Grouper)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getPatientDetailsRequest_v1_0Grouper.subclass:
            return getPatientDetailsRequest_v1_0Grouper.subclass(*args_, **kwargs_)
        else:
            return getPatientDetailsRequest_v1_0Grouper(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_Person_DateOfBirth(self): return self.Person_DateOfBirth
    def set_Person_DateOfBirth(self, Person_DateOfBirth): self.Person_DateOfBirth = Person_DateOfBirth
    def get_Person_Gender(self): return self.Person_Gender
    def set_Person_Gender(self, Person_Gender): self.Person_Gender = Person_Gender
    def get_Person_LocalIdentifier(self): return self.Person_LocalIdentifier
    def set_Person_LocalIdentifier(self, Person_LocalIdentifier): self.Person_LocalIdentifier = Person_LocalIdentifier
    def get_Person_NHSNumber(self): return self.Person_NHSNumber
    def set_Person_NHSNumber(self, Person_NHSNumber): self.Person_NHSNumber = Person_NHSNumber
    def get_Person_Name(self): return self.Person_Name
    def set_Person_Name(self, Person_Name): self.Person_Name = Person_Name
    def get_Person_Postcode(self): return self.Person_Postcode
    def set_Person_Postcode(self, Person_Postcode): self.Person_Postcode = Person_Postcode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.Person_DateOfBirth is not None or
            self.Person_Gender is not None or
            self.Person_LocalIdentifier is not None or
            self.Person_NHSNumber is not None or
            self.Person_Name is not None or
            self.Person_Postcode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000005GB01.getPatientDetailsRequest-v1-0Grouper', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000005GB01.getPatientDetailsRequest-v1-0Grouper')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000005GB01.getPatientDetailsRequest-v1-0Grouper')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000005GB01.getPatientDetailsRequest-v1-0Grouper', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000005GB01.getPatientDetailsRequest-v1-0Grouper'):
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000005GB01.getPatientDetailsRequest-v1-0Grouper', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.Person_DateOfBirth is not None:
            self.Person_DateOfBirth.export(outfile, level, namespace_, name_='Person.DateOfBirth', pretty_print=pretty_print)
        if self.Person_Gender is not None:
            self.Person_Gender.export(outfile, level, namespace_, name_='Person.Gender', pretty_print=pretty_print)
        if self.Person_LocalIdentifier is not None:
            self.Person_LocalIdentifier.export(outfile, level, namespace_, name_='Person.LocalIdentifier', pretty_print=pretty_print)
        if self.Person_NHSNumber is not None:
            self.Person_NHSNumber.export(outfile, level, namespace_, name_='Person.NHSNumber', pretty_print=pretty_print)
        if self.Person_Name is not None:
            self.Person_Name.export(outfile, level, namespace_, name_='Person.Name', pretty_print=pretty_print)
        if self.Person_Postcode is not None:
            self.Person_Postcode.export(outfile, level, namespace_, name_='Person.Postcode', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'Person.DateOfBirth':
            obj_ = Person_DateOfBirth.factory()
            obj_.build(child_)
            self.Person_DateOfBirth = obj_
            obj_.original_tagname_ = 'Person.DateOfBirth'
        elif nodeName_ == 'Person.Gender':
            obj_ = Person_Gender.factory()
            obj_.build(child_)
            self.Person_Gender = obj_
            obj_.original_tagname_ = 'Person.Gender'
        elif nodeName_ == 'Person.LocalIdentifier':
            obj_ = Person_LocalIdentifier.factory()
            obj_.build(child_)
            self.Person_LocalIdentifier = obj_
            obj_.original_tagname_ = 'Person.LocalIdentifier'
        elif nodeName_ == 'Person.NHSNumber':
            obj_ = Person_NHSNumber.factory()
            obj_.build(child_)
            self.Person_NHSNumber = obj_
            obj_.original_tagname_ = 'Person.NHSNumber'
        elif nodeName_ == 'Person.Name':
            obj_ = Person_Name.factory()
            obj_.build(child_)
            self.Person_Name = obj_
            obj_.original_tagname_ = 'Person.Name'
        elif nodeName_ == 'Person.Postcode':
            obj_ = Person_Postcode.factory()
            obj_.build(child_)
            self.Person_Postcode = obj_
            obj_.original_tagname_ = 'Person.Postcode'


class getPatientDetailsResponse_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, value=None, subject=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.value = value
        self.subject = subject
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, getPatientDetailsResponse_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if getPatientDetailsResponse_v1_0.subclass:
            return getPatientDetailsResponse_v1_0.subclass(*args_, **kwargs_)
        else:
            return getPatientDetailsResponse_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_subject(self): return self.subject
    def set_subject(self, subject): self.subject = subject
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.value is not None or
            self.subject is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='COMT_MT000016GB01.getPatientDetailsResponse-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('COMT_MT000016GB01.getPatientDetailsResponse-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='COMT_MT000016GB01.getPatientDetailsResponse-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='COMT_MT000016GB01.getPatientDetailsResponse-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='COMT_MT000016GB01.getPatientDetailsResponse-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='COMT_MT000016GB01.getPatientDetailsResponse-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.subject is not None:
            self.subject.export(outfile, level, namespace_, name_='subject', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'value':
            obj_ = valueType.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'subject':
            obj_ = Subject.factory()
            obj_.build(child_)
            self.subject = obj_
            obj_.original_tagname_ = 'subject'


class verifyNHSNumberRequest_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, queryEvent=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.queryEvent = queryEvent
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, verifyNHSNumberRequest_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if verifyNHSNumberRequest_v1_0.subclass:
            return verifyNHSNumberRequest_v1_0.subclass(*args_, **kwargs_)
        else:
            return verifyNHSNumberRequest_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_queryEvent(self): return self.queryEvent
    def set_queryEvent(self, queryEvent): self.queryEvent = queryEvent
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.queryEvent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.queryEvent is not None:
            self.queryEvent.export(outfile, level, namespace_, name_='queryEvent', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'queryEvent':
            obj_ = verifyNHSNumberRequest_v1_0Grouper.factory()
            obj_.build(child_)
            self.queryEvent = obj_
            obj_.original_tagname_ = 'queryEvent'


class verifyNHSNumberRequest_v1_0Grouper(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, Person_DateOfBirth=None, Person_NHSNumber=None, Person_Name=None):
        self.original_tagname_ = None
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.Person_DateOfBirth = Person_DateOfBirth
        self.Person_NHSNumber = Person_NHSNumber
        self.Person_Name = Person_Name
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, verifyNHSNumberRequest_v1_0Grouper)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if verifyNHSNumberRequest_v1_0Grouper.subclass:
            return verifyNHSNumberRequest_v1_0Grouper.subclass(*args_, **kwargs_)
        else:
            return verifyNHSNumberRequest_v1_0Grouper(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_Person_DateOfBirth(self): return self.Person_DateOfBirth
    def set_Person_DateOfBirth(self, Person_DateOfBirth): self.Person_DateOfBirth = Person_DateOfBirth
    def get_Person_NHSNumber(self): return self.Person_NHSNumber
    def set_Person_NHSNumber(self, Person_NHSNumber): self.Person_NHSNumber = Person_NHSNumber
    def get_Person_Name(self): return self.Person_Name
    def set_Person_Name(self, Person_Name): self.Person_Name = Person_Name
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.Person_DateOfBirth is not None or
            self.Person_NHSNumber is not None or
            self.Person_Name is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0Grouper', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0Grouper')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0Grouper')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0Grouper', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0Grouper'):
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='QUPA_MT000001GB01.verifyNHSNumberRequest-v1-0Grouper', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.Person_DateOfBirth is not None:
            self.Person_DateOfBirth.export(outfile, level, namespace_, name_='Person.DateOfBirth', pretty_print=pretty_print)
        if self.Person_NHSNumber is not None:
            self.Person_NHSNumber.export(outfile, level, namespace_, name_='Person.NHSNumber', pretty_print=pretty_print)
        if self.Person_Name is not None:
            self.Person_Name.export(outfile, level, namespace_, name_='Person.Name', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'Person.DateOfBirth':
            obj_ = Person_DateOfBirth.factory()
            obj_.build(child_)
            self.Person_DateOfBirth = obj_
            obj_.original_tagname_ = 'Person.DateOfBirth'
        elif nodeName_ == 'Person.NHSNumber':
            obj_ = Person_NHSNumber.factory()
            obj_.build(child_)
            self.Person_NHSNumber = obj_
            obj_.original_tagname_ = 'Person.NHSNumber'
        elif nodeName_ == 'Person.Name':
            obj_ = Person_Name.factory()
            obj_.build(child_)
            self.Person_Name = obj_
            obj_.original_tagname_ = 'Person.Name'


class verifyNHSNumberResponse_v1_0(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, classCode=None, moodCode=None, nullFlavor=None, updateMode=None, realmCode=None, typeId=None, templateId=None, id=None, code=None, value=None, component=None):
        self.original_tagname_ = None
        self.classCode = _cast(None, classCode)
        self.moodCode = _cast(None, moodCode)
        self.nullFlavor = _cast(None, nullFlavor)
        self.updateMode = _cast(None, updateMode)
        if realmCode is None:
            self.realmCode = []
        else:
            self.realmCode = realmCode
        self.typeId = typeId
        if templateId is None:
            self.templateId = []
        else:
            self.templateId = templateId
        self.id = id
        self.code = code
        self.value = value
        self.component = component
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, verifyNHSNumberResponse_v1_0)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if verifyNHSNumberResponse_v1_0.subclass:
            return verifyNHSNumberResponse_v1_0.subclass(*args_, **kwargs_)
        else:
            return verifyNHSNumberResponse_v1_0(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_realmCode(self): return self.realmCode
    def set_realmCode(self, realmCode): self.realmCode = realmCode
    def add_realmCode(self, value): self.realmCode.append(value)
    def insert_realmCode_at(self, index, value): self.realmCode.insert(index, value)
    def replace_realmCode_at(self, index, value): self.realmCode[index] = value
    def get_typeId(self): return self.typeId
    def set_typeId(self, typeId): self.typeId = typeId
    def get_templateId(self): return self.templateId
    def set_templateId(self, templateId): self.templateId = templateId
    def add_templateId(self, value): self.templateId.append(value)
    def insert_templateId_at(self, index, value): self.templateId.insert(index, value)
    def replace_templateId_at(self, index, value): self.templateId[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def get_component(self): return self.component
    def set_component(self, component): self.component = component
    def get_classCode(self): return self.classCode
    def set_classCode(self, classCode): self.classCode = classCode
    def get_moodCode(self): return self.moodCode
    def set_moodCode(self, moodCode): self.moodCode = moodCode
    def get_nullFlavor(self): return self.nullFlavor
    def set_nullFlavor(self, nullFlavor): self.nullFlavor = nullFlavor
    def get_updateMode(self): return self.updateMode
    def set_updateMode(self, updateMode): self.updateMode = updateMode
    def validate_cs(self, value):
        # Validate type cs, a restriction on xsd:token.
        if value is not None and Validate_simpletypes_:
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_patterns_, ))
    validate_cs_patterns_ = [['^[^\\s]*$']]
    def validate_NullFlavor(self, value):
        # Validate type NullFlavor, a restriction on None.
        pass
    def validate_cs_UpdateMode(self, value):
        # Validate type cs_UpdateMode, a restriction on cs.
        if value is not None and Validate_simpletypes_:
            value = str(value)
            enumerations = ['added', 'altered', 'removed', 'unchanged']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if not enumeration_respectee:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on cs_UpdateMode' % {"value" : value.encode("utf-8")} )
            if not self.gds_validate_simple_patterns(
                    self.validate_cs_UpdateMode_patterns_, value):
                warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_cs_UpdateMode_patterns_, ))
    validate_cs_UpdateMode_patterns_ = [['^[^\\s]*$']]
    def hasContent_(self):
        if (
            self.realmCode or
            self.typeId is not None or
            self.templateId or
            self.id is not None or
            self.code is not None or
            self.value is not None or
            self.component is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='COMT_MT000013GB01.verifyNHSNumberResponse-v1-0', namespacedef_='', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('COMT_MT000013GB01.verifyNHSNumberResponse-v1-0')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='COMT_MT000013GB01.verifyNHSNumberResponse-v1-0')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='COMT_MT000013GB01.verifyNHSNumberResponse-v1-0', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='COMT_MT000013GB01.verifyNHSNumberResponse-v1-0'):
        if self.classCode is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            outfile.write(' classCode=%s' % (quote_attrib(self.classCode), ))
        if self.moodCode is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            outfile.write(' moodCode=%s' % (quote_attrib(self.moodCode), ))
        if self.nullFlavor is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            outfile.write(' nullFlavor=%s' % (quote_attrib(self.nullFlavor), ))
        if self.updateMode is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            outfile.write(' updateMode=%s' % (quote_attrib(self.updateMode), ))
    def exportChildren(self, outfile, level, namespace_='', name_='COMT_MT000013GB01.verifyNHSNumberResponse-v1-0', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for realmCode_ in self.realmCode:
            realmCode_.export(outfile, level, namespace_, name_='realmCode', pretty_print=pretty_print)
        if self.typeId is not None:
            self.typeId.export(outfile, level, namespace_, name_='typeId', pretty_print=pretty_print)
        for templateId_ in self.templateId:
            templateId_.export(outfile, level, namespace_, name_='templateId', pretty_print=pretty_print)
        if self.id is not None:
            self.id.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        if self.code is not None:
            self.code.export(outfile, level, namespace_, name_='code', pretty_print=pretty_print)
        if self.value is not None:
            self.value.export(outfile, level, namespace_, name_='value', pretty_print=pretty_print)
        if self.component is not None:
            self.component.export(outfile, level, namespace_, name_='component', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('classCode', node)
        if value is not None and 'classCode' not in already_processed:
            already_processed.add('classCode')
            self.classCode = value
            self.validate_cs(self.classCode)    # validate type cs
        value = find_attr_value_('moodCode', node)
        if value is not None and 'moodCode' not in already_processed:
            already_processed.add('moodCode')
            self.moodCode = value
            self.validate_cs(self.moodCode)    # validate type cs
        value = find_attr_value_('nullFlavor', node)
        if value is not None and 'nullFlavor' not in already_processed:
            already_processed.add('nullFlavor')
            self.nullFlavor = value
            self.validate_NullFlavor(self.nullFlavor)    # validate type NullFlavor
        value = find_attr_value_('updateMode', node)
        if value is not None and 'updateMode' not in already_processed:
            already_processed.add('updateMode')
            self.updateMode = value
            self.validate_cs_UpdateMode(self.updateMode)    # validate type cs_UpdateMode
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'realmCode':
            obj_ = CS.factory()
            obj_.build(child_)
            self.realmCode.append(obj_)
            obj_.original_tagname_ = 'realmCode'
        elif nodeName_ == 'typeId':
            obj_ = II.factory()
            obj_.build(child_)
            self.typeId = obj_
            obj_.original_tagname_ = 'typeId'
        elif nodeName_ == 'templateId':
            obj_ = II.factory()
            obj_.build(child_)
            self.templateId.append(obj_)
            obj_.original_tagname_ = 'templateId'
        elif nodeName_ == 'id':
            obj_ = II_NHS_IdentifierType2.factory()
            obj_.build(child_)
            self.id = obj_
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'code':
            obj_ = codeType1.factory()
            obj_.build(child_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'value':
            obj_ = valueType2.factory()
            obj_.build(child_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
        elif nodeName_ == 'component':
            obj_ = Component.factory()
            obj_.build(child_)
            self.component = obj_
            obj_.original_tagname_ = 'component'


