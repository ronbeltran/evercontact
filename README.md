## Python API Client for EverContact

## Sample Usage:

First install evercontact module:

    cd evercontact
    python setup.py install

The use in your python script:

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    from evercontact import EverContact

    if __name__ == "__main__":

        signature_content = """
        Let’s meet next week.
        --
        Frédéric Meunier
        CTO
        Kwaga
        meunier@kwaga.com"""

        ec = EverContact('your-username', 'your-password')
        data = ec.fetch(
            '2011-02-12 08:32:14',
            'Le rapport',
            signature_content,
            'meunier@kwaga.com',
            ['recource@kwaga.com', 'ph1@kwaga.org'],
            'WTN_EVERYWHERE',
            'EXPLICIT_TO',
            )
        print data
