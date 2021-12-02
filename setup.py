import os

# Write bash aliases
file_path = os.path.realpath(__file__)
f = open("../.bash_aliases", "w")
f.writelines([
    "alias get='bash %s/get'" % file_path,
    "\nalias submit='bash %s/submit'" % file_path,
    "\nalias test='bash %s/test'" % file_path
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
  f = open("%s/id_rsa" % ssh_path, "w")
  f.write(os.getenv("private_ssh_key"))
  f.close()

  # Public ssh key
  f = open("%s/id_rsa.pub" % ssh_path, "w")
  f.write(os.getenv("public_ssh_key"))
  f.close()