# encoding: utf-8
# module Wms.SharedInfra.RuleEngine calls itself RuleEngine
# from Wms.SharedInfra, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Condition:
    """
    Condition()
    Condition(field: str, operator: str, value: str)
    Condition(field: str, operator: str, values: IEnumerable[str])
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, field=None, operator=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, field: str, operator: str, value: str)
        __new__(cls: type, field: str, operator: str, values: IEnumerable[str])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Field(self: Condition) -> str

Set: Field(self: Condition) = value
"""

    Operator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Operator(self: Condition) -> str

Set: Operator(self: Condition) = value
"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: Condition) -> IEnumerable[str]

Set: Values(self: Condition) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return Condition()

class ICondition:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Field(self: ICondition) -> str

Set: Field(self: ICondition) = value
"""

    Operator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Operator(self: ICondition) -> str

Set: Operator(self: ICondition) = value
"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: ICondition) -> IEnumerable[str]

Set: Values(self: ICondition) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ICondition()

class IRule:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Conditions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Conditions(self: IRule) -> List[ICondition]

Set: Conditions(self: IRule) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: IRule) -> DateTime

Set: CreatedOn(self: IRule) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: IRule) -> int

Set: Id(self: IRule) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: IRule) -> int

Set: Priority(self: IRule) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IRule()

class OperatorEnum:
    """ enum OperatorEnum, values: OperatorIn (2), OperatorIs (0), OperatorIsNot (1), OperatorNotIn (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OperatorIn = None
    OperatorIs = None
    OperatorIsNot = None
    OperatorNotIn = None
    value__ = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return OperatorEnum()

class Rule:
    """ Rule() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Conditions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Conditions(self: Rule) -> List[ICondition]

Set: Conditions(self: Rule) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: Rule) -> DateTime

Set: CreatedOn(self: Rule) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Rule) -> int

Set: Id(self: Rule) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: Rule) -> int

Set: Priority(self: Rule) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return Rule()

class RuleEngine():
    # no doc
    @staticmethod
    def CalculatePriority(*__args):
        """ CalculatePriority(printRules: IEnumerable[IRule])CalculatePriority(rule: IRule) -> int """
        pass

    @staticmethod
    def Execute(attributes, printRules):
        """ Execute(attributes: Dictionary[str, str], printRules: List[IRule]) -> IRule """
        pass

    @staticmethod
    def FindMatchingRules(attributes, printRules):
        """ FindMatchingRules(attributes: Dictionary[str, str], printRules: List[IRule]) -> List[IRule] """
        pass

    __all__ = [
        'CalculatePriority',
        'Execute',
        'FindMatchingRules',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return RuleEngine()

