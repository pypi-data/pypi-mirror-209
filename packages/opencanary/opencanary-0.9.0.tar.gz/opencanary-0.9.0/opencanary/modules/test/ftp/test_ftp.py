from opencanary.modules.ftp import CanaryFTP
from opencanary.config import config
from opencanary.logger import getLogger
from twisted.trial import unittest
from twisted.test import proto_helpers
from twisted.internet import reactor, defer

logger = getLogger(config)

class CanaryFTPTestCase(unittest.TestCase):

    def setUp(self):
        canaryFTP = CanaryFTP(config=config, logger=logger)
        # self.service = canaryFTP.getService()
        # self.service.startService()
        self.proto = canaryFTP.getService().args[1].buildProtocol(('127.0.0.1', config.getVal('ftp.port')))
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)

    def _test(self, operation, a, b, expected):
        self.proto.dataReceived(u'{} {} {}\r\n'.format(operation, a, b).encode('utf-8'))
        self.assertEqual(int(self.tr.value()), expected)

    def test_banner(self):
        # import pdb;pdb.set_trace()
        return self.assertEqual(self.tr.value(), '220 {}\r\n'.format(config.getVal('ftp.banner')))

    # @defer.inlineCallbacks
    def tearDown(self):
        # result = yield self.service.stopService()
        self.proto.wrappedProtocol.setTimeout(None)

    # def test_logging(self):
    #     import pdb; pdb.set_trace()
    #     return True


    # def test_add(self):
    #     return self._test('add', 7, 6, 13)


    # def test_subtract(self):
    #     return self._test('subtract', 82, 78, 4)


    # def test_multiply(self):
    #     return self._test('multiply', 2, 8, 16)


    # def test_divide(self):
    #     return self._test('divide', 14, 3, 4)