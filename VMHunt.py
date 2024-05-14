import re

from typing import List, Tuple, Dict
from bitstring import BitArray

instlist1 = []

def nop():
    pass

class Register:
    rax = 0
    eax = 1
    ax = 2
    ah = 3
    al = 4
    rbx = 5
    ebx = 6
    bx = 7
    bh = 8
    bl = 9
    rcx = 10
    ecx = 11
    cx = 12
    ch = 13
    cl = 14
    rdx = 15
    edx = 16
    dx = 17
    dh = 18
    dl = 19
    rsi = 20
    esi = 21
    si = 22
    edi = 23
    di = 24
    rsp = 25
    esp = 26
    sp = 27
    rbp = 28
    ebp = 29
    bp = 30
    r8 = 31
    r8d = 32
    r8w = 33
    r8b = 34
    r9 = 35
    r9d = 36
    r9w = 37
    r9b = 38
    r10 = 39
    r10d = 40
    r10w = 41
    r10b = 42
    r11 = 43
    r11d = 44
    r11w = 45
    r11b = 46
    r12 = 47
    r12d = 48
    r12w = 49
    r12b = 50
    r13 = 51
    r13d = 52
    r13w = 53
    r13b = 54
    r14 = 55
    r14d = 56
    r14w = 57
    r14b = 58
    r15 = 59
    r15d = 60
    r15w = 61
    r15b = 62
    rip = 63
    eip = 64
    st0 = 66
    st1 = 67
    st2 = 68
    st3 = 69
    st4 = 70
    st5 = 71
    st6 = 72
    st7 = 73
    eflags = 74
    cs = 75
    ds = 76
    es = 77
    fs = 78
    gs = 79
    ss = 80

    def isReg64(self, regname: str):
        return regname == "rax" or regname == "rbx" or regname == "rcx" or regname == "rdx" or regname == "rsi" or regname == "rdi" or regname == "rsp" or regname == "rbp" or regname == "r8" or regname == "r9" or regname == "r10" or regname == "r11" or regname == "r12" or regname == "r13" or regname == "r14" or regname == "r15" or regname == "rip"
    
    def isReg32(self, regname: str):
        return regname == "eax" or regname == "ebx" or regname == "ecx" or regname == "edx" or regname == "esi" or regname == "edi" or regname == "esp" or regname == "ebp"
    
    def isReg16(self, regname: str):
        return regname == "ax" or regname == "bx" or regname == "cx" or regname == "dx" or regname == "si" or regname == "di" or regname == "bp"
    
    def isReg8(self, regname: str):
        return regname == "al" or regname == "bl" or regname == "cl" or regname == "dl" or regname == "ah" or regname == "bh" or regname == "ch" or regname == "dh"

    def getRegParameter(self, regname: str, idx: list):
        if self.isReg64(regname):
            idx.append(0)
            idx.append(1)
            idx.append(2)
            idx.append(3)
            idx.append(4)
            idx.append(5)
            idx.append(6)
            idx.append(7)
            idx.append(8)

            if regname == "rax":
                return self.rax
            elif regname == "rbx":
                return self.rbx
            elif regname == "rcx":
                return self.rcx
            elif regname == "rdx":
                return self.rdx
            elif regname == "rsi":
                return self.rsi
            elif regname == "rdi":
                return self.rdi
            elif regname == "rsp":
                return self.rsp
            elif regname == "rbp":
                return self.rbp
            elif regname == "r8":
                return self.r8
            elif regname == "r9":
                return self.r9
            elif regname == "r10":
                return self.r10
            elif regname == "r11":
                return self.r11
            elif regname == "r12":
                return self.r12
            elif regname == "r13":
                return self.r13
            elif regname == "r14":
                return self.r14
            elif regname == "r15":
                return self.r15
            elif regname == "rip":
                return self.rip
            else:
                print("Unknown 64 bit reg: ", regname)
                return self.unk
        elif self.isReg32(regname):
            idx.append(0)
            idx.append(1)
            idx.append(2)
            idx.append(3)
            if regname == "eax":
                return self.rax
            elif regname == "ebx":
                return self.rbx
            elif regname == "ecx":
                return self.rcx
            elif regname == "edx":
                return self.rdx
            elif regname == "esi":
                return self.rsi
            elif regname == "edi":
                return self.rdi
            elif regname == "esp":
                return self.rsp
            elif regname == "ebp":
                return self.rbp
            else:
                print("Unknown 32 bit reg: ", regname)
                return self.unk
        elif self.isReg16(regname):
            idx.append(0)
            idx.append(1)
            if regname == "ax":
                return self.rax
            elif regname == "bx":
                return self.rbx
            elif regname == "cx":
                return self.rcx
            elif regname == "dx":
                return self.rdx
            elif regname == "si":
                return self.rsi
            elif regname == "di":
                return self.rdi
            elif regname == "bp":
                return self.rbp
            else:
                print("Unknown 16 bit reg: ", regname)
                return self.unk
        elif regname == "al" or regname == "bl" or regname == "cl" or regname == "dl":
            idx.append(0)
            if regname == "al":
                return self.rax
            elif regname == "bl":
                return self.rbx
            elif regname == "cl":
                return self.rcx
            elif regname == "dl":
                return self.rdx
            else:
                print("Unknown 8 bit reg: ", regname)
                return self.unk
        elif regname == "ah" or regname == "bh" or regname == "ch" or regname == "dh":
            idx.append(1)
            if regname == "ah":
                return self.rax
            elif regname == "bh":
                return self.rbx
            elif regname == "ch":
                return self.rcx
            elif regname == "dh":
                return self.rdx
            else:
                print("Unknown 8 bit reg: ", regname)
                return self.unk
        else:
            print("Unknown reg")
            return self.unk
    
class Type:
    IMM = 0
    REG = 1
    MEM = 2

class Operand:
    def __init__(self):
        self.ty = 0
        self.tag = 0
        self.bit = 0
        self.issegaddr = False
        self.segreg = ""
        self.field = ["", "", "", "", ""]

class Parameter:
    def __init__(self):
        self.ty = 0
        self.reg = 0
        self.idx = 0
        
    def __eq__(self, other):
        if self.ty == other.ty:
            if self.ty == Type.IMM:
                return self.idx == other.idx
            elif self.ty == Type.REG:
                return self.reg == other.reg and self.idx == other.idx
            elif self.ty == Type.MEM:
                return self.idx == other.idx
            else:
                return False
        else:
            return False
        
    def __lt__(self, other):
        if self.ty < other.ty:
            return True
        elif self.ty > other.ty:
            return False
        else:
            if self.ty == Type.IMM:
                return self.idx < other.idx
            elif self.ty == Type.REG:
                if self.reg < other.reg:
                    return True
                elif self.reg > other.reg:
                    return False
                else:
                    return self.idx < other.idx
            elif self.ty == Type.MEM:
                return self.idx < other.idx
            else:
                return True

    def isIMM(self):
        return self.ty == Type.IMM

    def show(self):
        if self.ty == Type.IMM:
            print("(IMM ", self.idx, ")")
        elif self.ty == Type.REG:
            print("(REG ", self.reg, ")")
        elif self.ty == Type.MEM:
            print("(MEM ", self.idx, ")")
        else:
            print("Parameter show() error: unkonwn src type.")

