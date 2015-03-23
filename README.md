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
    >>> print data['signature']
    BEGIN:VCARD
    VERSION:3.0
    N:Meunier;Frédéric;;;
    FN:Frédéric Meunier
    NAME:Frédéric Meunier
    PROFILE:VCARD
    SOURCE:http\\\://www.kwago.com
    ROLE:CTO
    ORG:Kwaga
    EMAIL:foo@kwago.com
    END:VCARD
    >>> 


## References:
vobject: http://vobject.skyhouseconsulting.com/
- vobject is used to parse vcard signature returned by evercontact api
