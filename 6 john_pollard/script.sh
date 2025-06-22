openssl x509 -in cert -pubkey -noout > pubkey.pem
RsaCtfTool --publickey pubkey.pem --dumpkey --private