class Inst:
    def __init__(self):
        self.id = 0
        self.addr = ""
        self.addrn = 0
        self.assembly = ""
        self.opc = 0
        self.opcstr = ""
        self.oprs = []
        self.oprnum = 0
        self.oprd = [Operand(), Operand(), Operand()]
        self.ctxreg = [0, 0, 0, 0, 0, 0, 0, 0]
        self.raddr = 0
        self.waddr = 0
        self.src = []
        self.dst = []
        self.src2 = []
        self.dst2 = []

    def addsrc(self, t, s):
        if t == Type.IMM:
            p = Parameter()
            p.ty = t
            p.idx = int(s, 16)
            self.src.append(p)
        elif t == Type.REG:
            v = []
            r = Register.getRegParameter(s, v)
            for i in range(len(v)):
                p = Parameter()
                p.ty = t
                p.reg = r
                p.idx = v[i]
                self.src.append(p)
        else:
            print("addsrc error!")

    def addsrc(self, t: Type, a):
        for i in range(a[0], a[1] + 1):
            p = Parameter()
            p.ty = t
            p.idx = i
            self.src.append(p)

    def adddst(self, t, s):
        if t == Type.REG:
            v = []
            r = Register.getRegParameter(s, v)
            for i in range(len(v)):
                p = Parameter()
                p.ty = t
                p.reg = r
                p.idx = v[i]
                self.dst.append(p)
        else:
            print("adddst error!")
            
    def adddst(self, t: Type, a):
        for i in range(a[0], a[1] + 1):
            p = Parameter()
            p.ty = t
            p.idx = i
            self.dst.append(p)
            
    def addsrc2(self, t, s):
        if t == Type.IMM:
            p = Parameter()
            p.ty = t
            p.idx = int(s, 16)
            self.src2.append(p)
        elif t == Type.REG:
            v = []
            r = Register.getRegParameter(s, v)
            for i in range(len(v)):
                p = Parameter()
                p.ty = t
                p.reg = r
                p.idx = v[i]
                self.src2.append(p)
        else:
            print("addsrc2 error!")

    def addsrc2(self, t: Type, a):
        for i in range(a[0], a[1] + 1):
            p = Parameter()
            p.ty = t
            p.idx = i
            self.src2.append(p)
            
    def adddst2(self, t, s):
        if t == Type.REG:
            v = []
            r = Register.getRegParameter(s, v)
            for i in range(len(v)):
                p = Parameter()
                p.ty = t
                p.reg = r
                p.idx = v[i]
                self.dst2.append(p)
        else:
            print("adddst2 error!")

    def adddst2(self, t: Type, a):
        for i in range(a[0], a[1] + 1):
            p = Parameter()
            p.ty = t
            p.idx = i
            self.dst2.append(p)        

def find_first_not_of(s, pos, c):
    for i in range(pos, len(s)):
        if s[i] != c:
            return i
    return -1

def parseTrace(traceFile):
    instlist = []
    with open(traceFile, 'r') as infile:
        num = 1
        for line in infile:
            if not line:
                continue

            line = line.strip()
            temp = ""
            disasstr = ""
            ins = Inst()
            ins.id = num
            num += 1

            strbuf = line.split(";")
            ins.addr = strbuf[0]
            ins.addrn = int(ins.addr, 16)
            disasstr = strbuf[1]
            ins.assembly = disasstr

            disasbuf = disasstr.split(" ")
            ins.opcstr = disasbuf[0]

            temp = disasstr.split(ins.opcstr + " ")
            if len(temp) != 1:
                temp = temp[1].split(", ")
                if len(temp) <= 1:
                    ins.oprs.append(temp[0])
                else:
                    for j in range(len(temp)):
                        string = temp[j].replace(" ", "").replace("dwordptr", "dword ptr ").replace("qwordptr", "qword ptr ").replace("wordptr", "word ptr ").replace("byteptr", "byte ptr ")
                        ins.oprs.append(string)

            ins.oprnum = len(ins.oprs)

            ctxreg = strbuf[2].split(",")
            for i in range(8):
                temp = ctxreg[i]
                ins.ctxreg[i] = int(temp, 16)
            
            temp = strbuf[2].split(",")
            ins.raddr = int(temp[16], 16)
            temp = strbuf[2].split(",")
            ins.waddr = int(temp[17], 16)

            instlist.append(ins)
    return instlist

def createDataOperand(s):
    reg8 = re.compile(r"al|ah|bl|bh|cl|ch|dl|dh")
    reg16 = re.compile(r"ax|bx|cx|dx|si|di|bp|cs|ds|es|fs|gs|ss")
    reg32 = re.compile(r"eax|ebx|ecx|edx|esi|edi|esp|ebp|st0|st1|st2|st3|st4|st5")
    reg64 = re.compile(r"rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15|rip")
    immvalue = re.compile(r"0x[0-9a-f]+")
    immvalue2 = re.compile(r"[0-9a-f]+")

    opr = Operand()

    if reg64.search(s):
        m = reg64.search(s)
        opr.ty = Type.REG
        opr.bit = 64
        opr.field[0] = m.group(0)
    elif reg32.search(s):
        m = reg32.search(s)
        opr.ty = Type.REG
        opr.bit = 32
        opr.field[0] = m.group(0)
    elif reg16.search(s):
        m = reg16.search(s)
        opr.ty = Type.REG
        opr.bit = 16
        opr.field[0] = m.group(0)
    elif reg8.search(s):
        m = reg8.search(s)
        opr.ty = Type.REG
        opr.bit = 8
        opr.field[0] = m.group(0)
    elif immvalue.search(s):
        m = immvalue.search(s)
        opr.ty = Type.IMM
        opr.bit = 32 if int(s, 16) & 0xffffffff00000000 == 0 else 64
        opr.field[0] = m.group(0)
    elif immvalue2.search(s):
        m = immvalue2.search(s)
        opr.ty = Type.IMM
        opr.bit = 32 if int(s, 16) & 0xffffffff00000000 == 0 else 64
        opr.field[0] = m.group(0)
    else:
        print("Unknown data operands: ", s)
    return opr

