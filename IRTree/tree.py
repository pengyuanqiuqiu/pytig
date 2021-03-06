#exp
class Const:
    def __init__(self, i, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children = ['CONST', i]


class Name:
    def __init__(self, n, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children = ['NAME', n]


class Temp:
    def __init__(self, t, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children = ['TEMP', t]


class Binop:
    def __init__(self, o, e1, e2, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children =  [o, e1, e2]


class Mem:
    def __init__(self, e, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children = ['MEM', e]


class Call:
    def __init__(self, f, l, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children = ['CALL', f, l]


class Eseq:
    def __init__(self, s, e, ty='TY_VOID', kind='ex'):
        self.ty = ty
        self.kind = kind
        self.children = ['ESEQ', s, e]

# stmt
class Move:
    def __init__(self, dst, src, ty='TY_VOID', kind='nx'):
        self.ty = ty
        self.kind = kind
        self.children = ['MOVE', dst, src]


class Exp:
    def __init__(self, e, ty='TY_VOID', kind='nx'):
        self.ty = ty
        self.kind = kind
        self.children = ['EXP', e]


class Jump:
    def __init__(self, e, labels, ty='TY_VOID', kind='nx'):
        self.ty = ty
        self.kind = kind
        self.children = ['JUMP', e, labels]


class Cjump:
    def __init__(self, o, e1, e2, t, f, ty='TY_VOID', kind='cx'):
        self.ty = ty
        self.kind = kind
        self.children = ['CJUMP', o, e1, e2, t, f]


class Seq:
    def __init__(self, s1, s2, ty='TY_VOID', kind='nx'):
        self.ty = ty
        self.kind = kind
        self.children = ['SEQ', s1, s2]


class Label:
    def __init__(self, n, ty='TY_VOID', kind='nx'):
        self.ty = ty
        self.kind = kind
        self.children = ['LABEL', n]