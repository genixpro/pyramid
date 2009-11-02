from zope.interface import implements

from repoze.bfg.interfaces import IAfterTraversal
from repoze.bfg.interfaces import INewRequest
from repoze.bfg.interfaces import INewResponse
from repoze.bfg.interfaces import IWSGIApplicationCreatedEvent

class NewRequest(object):
    """ An instance of this class is emitted as an event whenever
    repoze.bfg begins to process a new request.  The instance has an
    attribute, ``request``, which is the request object.  This class
    implements the ``repoze.bfg.interfaces.INewRequest`` interface."""
    implements(INewRequest)
    def __init__(self, request):
        self.request = request

class NewResponse(object):
    """ An instance of this class is emitted as an event whenever any
    repoze.bfg view returns a response..  The instance has an
    attribute, ``response``, which is the response object returned by
    the view.  This class implements the
    ``repoze.bfg.interfaces.INewResponse`` interface."""
    implements(INewResponse)
    def __init__(self, response):
        self.response = response

class AfterTraversal(object):
    implements(IAfterTraversal)
    """ An instance of this class is emitted as an event after the
    repoze.bfg router performs traversal (but before any view code is
    executed).  The instance has an attribute, ``request``, which is
    the request object returned by the view.  Notably, the request
    object will have an attribute named ``context``, which is the
    context that will be provided to the view which will eventually be
    called, as well as other attributes defined by the traverser.
    This class implements the
    ``repoze.bfg.interfaces.IAfterTraversal`` interface."""
    def __init__(self, request):
        self.request = request
    
class WSGIApplicationCreatedEvent(object):    
    """ An instance of this class is emitted as an event whenever a
    ``repoze.bfg`` application starts.  The instance has an attribute,
    ``app``, which is an instance of the ``repoze.bfg.router.Router``
    class that will handle WSGI requests.  This class implements the
    ``repoze.bfg.interfaces.IWSGIApplicationCreatedEvent`` interface."""
    implements(IWSGIApplicationCreatedEvent)
    def __init__(self, app):
        self.app = app
        self.object = app

