from pathlib import Path
from base64 import b64encode, b64decode

from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature

private_key_path = Path("~/.ssh/id_ed25519").expanduser()
with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_ssh_private_key(
            key_file.read(),
            password=None,
        )


def sign(message: str) -> str:
    signature = private_key.sign(message.encode())
    return b64encode(signature).decode()

## Verification 
public_key_path = Path("./key.pub")
with open(public_key_path, "rb") as key_file:
    public_key = serialization.load_ssh_public_key(
            key_file.read(),
        )

def verify(signature: str, message: str) -> bool:
    signature = b64decode(signature)
    try:
        public_key.verify(signature, message.encode())
        return True
    except InvalidSignature:
        return False


if __name__ == '__main__':
    segunda = sign('segunda')
    quarta = sign('quarta')

    print(segunda)
    print(quarta)
    print()
    print(verify(segunda, 'segunda'))
    print(verify(quarta, 'quarta'))
