# encoding: utf-8
# module Wms.SharedInfra.Cryptography.PasswordHashing calls itself PasswordHashing
# from Wms.SharedInfra,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class HashBytes(object):
 """ HashBytes() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HashBytes()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CreateFromString(key,salt):
  """ CreateFromString(key: str,salt: str) -> HashBytes """
  pass
 Key=None
 Salt=None


class HashBytesExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HashBytesExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromString(hashBytes,key,salt):
  """ FromString(hashBytes: HashBytes,key: str,salt: str) -> HashBytes """
  pass
 @staticmethod
 def KeyAsString(hashBytes):
  """ KeyAsString(hashBytes: HashBytes) -> str """
  pass
 @staticmethod
 def SaltAsString(hashBytes):
  """ SaltAsString(hashBytes: HashBytes) -> str """
  pass
 __all__=[
  'FromString',
  'KeyAsString',
  'SaltAsString',
 ]


class IPasswordHasher:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IPasswordHasher()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Hash(self,password,saltLength=None,keyLength=None,iterations=None):
  """
  Hash(self: IPasswordHasher,password: str,saltLength: int,keyLength: int,iterations: int) -> HashBytes
  Hash(self: IPasswordHasher,password: str) -> HashBytes
  """
  pass
 def Verify(self,password,salt,key,iterations=None):
  """
  Verify(self: IPasswordHasher,password: str,salt: Array[Byte],key: Array[Byte],iterations: int) -> bool
  Verify(self: IPasswordHasher,password: str,salt: Array[Byte],key: Array[Byte]) -> bool
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class PBKDF2PasswordHasher(object):
 """ PBKDF2PasswordHasher() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PBKDF2PasswordHasher()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Hash(self,password,saltLength=None,keyLength=None,iterations=None):
  """
  Hash(self: PBKDF2PasswordHasher,password: str,saltLength: int,keyLength: int,iterations: int) -> HashBytes
  Hash(self: PBKDF2PasswordHasher,password: str) -> HashBytes
  """
  pass
 def Verify(self,password,salt,key,iterations=None):
  """
  Verify(self: PBKDF2PasswordHasher,password: str,salt: Array[Byte],key: Array[Byte],iterations: int) -> bool
  Verify(self: PBKDF2PasswordHasher,password: str,salt: Array[Byte],key: Array[Byte]) -> bool
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

