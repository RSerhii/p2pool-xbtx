from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['xbtx']
SHARE_PERIOD = 60 # seconds
CHAIN_LENGTH = 24*60 # shares
REAL_CHAIN_LENGTH = 24*60 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923610'.decode('hex')
PREFIX = '58425443'.decode('hex')
P2P_PORT = 7778
MIN_TARGET = 0
MAX_TARGET = 2**(256-8) - 1
PERSIST = False
WORKER_PORT = 28336
BOOTSTRAP_ADDRS = ''
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK=lambda v: v >= 70030
