# encoding: utf-8
# module Wms.RemotingObjects.Blobs calls itself Blobs
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BlobContent():
    """ BlobContent() """
    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: BlobContent) -> Array[Byte]

Set: Content(self: BlobContent) = value
"""

    MimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MimeType(self: BlobContent) -> str

Set: MimeType(self: BlobContent) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return BlobContent()

