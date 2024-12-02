from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import base64

# Generate RSA Key Pair
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()

# Sign the Document
def sign_document(private_key, document):
    return private_key.sign(document, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

# Verify the Signature
def verify_signature(public_key, document, signature):
    try:
        public_key.verify(signature, document, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True
    except:
        return False

# Main Execution
if __name__ == "__main__":
    private_key, public_key = generate_keys()
    document = b"This is a confidential document."
    
    # Sign the document and verify
    signature = sign_document(private_key, document)
    print(f"Document: {document.decode()}")
    #print(f"Signature (Base64): {base64.b64encode(signature).decode()}")
    print(f"Signature Valid: {verify_signature(public_key, document, signature)}")
    
    # Optionally, save keys
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
