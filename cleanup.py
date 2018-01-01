import getPatientDetailsReq
import getPatientDetailsBySearchReq
import getPatientDetailsByNHSNumberReq
import getNHSNumberReq
import verifyNHSNumberReq
import verifyNHSNumberResp
import getNHSNumberResp
import getPatientDetailsResp

from getPatientDetailsReq import *
from getPatientDetailsBySearchReq import *
from getPatientDetailsByNHSNumberReq import *
from getNHSNumberReq import *
from verifyNHSNumberReq import *
from getPatientDetailsReq import GeneratedsSuper
from verifyNHSNumberResp import *
from getNHSNumberResp import *
from getPatientDetailsResp import *

import inspect
common_start_block = """
from smsp.schema_utils import *
from smsp.schema_utils import _cast
if True:
"""    
req_start_block = """
from smsp.schema_utils import *
from smsp.schema_utils import _cast
from smsp.common_itk import *
"""

written_names = []
def write_class_tree(f,tree, indent=-1):
    global written_names
    
    if isinstance(tree, list):
        for node in tree:
            write_class_tree(f,node, indent+1)
    else:
        if not tree[0].__name__ in written_names:
            comments = inspect.getcomments(eval(tree[0].__name__))
            code = inspect.getsource(eval(tree[0].__name__))
            if comments:
                f.write(comments)
            f.write(code)
            f.write("\n\n")
            written_names.append(tree[0].__name__)
    return

def print_class_tree(f,tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(f,node, indent+1)
    else:
        print('  ' * indent, tree[0].__name__)
    return

objs = {}

for i in getPatientDetailsReq.__all__:
    objs[i] = objs.get(i,0)+1
for i in getPatientDetailsBySearchReq.__all__:
    objs[i] = objs.get(i,0)+1
for i in getPatientDetailsByNHSNumberReq.__all__:
    objs[i] = objs.get(i,0)+1
for i in getNHSNumberReq.__all__:
    objs[i] = objs.get(i,0)+1
for i in verifyNHSNumberReq.__all__:
    objs[i] = objs.get(i,0)+1
for i in verifyNHSNumberResp.__all__:
    objs[i] = objs.get(i,0)+1
for i in getNHSNumberResp.__all__:
    objs[i] = objs.get(i,0)+1
for i in getPatientDetailsResp.__all__:
    objs[i] = objs.get(i,0)+1

common_classes = []
single_classes = []
for name,count in objs.items():
    #if count>1:
    if "Request" not in name and "Response" not in name:
        common_classes.append(eval(name))
    else:
        single_classes.append(eval(name))
        
common_class_tree = inspect.getclasstree(common_classes,unique=True)
with open("built/common_itk_tofix.py","w") as f:
    f.write(common_start_block)
    f.write("\n")
    write_class_tree(f,common_class_tree)
single_class_tree = inspect.getclasstree(single_classes,unique=True)
with open("built/smsp_itk.py","w") as f:
    f.write(req_start_block)
    f.write("\n")
    write_class_tree(f,single_class_tree)

#Now some fixes in common_itk - not sure why they are required but they are
with open("built/common_itk_tofix.py") as f:
    data = f.read()
    data = data.replace(
        "super(ST, self).__init__(nullFlavor, updateMode, representation, mediaType, language, compression, integrityCheck, integrityCheckAlgorithm, reference, thumbnail, anytypeobjs_, valueOf_, mixedclass_, content_, extensiontype_, )",
        "super(ST, self).__init__(nullFlavor, updateMode, representation, mediaType, language, compression, integrityCheck, integrityCheckAlgorithm, reference, thumbnail, anytypeobjs_, valueOf_, mixedclass_, content_,)")
    data = data.replace(
        "super(CV, self).__init__(nullFlavor, updateMode, code, codeSystem, codeSystemName, codeSystemVersion, displayName, originalText, qualifier, group, translation, extensiontype_, )",
        "super(CV, self).__init__(nullFlavor, updateMode, code, codeSystem, codeSystemName, codeSystemVersion, displayName, originalText, qualifier, group, translation, )")
    data = data.replace(
        ", anytypeobjs_, anytypeobjs_,",
        ", anytypeobjs_,")
    data = data.replace(
        "super(ADXP, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)",
        "super(ADXP, self).exportChildren(outfile, level, namespace_, name_, fromsubclass_, pretty_print=pretty_print)")
    
    fixed = open("built/common_itk.py","w")
    fixed.write(data)
