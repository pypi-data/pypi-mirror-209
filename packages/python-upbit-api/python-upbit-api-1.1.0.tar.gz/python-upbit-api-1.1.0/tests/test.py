import pprint

from upbit import Upbit

upbit = Upbit('lxioiqBwiW9HiMAE9F65HweqGB1qzIxRazE8q557', 'RTe81YmsW1C01XT7tMvYPw9wx8NDf9FlhpGt1UNx')
res = upbit.get_deposits(currency='KRW')
# res = upbit.get_deposits(txids=['307176bd3a81e4d9ca5a9dd1f5fa70b1dd3de567901b5419fab17471633e5555'])
# res = upbit.get_wallet_status()
# res = upbit.create_coin_address('BTC', net_type='BTC')
pprint.pprint(res.json())
