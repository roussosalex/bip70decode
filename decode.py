#!/usr/bin/env python3
import sys
import base58
import hashlib
import urllib3
import binascii
import datetime
import paymentrequest_pb2
import urllib.parse
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')


def url_from_input(addr):
    return addr if addr.find("bitcoin:") != 0 else urllib.parse.parse_qs(addr.split("?", 1)[1])['r'][0]


def address_from_script(p2pkh):
    p = '00' + p2pkh.hex()[6:-4]
    d = int(p + hashlib.new('sha256', hashlib.sha256(binascii.unhexlify(p)).digest()).hexdigest()[0:8], 16)
    return '1' + base58.b58encode(d.to_bytes((d.bit_length() + 7) // 8, 'big')).decode('ascii')


def decode_pr(addr):
    dat = http.request('GET', url_from_input(addr), headers={'Accept': 'application/bitcoin-paymentrequest'}).data
    req = paymentrequest_pb2.PaymentRequest().FromString(dat)
    return paymentrequest_pb2.PaymentDetails().FromString(req.serialized_payment_details)


def print_pr(pr):
    print("Local time of invoice:", datetime.datetime.fromtimestamp(pr.time).strftime("%Y-%m-%d %H:%M:%S"))
    print("Local time of expiry:", datetime.datetime.fromtimestamp(pr.expires).strftime("%Y-%m-%d %H:%M:%S"))
    print("Amount:", pr.outputs[0].amount / 100000000)
    print("Address:", address_from_script(pr.outputs[0].script))


print_pr(decode_pr(sys.argv[1]))
