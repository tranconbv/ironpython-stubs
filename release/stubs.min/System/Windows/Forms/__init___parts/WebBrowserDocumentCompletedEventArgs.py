class WebBrowserDocumentCompletedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.WebBrowser.DocumentCompleted event.
 
 WebBrowserDocumentCompletedEventArgs(url: Uri)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return WebBrowserDocumentCompletedEventArgs()

 @staticmethod
 def __new__(self,url):
  """ __new__(cls: type,url: Uri) """
  pass
 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the document to which the System.Windows.Forms.WebBrowser control has navigated.

Get: Url(self: WebBrowserDocumentCompletedEventArgs) -> Uri

"""


