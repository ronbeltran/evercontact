## Python API Client for EverContact

## Sample Usage:

First install evercontact module:

    cd evercontact
    python setup.py install

    >>> from evercontact import EverContact
    >>> 
    >>> signature_content = """
    ... Let’s meet next week.
    ... --
    ... Frédéric Meunier
    ... CTO
    ... Kwago
    ... foo@kwago.com"""
    >>> 
    >>> ec = EverContact('your-username', 'your-password')
    >>> data = ec.fetch(
    ...     '2011-02-12 08:32:14',
    ...     'Le rapport',
    ...     signature_content,
    ...     'foo@kwago.com',
    ...     ['bar@kwago.com', 'baz@kwago.org'],
    ...     'WTN_EVERYWHERE',
    ...     'EXPLICIT_TO',
    ...     )
    >>> print data
    {u'signatureSnippet': u'Fr\xe9d\xe9ric Meunier\nCTO\nKwaga\nfoo@kwago.com', u'uid': 1427098098624, u'success': True, u'errorMessages': [], u'signature': {u'name': [<NAME{}Fr?d?ric Meunier>], u'n': [<N{} Fr?d?ric  Meunier >], u'source': [<SOURCE{}http\\://www.kwago.com>], u'version': [<VERSION{}3.0>], u'role': [<ROLE{}CTO>], u'org': [<ORG{}[u'Kwaga']>], u'email': [<EMAIL{}foo@kwago.com>], u'fn': [<FN{}Fr?d?ric Meunier>]}, u'mailId': u'name-in-1427098098624'}
    >>> 


## References:
vobject: http://vobject.skyhouseconsulting.com/
- vobject is used to parse vcard signature returned by evercontact api
