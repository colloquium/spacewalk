# Makefile for registration server for RHNS
#
# $Id: Makefile,v 1.11 2004/05/28 01:35:32 bretm Exp $

# what is the backend top dir
TOP     = ../..

# Specific stuff
SUBDIR		= rhn/actions
##EXEC_FILES	= rhncfg-client
FILES           = __init__ solarispkgs
##CONFIG_FILES    = rhncfg-client.conf

# man pages
##DOCBOOK = $(wildcard /usr/bin/docbook2man)
##SGMLS	= $(wildcard *.sgml)
##MANS	= $(patsubst %.sgml,%.8,$(SGMLS))
##MANDIR	?= /usr/man

EXTRA_DIRS	= $(BINDIR) $(CONFDIR) $(MANDIR)/man8

include $(TOP)/Makefile.defs

ifneq ($(DOCBOOK),)
# install man pages
all	:: $(MANS)
install :: $(MANS) $(PREFIX)/$(MANDIR)
	$(INSTALL_DATA) $(MANS) $(PREFIX)/$(MANDIR)/man8
clean   ::
	@rm -fv $(MANS) manpage.*
endif

%.8 : %.sgml
	/usr/bin/docbook2man $<

install	:: install-bin install-conf

