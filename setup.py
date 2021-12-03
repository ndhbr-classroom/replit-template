import os
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

# Write bash aliases
file_path = os.path.realpath(os.path.dirname(__file__))
f = open("../.custom_bashrc", "w")
f.writelines([
    "PS1=\"\e[0;32mOTH-Console\e[0m> \""
    "\nalias get='bash %s/get.sh'" % file_path,
    "\nalias submit='bash %s/submit.sh'" % file_path,
    "\nalias check='bash %s/check.sh'" % file_path
])
f.close()

# Add git keys
ssh_path = "../.ssh"
try:
  # Create ssh folder
  if not os.path.isdir(ssh_path):
    os.mkdir(ssh_path)
except OSError:
  print ("Creation of the directory %s failed" % ssh_path)
else:
  # Crypto key
  key = rsa.generate_private_key(
      backend=crypto_default_backend(),
      public_exponent=65537,
      key_size=2048
  )

  # Private ssh key
  private_ssh_key_path = "%s/id_rsa" % ssh_path
  private_ssh_key = os.getenv("private_ssh_key")
  if not private_ssh_key:
    private_ssh_key = key.private_bytes(
      crypto_serialization.Encoding.PEM,
      crypto_serialization.PrivateFormat.PKCS8,
      crypto_serialization.NoEncryption()
    )
  f = open(private_ssh_key_path, "w")
  f.write(private_ssh_key.decode("utf-8") or "")
  f.close()
  os.chmod(private_ssh_key_path, 0o600)

  # Public ssh key
  public_ssh_key_path = "%s/id_rsa.pub" % ssh_path
  public_ssh_key = os.getenv("public_ssh_key")
  if not public_ssh_key:
    public_key = key.public_key().public_bytes(
      crypto_serialization.Encoding.OpenSSH,
      crypto_serialization.PublicFormat.OpenSSH
    )
  f = open(public_ssh_key_path, "w")
  f.write(public_key.decode("utf-8") or "")
  f.close()
  os.chmod(public_ssh_key_path, 0o600)

  # Environment
  f = open("%s/.env" %file_path, "w")
  f.writelines([
    "public_ssh_key=\"%s\"" % public_ssh_key,
    "\nprivate_ssh_key=\"%s\"" % private_ssh_key
  ])
  f.close()

  print("Starting OTH-Console...")
  # Missing SSH key warning
  # TODO: we may generate a key pair for the user
  if not os.getenv("public_ssh_key"):
    print("Warning: public_ssh_key not set (secrets tab)")
  if not os.getenv("private_ssh_key"):
    print("Warning: private_ssh_key not set (secrets tab)")
  print("\nYou now can use the commands get, check and submit.")