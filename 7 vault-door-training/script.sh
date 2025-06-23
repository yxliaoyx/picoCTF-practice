PASSWORD=$(grep 'password.equals' VaultDoorTraining.java | cut -d'"' -f2)
echo "picoCTF{$PASSWORD}"
