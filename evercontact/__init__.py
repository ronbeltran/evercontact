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
        payload: dict
            Mandatory keys are the following:
            - ApiUser: API login access.
            - Date: The Message Date, UTC and ISO formatted.
                (e.g. 2011-11-04 13:44:34)
            - Subject: The Message Subject
            - HeaderFrom: The Message Sender(s).
                Please note this parameter should be
                repeated when there are multiple senders.
            - HeaderTo: The Message “To” Recipient(s).
                Please note this parameter should be
                repeated when there are multiple receivers.
            - AddressingMode: Specify whether the mail is an
                outgoing (EXPLICIT_FROM) or incoming (EXPLICIT_TO,
                EXPLICIT_CC).  If this information is not available,
                please include OTHER.
            - Content: The Message Content, plain text/html.
                Note: Content having more than 100 000 bytes
                will return an Error

            Optional keys are the following:
            - HeaderCC: The Message “Cc” or “Bcc” Recipients
                Please note this parameter should be repeated
                when there are multiple receivers.
            - AttachedFiles: Use File Names & extension.
                Please note this parameter should be repeated when there are
                multiple file attachments.
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