def createAddrOperand(s):
    addr1 = re.compile(r"0x[0-9a-fA-F]+")
    addr2 = re.compile(r"eax|ebx|ecx|edx|esi|edi|esp|ebp")
    addr3 = re.compile(r"(eax|ebx|ecx|edx|esi|edi|esp|ebp)\*([0-9])")

    addr4 = re.compile(r"(eax|ebx|ecx|edx|esi|edi|esp|ebp)(\+|-)(0x[0-9a-fA-F]+)")
    addr5 = re.compile(r"(eax|ebx|ecx|edx|esi|edi|esp|ebp)\+(eax|ebx|ecx|edx|esi|edi|esp|ebp)\*([0-9])")
    addr6 = re.compile(r"(eax|ebx|ecx|edx|esi|edi|esp|ebp)\*([0-9])(\+|-)(0x[0-9a-fA-F]+)")
    
    addr7 = re.compile(r"(eax|ebx|ecx|edx|esi|edi|esp|ebp)\+(eax|ebx|ecx|edx|esi|edi|esp|ebp)\*([0-9])(\+|-)(0x[0-9a-fA-F]+)")
    
    addr8 = re.compile(r"0x[0-9a-fA-F]+")
    addr9 = re.compile(r"rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15")
    addr10 = re.compile(r"(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)\*([0-9])")

    addr11 = re.compile(r"(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)(\+|-)(0x[0-9a-fA-F]+)")
    addr12 = re.compile(r"(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)\+(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)\*([0-9])")
    addr13 = re.compile(r"(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)\*([0-9])(\+|-)(0x[0-9a-fA-F]+)")
    
    addr14 = re.compile(r"(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)\+(rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|r8|r9|r10|r11|r12|r13|r14|r15)\*([0-9])(\+|-)(0x[0-9a-fA-F]+)")

    opr = Operand()

    if addr14.search(s):
            m = addr14.search(s)
            opr.ty = Type.MEM
            opr.tag = 7
            opr.field[0] = m.group(1)
            opr.field[1] = m.group(2)
            opr.field[2] = m.group(3)
            opr.field[3] = m.group(4)
            opr.field[4] = m.group(5)
    elif addr11.search(s):
            m = addr11.search(s)
            opr.ty = Type.MEM
            opr.tag = 4
            asd = m.groups()
            opr.field[0] = m.group(1)
            opr.field[1] = m.group(2)
            opr.field[2] = m.group(3)
    elif addr12.search(s):
            m = addr12.search(s)
            opr.ty = Type.MEM
            opr.tag = 5
            opr.field[0] = m.group(1)
            opr.field[1] = m.group(2)
            opr.field[2] = m.group(3)
    elif addr13.search(s):
            m = addr13.search(s)
            opr.ty = Type.MEM
            opr.tag = 6
            opr.field[0] = m.group(1)
            opr.field[1] = m.group(2)
            opr.field[2] = m.group(3)
            opr.field[3] = m.group(4)
    elif addr10.search(s):
            m = addr10.search(s)
            opr.ty = Type.MEM
            opr.tag = 3
            opr.field[0] = m.group(1)
            opr.field[1] = m.group(2)
    elif addr8.search(s):
            m = addr8.search(s)
            opr.ty = Type.MEM
            opr.tag = 1
            opr.field[0] = m.group(0)
    elif addr9.search(s):
            m = addr9.search(s)
            opr.ty = Type.MEM
            opr.tag = 2
            opr.field[0] = m.group(0)
    else:
            if addr7.search(s):
                m = addr7.search(s)
                opr.ty = Type.MEM
                opr.tag = 7
                opr.field[0] = m.group(1)
                opr.field[1] = m.group(2)
                opr.field[2] = m.group(3)
                opr.field[3] = m.group(4)
                opr.field[4] = m.group(5)
            elif addr4.search(s):
                m = addr4.search(s)
                opr.ty = Type.MEM
                opr.tag = 4
                asd = m.groups()
                opr.field[0] = m.group(1)
                opr.field[1] = m.group(2)
                opr.field[2] = m.group(3)
            elif addr5.search(s):
                m = addr5.search(s)
                opr.ty = Type.MEM
                opr.tag = 5
                opr.field[0] = m.group(1)
                opr.field[1] = m.group(2)
                opr.field[2] = m.group(3)
            elif addr6.search(s):
                m = addr6.search(s)
                opr.ty = Type.MEM
                opr.tag = 6
                opr.field[0] = m.group(1)
                opr.field[1] = m.group(2)
                opr.field[2] = m.group(3)
                opr.field[3] = m.group(4)
            elif addr3.search(s):
                m = addr3.search(s)
                opr.ty = Type.MEM
                opr.tag = 3
                opr.field[0] = m.group(1)
                opr.field[1] = m.group(2)
            elif addr1.search(s):
                m = addr1.search(s)
                opr.ty = Type.MEM
                opr.tag = 1
                opr.field[0] = m.group(0)
            elif addr2.search(s):
                m = addr2.search(s)
                opr.ty = Type.MEM
                opr.tag = 2
                opr.field[0] = m.group(0)
            else:
                print("Unknown addr operands: ", s)
    return opr

def createOperand(s):
    ptr = re.compile(r"ptr \[(.*)\]")
    byteptr = re.compile(r"byte ptr \[(.*)\]")
    wordptr = re.compile(r"word ptr \[(.*)\]")
    dwordptr = re.compile(r"dword ptr \[(.*)\]")
    qwordptr = re.compile(r"qword ptr \[(.*)\]")
    segptr = re.compile(r"dword ptr (fs|gs):\[(.*)\]")
    segptr2 = re.compile(r"qword ptr (fs|gs):\[(.*)\]")

    opr = Operand()

    if "ptr" in s:
        if segptr.search(s):
            m = segptr.search(s)
            opr = createAddrOperand(m.group(2))
            opr.issegaddr = True
            opr.bit = 32
            opr.segreg = m.group(1)
        elif segptr2.search(s):
            m = segptr2.search(s)
            opr = createAddrOperand(m.group(2))
            opr.issegaddr = True
            opr.bit = 64
            opr.segreg = m.group(1)
        elif qwordptr.search(s):
            m = qwordptr.search(s)
            opr = createAddrOperand(m.group(1))
            opr.bit = 64
        elif dwordptr.search(s):
            m = dwordptr.search(s)
            opr = createAddrOperand(m.group(1))
            opr.bit = 32
        elif wordptr.search(s):
            m = wordptr.search(s)
            opr = createAddrOperand(m.group(1))
            opr.bit = 16
        elif byteptr.search(s):
            m = byteptr.search(s)
            opr = createAddrOperand(m.group(1))
            opr.bit = 8
        elif ptr.search(s):
            m = ptr.search(s)
            opr = createAddrOperand(m.group(1))
            opr.bit = 32
        else:
            print("Unkown addr: ", s)
    else:
        opr = createDataOperand(s)
    return opr

def parseOperand(instlist1):
    for i in range(len(instlist1)):
        for j in range(instlist1[i].oprnum):
            instlist1[i].oprd[j] = createOperand(instlist1[i].oprs[j])

class ValueTy:
    SYMBOL = 0
    CONCRETE = 1
    HYBRID = 2
    UNKNOWN = 3

class OperTy:
    ADD = 0
    MOV = 1
    SHL = 2
    XOR = 3
    SHR = 4

BitRange = Tuple[int, int]

class Operation:
    def __init__(self, opt: str, v1: 'Value', v2: 'Value' = None, v3: 'Value' = None):
        self.opty = opt
        self.val = [v1, v2, v3]

class BitSet:
    def __init__(self, size):
        self.size = size
        self.bits = 0

    def __getitem__(self, pos):
        if not (0 <= pos < self.size):
            raise IndexError("Bit position out of range.")
        return (self.bits >> pos) & 1

    def __setitem__(self, pos, value):
        if not (0 <= pos < self.size):
            raise IndexError("Bit position out of range.")
        if value:
            self.bits |= (1 << pos)
        else:
            self.bits &= ~(1 << pos)

    def set(self, pos):
        self.bits |= (1 << pos)

    def clear(self, pos):
        self.bits &= ~(1 << pos)

    def toggle(self, pos):
        self.bits ^= (1 << pos)

    def __lshift__(self, count):
        self.bits <<= count
        self.bits &= (1 << self.size) - 1  # Keep the bits within the size limit
        return self

    def __rshift__(self, count):
        self.bits >>= count
        return self

    def __str__(self):
        return f"{self.bits:0{self.size}b}"[::-1]

    def __repr__(self):
        return f"BitSet({self.size}) with bits {self.bits}"

class Value:
    idseed = 0

    def __init__(self, vty: ValueTy, oper=None, l=64, con=None, bs=None):
        self.id = Value.idseed
        Value.idseed += 1
        if Value.idseed == 413470:
            nop()
        self.valty = vty
        self.opr = oper
        self.conval = con
        self.bsconval = BitSet(l) if bs is None else bs
        self.brange = None if con is None else (0, 31)
        self.childs = {}
        self.len = l

    def isSymbol(self) -> bool:
        return self.valty == ValueTy.SYMBOL

    def isConcrete(self) -> bool:
        return self.valty == ValueTy.CONCRETE

    def isHybrid(self) -> bool:
        return self.valty == ValueTy.HYBRID

