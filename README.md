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
    ... Kwaga
    ... meunier@kwaga.com"""
    >>> 
    >>> ec = EverContact('your-username', 'your-password')
    >>> data = ec.fetch(
    ...     '2011-02-12 08:32:14',
    ...     'Le rapport',
    ...     signature_content,
    ...     'meunier@kwaga.com',
    ...     ['recource@kwaga.com', 'ph1@kwaga.org'],
    ...     'WTN_EVERYWHERE',
    ...     'EXPLICIT_TO',
    ...     )
    >>> print data
    {u'signatureSnippet': u'Fr\xe9d\xe9ric Meunier\nCTO\nKwaga\nmeunier@kwaga.com', u'uid': 1427098098624, u'success': True, u'errorMessages': [], u'signature': {u'name': [<NAME{}Fr?d?ric Meunier>], u'n': [<N{} Fr?d?ric  Meunier >], u'source': [<SOURCE{}http\\://www.kwaga.com>], u'version': [<VERSION{}3.0>], u'role': [<ROLE{}CTO>], u'org': [<ORG{}[u'Kwaga']>], u'email': [<EMAIL{}meunier@kwaga.com>], u'fn': [<FN{}Fr?d?ric Meunier>]}, u'mailId': u'collabspot-in-1427098098624'}
    >>> 


## References:
vobject: http://vobject.skyhouseconsulting.com/
- vobject is used to parse vcard signature returned by evercontact api
