from OpenSSL import crypto
import base64


TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA


def getKey_Cert ():
    """
    Function to generate a pair of key type DSA
    Parameter:  None
    Return:
        key:    the private key for signing the message (PKey)
        cer:    signing certificate, or public key (X509)
    """
    key = crypto.PKey()
    cer = crypto.X509()
    crypto.PKey.generate_key(key, TYPE_DSA, 256)
    cer.set_pubkey(key)
    return key, cer


def makeSendMessage(message, key):
    """
    Function to generate MACs and combine with the messsage before sending
    Parameter:  
        message:  original message (bytes)
        key:      the private key for signing the message (PKey)
    Return:
        outbound: the combined message to be sent (bytes)
    """
    MAC = crypto.sign(key, message.encode(), "sha256") 
    outbound = message.encode().replace(b'00000', b'000001') + b'000000' + MAC.replace(b'00000', b'000001')
    return outbound


def getMessage (inbound, cer):
    """
    Function to separate MACs and the messsage from inbound data
    Parameter:  
        inbound: received message (bytes)
        cer:     signing certificate, or public key (X509)
    Return:
        message: original message (bytes)
    """
    message, _, MAC = inbound.partition(b'000000')
    message = message.replace(b'000001', b'00000')
    MAC = MAC.replace(b'000001', b'00000')
    if _:
        try:
            crypto.verify(cer, MAC, message, "sha256")
            return message
        except:
            print ("Unauthentic")
            return ""
    else:
        print ("Error during transmition")
        return ""


key, cer = getKey_Cert()

message = "Hello! m"
print (len(message.encode()))
outbound = makeSendMessage(message, key)
message = getMessage (outbound, cer) 
print (message)




    