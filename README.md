## Purpose
Minimal Python BIP70 URI and URL decoder. Tested with BitPay Payment Protocol invoices.

## Usage
Required python packages: `urllib3`, `base58` and `protobuf`

Use with a BIP70 request URL or URI:
```
./decode.py https://merchant.test/payment.php?id=1234
./decode.py bitcoin:1jakISJ?a=1&b=2&r=https://merchant.test/payment/1234
./decode.py bitcoin:?r=https://merchant.test/payment/1234

> Local time of invoice: 2018-10-19 20:22:25
> Local time of expiry: 2018-10-19 20:37:25
> Amount: 0.013000
> Address: 12HBETYHLfcsX9CpASQMhvsEThegNstcma

```

## Limitations
- Limited to one output
- Limited to P2PKH script in the output

## License
These scripts, unless otherwise stated, are subject to the MIT license.
