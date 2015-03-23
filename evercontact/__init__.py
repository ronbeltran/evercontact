# -*- coding: UTF-8 -*-
import json

import vobject
import requests
from requests.auth import HTTPBasicAuth

EVERCONTACT_API_ENDPOINT = 'https://api.evercontact.com/pulse-api/tag'


class EverContact(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def fetch(self, payload, signature_format='json'):
        """ EverContact API by default returns signature data in VCard format.
        signature: String
        Can be either in `vcard` or `json`
        """

        resp = requests.post(EVERCONTACT_API_ENDPOINT, data=payload,
                             auth=HTTPBasicAuth(self.username, self.password))
        content = json.loads(resp.content)
        if signature_format not in ['json', 'vcard']:
            return content
        if signature_format == 'vcard':
            return content
        signature = content['signature']
        content['signature'] = vobject.readOne(signature).contents
        return content

