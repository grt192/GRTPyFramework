from wpilib import NetworkTable as NT
from wpilib import BooleanArray, NumberArray, StringArray
from wpilib import ITableListener

class ITable:
    """
    Wrapper for robotpy SIP ITable interface

    Wrapped to be more pythonic.
    Works like a dictionary, items can be set as strings, numbers,
    or lists of homogeneous items (lists of strings, booleans, numbers)

    this.nettab is the wrapped wpilib.ITable instance
    (for use with C++ functions, for instance)
    """

    def __init__(self, nettab):
        self.nettab = nettab
        self.__contains__ = nettab.ContainsKey
        self.contains_subtable = nettab.ContainsSubTable
        self.add_table_listener = nettab.AddTableListener
        self.remove_table_listener = nettab.RemoveTableListener
        self.add_subtable_listener = nettab.AddSubTableListener
        self.is_connected = nettab.IsConnected
        self.is_server = nettab.IsServer

    def __contains__(self, key):
        return self.nettab.ContainsKey(key)

    def __getitem__(self, key):
        if key in self:
            val = self.nettab.GetValue(key)
            if isinstance(val, (BooleanArray, NumberArray, StringArray)):
                return _arraydata_to_list(val)
            return val
        else:
            return None

    def __setitem__(self, key, val):
        if isinstance(val, (float, int)):
            self.nettab.PutNumber(key, val)
        elif isinstance(val, str):
            self.nettab.PutString(key, val)
        elif isinstance(val, bool):
            self.nettab.PutBoolean(key, val)
        elif isinstance(val, list):
            self.nettab.PutValue(key, _list_to_arraydata(val))
        else:
            raise Exception("Value given is not a number, string, or list.")

    def get_subtable(self, key):
        """
        Returns a wrapped subtable.
        """
        return ITable(self.nettab.GetSubTable(key))


class Listener(ITableListener):
    """
    Interface for listener for table changes.
    """
    def __init__(self):
        ITableListener.__init__(self)

    def ValueChanged(self, table, key, value, is_new):
        print('Value changed: key %s, isNew: %s: %s' % (key, is_new, table.GetValue(key)))


def set_server():
    NT.SetServerMode()


def set_client():
    NT.SetClientMode()


def set_ip(ip):
    NT.SetIPAddress(ip)


def set_team(team):
    NT.SetTeam(team)


def initialize():
    NT.Initialize()


def get_table(key):
    """
    Returns a wrapped subtable.
    """
    return ITable(NT.GetTable(key))


def _list_to_arraydata(lst):
    if len(lst) == 0:
        return StringArray()
    try:
        if isinstance(lst[0], (float, int)):
            arr = NumberArray()
            for x in lst:
                arr.add(float(x))
        elif isinstance(lst[0], str):
            arr = StringArray()
            for x in lst:
                arr.add(str(x))
        elif isinstance(lst[0], bool):
            arr = BooleanArray()
            for x in lst:
                arr.add(bool(x))
    except:
        raise Exception("List given is probably not homogeneous.")


def _arraydata_to_list(arr):
    return [arr.get(i) for i in range(arr.size())]
