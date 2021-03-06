# Makefile for spacewalk-utils
#
# $Id$

NAME := spacewalk-utils

SUBDIR  = utils

FILES	= __init__ systemSnapshot migrateSystemProfile
SCRIPTS = sw-system-snapshot migrate-system-profile spacewalk-api apply_errata \
	  scr.cgi spacewalk-common-channels delete-old-systems-interactive spacewalk-hostname-rename \
	  spacewalk-dump-schema
CONFIGS = spacewalk-common-channels.ini

DOCBOOK = $(wildcard /usr/bin/docbook2man)

SGMLS	= $(wildcard *.sgml)
MANS	= $(patsubst %.sgml,%.8,$(SGMLS) )

BINDIR	= /usr/bin
MANDIR	?= /usr/man
CONFDIR = /etc/rhn

EXTRA_DIRS = $(MANDIR)/man8 $(BINDIR) $(CONFDIR)

include Makefile.defs

# install scripts
all :: $(SCRIPTS)
install :: $(SCRIPTS) $(PREFIX)/$(BINDIR)
	$(INSTALL_BIN) $(SCRIPTS) $(PREFIX)/$(BINDIR)

ifneq ($(DOCBOOK),)
# install man pages
all	:: $(MANS)
	pod2man --section=8 spacewalk-api spacewalk-api.8
	pod2man --section=8 delete-old-systems-interactive delete-old-systems-interactive.8
	pod2man --section=8 spacewalk-dump-schema spacewalk-dump-schema.8
install :: $(MANS) $(PREFIX)/$(MANDIR)
	$(INSTALL_DATA) $(MANS) spacewalk-api.8* delete-old-systems-interactive.8 spacewalk-dump-schema.8* $(PREFIX)/$(MANDIR)/man8
install :: $(CONFIGS) $(PREFIX)/$(CONFDIR)
	$(INSTALL_DATA) $(CONFIGS) $(PREFIX)/$(CONFDIR)
endif

%.new : %
	sed -e 's|@@ROOT@@|$(ROOT)|g' <$* >$@

%.8 : %.sgml
	$(DOCBOOK) $<

clean ::
	@rm -fv $(MANS) manpage.* *.new

