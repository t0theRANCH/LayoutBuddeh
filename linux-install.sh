# change permissions and name
chmod +x main.py
mv main.py layout-buddeh

# make a directory to install user-created scripts and programs
mkdir -p ~/bin/layout-buddeh
mv layout-buddeh ~/bin/layout-buddeh
mv diagram.txt ~/bin/layout-buddeh
mv title.txt ~/bin/layout-buddeh

# add new directory to path
export PATH=$PATH":$HOME/bin/layout-buddeh"
echo 'export PATH=$PATH":$HOME/bin/layout-buddeh"' >> .profile
source .profile

# delete downloaded folder
rm -rf -- "$(pwd -P)" && cd ..