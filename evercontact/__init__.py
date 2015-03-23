# -*- coding: UTF-8 -*-
import logging
import json

import vobject
import requests

EVERCONTACT_API_ENDPOINT = 'https://api.evercontact.com/pulse-api/tag'
ADDRESSING_MODE = [
    'EXPLICIT_FROM',
    'EXPLICIT_TO',
    'EXPLICIT_CC',
    'OTHER',
]
ANALYSIS_STRATEGY = ['KWAGA_CORE', 'WTN_EVERYWHERE']


class MandatoryFieldError(ValueError):

    message = u'Missing mandatory {name} field.'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.message.format(name=self.name)


class EverContact(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def fetch(self, date, subject, content,
              header_from, header_to, analysis_strategy,
              addressing_mode='OTHER', header_cc=None, attach_files=None,
              signature_format='json'):
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
            - AnalysisStrategy:
                KWAGA_CORE for accuracy, WTN_EVERYWHERE in other cases

            Optional keys are the following:
            - HeaderCC: The Message “Cc” or “Bcc” Recipients
                Please note this parameter should be repeated
                when there are multiple receivers.
            - AttachedFiles: Use File Names & extension.
                Please note this parameter should be repeated when there are
                multiple file attachments.
        """
        if header_from is None:
            raise MandatoryFieldError('HeaderFrom')
        if header_to is None:
            raise MandatoryFieldError('HeaderTo')
        if addressing_mode not in ADDRESSING_MODE:
            raise ValueError('Invalid value for AddressingMode: {0}'.format(
                addressing_mode))
        if analysis_strategy not in ANALYSIS_STRATEGY:
            raise ValueError('Invalid value for AnalysisStrategy: {0}'.format(
                analysis_strategy))
        if header_cc is None:
            header_cc = []
        if attach_files is None:
            attach_files = []
        payload = {
            'Date': date,
            'ApiUser': self.username,
            'Subject': subject,
            'HeaderFrom': header_from,
            'HeaderTo': header_to,
            'AddressingMode': addressing_mode,
            'AnalysisStrategy': analysis_strategy,
            'Content': content,
        }
        if header_cc:
            payload.update({'HeaderCC': header_cc})
        if attach_files:
            payload.update({'AttachedFiles': attach_files})

        resp = requests.post(EVERCONTACT_API_ENDPOINT, data=payload,
                             auth=(self.username, self.password))
        content = json.loads(resp.content)

        if signature_format not in ['json', 'vcard']:
            return content
        if signature_format == 'vcard':
            return content
        signature = content['signature']
        sig_vobject = vobject.readOne(signature).contents
        content['signature_json'] = sig_vobject
        logging.info(vobject.readOne(signature).prettyPrint())
        return content
