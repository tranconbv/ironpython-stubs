# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.ColliReferences calls itself ColliReferences
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ColliBarcodeResult(object):
 """ ColliBarcodeResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ColliBarcodeResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: ColliBarcodeResult) -> str

Set: Barcode(self: ColliBarcodeResult)=value
"""

 FaultMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FaultMessage(self: ColliBarcodeResult) -> str

Set: FaultMessage(self: ColliBarcodeResult)=value
"""

 IsOwnCompanySSCC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies if the barcode is a SSCC barcode of this company

Get: IsOwnCompanySSCC(self: ColliBarcodeResult) -> bool

Set: IsOwnCompanySSCC(self: ColliBarcodeResult)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: ColliBarcodeResult) -> ReferenceType

Set: Type(self: ColliBarcodeResult)=value
"""



class ValidateColliReferencesArgs(object):
 """
 ValidateColliReferencesArgs()
 ValidateColliReferencesArgs(innerReference: str,outerReference: str,*exclusion: Array[object])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ValidateColliReferencesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,innerReference=None,outerReference=None,exclusion=None):
  """
  __new__(cls: type)
  __new__(cls: type,innerReference: str,outerReference: str,*exclusion: Array[object])
  """
  pass
 ExclusionList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExclusionList(self: ValidateColliReferencesArgs) -> List[object]

Set: ExclusionList(self: ValidateColliReferencesArgs)=value
"""

 InnerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InnerReference(self: ValidateColliReferencesArgs) -> str

Set: InnerReference(self: ValidateColliReferencesArgs)=value
"""

 OuterReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OuterReference(self: ValidateColliReferencesArgs) -> str

Set: OuterReference(self: ValidateColliReferencesArgs)=value
"""

 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Result(self: ValidateColliReferencesArgs) -> ValidateColliReferencesResult

Set: Result(self: ValidateColliReferencesArgs)=value
"""



class ValidateColliReferencesResult(object):
 """
 ValidateColliReferencesResult()
 ValidateColliReferencesResult(isInnerReferenceValid: bool,isOuterReferenceValid: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ValidateColliReferencesResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,isInnerReferenceValid=None,isOuterReferenceValid=None):
  """
  __new__(cls: type)
  __new__(cls: type,isInnerReferenceValid: bool,isOuterReferenceValid: bool)
  """
  pass
 IsInnerReferenceValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsInnerReferenceValid(self: ValidateColliReferencesResult) -> Nullable[bool]

Set: IsInnerReferenceValid(self: ValidateColliReferencesResult)=value
"""

 IsOuterReferenceValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsOuterReferenceValid(self: ValidateColliReferencesResult) -> Nullable[bool]

Set: IsOuterReferenceValid(self: ValidateColliReferencesResult)=value
"""



