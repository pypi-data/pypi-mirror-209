import lib_dzne_basetables as _bt
import lib_dzne_tsv as _tsv
import lib_dzne_workbook as _wb
import lib_dzne_seq as _seq
import tomllib as _tomllib
import tomli_w as _tomli_w
import os as _os
import pandas as _pd
import openpyxl as _xl

class _StreamType:
    class _Stream:
        @property
        def streamType(self):
            return self._streamType
        @property
        def extension(self):
            return _StreamType.get_extension(self._string)
        def __str__(self):
            return self._string
        def read(self):
            if self._string == "":
                return self._streamType.get_default_data()
            return self._streamType.read(self._string)
        def write(self, data, overwrite=False):
            if self._string == "":
                self._streamType.drop_data()
            if _os.os.path.exists(self._string) and not overwrite:
                raise FileExistsError(self._string)
            self._streamType.write(self._string, data)
    def __call__(self, string):
        if type(string) is not str:
            raise TypeError(f"Streams can only be created from strings! The type {type(string)} is not supported! ")
        if string not in ("", '-') and self._extensions is not None:
            x = _os.os.path.splitext(string)[1]
            if x not in self._extensions.keys():
                raise ValueError(f"{string.__repr__()}: {x.__repr__()} not among {tuple(self._extensions.keys())}! ")
        stream = _StreamType._Stream()
        stream._streamType = self
        stream._string = string
        return stream
    def __init__(self, *, extensions=None):
        self._extensions = dict(extensions) if (extensions is not None) else None
    def read(self, string):
        raise NotImplementedError()
    def write(self, string, data):
        raise NotImplementedError()
    def get_default_data(self):
        raise NotImplementedError()
    def drop_data(self):
        raise ValueError("It is forbidden to drop the data. ")
    @property
    def extensions(self):
        return dict(self._extensions) if (self._extensions is not None) else None

class TabStreamType(_StreamType):
    def read(self, string, *, strip=False, **kwargs):
        data = _tsv.read_DataFrame(string, **kwargs)
        if strip:
            data = data.applymap(lambda x: x.strip())
        return data
    def write(self, string, data, *, strip=False):
        if strip:
            data = data.applymap(lambda x: x.strip())
        _tsv.write_DataFrame(string, data)
    def get_default_data(self):
        return _pd.DataFrame()

class BASEStreamType(TabStreamType):
    def __init__(self, basetype=None):
        self._basetype = basetype
        if basetype is None:
            x = None
        elif basetype in {'a', 'd', 'm', 'y', 'c'}:
            x = {f".{basetype}base": f"{basetype}base"}
        else:
            raise ValueError()
        super().__init__(extensions=x)
    def read(self, string, **kwargs):
        data = super().read(string, **kwargs)
        data = _bt.table.make(data, basetype=self._basetype)
        return data
    def write(self, string, data):
        data = _bt.table.make(data, basetype=self._basetype)
        super().write(string, data)
    def get_default_data(self):
        return _bt.table.make(basetype=self._basetype)

class TOMLStreamType(_StreamType):
    def __init__(self):
        super().__init__(extensions={'.toml': "TOML"})
    def read(self, string):
        with open(string, 'rb') as s:
            return _tomllib.load(s)
    def write(self, string, data):
        with open(string, 'wb') as s:
            _tomli_w.dump(data, s)
    def get_default_data(self):
        return dict()


class TextStreamType(_StreamType):
    def __init__(self):
        super().__init__(extensions={'.log': 'Log', '.txt': 'Text'})
    def read(self, string):
        lines = list()
        with open(file, 'r') as s:
            for line in s:
                assert line.endswith('\n')
                lines.append(line[:-1])
        return lines
    def write(self, string, data):
        with open(file, 'w') as s:
            for line in lines:
                print(line, file=s)
    def get_default_data(self):
        return list()


class WorkbookStreamType(_StreamType):
    def __init__(self):
        super().__init__(extensions={'.xlsx':'excel'})
    def read(self, string):
        return _wb.from_file(string)
    def write(self, string, data):
        if type(data) is not _xl.Workbook:
            raise TypeError()
        data.save(filename=string)
    def get_default_data(self):
        return _xl.Workbook()

class SeqreadInStreamType(_StreamType):
    def __init__(self):
        super().__init__(extensions={'.phd': 'phd', '.ab1': 'abi'})
    def read(self, string):
        x = _os.path.splitext(string)[1]
        return _seq.SeqRead(
            file=string, 
            format=self.extensions[x],
        )
    def get_default_data(self):
        return _seq.SeqRead()
class SeqreadOutStreamType(_StreamType):
    def __init__(self):
        super().__init__(extensions={'.phd': 'phd'})
    def write(self, string, data):
        x = _os.path.splitext(string)[1]
        _seq.SeqRead(data).save(
            file=string,
            format=self.extensions[x],
        )








        