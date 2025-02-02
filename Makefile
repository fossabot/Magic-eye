PYTHON = python3
PIP = pip3
# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = install
PYINSTALLER_86_64= pyinstaller  --target-arch=86_64 --hidden-import src/settings  -n 'Magic Eye' --onedir src/MagicEye.py --noconfirm
PYINSTALLER_arm_64= pyinstaller --target-arch=arm64  --hidden-import src/settings -n 'Magic Eye' --onedir src/MagicEye.py --noconfirm
USER=$(shell logname)
#use sudo before executing
install:
	mkdir /home/$(USER)/.config/MagicEye
	$(PYTHON) src/settings.py
	$(PYINSTALLER_86_64)
	cp -r MagicEye-icon  /home/$(USER)/.local/share/icons
	chmod +x 'Magic Eye.desktop'
	cp -r 'Magic Eye.desktop' /home/$(USER)/.local/share/applications/
	cp -r 'dist/Magic Eye' /usr/local/bin

uninstall:
	rm -rf /home/$(USER)/.config/MagicEye
	rm -rf /home/$(USER)/.local/share/icons/MagicEye-icon
	rm -rf /home/$(USER)/.local/share/applications/'Magic Eye.desktop'
	rm -rf /usr/local/bin/'Magic Eye'

update:
	rm -rf /usr/local/bin/'Magic Eye'
	$(PYINSTALLER_86_64)
	cp -r  'dist/Magic Eye' /usr/local/bin
	cp -r 'Magic Eye.desktop' /home/$(USER)/.local/share/applications/

installArm:
	mkdir /home/$(USER)/.config/MagicEye
	$(PYTHON) src/settings.py
	$(PYINSTALLER_AArch_64)
	cp -r MagicEye-icon  /home/$(USER)/.local/share/icons
	chmod +x 'Magic Eye.desktop'
	cp -r 'Magic Eye.desktop' /home/$(USER)/.local/share/applications/
	cp -r 'dist/Magic Eye' /usr/local/bin

updateArm:
	rm -rf /usr/local/bin/'Magic Eye'
	$(PYINSTALLER_AArch_64)

	cp -r  'dist/Magic Eye' /usr/local/bin
	cp -r 'Magic Eye.desktop' /home/$(USER)/.local/share/applications/

# In this context, the *.project pattern means "anything that has the .project extension"
