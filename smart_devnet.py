from datetime import datetime
import json

from rfc3339 import rfc3339
import requests

URL_TEMPLATE = ("https://npwifi.smart.com.ph/1/smsmessaging/outbound/%s/"
    + "requests")


class SmartDevnet(object):

    def __init__(self, sp_id, sp_password, nonce, created_at, access_code,
                             sp_service_id, path_to_cert):
        self.sp_id = sp_id
        self.sp_password = sp_password
        self.access_code = access_code
        self.url = URL_TEMPLATE % access_code
        self.path_to_cert = path_to_cert
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'WSSE realm="SDP",profile="UsernameToken"',
            'X-RequestHeader': ('request TransId="", ServiceId="%s"' %
                                sp_service_id),
            }

    def send_sms(self, mobile_number, message):
        self.headers['X-WSSE'] = ('UsernameToken Username="%s",' +
                                  'PasswordDigest="%s",' +
                                  'Nonce="%s",' +
                                  'Created="%s"'
                                  ) % (self.sp_id, self.sp_password, "nonce",
                                  rfc3339(datetime.utcnow()) + 'Z')
        data = json.dumps({
            'outboundSMSMessageRequest': {
                'address': ['tel:#' + str(mobile_number)],
                'senderAddress': self.access_code,
                'outboundSMSTextMessage': {
                    'message': message
                    }
                }
            })
        return requests.post(self.url, data=data, cert=self.path_to_cert,
                             headers=self.headers)
