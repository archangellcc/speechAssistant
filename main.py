import sys
sys.path.append(r"C:\Users\archangel\Desktop\我的项目")
from speechAssistant.openModule import openRule as oR
from dragonfly import Grammar
#问题1 不支持英文文件名(致命)
open_R=oR.openRule()
gr=Grammar("n")
gr.add_rule(open_R)
gr.load()
print("end")
