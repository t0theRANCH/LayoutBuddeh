# change permissions and name
chmod +x main.py
mv main.py layout-buddeh

# make a directory to install user-created scripts and programs
mkdir -p ~/bin
cp layout-buddeh ~/bin

# add new directory to path
export PATH=$PATH":$HOME/bin"
echo 'export PATH=$PATH":$HOME/bin"' >> .profile
source .profile