import argparse_aaron_alphabet as _argparse
import os_aaron_alphabet as _os
import string as _string
import subprocess as _subprocess
import sys as _sys


class TaggingCommandParser:
    def __init__(self):
        raise NotImplementedError()
    @staticmethod
    def parse(value):
        ans = list()
        parts = [x.strip() for x in value.split()]
        for x in parts:
            if x == "":
                continue
            mode = x[0]
            tag = x[1:]
            if mode not in "+-":
                raise ValueError()
            ans.append((mode, tag))
        return ans

class ClineParser:
    FILE = 0
    STRIP = 1
    FORMAT = 2
    def __init__(self):
        raise NotImplementedError()
    @staticmethod
    def explain():
        return """\
A command to be executed on every found file. 
\t-\tescape
\t{}\tfile
\t§\tstrip
\t%\tformat"""
    @classmethod
    def dictionary(cls):
        return {
            '{}': cls.FILE,
            '§': cls.STRIP,
            '%': cls.FORMAT,
        }
    @classmethod
    def parse(cls, args, *, file):
        args = cls.parse_escape(args)
        args = cls.parse_file(args, file=file)
        args = cls.parse_strip(args)
        args = cls.parse_format(args)
        return args
    @classmethod
    def parse_escape(cls, args):
        ans = list()
        escape = False
        for arg in args:
            if escape:
                escape = False
                ans.append(arg)
                continue
            if arg == "-":
                escape = True
                continue
            ans.append(cls.dictionary().get(arg, arg))
        if escape:
            raise ValueError("Unescaped escape-command at the end! ")
        return ans
    @classmethod
    def parse_file(cls, args, *, file):
        ans = list()
        for arg in args:
            if arg == cls.FILE:
                ans.append(file)
            else:
                ans.append(arg)
        return ans
    @classmethod
    def parse_strip(cls, args):
        ans = list()
        escape = 0
        for arg in args:
            if arg == cls.STRIP:
                escape += 1
                continue
            if escape:
                ans.append(arg[escape:])
                escape = 0
            else:
                ans.append(arg)
        if escape != 0:
            raise ValueError("Unescaped strip-command at the end! ")
        return ans
    @classmethod
    def parse_format(cls, args):
        ans = list()
        escape = None
        for arg in args:
            if arg == cls.FORMAT:
                if escape is None:
                    escape = list()
                else:
                    ans.append(escape[0] % tuple(escape[1:]))
                    escape = None
            elif escape is None:
                ans.append(arg)
            elif type(arg) is str:
                escape.append(arg)
            else:
                raise ValueError()
        if escape is not None:
            raise ValueError("Format-command remains unclosed! ")
        return ans


        
        
class Lever:
    def __init__(self, value):
        self.file = value
    def __str__(self):
        return self.file
    def tag(self, *values):
        self.tags = self.tags + tuple(values)
    def untag(self, *values):
        values = [Lever._tag(x) for x in values]
        self.tags = (x for x in self.tags if (x not in values))
    def mayconflictwith(self, value):
        return self.tagfree_clone().absfile == value.tagfree_clone().absfile
    def clone(self, tagfree=False):
        ans = Lever(self)
        if tagfree:
            ans.tags = tuple()
        return ans

    @staticmethod
    def _tag(value):
        value = str(value).strip().lower()
        if "#" in value:
            raise ValueError(f"{ascii(value)} is not a legal tag! ")
        ans = ""
        for ch in value:
            if ch == "#":
                raise ValueError()
            elif ch in (_string.ascii_lowercase + _string.digits):
                ans += ch
            else:
                ans += "-"
        ans = ans.strip("-")
        if ans == "":
            return "-"
        else:
            return ans


    @property
    def file(self):
        return _os.os.path.normpath(_os.os.path.join(self.directory, self.filename))
    @file.setter
    def file(self, value):
        self.directory, self.filename = _os.os.path.split(str(value))

    @property
    def absfile(self):
        return _os.os.path.abspath(self.file)

    @property
    def filename(self):
        return " #".join((self.filetitle,) + self.tags) + self.ext
    @filename.setter
    def filename(self, value):
        y, self.ext = _os.os.path.splitext(str(value))
        y = y.replace("\xa0", " ")
        tags = list()
        words = list()
        for part in y.split(" "):
            if part == "":
                continue
            elif part.startswith("#"):
                tags.append(part[1:])
            else:
                words.append(part)
        self.filetitle = " ".join(words)
        self.tags = tags

    @property
    def directory(self):
        return self._directory
    @directory.setter
    def directory(self, value):
        self._directory = _os.os.path.normpath(str(value))

    @property
    def absdirectory(self):
        return _os.os.path.abspath(self.directory)

    @property
    def ext(self):
        return self._ext
    @ext.setter
    def ext(self, value):
        self._ext = str(value)

    @property
    def filetitle(self):
        return self._filetitle
    @filetitle.setter
    def filetitle(self, value):
        value = str(value)
        if "#" in value:
            raise ValueError(f"{ascii(value)} is not a legal filetitle! ")
        ans = ""
        for x in value:
            if x in (_string.ascii_letters + _string.digits):
                ans += x
            else:
                ans += "-"
        ans = ans.strip("-")
        if ans == "":
            ans = "-"
        self._filetitle = ans

    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, value):
        ans = list()
        for x in value:
            y = Lever._tag(x)
            if y not in ans:
                ans.append(y)
        self._tags = tuple(ans)



    


