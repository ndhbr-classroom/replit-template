import os

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
  # Private ssh key
  private_ssh_key_path = "%s/id_rsa" % ssh_path
  f = open(private_ssh_key_path, "w")
  f.write(os.getenv("private_ssh_key") or "")
  f.close()
  os.chmod(private_ssh_key_path, 0o600)

  # Public ssh key
  public_ssh_key_path = "%s/id_rsa.pub" % ssh_path
  f = open(public_ssh_key_path, "w")
  f.write(os.getenv("public_ssh_key") or "")
  f.close()
  os.chmod(public_ssh_key_path, 0o600)

  print("Starting OTH-Console...")
  # Missing SSH key warning
  # TODO: we may generate a key pair for the user
  if os.getenv("public_ssh_key") == None:
    print("Warning: public_ssh_key not set (secrets tab)")
  if os.getenv("private_ssh_key") == None:
    print("Warning: private_ssh_key not set (secrets tab)")
  print("\nYou now can use the commands get, check and submit.")