class SEEngine:
    def __init__(self):
        self.ctx = {}
        self.start = 0
        self.end = 0
        self.ip = 0
        self.mem = {}
        self.meminput = {}
        self.reginput = {}

    def memfind_ar(self, ar):
        if ar in self.mem:
            return True
        else:
            return False

    def memfind(self, b, e):
        ar = (b, e)
        if ar in self.mem:
            return True
        else:
            return False
        
    def init(self, v1, v2, v3, v4, v5, v6, v7, v8, it1, it2):
        self.ctx["eax"] = v1
        self.ctx["ebx"] = v2
        self.ctx["ecx"] = v3
        self.ctx["edx"] = v4
        self.ctx["esi"] = v5
        self.ctx["edi"] = v6
        self.ctx["esp"] = v7
        self.ctx["ebp"] = v8

        self.reginput[v1] = "eax"
        self.reginput[v2] = "ebx"
        self.reginput[v3] = "ecx"
        self.reginput[v4] = "edx"
        self.reginput[v5] = "esi"
        self.reginput[v6] = "edi"
        self.reginput[v7] = "esp"
        self.reginput[v8] = "ebp"

        self.start = it1
        self.end = it2

    def init(self, it1, it2):
        self.start = it1
        self.end = it2    

    def initAllRegSymol(self, it1, it2):
        v1 = Value(vty=ValueTy.SYMBOL)
        v2 = Value(vty=ValueTy.SYMBOL)
        v3 = Value(vty=ValueTy.SYMBOL)
        v4 = Value(vty=ValueTy.SYMBOL)
        v5 = Value(vty=ValueTy.SYMBOL)
        v6 = Value(vty=ValueTy.SYMBOL)
        v7 = Value(vty=ValueTy.SYMBOL)
        v8 = Value(vty=ValueTy.SYMBOL)
        v9 = Value(vty=ValueTy.SYMBOL)
        v10 = Value(vty=ValueTy.SYMBOL)
        v11 = Value(vty=ValueTy.SYMBOL)
        v12 = Value(vty=ValueTy.SYMBOL)
        v13 = Value(vty=ValueTy.SYMBOL)
        v14 = Value(vty=ValueTy.SYMBOL)
        v15 = Value(vty=ValueTy.SYMBOL)
        v16 = Value(vty=ValueTy.SYMBOL)
        v17 = Value(vty=ValueTy.SYMBOL)

        self.ctx["rax"] = v1
        self.ctx["rbx"] = v2
        self.ctx["rcx"] = v3
        self.ctx["rdx"] = v4
        self.ctx["rsi"] = v5
        self.ctx["rdi"] = v6
        self.ctx["rsp"] = v7
        self.ctx["rbp"] = v8
        self.ctx["r8"] =  v9
        self.ctx["r9"] =  v10
        self.ctx["r10"] = v11
        self.ctx["r11"] = v12
        self.ctx["r12"] = v13
        self.ctx["r13"] = v14
        self.ctx["r14"] = v15
        self.ctx["r15"] = v16
        self.ctx["rip"] = v17

        self.reginput[v1] = "rax"
        self.reginput[v2] = "rbx"
        self.reginput[v3] = "rcx"
        self.reginput[v4] = "rdx"
        self.reginput[v5] = "rsi"
        self.reginput[v6] = "rdi"
        self.reginput[v7] = "rsp"
        self.reginput[v8] = "rbp"
        self.reginput[v9] = "r8"
        self.reginput[v10] = "r9"
        self.reginput[v11] = "r10"
        self.reginput[v12] = "r11"
        self.reginput[v13] = "r12"
        self.reginput[v14] = "r13"
        self.reginput[v15] = "r14"
        self.reginput[v16] = "r15"
        self.reginput[v17] = "rip"
        
        self.start = it1
        self.end = it2
        
    def hasVal(self, v: Value, start, end):
        br = (start, end)
        if v == None:
            pass
        if br in v.childs:
            return True
        else:
            return False

    def getParentReg(self, s):
        if s == "eax": return "rax"
        elif s == "ebx": return "rbx"
        elif s == "ecx": return "rcx"
        elif s == "edx": return "rdx"
        elif s == "esi": return "rsi"
        elif s == "edi": return "rdi"
        elif s == "esp": return "rsp"
        elif s == "ebp": return "rbp"
        elif s == "ax": return "rax"
        elif s == "bx": return "rbx"
        elif s == "cx": return "rcx"
        elif s == "dx": return "rdx"
        elif s == "si": return "rsi"
        elif s == "di": return "rdi"
        elif s == "bp": return "rbp"
        elif s == "al": return "rax"
        elif s == "bl": return "rbx"
        elif s == "cl": return "rcx"
        elif s == "dl": return "rdx"
        elif s == "ah": return "rax"
        elif s == "bh": return "rbx"
        elif s == "ch": return "rcx"
        elif s == "dh": return "rdx"
        elif s == 'r8d': return 'r8'
        elif s == 'r9d': return 'r9'
        elif s == 'r10d': return 'r10'
        elif s == 'r11d': return 'r11'
        elif s == 'r12d': return 'r12'
        elif s == 'r13d': return 'r13'
        elif s == 'r14d': return 'r14'
        elif s == 'r15d': return 'r15'
        elif s == 'r8w': return 'r8'
        elif s == 'r9w': return 'r9'
        elif s == 'r10w': return 'r10'
        elif s == 'r11w': return 'r11'
        elif s == 'r12w': return 'r12'
        elif s == 'r13w': return 'r13'
        elif s == 'r14w': return 'r14'
        elif s == 'r15w': return 'r15'
        elif s == 'r8b': return 'r8'
        elif s == 'r9b': return 'r9'
        elif s == 'r10b': return 'r10'
        elif s == 'r11b': return 'r11'
        elif s == 'r12b': return 'r12'
        elif s == 'r13b': return 'r13'
        elif s == 'r14b': return 'r14'
        elif s == 'r15b': return 'r15'
        elif s == 'bpl': return 'rbp'
        elif s == 'spl': return 'rsp'
        else:
            return s

    def readVal(self, v: Value, start, end):
        br = (start, end)
        if br in v.childs:
            return v.childs[br]
        else:
            return None

    def buildop2(self, opty, v1: Value, v2: Value):
        oper = Operation(opty, v1, v2)
        result = None
        if opty == "concat":
            if v1.isSymbol() and v2.isSymbol():
                result = Value(ValueTy.SYMBOL, oper)
                result.len = v1.len + v2.len
            elif v1.isConcrete() and v2.isConcrete():
                result = Value(ValueTy.CONCRETE, oper)
                result.conval = v1.conval + v2.conval
                result.len = v1.len + v2.len
            else:
                result = Value(ValueTy.HYBRID, oper)
                result.len = v1.len + v2.len
                if v1.isSymbol():
                    result.childs[(0, v1.len - 1)] = v1
                elif v1.isConcrete():
                    v1_bs = BitSet(v1.len)
                    v1_bs.bits = int(v1.conval, 16)
                    v1_con = Value(ValueTy.CONCRETE, bs=v1_bs, l=v1.len)
                    v1_con.brange = (0, v1.len - 1)
                    result.childs[(0, v1.len - 1)] = v1_con
                else:  # v1 is hybrid
                    for br, v in v1.childs.items():
                        result.childs[br] = v
                
                if v2.isSymbol():
                    result.childs[(v1.len, v1.len + v2.len - 1)] = v2
                elif v2.isConcrete():
                    v2_bs = BitSet(v2.len)
                    v2_bs.bits = int(v2.conval, 16)
                    v2_con = Value(ValueTy.CONCRETE, bs=v2_bs, l=v2.len)
                    v2_con.brange = (v1.len, v1.len + v2.len - 1)
                    result.childs[(v1.len, v1.len + v2.len - 1)] = v2_con
                else:  # v2 is hybrid
                    for br, v in v2.childs.items():
                        new_br = (br[0] + v1.len, br[1] + v1.len)
                        result.childs[new_br] = v
        else:
            if v1.isSymbol() or v2.isSymbol():
                result = Value(ValueTy.SYMBOL, oper)
                result.len = v1.len  # Assuming v1 and v2 have the same length for other operations
            else:
                result = Value(ValueTy.CONCRETE, oper)
                result.len = v1.len  # Assuming v1 and v2 have the same length for other operations
        return result
    
    def buildop1(self, opty, v1: Value):
        oper = Operation(opty, v1)
        result = None
        if v1.isSymbol():
            result = Value(ValueTy.SYMBOL, oper)
        else:
            result = Value(ValueTy.CONCRETE, oper)
        return result
    
    def bs2str(self, bs: BitSet, br: BitRange):
        start, end = br
        ui = 0
        step = 1
        for i in range(start, end + 1):
            ui += bs[i] * step
            step *= 2
        return f"0x{ui:x}"
    
    def readReg(self, s):
        if s == "rax" or s == "rbx" or s == "rcx" or s == "rdx" or s == "rsi" or s == "rdi" or s == "rsp" or s == "rbp" or s == "r8" or s == "r9" or s == "r10" or s == "r11" or s == "r12" or s == "r13" or s == "r14" or s == "r15" or s == "rip":
            return self.ctx[s]
        elif s == "eax" or s == "ebx" or s == "ecx" or s == "edx" or s == "esi" or s == "edi" or s == "esp" or s == "ebp" or s == "r8d" or s == "r9d" or s == "r10d" or s == "r11d" or s == "r12d" or s == "r13d" or s == "r14d" or s == "r15d":
            v0 = self.ctx[self.getParentReg(s)]
            v1 = Value(ValueTy.CONCRETE, "0x00000000ffffffff")
            return self.buildop2("and", v0, v1)
        elif s == "ax" or s == "bx" or s == "cx" or s == "dx" or s == "si" or s == "di" or s == "bp":
            if self.hasVal(self.ctx[self.getParentReg(s)], 0, 15):
                return self.readVal(self.ctx[self.getParentReg(s)], 0, 15)
            else:
                v0 = self.ctx[self.getParentReg(s)]
                v1 = Value(ValueTy.CONCRETE, "0x0000ffff")
                return self.buildop2("and", v0, v1)
        elif s == "al" or s == "bl" or s == "cl" or s == "dl":
            rname = self.getParentReg(s)
            if self.hasVal(self.ctx[rname], 0, 7):
                return self.readVal(self.ctx[rname], 0, 7)
            else:
                v0 = self.ctx[rname]
                v1 = Value(ValueTy.CONCRETE, "0x000000ff")
                return self.buildop2("and", v0, v1)
        elif s == "ah" or s == "bh" or s == "ch" or s == "dh":
            rname = self.getParentReg(s)
            if self.hasVal(self.ctx[rname], 8, 15):
                return self.readVal(self.ctx[rname], 8, 15)
            else:
                v0 = self.ctx[rname]
                v1 = Value(ValueTy.CONCRETE, "0x0000ff00")
                v2 = self.buildop2("and", v0, v1)
                v3 = Value(ValueTy.CONCRETE, "0x8")
                return self.buildop2("shr", v2, v3)
        else:
            print("unknown reg name!")
            return None
        
    def writeVal(self, fromv: Value, tov: Value, start, end):
        res = Value(ValueTy.HYBRID)
        brfrom = (start, end)
        if tov.isHybrid():
            if brfrom in tov.childs:
                tov.childs[brfrom] = fromv
                return tov
            else:
                print("writeVal: no child in to match the from!")
                return None
        elif fromv.isSymbol() and tov.isConcrete():
            s1 = tov.brange[0]
            e1 = tov.brange[1]
            v1 = Value(ValueTy.CONCRETE, bs=tov.bsconval)
            v2 = Value(ValueTy.CONCRETE, bs=tov.bsconval)
            v1.brange = (s1, start-1)
            v1.conval = self.bs2str(v1.bsconval, v1.brange)
            v2.brange = (end+1, e1)
            v2.conval = self.bs2str(v2.bsconval, v2.brange)
            res.childs[v1.brange] = v1
            res.childs[brfrom] = fromv
            res.childs[v2.brange] = v2
            return res
        else:
            print("writeVal: the case is missing!")
            return None
        
    def writeReg(self, s: str, v: Value):
        res = None
        if s in ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rsp", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]:
            self.ctx[s] = v
        elif s in ["eax", "ebx", "ecx", "edx", "esi", "edi", "esp", "ebp", "r8d", "r9d", "r10d", "r11d", "r12d", "r13d", "r14d", "r15d"]:
            self.ctx[self.getParentReg(s)] = v
        elif s in ["ax", "bx", "cx", "dx", "si", "di", "bp", "r8w", "r9w", "r10w", "r11w", "r12w", "r13w", "r14w", "r15w"]:
            v0 = Value(ValueTy.CONCRETE, "0xffff0000")
            v1 = self.ctx[self.getParentReg(s)]
            v2 = self.buildop2("and", v1, v0)
            res = self.buildop2("or", v2, v)
            self.ctx[self.getParentReg(s)] = res
        elif s in ["al", "bl", "cl", "dl", "r8b", "r9b", "r10b", "r11b", "r12b", "r13b", "r14b", "r15b"]:
            rname = self.getParentReg(s)
            v0 = Value(ValueTy.CONCRETE, "0xffffff00")
            v1 = self.ctx[self.getParentReg(s)]
            v2 = self.buildop2("and", v1, v0)
            res = self.buildop2("or", v2, v)
            self.ctx[rname] = res
        elif s in ["ah", "bh", "ch", "dh"]:
            rname = self.getParentReg(s)
            if self.ctx[rname].isConcrete() and v.isSymbol():
                self.ctx[rname] = self.writeVal(v, self.ctx[rname], 8, 15)
            else:
                v0 = Value(ValueTy.CONCRETE, "0x8")
                v1 = self.buildop2("shl", v, v0)
                v2 = Value(ValueTy.CONCRETE, "0xffff00ff")
                v3 = self.ctx[rname]
                v4 = self.buildop2("and", v3, v2)
                res = self.buildop2("or", v4, v1)
                self.ctx[rname] = res
        else:
            print("unknown reg name!")
            
    def issubset(self, ar, superset):
        for curar in self.mem.keys():
            if curar[0] <= ar[0] and curar[1] >= ar[1]:
                superset[0] = curar[0]
                superset[1] = curar[1]
                return True
        return False
    
    def issuperset(self, ar, subset):
        for curar in self.mem.keys():
            if curar[0] >= ar[0] and curar[1] <= ar[1]:
                subset[0] = curar[0]
                subset[1] = curar[1]
                return True
        return False
    
    def isnew(self, ar):
        for curar in self.mem.keys():
            if (curar[0] <= ar[0] and curar[1] >= ar[0]) or (curar[0] <= ar[1] and curar[1] >= ar[1]):
                return False
        return True
    
    def readMem(self, addr, nbyte):
        end = addr + nbyte - 1
        ar = (addr, end)
        res = [0, 0]
        if self.memfind_ar(ar):
            return self.mem[ar]
        if self.isnew(ar):
            v = Value(ValueTy.SYMBOL, l=nbyte)
            self.mem[ar] = v
            self.meminput[v] = ar
            return v
        elif self.issubset(ar, res):
            b1, e1 = ar
            b2, e2 = (res[0], res[1])
            mask = "0x"
            for i in range(e2, b2 - 1, -1):
                if i >= b1 and i <= e1:
                    mask += "ff"
                else:
                    mask += "00"
            low0 = f"0x{(b1-b2) * 8:x}"
            v0 = self.mem[(res[0], res[1])]
            v1 = Value(ValueTy.CONCRETE, con=mask)
            v2 = self.buildop2("and", v0, v1)
            v3 = Value(ValueTy.CONCRETE, con=low0)
            v4 = self.buildop2("shr", v2, v3)
            return v4
        else: # Partial overlapping symbolic memory access 구현
            overlaps = []
            for curar in self.mem.keys():
                if (curar[0] <= ar[0] <= curar[1]) or (ar[0] <= curar[0] <= ar[1]):
                    overlaps.append(curar)
            
            if len(overlaps) == 0:
                print("readMem: No overlapping symbolic memory found!")
                v = Value(ValueTy.SYMBOL, l=nbyte)
                self.mem[ar] = v
                self.meminput[v] = ar
                return v
            
            overlaps.sort(key=lambda x: x[0])
            
            extracted_parts = []
            prev_end = ar[0]
            for overlap in overlaps:
                b1, e1 = overlap
                b2, e2 = ar
                if b1 < b2:
                    extracted_parts.append((prev_end, b2 - 1, Value(ValueTy.SYMBOL, l=b2-prev_end)))
                    prev_end = b2
                if e1 > e2:
                    extracted_parts.append((max(b1, prev_end), e2, self.mem[overlap]))
                    extracted_parts.append((e2 + 1, e1, Value(ValueTy.SYMBOL, l=e1-e2)))
                else:
                    extracted_parts.append((max(b1, prev_end), min(e1, e2), self.mem[overlap]))
                prev_end = min(e1, e2) + 1
            
            if prev_end <= ar[1]:
                extracted_parts.append((prev_end, ar[1], Value(ValueTy.SYMBOL, l=ar[1]-prev_end+1)))
            
            result = None
            for part in extracted_parts:
                start, end, v = part
                if result is None:
                    result = v
                else:
                    result = self.buildop2("concat", result, v)
            
            return result
        
    def writeMem(self, addr, nbyte, v):
        end = addr + nbyte - 1
        ar = (addr, end)
        res = [0, 0]
        if self.memfind_ar(ar) or self.isnew(ar):
            self.mem[ar] = v
            return
        elif self.issuperset(ar, res):
            self.mem.pop((res[0], res[1]))
            self.mem[ar] = v
            return
        elif self.issubset(ar, res):
            b1, e1 = ar
            b2, e2 = res
            mask = "0x"
            for i in range(e2, b2 - 1, -1):
                if i >= b1 and i <= e1:
                    mask += "ff"
                else:
                    mask += "00"
            low0 = f"0x{(b1-b2) * 8:x}"
            v0 = self.mem[(res[0], res[1])]
            v1 = Value(ValueTy.CONCRETE, con=mask)
            v2 = self.buildop2("and", v0, v1)
            v3 = Value(ValueTy.CONCRETE, con=low0)
            v4 = self.buildop2("shl", v, v3)
            v5 = self.buildop2("or", v2, v4)
            self.mem[(res[0], res[1])] = v5
            return
        else:
            print("writeMem: Partial overlapping symbolic memory access is not implemented yet!")
            return
    
    def getRegConVal(self, reg):
        if reg == "eax" or reg == "ebx" or reg == "ecx" or reg == "edx" or reg == "esi" or reg == "edi" or reg == "esp" or reg == "ebp":
            return self.ctx[self.getParentReg(reg)]
        elif reg == "rax" or reg == "rbx" or reg == "rcx" or reg == "rdx" or reg == "rsi" or reg == "rdi" or reg == "rsp" or reg == "rbp" or reg == "r8" or reg == "r9" or reg == "r10" or reg == "r11" or reg == "r12" or reg == "r13" or reg == "r14" or reg == "r15":
            return self.ctx[reg]
        else:
            print("now only get 64, 32 bit register's concrete value.")
            return 0
        
    def calcAddr(self, opr):
        r1, r2, c = 0, 0, 0
        n = 0
        if opr.tag == 7:
            r1 = self.getRegConVal(opr.field[0])
            r2 = self.getRegConVal(opr.field[1])
            n = int(opr.field[2])
            c = int(opr.field[4], 16)
            if opr.field[3] == "+":
                return r1 + r2 * n + c
            elif opr.field[3] == "-":
                return r1 + r2 * n - c
            else:
                print("unrecognized addr: tag 7")
                return 0
        elif opr.tag == 4:
            r1 = self.getRegConVal(opr.field[0])
            c = int(opr.field[2], 16)
            if opr.field[1] == "+":
                return r1 + c
            elif opr.field[1] == "-":
                return r1 - c
            else:
                print("unrecognized addr: tag 4")
                return 0
        elif opr.tag == 5:
            r1 = self.getRegConVal(opr.field[0])
            r2 = self.getRegConVal(opr.field[1])
            n = int(opr.field[2])
            return r1 + r2 * n
        elif opr.tag == 6:
            r2 = self.getRegConVal(opr.field[0])
            n = int(opr.field[1])
            c = int(opr.field[3], 16)
            if opr.field[2] == "+":
                return r2 * n + c
            elif opr.field[2] == "-":
                return r2 * n - c
            else:
                print("unrecognized addr: tag 6")
                return 0
        elif opr.tag == 3:
            r2 = self.getRegConVal(opr.field[0])
            n = int(opr.field[1])
            return r2 * n
        elif opr.tag == 1:
            c = int(opr.field[0], 16)
            return c
        elif opr.tag == 2:
            r1 = self.getRegConVal(opr.field[0])
            return r1
        else:
            print("unrecognized addr tag")

    def symexec(self, instlist1):
        for it in instlist1:
            # print(f"Line {it.id}: {it.opcstr} {it.oprs}")
            if it.opcstr in ["test","jmp","jz","jbe","jo","jno","js","jns","je","jne",
                             "jnz","jb","jnae","jc","jnb","jae",
                             "jnc","jna","ja","jnbe","jl",
                             "jnge","jge","jnl","jle","jng","jg",
                             "jnle","jp","jpe","jnp","jpo","jcxz",
                             "jecxz", "ret", "cmp", "call"]:
                continue

            if it.oprnum == 0:
                continue
            elif it.oprnum == 1:
                op0 = it.oprd[0]
                v0 = None
                res = None
                temp = None
                nbyte = 0
                if it.opcstr == "push":
                    if op0.ty == Type.IMM:
                        v0 = Value(ValueTy.CONCRETE, op0.field[0])
                        self.writeMem(it.waddr, 4, v0)
                    elif op0.ty == Type.REG:
                        nbyte = int(op0.bit / 8)
                        temp = self.readReg(op0.field[0])
                        self.writeMem(it.waddr, nbyte, temp)
                    elif op0.ty == Type.MEM:
                        nbyte = int(op0.bit / 8)
                        v0 = self.readMem(it.raddr, nbyte)
                        self.writeMem(it.waddr, nbyte, v0)
                    else:
                        print("push error: the operand is not Imm, Reg or Mem!")
                        return 1
                elif it.opcstr == "pop":
                    if op0.ty == Type.REG:
                        nbyte = int(op0.bit / 8)
                        temp = self.readMem(it.raddr, nbyte)
                        self.writeReg(op0.field[0], temp)
                    elif op0.ty == Type.MEM:
                        nbyte = int(op0.bit / 8)
                        temp = self.readMem(it.raddr, nbyte)
                        self.writeMem(it.waddr, nbyte, temp)
                    else:
                        print("pop error: the operand is not Reg!")
                        return 1
                elif it.opcstr == "inc":
                    if op0.ty == Type.REG:
                        nbyte = int(op0.bit / 8)
                        v0 = self.readReg(op0.field[0])
                        v1 = Value(ValueTy.CONCRETE, "0x1")
                        res = self.buildop2("add", v0, v1)
                        self.writeReg(op0.field[0], res)
                    else:
                        print("inc error: the operand is not Reg!")
                        return 1
                elif it.opcstr == "dec":
                    if op0.ty == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        v1 = Value(ValueTy.CONCRETE, "0xffffffff")
                        res = self.buildop2("add", v0, v1)
                        self.writeReg(op0.field[0], res)
                    else:
                        print("dec error: the operand is not Reg!")
                        return 1
                elif it.opcstr == "neg":
                    if op0.ty == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        v1 = Value(ValueTy.CONCRETE, "0x0")
                        res = self.buildop2("sub", v1, v0)
                        self.writeReg(op0.field[0], res)
                    else:
                        print("neg error: the operand is not Reg!")
                        return 1
                elif it.opcstr == "not":
                    if op0.ty == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        v1 = Value(ValueTy.CONCRETE, "0xffffffff")
                        res = self.buildop2("xor", v0, v1)
                        self.writeReg(op0.field[0], res)
                    else:
                        print("not error: the operand is not Reg!")
                        return 1
                elif it.opcstr == "mul":
                    if op0.ty == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        v1 = self.readReg("rax")
                        res = self.buildop2("mul", v0, v1)
                        self.writeReg("rax", res)
                    else:
                        print("mul error: the operand is not Reg!")
                        return 1
                elif it.opcstr == "div":
                    if op0.ty == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        v1 = self.readReg("rax")
                        res = self.buildop2("div", v0, v1)
                        self.writeReg("rax", res)
                    else:
                        print("div error: the operand is not Reg!")
                        return 1               
                else:                   
                    if op0 == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        res = self.buildop1(it.opcstr, v0)
                        self.writeReg(op0.field[0], res)
                    elif op0 == Type.MEM:
                        nbyte = int(op0.bit / 8)
                        v0 = self.readMem(it.raddr, nbyte)
                        res = self.buildop1(it.opcstr, v0)
                        self.writeMem(it.waddr, nbyte, res)
                    else:
                        print("[Error] Line ", it.id, ": Unknown 1 op instruction!")
                        return 1
            elif it.oprnum == 2:
                op0 = it.oprd[0]
                op1 = it.oprd[1]
                if it.opcstr == "mov":
                    if op0.ty == Type.REG:
                        if op1.ty == Type.IMM:
                            v1 = Value(ValueTy.CONCRETE, op1.field[0])
                            self.writeReg(op0.field[0], v1)
                        elif op1.ty == Type.REG:
                            temp = self.readReg(op1.field[0])
                            self.writeReg(op0.field[0], temp)
                        elif op1.ty == Type.MEM:
                            nbyte = int(op1.bit / 8)
                            v1 = self.readMem(it.raddr, nbyte)
                            self.writeReg(op0.field[0], v1)
                        else:
                            print("op1 is not ImmValue, Reg or Mem")
                            return 1
                    elif op0.ty == Type.MEM:
                        if op1.ty == Type.IMM:
                            temp = Value(ValueTy.CONCRETE, op1.field[0])
                            nbyte = int(op0.bit / 8)
                            self.writeMem(it.waddr, nbyte, temp)
                        elif op1.ty == Type.REG:
                            temp = self.readReg(op1.field[0])
                            nbyte = int(op0.bit / 8)
                            self.writeMem(it.waddr, nbyte, temp)
                    else:
                        print("Error: The first operand in MOV is not Reg or Mem!")
                elif it.opcstr == "lea":
                    if op0.ty != Type.REG or op1.ty != Type.MEM:
                        print("lea format error!")
                    if op1.tag == 5:
                        f0 = self.readReg(op1.field[0])
                        f1 = self.readReg(op1.field[1])
                        f2 = Value(ValueTy.CONCRETE, op1.field[2])
                        res = self.buildop2("imul", f1, f2)
                        res = self.buildop2("add",f0, res)
                        self.writeReg(op0.field[0], res)
                    if op1.tag == 5:
                        f0 = self.readReg(op1.field[0])
                        f1 = self.readReg(op1.field[1])
                        f2 = Value(ValueTy.CONCRETE, op1.field[2])
                        res = self.buildop2("imul", f1, f2)
                        res = self.buildop2("add",f0, res)
                        self.writeReg(op0.field[0], res)
                    else:
                        print("Other tags in addr is not ready for lea!")
                elif it.opcstr == "xchg":
                    if op1.ty == Type.REG:
                        v1 = self.readReg(op1.field[0])
                        if op0.ty == Type.REG:
                            v0 = self.readReg(op0.field[0])
                            self.writeReg(op1.field[0], v0)
                            self.writeReg(op0.field[0], v1)
                        elif op0.ty == Type.MEM:
                            nbyte = int(op0.bit / 8)
                            v0 = self.readMem(it.raddr, nbyte)
                            self.writeReg(op1.field[0], v0)
                            self.writeMem(it.waddr, nbyte, v1)
                        else:
                            print("xchg error: 1")
                    elif op1.ty == Type.MEM:
                        nbyte = int(op1.bit / 8)
                        v1 = self.readMem(it.raddr, nbyte)
                        if op0.ty == Type.REG:
                            v0 = self.readReg(op0.field[0])
                            self.writeReg(op0.field[0], v1)
                            self.writeMem(it.waddr, nbyte, v0)
                        else:
                            print("xchg error 3")
                    else:
                        print("xchg error: 2")
                elif it.opcstr == "shl":
                    if op0.ty == Type.REG and op1.ty == Type.IMM and self.readReg(op0.field[0]).isHybrid():
                        v0 = self.readReg(op0.field[0])
                        offset = int(op1.field[0], 0, 16)
                        newchilds = {}
                        for i in v0.childs:
                            v = i
                            if v.valty == ValueTy.SYMBOL:
                                if i.first != 0:
                                    v.brange.first = i.first + offset
                                v.brange.second = i.second + offset
                                if v.brange.second > 31:
                                    v.brange.second = 31
                            elif v.valty == ValueTy.CONCRETE:
                                v.bsconval <<= offset
                                if v.brange.first != 0:
                                    v.brange.first += offset
                                v.brange.second += offset
                                if v.brange.second > 31:
                                    v.brange.second = 31
                                v.conval = self.bs2str(v.bsconval, v.brange)
                            else:
                                print("shl: unknown value type")
                            newchilds[i] = v
                        v0.childs = newchilds
                    else:
                        if op1.ty == Type.IMM:
                            v1 = Value(ValueTy.CONCRETE, op1.field[0])
                        elif op1.ty == Type.REG:
                            v1 = self.readReg(op1.field[0])
                        elif op1.ty == Type.MEM:
                            nbyte = int(op1.bit / 8)
                            v1 = self.readMem(it.raddr, nbyte)
                        else:
                            print("other instructions: op1 is not ImmValue, Reg, or Mem!")
                            return 1

                        if op0.ty == Type.REG:
                            v0 = self.readReg(op0.field[0])
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeReg(op0.field[0], res)
                        elif op0.ty == Type.MEM:
                            nbyte = int(op0.bit / 8)
                            v0 = self.readMem(it.raddr, nbyte)
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeMem(it.waddr, nbyte, res)
                        else:
                            print("other instructions: op2 is not ImmValue, Reg, or Mem!")
                            return 1
                elif it.opcstr == "shr":
                    if op0.ty == Type.REG and op1.ty == Type.IMM and self.readReg(op0.field[0]).isHybrid():
                        v0 = self.readReg(op0.field[0])
                        offset = int(op1.field[0], 0, 16)
                        for i in v0.childs:
                            v = i
                            if v.valty == ValueTy.SYMBOL:
                                if v.brange.second != 31:
                                    v.brange.second -= offset
                                v.brange.first -= offset
                                if v.brange.first < 0:
                                    v.brange.first = 0
                            elif v.valty == ValueTy.CONCRETE:
                                v.bsconval >>= offset
                                if v.brange.second != 31:
                                    v.brange.second -= offset
                                v.brange.first -= offset
                                if v.brange.first < 0:
                                    v.brange.first = 0
                                v.conval = self.bs2str(v.bsconval, v.brange)
                            else:
                                print("shr: unknown value type")
                    else:
                        if op1.ty == Type.IMM:
                            v1 = Value(ValueTy.CONCRETE, op1.field[0])
                        elif op1.ty == Type.REG:
                            v1 = self.readReg(op1.field[0])
                        elif op1.ty == Type.MEM:
                            nbyte = int(op1.bit / 8)
                            v1 = self.readMem(it.raddr, nbyte)
                        else:
                            print("other instructions: op1 is not ImmValue, Reg, or Mem!")
                            return 1

                        if op0.ty == Type.REG:
                            v0 = self.readReg(op0.field[0])
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeReg(op0.field[0], res)
                        elif op0.ty == Type.MEM:
                            nbyte = int(op0.bit / 8)
                            v0 = self.readMem(it.raddr, nbyte)
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeMem(it.waddr, nbyte, res)
                        else:
                            print("other instructions: op2 is not ImmValue, Reg, or Mem!")
                            return 1
                elif it.opcstr == "and":
                    if op0.ty == Type.REG and op1.ty == Type.IMM and self.readReg(op0.field[0]).isHybrid():
                        v0 = self.readReg(op0.field[0])
                        v1 = Value(ValueTy.CONCRETE, op1.field[0])
                        status = True
                        for i in v0.childs:
                            if i.valty == ValueTy.SYMBOL:
                                for j in range(i.first, i.second):
                                    if v1.bsconval[j] == 1:
                                        status = False
                        if status == True:
                            res = Value(ValueTy.CONCRETE)
                            res.brange.first = 0
                            res.brange.second = 31
                            for i in v0.childs:
                                if i.valty == ValueTy.SYMBOL:
                                    for j in range(i.first, i.second):
                                        res.bsconval[j] = 0
                                elif i.valty == ValueTy.CONCRETE:
                                    for j in range(i.first, i.second):
                                        res.bsconval[j] = i.bsconval[j] & v1.bsconval[j]
                                else:
                                    print("unkown val type")
                            res.conval = self.bs2str(res.bsconval, res.brange)
                            self.writeReg(op0.field[0], res)
                    else:
                        if op1.ty == Type.IMM:
                            v1 = Value(ValueTy.CONCRETE, op1.field[0])
                        elif op1.ty == Type.REG:
                            v1 = self.readReg(op1.field[0])
                        elif op1.ty == Type.MEM:
                            nbyte = int(op1.bit / 8)
                            v1 = self.readMem(it.raddr, nbyte)
                        else:
                            print("other instructions: op1 is not ImmValue, Reg, or Mem!")
                            return 1

                        if op0.ty == Type.REG:
                            v0 = self.readReg(op0.field[0])
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeReg(op0.field[0], res)
                        elif op0.ty == Type.MEM:
                            nbyte = int(op0.bit / 8)
                            v0 = self.readMem(it.raddr, nbyte)
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeMem(it.waddr, nbyte, res)
                        else:
                            print("other instructions: op2 is not ImmValue, Reg, or Mem!")
                            return 1
                elif it.opcstr == "or":
                    if op0.ty == Type.REG and op1.ty == Type.IMM and self.readReg(op0.field[0]).isHybrid():
                        v0 = self.readReg(op0.field[0])
                        v1 = Value(ValueTy.CONCRETE, op1.field[0])
                        status = True
                        for i in v0.childs:
                            if i.valty == ValueTy.SYMBOL:
                                for j in range(i.first, i.second):
                                    if v1.bsconval[j] == 0:
                                        status = False
                        if status == True:
                            res = Value(ValueTy.CONCRETE)
                            res.brange.first = 0
                            res.brange.second = 31
                            for i in v0.childs:
                                if i.valty == ValueTy.SYMBOL:
                                    for j in range(i.first, i.second):
                                        res.bsconval[j] = 1
                                elif i.valty == ValueTy.CONCRETE:
                                    for j in range(i.first, i.second):
                                        res.bsconval[j] = i.bsconval[j] | v1.bsconval[j]
                                else:
                                    print("unkown val type")
                            res.conval = self.bs2str(res.bsconval, res.brange)
                            self.writeReg(op0.field[0], res)
                    else:
                        if op1.ty == Type.IMM:
                            v1 = Value(ValueTy.CONCRETE, op1.field[0])
                        elif op1.ty == Type.REG:
                            v1 = self.readReg(op1.field[0])
                        elif op1.ty == Type.MEM:
                            nbyte = int(op1.bit / 8)
                            v1 = self.readMem(it.raddr, nbyte)
                        else:
                            print("other instructions: op1 is not ImmValue, Reg, or Mem!")
                            return 1

                        if op0.ty == Type.REG:
                            v0 = self.readReg(op0.field[0])
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeReg(op0.field[0], res)
                        elif op0.ty == Type.MEM:
                            nbyte = int(op0.bit / 8)
                            v0 = self.readMem(it.raddr, nbyte)
                            res = self.buildop2(it.opcstr, v0, v1)
                            self.writeMem(it.waddr, nbyte, res)
                        else:
                            print("other instructions: op2 is not ImmValue, Reg, or Mem!")
                            return 1
                else:
                    if op1.ty == Type.IMM:
                        v1 = Value(ValueTy.CONCRETE, op1.field[0])
                    elif op1.ty == Type.REG:
                        v1 = self.readReg(op1.field[0])
                    elif op1.ty == Type.MEM:
                        nbyte = int(op1.bit / 8)
                        v1 = self.readMem(it.raddr, nbyte)
                    else:
                        print("other instructions: op1 is not ImmValue, Reg, or Mem!")
                        return 1

                    if op0.ty == Type.REG:
                        v0 = self.readReg(op0.field[0])
                        res = self.buildop2(it.opcstr, v0, v1)
                        self.writeReg(op0.field[0], res)
                    elif op0.ty == Type.MEM:
                        nbyte = int(op0.bit / 8)
                        v0 = self.readMem(it.raddr, nbyte)
                        res = self.buildop2(it.opcstr, v0, v1)
                        self.writeMem(it.waddr, nbyte, res)
                    else:
                        print("other instructions: op2 is not ImmValue, Reg, or Mem!")
                        return 1
            elif it.oprnum == 3:
                op0 = it.oprd[0]
                op1 = it.oprd[1]
                op2 = it.oprd[2]
                v1 = None
                v2 = None
                res = None
                if it.opcstr == "imul" and op0.ty == Type.REG and op1.ty == Type.REG and op2.ty == Type.IMM:
                    v1 = self.readReg(op1.field[0])
                    v2 = Value(ValueTy.CONCRETE, op2.field[0])
                    res = self.buildop2(it.opcstr, v1, v2)
                    self.writeReg(op0.field[0], res)
                else:
                    print("three operands instructions other than imul are not handled!")
            else:
                print("all instructions: number of operands is larger than 4!")
        return 0
    
    def print_depth(self, string, depth):
        string2 = ""
        for i in range(depth):
            string2 += " "
        string2 += string
        print(string2)
        with open("output.txt", "a") as f:
            f.write(string2 + "\n")

    def traverse2(self, v, depth=0):
        if v == None:
            return
        if v.opr == None:
            if v.valty == ValueTy.CONCRETE:
                self.print_depth(v.conval, depth)
            elif v.valty == ValueTy.SYMBOL:
                self.print_depth(f"sym{v.id}", depth)
            elif v.valty == ValueTy.HYBRID:
                self.print_depth(f"[hyb{v.id}", depth)
                for i in v.childs:
                    self.print_depth(f"[{i.first.first},{i.first.second}]:", depth)
                    depth += 1
                    self.traverse2(i.second, depth)
                    depth -= 1
                self.print_depth("]", depth)
            else:
                self.print_depth("unknown type", depth)
                return
        else:
            if isinstance(v.opr, Operation):
                self.print_depth(f"({v.opr.opty} ", depth)
                depth += 1
                self.traverse2(v.opr.val[0], depth)
                depth -= 1
                self.print_depth(" ", depth)
                depth += 1
                self.traverse2(v.opr.val[1], depth)
                depth -= 1
                self.print_depth(")", depth)
            else:
                if isinstance(v.opr, str):
                    self.print_depth(v.opr, depth)
                else:
                    self.print_depth("unknown opr type", depth)
        return
    


    def dumpreg(self, reg):
        depth = 0
        v = self.ctx[reg]
        print("reg", reg, "=")
        depth += 1
        self.traverse2(v, depth)
        depth -= 1
        print()
                
def main():
    traceFile = "instrace.txt"

    instlist1 = parseTrace(traceFile)
    parseOperand(instlist1)
    
    se1 = SEEngine()
    se1.initAllRegSymol(instlist1[0], instlist1[-1])
    se1.symexec(instlist1)
    se1.dumpreg("rax")

if __name__ == '__main__':
    main()