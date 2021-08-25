# Author : Ashwini Sahu
# GitHub : https://github.com/ASHWIN990/template
# Date   : Tue Aug 24 06:57:50 PM IST 2021

TEMPLATE_INSTALL_PATH := /usr/share
BIN_INSTALL_PATH := /usr/bin

install:
	@echo "Installing Binary to    : $(BIN_INSTALL_PATH)/template"
	@echo "Installing Templates to : $(TEMPLATE_INSTALL_PATH)/template_maker"
	@install -Dm775 template.py    -T $(BIN_INSTALL_PATH)/template
	@install -Dm644 template_maker/* -t $(TEMPLATE_INSTALL_PATH)/template_maker
	
uninstall:
	@echo "Removing Binary from    : $(BIN_INSTALL_PATH)/template"
	@echo "Removing Templates from : $(TEMPLATE_INSTALL_PATH)/template_maker"
	@rm $(BIN_INSTALL_PATH)/template
	@rm -rf $(TEMPLATE_INSTALL_PATH)/template_maker/
