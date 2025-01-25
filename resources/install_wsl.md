```sh
wsl install
wsl --list
wsl --set-default Ubuntu

sudo apt update
sudo apt install python3
whereis python
alias python=python3
chmod +x /mnt/c/scripts/serveur/jboss.py

sudo apt-get install dos2unix
cd /mnt/c/scripts/serveur/
find -type f -print0 | xargs -0 dos2unix

nano ~/.bashrc
export PYTHONPATH="${PYTHONPATH}:/mnt/c/scripts/lib"

nvm
https://monovm.com/blog/install-nvm-on-ubuntu/
```