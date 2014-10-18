from dragonfly import CompoundRule, Dictation
from speechAssistant.xmlHandle import xmlParser as xP
import subprocess
class openRule(CompoundRule):
    spec="open <file>"
    extras=[Dictation("file"),]
    def _process_recognition(self,node,extras):
        dictation_fileName=str(extras["file"])
        names=xP.openTable_xmlParser.xmlObject.findall("./openFile/name")
        paths=xP.openTable_xmlParser.xmlObject.findall("./openFile/path")
        exe_list=[]
        for i_n,i_p in zip(names,paths):
            if i_n.text==dictation_fileName:
                exe_list.append((i_n,i_p))
        if len(exe_list)==1:
            exe_path=str(exe_list[0][1].text)
            print(exe_path)
            opened_handle=subprocess.Popen(exe_path,shell=True)
            
                
                
        

     
