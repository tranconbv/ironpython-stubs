# encoding: utf-8
# module Wms.RemotingObjects.DocumentQueue.Messages calls itself Messages
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ChangePrintJobStatusMessage(object):
 """ ChangePrintJobStatusMessage() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ChangePrintJobStatusMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ExternalJobId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Job id giving by External service.

Get: ExternalJobId(self: ChangePrintJobStatusMessage) -> str

Set: ExternalJobId(self: ChangePrintJobStatusMessage)=value
"""

 JobId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Job id giving by BOXwise server.

Get: JobId(self: ChangePrintJobStatusMessage) -> str

Set: JobId(self: ChangePrintJobStatusMessage)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Informational message about the new status.

Get: Message(self: ChangePrintJobStatusMessage) -> str

Set: Message(self: ChangePrintJobStatusMessage)=value
"""

 NewStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """New status the job got on this change.

Get: NewStatus(self: ChangePrintJobStatusMessage) -> PrintJobStatusEnum

Set: NewStatus(self: ChangePrintJobStatusMessage)=value
"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A timestamp in UTC when this message was created

Get: TimeStamp(self: ChangePrintJobStatusMessage) -> DateTime

Set: TimeStamp(self: ChangePrintJobStatusMessage)=value
"""



class GetStatusOfJobsMessage(object):
 """
 request a status update of multiple jobs.
 
 GetStatusOfJobsMessage()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetStatusOfJobsMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Jobs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Jobs we want a report of,if possible.

Get: Jobs(self: GetStatusOfJobsMessage) -> List[Item]

Set: Jobs(self: GetStatusOfJobsMessage)=value
"""


 Item=None


class PrintJobDispatchedMessage(object):
 """
 Message to let boxwise know printerjob has been dispatched to printer(service).
 
 PrintJobDispatchedMessage()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintJobDispatchedMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ExternalJobId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Job id the job got by the external platform when dispatching job.

Get: ExternalJobId(self: PrintJobDispatchedMessage) -> str

Set: ExternalJobId(self: PrintJobDispatchedMessage)=value
"""

 JobId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Job id giving by BOXwise server.

Get: JobId(self: PrintJobDispatchedMessage) -> str

Set: JobId(self: PrintJobDispatchedMessage)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Informational message.

Get: Message(self: PrintJobDispatchedMessage) -> str

Set: Message(self: PrintJobDispatchedMessage)=value
"""

 NewStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Current status of the job,expect to be: dispatched

Get: NewStatus(self: PrintJobDispatchedMessage) -> PrintJobStatusEnum

Set: NewStatus(self: PrintJobDispatchedMessage)=value
"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A timestamp in UTC when this message was created

Get: TimeStamp(self: PrintJobDispatchedMessage) -> DateTime

Set: TimeStamp(self: PrintJobDispatchedMessage)=value
"""



class StartPrintJobMessage(object):
 """
 Message to request a print of a document.
 
 StartPrintJobMessage()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StartPrintJobMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 BlobContainerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Blob container name where the document contents are stored under.

Get: BlobContainerName(self: StartPrintJobMessage) -> str

Set: BlobContainerName(self: StartPrintJobMessage)=value
"""

 BlobName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Blob name where the document contents are stored under.

Get: BlobName(self: StartPrintJobMessage) -> str

Set: BlobName(self: StartPrintJobMessage)=value
"""

 DocumentName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name that will be usd for the print job (seen in the print job queue).

Get: DocumentName(self: StartPrintJobMessage) -> str

Set: DocumentName(self: StartPrintJobMessage)=value
"""

 DocumentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of document to print (pdf/raw etc)

Get: DocumentType(self: StartPrintJobMessage) -> DocumentTypeEnum

Set: DocumentType(self: StartPrintJobMessage)=value
"""

 JobId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Job id giving by BOXwise server.

Get: JobId(self: StartPrintJobMessage) -> str

Set: JobId(self: StartPrintJobMessage)=value
"""

 PrinterId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the printer in the external service.

Get: PrinterId(self: StartPrintJobMessage) -> str

Set: PrinterId(self: StartPrintJobMessage)=value
"""

 PrinterOptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Printer options to use for doing this printjob.

Get: PrinterOptions(self: StartPrintJobMessage) -> PrintingOptions

Set: PrinterOptions(self: StartPrintJobMessage)=value
"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A timestamp in UTC when this message was created

Get: TimeStamp(self: StartPrintJobMessage) -> DateTime

Set: TimeStamp(self: StartPrintJobMessage)=value
"""