class Formula:
    def __init__(self):
        raise NotImplementedError()
    @staticmethod
    def isformula(value):
        return issubclass(type(value), Formula)
    @staticmethod
    def from_string(value):
        value = str(value)
        for x in "()~&|^":
            value = value.replace(x, f" {x} ")
        parts = [x.strip() for x in value.split()]
        parts = [x for x in parts if x != ""]
        return Formula.from_iter(parts)
    @staticmethod
    def _from_part(value):
        if value in list("()~&|^"):
            return value
        if Formula.isformula(value):
            return value
        return Get(value)
    @staticmethod
    def from_iter(values):
        parts = [Formula._from_part(x) for x in values]
        while "(" in parts:
            closing = parts.index(")")
            opening = closing - 1
            while opening >= 0:
                if parts[opening] == "(":
                    break
                opening -= 1
            else:
                raise ValueError()
            x = Formula._from_iter(parts[opening+1:closing])
            parts = parts[:opening] + [x] + parts[closing+1:]
        return Formula._from_iter(parts)
    @staticmethod
    def _from_iter(values):
        if len(values) == 0:
            return Const(True)
        if (len(values) == 1) and (values[0] == "~"):
            return Const(False)
        values = list(values)
        while "~" in values:
            i = values.index("~")
            x = Unitary(*values[i:i+2])
            values = values[:i] + [x] + values[i+2:]
        while len(values) > 1:
            x = Multi(values[1], values[0], values[2])
            values = [x] + values[3:]
        return values[0]

class Const(Formula):
    def __init__(self, value):
        self.value = value
    def __call__(self, info=None):
        return self.value
    def __repr__(self):
        return f"Const: {self.value}"

class Get(Formula):
    def __init__(self, key):
        self.key = key
    def __call__(self, info):
        return info(self.key)
    def __repr__(self):
        return f"Get: {self.key}"

class OP(Formula):
    def __call__(self, info):
        values = [s(info) for s in self.subformulas]
        return type(self).calc(self.mode, *values)

class Multi(OP):
    def __init__(self, mode, *subformulas):
        self.mode = mode
        self.subformulas = subformulas
    @staticmethod
    def calc(mode, *values):
        if mode == "&":
            return all(values)
        if mode == "|":
            return any(values)
        if mode == "^":
            return bool(sum(bool(v) for v in values) % 2)
        raise ValueError()
    def __repr__(self):
        return "(" + f"){self.mode}(".join(s.__repr__() for s in self.subformulas) + ")"

class Unitary(OP):
    def __init__(self, mode, subformula):
        self.mode = mode
        self.subformula = subformula
    @staticmethod
    def calc(mode, value):
        if mode == "~":
            return not value
        raise ValueError()
    @property
    def subformulas(self):
        return [self.subformula]
    def __repr__(self):
        return f"{self.mode}({self.subformula.__repr__()})"

class Info:
    def __init__(self, data):
        self.data = data
    def __call__(self, key):
        return self.data.get(key, False)





        
def main(args=None):
    parser = _argparse.parser()
    parser.add_argument('tagfilter', nargs='?', default=Const(True), type=Formula.from_string)
    parser.add_argument('-I', '--inputs', dest='I', default=['.'], nargs='+', help="Target files and target folders. ")
    parser.add_argument('-C', '--change', dest='C', type=TaggingCommandParser.parse, help="Change tagging, i.e. '+tag1 -tag2 -tag3'. ")
    parser.add_argument('-x', '--exec', dest='x', nargs='+', action='append', help=ClineParser.explain())
    #parser.add_argument('-i', '--interactive', dest='i', action='store_true', default=False)
    ns = parser.parse_args(args)
    run(**vars(ns))


def run(*, tagfilter, C, x, I):
    files = _os.walk(*I)
    files.sort()
    levers = {file:Lever(file) for file in files}
    _files = dict()
    for file in files:
        clone = str(levers[file].clone(tagfree=True))
        if clone in _files.keys():
            print(f"Warning: {ascii(_files[clone])} vs {ascii(file)}")
        else:
            _files[clone] = file
    for file in files:
        lever = levers[file]
        info = Info({tag: True for tag in lever.tags})
        if not tagfilter(info):
            continue
        printmode = True
        if C is not None:
            printmode = False
            for mode, tag in C:
                if mode == "+":
                    lever.tag(tag)
                else:
                    lever.untag(tag)
            if _os.os.path.abspath(file) != lever.absfile:
                if _os.os.path.exists(lever.file):
                    raise FileExistsError(f"The file {ascii(lever.file)} already exists! ")
                _os.os.rename(file, lever.file)
        if x is not None:
            printmode = False
            for line in x:
                _subprocess.run(ClineParser.parse(line, file=file), check=True)
        if printmode:
            print(file.__repr__())




if __name__ == '__main__':
    main()
