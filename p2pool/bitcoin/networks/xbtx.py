import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

import scryptSquared as scrypt2

P2P_PREFIX = '58425443'.decode('hex')
P2P_PORT = 8778
ADDRESS_VERSION = 60
RPC_PORT = 8766
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue('xbtsaddress' in (yield bitcoind.rpc_help()) and not (yield bitcoind.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 1000 # good enough for now
POW_FUNC = lambda data: pack.IntType(256).unpack(scrypt2.getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'XBTX'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bitcoinsubsidium') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BitcoinSubsidium/') if platform.system() == 'Darwin' else os.path.expanduser('/root/.BitcoinSubsidium'), 'BitcoinSubsidium.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://144.76.99.135/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://144.76.99.135/address/'
TX_EXPLORER_URL_PREFIX = 'http://144.76.99.135/tx/'
SANE_TARGET_RANGE = (2**(256-32) - 1, 2**(256-8) - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.1e8
