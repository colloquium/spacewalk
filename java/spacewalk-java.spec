%{!?__redhat_release:%define __redhat_release UNKNOWN}
%define cobprofdir      %{_localstatedir}/lib/rhn/kickstarts
%define cobprofdirup    %{_localstatedir}/lib/rhn/kickstarts/upload
%define cobprofdirwiz   %{_localstatedir}/lib/rhn/kickstarts/wizard
%define cobdirsnippets  %{_localstatedir}/lib/rhn/kickstarts/snippets
%define realcobsnippetsdir  %{_localstatedir}/lib/cobbler/snippets

%if  0%{?rhel} && 0%{?rhel} < 6
%define appdir          %{_localstatedir}/lib/tomcat5/webapps
%define jardir          %{_localstatedir}/lib/tomcat5/webapps/rhn/WEB-INF/lib
%else
%define appdir          %{_localstatedir}/lib/tomcat6/webapps
%define jardir          %{_localstatedir}/lib/tomcat6/webapps/rhn/WEB-INF/lib
%endif

Name: spacewalk-java
Summary: Spacewalk Java site packages
Group: Applications/Internet
License: GPLv2
Version: 1.3.15
Release: 1%{?dist}
URL:       https://fedorahosted.org/spacewalk
Source0:   https://fedorahosted.org/releases/s/p/spacewalk/%{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
ExcludeArch: ia64

Summary: Java web application files for Spacewalk
Group: Applications/Internet
Requires: bcel
Requires: c3p0
Requires: hibernate3 >= 0:3.2.4
Requires: java >= 1:1.6.0
Requires: java-devel >= 1:1.6.0
Requires: jakarta-commons-lang >= 0:2.1
Requires: jakarta-commons-codec
Requires: jakarta-commons-discovery
Requires: jakarta-commons-cli
Requires: jakarta-commons-el
Requires: jakarta-commons-io
Requires: jakarta-taglibs-standard
Requires: jasper5
Requires: jcommon
Requires: jfreechart >= 1.0.9
Requires: jpam
Requires: jta
Requires: log4j
Requires: redstone-xmlrpc
Requires: oscache
Requires: servletapi5
Requires: struts >= 0:1.2.9
%if  0%{?rhel} && 0%{?rhel} < 6
Requires: tomcat5
%else
Requires: tomcat6
%endif
Requires: xalan-j2 >= 0:2.6.0
Requires: xerces-j2
Requires: simple-core
Requires: sitemesh
Requires: stringtree-json
Requires: spacewalk-java-config
Requires: spacewalk-java-lib
Requires: spacewalk-java-jdbc
Requires: spacewalk-branding
Requires: jpackage-utils >= 0:1.5
Requires: cobbler >= 2.0.0
%if  0%{?fedora} && 0%{?fedora} >= 14
Requires: apache-commons-beanutils
Requires: apache-commons-logging
%else
Requires: jakarta-commons-logging
%endif
BuildRequires: ant
BuildRequires: ant-apache-regexp
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: ant-contrib
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: antlr >= 0:2.7.6
BuildRequires: jpam
BuildRequires: tanukiwrapper
%if  0%{?rhel} && 0%{?rhel} < 5
BuildRequires: javamail
%else
Requires: classpathx-mail
BuildRequires: classpathx-mail
%endif
BuildRequires: jsp
BuildRequires: checkstyle

# Sadly I need these to symlink the jars properly.
BuildRequires: asm
BuildRequires: bcel
BuildRequires: c3p0
BuildRequires: concurrent
BuildRequires: cglib
BuildRequires: ehcache
BuildRequires: dom4j
BuildRequires: hibernate3
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-discovery
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-validator
BuildRequires: jakarta-taglibs-standard
BuildRequires: jasper5
BuildRequires: jcommon
BuildRequires: jdom
BuildRequires: jfreechart >= 0:1.0.9
BuildRequires: jta
BuildRequires: redstone-xmlrpc
BuildRequires: oscache
BuildRequires: quartz
BuildRequires: simple-core
BuildRequires: stringtree-json
BuildRequires: struts
BuildRequires: sitemesh
BuildRequires: postgresql-jdbc
# the following line is for spell checking script
BuildRequires: aspell aspell-en libxslt
Obsoletes: rhn-java < 5.3.0
Obsoletes: rhn-java-sat < 5.3.0
Obsoletes: rhn-oracle-jdbc-tomcat5 <= 1.0
Provides: rhn-java = %{version}-%{release}
Provides: rhn-java-sat = %{version}-%{release}
Provides: rhn-oracle-jdbc-tomcat5 = %{version}-%{release}

%description
This package contains the code for the Java version of the Spacewalk Web Site.

%package config
Summary: Configuration files for RHN Java
Group: Applications/Internet
Obsoletes: rhn-java-config < 5.3.0
Obsoletes: rhn-java-config-sat < 5.3.0
Provides: rhn-java-config = %{version}-%{release}
Provides: rhn-java-config-sat = %{version}-%{release}

%description config
This package contains the configuration files for the Spacewalk Java web
application and taskomatic process.

%package lib
Summary: Jar files for Spacewalk Java
Group: Applications/Internet
Obsoletes: rhn-java-lib < 5.3.0
Obsoletes: rhn-java-lib-sat < 5.3.0
Provides: rhn-java-lib = %{version}-%{release}
Provides: rhn-java-lib-sat = %{version}-%{release}

%description lib
This package contains the jar files for the Spacewalk Java web application
and taskomatic process.

%package oracle
Summary: Oracle database backend support files for Spacewalk Java
Group: Applications/Internet
Requires: ojdbc14
Provides: spacewalk-java-jdbc = %{version}-%{release}

%description oracle
This package contains Oracle database backend files for the Spacewalk Java.

%package postgresql
Summary: PostgreSQL database backend support files for Spacewalk Java
Group: Applications/Internet
Requires: postgresql-jdbc
Provides: spacewalk-java-jdbc = %{version}-%{release}

%description postgresql
This package contains PostgreSQL database backend files for the Spacewalk Java.

%package -n spacewalk-taskomatic
Summary: Java version of taskomatic
Group: Applications/Internet
Requires: bcel
Requires: c3p0
Requires: cglib
Requires: hibernate3 >= 0:3.2.4
Requires: java >= 0:1.6.0
Requires: java-devel >= 0:1.6.0
Requires: jakarta-commons-lang >= 0:2.1
Requires: jakarta-commons-cli
Requires: jakarta-commons-codec
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-logging
Requires: jakarta-taglibs-standard
Requires: jcommon
Requires: jfreechart >= 0:1.0.9
Requires: jpam
Requires: log4j
Requires: oscache
Requires: xalan-j2 >= 0:2.6.0
Requires: xerces-j2
Requires: tanukiwrapper
Requires: simple-core
Requires: spacewalk-java-config
Requires: spacewalk-java-lib
Requires: spacewalk-java-jdbc
Requires: concurrent
Requires: quartz
Requires: cobbler >= 2.0.0
Obsoletes: taskomatic < 5.3.0
Obsoletes: taskomatic-sat < 5.3.0
Provides: taskomatic = %{version}-%{release}
Provides: taskomatic-sat = %{version}-%{release}
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts

%description -n spacewalk-taskomatic
This package contains the Java version of taskomatic.

%prep
%setup -q

%build
# compile only java sources (no packing here)
ant -Dprefix=$RPM_BUILD_ROOT init-install compile
# checkstyle is broken on Fedora 14 se we skip for now
%if (0%{?rhel} && 0%{?rhel} < 6) || (0%{?fedora} && 0%{?fedora} < 13)
echo "Running checkstyle on java main sources"
export CLASSPATH="build/classes"
export BASE_OPTIONS="-Djavadoc.method.scope=public \
-Djavadoc.type.scope=package \
-Djavadoc.var.scope=package \
-Dcheckstyle.cache.file=build/checkstyle.cache.src \
-Djavadoc.lazy=false \
-Dcheckstyle.header.file=buildconf/LICENSE.txt"
find . -name *.java | grep -vE '(/test/|/jsp/|/playpen/)' | \
xargs checkstyle -c buildconf/checkstyle.xml
echo "Running checkstyle on java test sources"
export BASE_OPTIONS="-Djavadoc.method.scope=nothing \
-Djavadoc.type.scope=nothing \
-Djavadoc.var.scope=nothing \
-Dcheckstyle.cache.file=build/checkstyle.cache.test \
-Djavadoc.lazy=false \
-Dcheckstyle.header.file=buildconf/LICENSE.txt"
find . -name *.java | grep -E '/test/' | grep -vE '(/jsp/|/playpen/)' | \
xargs checkstyle -c buildconf/checkstyle.xml
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if  0%{?rhel} && 0%{?rhel} < 6
ant -Dprefix=$RPM_BUILD_ROOT install-tomcat5
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/tomcat5/Catalina/localhost/
install -m 755 conf/rhn.xml $RPM_BUILD_ROOT%{_sysconfdir}/tomcat5/Catalina/localhost/rhn.xml
%else
ant -Dprefix=$RPM_BUILD_ROOT install-tomcat6
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/tomcat6/Catalina/localhost/
install -m 755 conf/rhn6.xml $RPM_BUILD_ROOT%{_sysconfdir}/tomcat6/Catalina/localhost/rhn.xml
%endif

# check spelling errors in all resources for English
scripts/spelling/check_java.sh . en_US

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/rhn
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/rhn/default
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/share/rhn
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/share/rhn/lib
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/share/rhn/classes
install -d -m 755 $RPM_BUILD_ROOT%{cobprofdir}
install -d -m 755 $RPM_BUILD_ROOT%{cobprofdirup}
install -d -m 755 $RPM_BUILD_ROOT%{cobprofdirwiz}
install -d -m 755 $RPM_BUILD_ROOT%{cobdirsnippets}
install -d -m 755 $RPM_BUILD_ROOT%{_var}/spacewalk/systemlogs

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 644 conf/default/rhn_hibernate.conf $RPM_BUILD_ROOT%{_sysconfdir}/rhn/default/rhn_hibernate.conf
install -m 644 conf/default/rhn_taskomatic_daemon.conf $RPM_BUILD_ROOT%{_sysconfdir}/rhn/default/rhn_taskomatic_daemon.conf
install -m 644 conf/default/rhn_org_quartz.conf $RPM_BUILD_ROOT%{_sysconfdir}/rhn/default/rhn_org_quartz.conf
install -m 755 conf/logrotate/rhn_web_api $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/rhn_web_api
install -m 755 scripts/taskomatic $RPM_BUILD_ROOT%{_initrddir}
install -m 644 build/webapp/rhnjava/WEB-INF/lib/rhn.jar $RPM_BUILD_ROOT%{_datadir}/rhn/lib
install -m 644 conf/log4j.properties.taskomatic $RPM_BUILD_ROOT%{_datadir}/rhn/classes/log4j.properties

install -m 644 conf/cobbler/snippets/keep_system_id  $RPM_BUILD_ROOT%{cobdirsnippets}/keep_system_id
install -m 644 conf/cobbler/snippets/post_reactivation_key  $RPM_BUILD_ROOT%{cobdirsnippets}/post_reactivation_key
install -m 644 conf/cobbler/snippets/post_delete_system  $RPM_BUILD_ROOT%{cobdirsnippets}/post_delete_system
install -m 644 conf/cobbler/snippets/redhat_register  $RPM_BUILD_ROOT%{cobdirsnippets}/redhat_register

ln -s -f /usr/sbin/tanukiwrapper $RPM_BUILD_ROOT%{_bindir}/taskomaticd
ln -s -f %{_javadir}/ojdbc14.jar $RPM_BUILD_ROOT%{jardir}/ojdbc14.jar
install -d -m 755 $RPM_BUILD_ROOT%{realcobsnippetsdir}
ln -s -f  %{cobdirsnippets} $RPM_BUILD_ROOT%{realcobsnippetsdir}/spacewalk
touch $RPM_BUILD_ROOT%{_var}/spacewalk/systemlogs/audit-review.log

%if (0%{?rhel} && 0%{?rhel} < 6) || (0%{?fedora} && 0%{?fedora} < 13)
ln -s -f %{_javadir}/asm/asm.jar  $RPM_BUILD_ROOT%{_datadir}/rhn/lib/spacewalk-asm.jar
%else
ln -s -f %{_javadir}/objectweb-asm/asm.jar  $RPM_BUILD_ROOT%{_datadir}/rhn/lib/spacewalk-asm.jar
%endif

# delete JARs which must not be deployed
rm -rf $RPM_BUILD_ROOT%{jardir}/jspapi.jar
rm -rf $RPM_BUILD_ROOT%{jardir}/jasper5-compiler.jar


%clean
rm -rf $RPM_BUILD_ROOT

%pre
rm -f %{realcobsnippetsdir}/spacewalk

%post -n spacewalk-taskomatic
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add taskomatic

%preun -n spacewalk-taskomatic
if [ $1 = 0 ] ; then
   /sbin/service taskomatic stop >/dev/null 2>&1
   /sbin/chkconfig --del taskomatic
fi

%files
%defattr(644,tomcat,tomcat,775)
%dir %{appdir}
%dir %{appdir}/rhn/
%{appdir}/rhn/apidoc/
%{appdir}/rhn/css/
%{appdir}/rhn/errata/
%{appdir}/rhn/help/
%{appdir}/rhn/img/
%{appdir}/rhn/META-INF/
%{appdir}/rhn/schedule/
%{appdir}/rhn/systems/
%{appdir}/rhn/users/
%{appdir}/rhn/*.jsp
%{appdir}/rhn/WEB-INF/classes
%{appdir}/rhn/WEB-INF/decorators
%{appdir}/rhn/WEB-INF/includes
%{appdir}/rhn/WEB-INF/nav
%{appdir}/rhn/WEB-INF/pages
%{appdir}/rhn/WEB-INF/*.xml
# list of all jar symlinks without any version numbers
# and wildcards (except non-symlinks dwr and velocity)
%{jardir}/antlr.jar
%{jardir}/bcel.jar
%{jardir}/c3p0.jar
%{jardir}/cglib.jar
%{jardir}/commons-beanutils.jar
%{jardir}/commons-cli.jar
%{jardir}/commons-codec.jar
%{jardir}/commons-collections.jar
%{jardir}/commons-digester.jar
%{jardir}/commons-discovery.jar
%{jardir}/commons-el.jar
%{jardir}/commons-fileupload.jar
%{jardir}/commons-io.jar
%{jardir}/commons-lang.jar
%{jardir}/commons-logging.jar
%{jardir}/commons-validator.jar
%{jardir}/concurrent.jar
%{jardir}/dom4j.jar
%{jardir}/dwr-*.jar
%{jardir}/hibernate3.jar
%{jardir}/jaf.jar
%{jardir}/jasper5-runtime.jar
%{jardir}/javamail.jar
%{jardir}/jcommon.jar
%{jardir}/jdom.jar
%{jardir}/jpam.jar
%{jardir}/jta.jar
%{jardir}/log4j.jar
%{jardir}/oro.jar
%{jardir}/oscache.jar
%{jardir}/quartz.jar
%{jardir}/redstone-xmlrpc-client.jar
%{jardir}/redstone-xmlrpc.jar
%{jardir}/rhn.jar
%{jardir}/simple-core.jar
%{jardir}/sitemesh.jar
%{jardir}/stringtree-json.jar
%{jardir}/struts.jar
%{jardir}/taglibs-core.jar
%{jardir}/taglibs-standard.jar
%{jardir}/tanukiwrapper.jar
%{jardir}/velocity-*.jar
%{jardir}/xalan-j2.jar
%{jardir}/xerces-j2.jar
%{jardir}/xml-commons-apis.jar
# jars for particular versions
%if (0%{?rhel} && 0%{?rhel} < 6) || (0%{?fedora} && 0%{?fedora} < 13)
%{jardir}/asmasm-analysis.jar
%{jardir}/asmasm-attrs.jar
%{jardir}/asmasm-tree.jar
%{jardir}/asmasm-util.jar
%{jardir}/asmasm-xml.jar
%{jardir}/asmasm.jar
%{jardir}/asmkasm.jar
%{jardir}/jfreechart.jar
%else
%{jardir}/objectweb-asm_asm.jar
%{jardir}/jfreechartjfreechart.jar
%endif
%dir %{cobprofdir}
%dir %{cobprofdirup}
%dir %{cobprofdirwiz}
%dir %{cobdirsnippets}
%config %{cobdirsnippets}/keep_system_id
%config %{cobdirsnippets}/post_reactivation_key
%config %{cobdirsnippets}/post_delete_system
%config %{cobdirsnippets}/redhat_register
%if  0%{?rhel} && 0%{?rhel} < 6
%config(noreplace) %{_sysconfdir}/tomcat5/Catalina/localhost/rhn.xml
%else
%config(noreplace) %{_sysconfdir}/tomcat6/Catalina/localhost/rhn.xml
%endif
%{realcobsnippetsdir}/spacewalk
%attr(755, tomcat, root) %{_var}/spacewalk/systemlogs
%ghost %attr(644, tomcat, root) %{_var}/spacewalk/systemlogs/audit-review.log

%files -n spacewalk-taskomatic
%attr(755, root, root) %{_initrddir}/taskomatic
%attr(755, root, root) %{_bindir}/taskomaticd
%attr(755, root, root) %{_datadir}/rhn/lib/spacewalk-asm.jar


%files config
%defattr(644, root, root)
%config %{_sysconfdir}/rhn/default/rhn_hibernate.conf
%config %{_sysconfdir}/rhn/default/rhn_taskomatic_daemon.conf
%config %{_sysconfdir}/rhn/default/rhn_org_quartz.conf
%config %{_sysconfdir}/logrotate.d/rhn_web_api


%files lib
%defattr(644, root, root)
%{_datadir}/rhn/classes/log4j.properties
%{_datadir}/rhn/lib/rhn.jar

%files oracle
%defattr(644, root, root)
%{jardir}/ojdbc14.jar

%files postgresql
%defattr(644, root, root)
%{jardir}/postgresql-jdbc.jar

%changelog
* Wed Nov 24 2010 Lukas Zapletal 1.3.15-1
- 615026 - [Multi-Org] Grants for channel permission edits throws ISE
- 642226 - do not look for the VT channel in case of RHEL6 base channels
- adding last_modified attribute to the ChannelSerializer

* Tue Nov 23 2010 Lukas Zapletal 1.3.14-1
- 646817 - System health indicator in "Systems" related pages not displayed

* Mon Nov 22 2010 Michael Mraka <michael.mraka@redhat.com> 1.3.13-1
- PE2.evr.as_vre_simple() -> evr_t_as_vre_simple(PE2.evr) (PG)
- removed rowid from query (PG)
- 646401 - setting missing RhnSetDecl

* Mon Nov 22 2010 Lukas Zapletal 1.3.12-1
- Fixing two queries in system overview (monitoring)
- Replacing DECODE with ANSI compatible CASE-WHEN
- Adding missing monitoring state (UNKNOWN)

* Mon Nov 22 2010 Michael Mraka <michael.mraka@redhat.com> 1.3.11-1
- 655519 - PE2.evr.as_vre_simple() -> evr_t_as_vre_simple(PE2.evr) (PG)
- 655515 - changed DECODE to ANSI CASE (PG)
- fixing several issues in system_overview query

* Fri Nov 19 2010 Michael Mraka <michael.mraka@redhat.com> 1.3.10-1
- fixed wrongly rendered API doc

* Fri Nov 19 2010 Lukas Zapletal 1.3.9-1
- Fixing JOIN in monitoring status query (System_queries.xml)

* Fri Nov 19 2010 Lukas Zapletal 1.3.8-1
- Removing from SQL clause (System_queries) causing bugs in monitoring

* Fri Nov 19 2010 Michael Mraka <michael.mraka@redhat.com> 1.3.7-1
- fixed outer joins

* Thu Nov 18 2010 Lukas Zapletal 1.3.6-1
- Replacing DECODE function with CASE-SWITCH (multiple times)
- 642599 use redhat_management_server insted of http_server in reactivation
  snippet 

* Thu Nov 18 2010 Tomas Lestach <tlestach@redhat.com> 1.3.5-1
- 654275 - make repo generation faster in the RHN way (tlestach@redhat.com)
- checkstyle fix (tlestach@redhat.com)
- fix CreateProfileWizardTest.testSuccess test (tlestach@redhat.com)
- store null as empty argumets (instead of empty string) (tlestach@redhat.com)
- fix DataSourceParserTest.testNullParam (tlestach@redhat.com)
- check for parameter presence in the CachedStatement (tlestach@redhat.com)

* Tue Nov 16 2010 Lukas Zapletal 1.3.4-1
- Replacing sysdate in SQL INSERT with current_timestamp

* Tue Nov 16 2010 Lukas Zapletal 1.3.3-1
- Adding one jar ignore to spacewalk-java.spec for F14 
- Turning off checkstyle in the java spec for F14 
- Adding requires for F14 in spacewalk-java.spec 

* Tue Nov 16 2010 Lukas Zapletal 1.3.2-1
- No longer distributing jar symlinks with version numbers
- use an existing column name in ORDER BY statements 
- Revert "Implement new API call packages.getPackageIdFromPath"
- Implement new API call packages.getPackageIdFromPath 
- allow setting null value as paramter 
- fix TaskManagerTest.testGetCurrentDBTime test 
- 645694 - introducing cleanup-packagechangelog-data task 

* Mon Nov 15 2010 Tomas Lestach <tlestach@redhat.com> 1.3.1-1
- checkstyle fix (tlestach@redhat.com)
- Bumping package versions for 1.3. (jpazdziora@redhat.com)

* Mon Nov 15 2010 Jan Pazdziora 1.2.111-1
- 653305 - do not access the login information, if the user is null
  (tlestach@redhat.com)

* Sat Nov 13 2010 Tomas Lestach <tlestach@redhat.com> 1.2.110-1
- better call stored functions with correct parameter order
  (tlestach@redhat.com)
- fix daily-summary task(PG) (tlestach@redhat.com)
- comapre chars with chars(PG) (tlestach@redhat.com)
- Restore 'yumrepo_last_sync' (colin.coe@gmail.com)
- Update the ChannelSerializer to show all associated repos
  (colin.coe@gmail.com)
- removing old changelog hibernate stuff that no longer works now that things
  are stored differently (jsherril@redhat.com)

* Fri Nov 12 2010 Lukas Zapletal 1.2.109-1
- Deletion from base table and not from view (PG)

* Fri Nov 12 2010 Tomas Lestach <tlestach@redhat.com> 1.2.108-1
- replace the rest of (+)s in config_queries.xml (tlestach@redhat.com)
- replace the rest of NVL functions in config_queries.xml (tlestach@redhat.com)
- enable comparism of sandbox other files(PG) (tlestach@redhat.com)
- enable config file deployment(PG) (tlestach@redhat.com)
- enable config target systems page (tlestach@redhat.com)
- enable config subscribed systems page (tlestach@redhat.com)
- enable deply file page(PG) (tlestach@redhat.com)
- enable "Manage Revisions" page (tlestach@redhat.com)
- store NULL if selinuxCtx is empty (tlestach@redhat.com)
- enable listing of config managed systems(PG) (tlestach@redhat.com)
- list centrally managed congif files(PG) (tlestach@redhat.com)
- enable listing of config files(PG) (tlestach@redhat.com)
- enable upload of config files(PG) (tlestach@redhat.com)
- do not set null value of type Types.VARCHAR for prepared statements
  (tlestach@redhat.com)
- enable (un)subscription to config channels via SSM(PG) (tlestach@redhat.com)
- replacing another MINUS by OUTER JOIN(PG) (tlestach@redhat.com)
- replacing NVL by COALESCE(PG) (tlestach@redhat.com)
- rewriting MINUS to OUTER JOIN(PG) (tlestach@redhat.com)
- enable creation of config channels(PG) (tlestach@redhat.com)

* Fri Nov 12 2010 Lukas Zapletal 1.2.107-1
- Revert "Removing commons-discovery jar from spacewalk-java.spec"
- Add missing file from previous commit 
- Implement getRepoDetails API calls 
- Correct the xmlrpc.doc 
- 647806 - Implement API calls for external repos 
- 652626 - correct typo in named query 

* Fri Nov 12 2010 Lukas Zapletal 1.2.106-1
- Removing jasper5-compiler jar from spacewalk-java.spec 
- Removing commons-discovery jar from spacewalk-java.spec 

* Fri Nov 12 2010 Lukas Zapletal 1.2.105-1
- Adding missing jakarta-commons-discovery require for RHEL6+/FC13+

* Thu Nov 11 2010 Lukas Zapletal 1.2.104-1
- Removing extra slash after RPM_BUILD_ROOT 
- We do not distribute jspapi.jar now - according to Servlet Spec 2.3
- Add missing ssm.migrate.systems.notrust to StringResource
- Implement channel.software.listUserRepos API call 

* Thu Nov 11 2010 Lukas Zapletal 1.2.103-1
- Replacing one more NVL with COALESCE function 
- Replacing NVL with COALESCE function 

* Thu Nov 11 2010 Lukas Zapletal 1.2.102-1
- Correcting one more ANSI JOIN syntax in channel queries (PG)
- Correcting ANSI JOIN syntax in channel queries 
- Correcting spaces in channel queries xml file 
- Making two server group portable 
- Correcting NULL values in channel manager repo gen 

* Thu Nov 11 2010 Lukas Zapletal 1.2.101-1
- Correcting spacewalk-java.spec - removing doubled files

* Thu Nov 11 2010 Lukas Zapletal 1.2.100-1
- Correcting spacewalk-java.spec - JDBC driver links

* Wed Nov 10 2010 Lukas Zapletal 1.2.99-1
- Fixing table aliases for DISTINCT queries (PG)

* Wed Nov 10 2010 Tomas Lestach <tlestach@redhat.com> 1.2.98-1
- updating alias to match the dto object attribute (tlestach@redhat.com)
- setting an alias for subquery(PG) (tlestach@redhat.com)
- enable SSM Package upgrade process(PG) (tlestach@redhat.com)
- fix OUTER JOIN from recent commit (tlestach@redhat.com)
- fix OUTER JOIN from recent commit (tlestach@redhat.com)
- fix OUTER JOIN from recent commit (tlestach@redhat.com)
- fixing queries, where rhnServer was unexpectedly joined to the query
  (tlestach@redhat.com)
- fixing broken queries (due to ORDER BY statements) (tlestach@redhat.com)
- setting action name for package verification (tlestach@redhat.com)

* Wed Nov 10 2010 Lukas Zapletal 1.2.97-1
- Correcting spec for spacewalk-java (JAR symlinks)

* Tue Nov 09 2010 Tomas Lestach <tlestach@redhat.com> 1.2.96-1
- enable SSM Package remove process(PG) (tlestach@redhat.com)
- enable SSM Package install process(PG) (tlestach@redhat.com)
- enable SSM Package upgrade page(PG) (tlestach@redhat.com)
- enable SSM Package remove page(PG) (tlestach@redhat.com)
- enable SSM Package install page(PG) (tlestach@redhat.com)
- enable Virtual Systems page(PG) (tlestach@redhat.com)

* Mon Nov 08 2010 Tomas Lestach <tlestach@redhat.com> 1.2.95-1
- fix creating of groups(PG) (tlestach@redhat.com)
- do not pass string params, when numeric are expected(PG)
  (tlestach@redhat.com)
- reduced logging of RpmRepositoryWriter (tlestach@redhat.com)
- create setters with byte[] param(PG) for repo generation code
  (tlestach@redhat.com)
- updating logging of ChannelRepodataWorker (tlestach@redhat.com)
- updated logging of ChannelRepodataDriver (tlestach@redhat.com)
- adding extra logging to KickstartFileSyncTask (tlestach@redhat.com)
- removing unused code from KickstartFileSyncTask (tlestach@redhat.com)

* Fri Nov 05 2010 Tomas Lestach <tlestach@redhat.com> 1.2.94-1
- removing insert of NULL value(PG) (tlestach@redhat.com)

* Fri Nov 05 2010 Lukas Zapletal 1.2.93-1
- Two config queries are ported to PostgreSQL 
- rewriting INSERT ALL in insert_channel_packages_in_set (PG)

* Thu Nov 04 2010 Lukas Zapletal 1.2.92-1
- Replacing 4 occurances of NVL with ANSI COALESCE 
- 645842 - return macro delims for config files 

* Thu Nov 04 2010 Miroslav Suchý <msuchy@redhat.com> 1.2.91-1
- fixing build errors (msuchy@redhat.com)

* Thu Nov 04 2010 Miroslav Suchý <msuchy@redhat.com> 1.2.90-1
- fixing build errors (msuchy@redhat.com)

* Wed Nov 03 2010 Miroslav Suchý <msuchy@redhat.com> 1.2.89-1
- 647099 - add API call isMonitoringEnabledBySystemId (msuchy@redhat.com)

* Wed Nov 03 2010 Tomas Lestach <tlestach@redhat.com> 1.2.88-1
- 649319 - enable upload of binary files (tlestach@redhat.com)
- removing dead code (tlestach@redhat.com)
- use public static string instead of directly calling query name
  (tlestach@redhat.com)
- migrating change log to java, and making it use the rpm itself instead of the
  database (jsherril@redhat.com)

* Wed Nov 03 2010 Lukas Zapletal 1.2.87-1
- Using general nextval function in ssm operation queries 
- fixing some fedora 14 provisioning issues 

* Tue Nov 02 2010 Lukas Zapletal 1.2.86-1
- Removing unnecessary JSPF fragment file 

* Tue Nov 02 2010 Lukas Zapletal 1.2.85-1
- Fixing unambiguous column 'name' for PostgreSQL 
- 645829 - make it possile to update macro delimiters 
- 645829 - do not trim curly brackets in macro delimiters 
- removing unnecessary condition 

* Tue Nov 02 2010 Lukas Zapletal 1.2.84-1
- Changing the way how taskomatic connects to PostgreSQL db
- Replacing some constants with ConfigDefaults in java codebase

* Tue Nov 02 2010 Jan Pazdziora 1.2.83-1
- Typo in a java resource (lzap+git@redhat.com)
- Spelling java resource script correction + retab (lzap+git@redhat.com)
- ErrataMailer improvements (tlestach@redhat.com)
- bumping API version to identify new API call availability
  (tlestach@redhat.com)

* Tue Nov 02 2010 Lukas Zapletal 1.2.82-1
- Renaming two ignored unit tests properly 
- Removing unused methods from java db manager 
- Removing unused class from java db manager 
- Removing unused class - Worker 
- Removing dead code in two tests 
- Fixing table name aliases 
- Two classes were not serializabled while putting them into HttpSession
- Fixing date diff in alerts 
- making kickstart channel list sorted alphabetically 
- sorting activation key base channel drop down by alphabetical order
- 648470 - changing manage package page to sort channels by name
- 644880 - check for arch compatibility when adding packages into a channel
- 647099 - introducing satellite.isMonitoringEnabled API 
- replace web.is_monitoring_backend with
  ConfigDefaults.WEB_IS_MONITORING_BACKEND 
- fixing ISE on package deletion due to RHNSAT.RHN_PFDQUEUE_PATH_UQ violation

* Mon Nov 01 2010 Tomas Lestach <tlestach@redhat.com> 1.2.81-1
- updating logging of SessionCleanup task (tlestach@redhat.com)
- checkstyle fix (tlestach@redhat.com)

* Mon Nov 01 2010 Tomas Lestach <tlestach@redhat.com> 1.2.80-1
- adding new TimeSeriesCleanUp taskomatic task (tlestach@redhat.com)
- Fixing system_available_packages -- the order by got lost in previous
  commits, and the name_upper is still there. (jpazdziora@redhat.com)

* Mon Nov 01 2010 Tomas Lestach <tlestach@redhat.com> 1.2.79-1
- 645702 - remove rhnPaidErrataTempCache temporary table (tlestach@redhat.com)

* Fri Oct 29 2010 Miroslav Suchý <msuchy@redhat.com> 1.2.78-1
- removing unused imports

* Fri Oct 29 2010 Jan Pazdziora 1.2.77-1
- removed unused Spacewalk (Certificate Signing Key) <jmrodri@nc.rr.com> key
  from keyring (michael.mraka@redhat.com)
- Operations on rhnSatelliteChannelFamily are not longer called, removing the
  queries.
- Method deactivateSatellite not used (presumably hosted only), removing.
- Queries channel_download_categories_by_type and
  satellite_channel_download_categories_by_type not used after previous
  removal, removing.
- ISOCategory not referenced, removing.
- The listDownloadCategories is not used, removing.

* Fri Oct 29 2010 Lukas Zapletal 1.2.76-1
- Making DISTINCT-ORDER BY package/system queries portable
- Removing unnecessary subselect 
- Simplifying ORDER BY clauses in package queries 
- Revert "Reverting "Removed unnecessary ORDER BY" commits and fixing"
  

* Wed Oct 27 2010 Shannon Hughes <shughes@redhat.com> 1.2.75-1
- fix for checkstyle (shughes@redhat.com)

* Wed Oct 27 2010 Lukas Zapletal 1.2.74-1
- Fixing missing brace in Taskomatic query 
- Addressing issue in system overview 
- PostgreSQL needs FROM keyword in DELETE 
- Adding missing interval keyword to Taskomatic 
- Protocol config value is now used in Taskomatic 
- Getting taskomatic working on PostgreSQL 
- removing unneeded insmod on kickstart %pre script, since they are already
  loaded 
- fixing query to run correctly, c.id was not valid because the join did not
  come directly after rhnChannel c 
- adding missing import 
- 646892 - fixing issue where kickstart expiration would occur after current
  date and not scheduled date of kickstart 
- removing need of setNvreUpper method in PackageOverview 
- fixing broken if statement in snippet 
- fixing broken query used by SSM System delete 

* Mon Oct 25 2010 Lukas Zapletal 1.2.73-1
- Fixing Taskomatic blob handling (now binary)
- Support for PostgreSQL driver in Taskomatic
- Implement API calls for System Currency

* Mon Oct 25 2010 Lukas Zapletal 1.2.72-1
- Addressing subquery in FROM must have an alias issue (fix)
- Sorting fix in packages for PostgreSQL
- Reverting "Removed unnecessary ORDER BY" commits and fixing
- Default cast fix for PostgreSQL
- Use the { call ... } syntax instead of the direct PL/SQL.

* Mon Oct 25 2010 Jan Pazdziora 1.2.71-1
- 639999 - adding %end tags to generated kickstart files if os is fedora or
  RHEL 6 (jsherril@redhat.com)

* Thu Oct 21 2010 Jan Pazdziora 1.2.70-1
- Fix checkstyle errors (colin.coe@gmail.com)

* Thu Oct 21 2010 Lukas Zapletal 1.2.69-1
- Fixed all LEFT OUTER JOINs in Channels 
- Fixed LEFT OUTER JOIN for PostgreSQL in Software Channels
- Removed unnecessary ORDER BY in DISTINCT query. 
- Simplified SQL query with evr_t_as_vre_simple function. 
- Fixed composite type accessing for PostgreSQL for all packages
- Simplified SQL query with evr_t_as_vre_simple function. 
- Fixed composite type accessing for PostgreSQL 
- Sorting fix in packages for PostgreSQL 
- Fix of evr_t_as_vre_simple PostgreSQL function 
- ANSI JOIN syntax fix for PostgreSQL in system update 
- PostgreSQL fix in package search 
- Integer-Long fix in channel subscribers for PostgreSQL 
- Update System Currency to use rhn.cfg file 

* Wed Oct 20 2010 Lukas Zapletal 1.2.68-1
- Rewrite of LEFT OUTER JOIN into ANSI syntax 
- Function evr_t_as_vre_simple in all package queries now general
- Using date time function instead of arithmetics 
- Sysdate replaced with current_timestamp 
- Removed unnecessary ORDER BY in SELECT COUNT
- Use the global function evr_t_as_vre_simple in package_ids_in_set instead of
  method .as_vre_simple; this works on PostgreSQL as well.

* Wed Oct 20 2010 Jan Pazdziora 1.2.67-1
- Delete from rhnPackageChangeLogRec, not from the view.
- Fix ISE in AK child channel page (colin.coe@gmail.com)

* Wed Oct 20 2010 Lukas Zapletal 1.2.66-1
- Removed unnecessary ORDER BY 
- Using date time function instead of arithmetics 
- Added setHasSubscription for Integer 
- Using date time function instead of arithmetics 
- Fix in PostgreSQL (ORDER BY) in Out Of Date system list.
- Fixed comma in ANSI JOIN syntax from previous commit 
- Left join now in ANSI syntax for virtual system list. 
- Fix in PostgreSQL plus NVL fix
- All DECODE functions replaced with CASE-WHEN in System_queries
- Fixing system overview list for PostgreSQL 

* Tue Oct 19 2010 Tomas Lestach <tlestach@redhat.com> 1.2.65-1
- removing unused imports (tlestach@redhat.com)
- 644361 - use cache instead of view for update check (tlestach@redhat.com)
- Port /network/systems/groups/create.pxt, part 2 (colin.coe@gmail.com)
- Port /network/systems/groups/create.pxt (colin.coe@gmail.com)
- Port /network/systems/details/custominfo/new_value.pxt (colin.coe@gmail.com)
- Port /network/systems/details/custominfo/remove_value_conf.pxt
  (colin.coe@gmail.com)
- More checkstyle fixes (colin.coe@gmail.com)
- Fix checkstyle errors (colin.coe@gmail.com)
- Fix missing links (colin.coe@gmail.com)
- Fix /rhn/systems/details/UpdateCustomData.do (colin.coe@gmail.com)
- Port /network/systems/details/custominfo/edit.pxt (colin.coe@gmail.com)
- Fix NPE when lastModifier is null (colin.coe@gmail.com)
- Port /network/systems/details/custominfo/index.pxt (colin.coe@gmail.com)
- Fix page not updating description (colin.coe@gmail.com)
- Checkstyle fixes (colin.coe@gmail.com)
- Port /network/systems/custominfo/edit.pxt (colin.coe@gmail.com)
- 644349 - remove hasProcessedErrata method (tlestach@redhat.com)
- 644349 - extend ErrataMailer logging (tlestach@redhat.com)
- 644349 - do not update/delete all errata entries when the erratum affects
  multiple channels (tlestach@redhat.com)
- 644349 - do not list one system several times in the errata notification
  e-mail (tlestach@redhat.com)

* Tue Oct 19 2010 Lukas Zapletal 1.2.64-1
- Fixing system list for Oracle

* Mon Oct 18 2010 Jan Pazdziora 1.2.63-1
- fixing broken tag

* Mon Oct 18 2010 Lukas Zapletal 1.2.62-1
- DECODE replaced with ANSI compatible CASE WHEN

* Mon Oct 18 2010 Jan Pazdziora 1.2.61-1
- Better exception logging in cached statement (lzap+git@redhat.com)
- System list now working on Postgresql (lzap+git@redhat.com)

* Fri Oct 15 2010 Lukas Zapletal 1.2.60-1
- Checkstyle fixes 
- Checkstyle testing report now part of java spec 
- Removed unused query 
- Made the list tag dataset manipulator handle maps 

* Wed Oct 13 2010 Tomas Lestach <tlestach@redhat.com> 1.2.59-1
- 642519 - associate only unique keywords with an erratum (tlestach@redhat.com)
- 642203- Removed the Task Status page for it needs a serious work over with
  our new configs (paji@redhat.com)

* Tue Oct 12 2010 Tomas Lestach <tlestach@redhat.com> 1.2.58-1
- 630884 - send email notification when errata get synced (tlestach@redhat.com)
- Checkstyle fixes (colin.coe@gmail.com)
- Port /network/systems/custominfo/delete.pxt (colin.coe@gmail.com)
- Port /network/systems/details/delete_confirm.pxt (colin.coe@gmail.com)
- Move the cobbler requirement to version 2.0.0. (jpazdziora@redhat.com)

* Mon Oct 11 2010 Lukas Zapletal 1.2.57-1
- Added Hibernate empty varchar interceptor
- Fixed empty varchars during admin registration

* Fri Oct 08 2010 Jan Pazdziora 1.2.56-1
- PostgreSQL does not like to ORDER BY by something which is not in DISTINCT.
- Since query Channel.findAllBaseChannels was replaced with sql-query, removing
  the query.
- The query visible_to_user_ids-back does not seem to be referenced from
  anywhere, removing.
- Moving the quartz-oracle Requires from spacewalk-taskomatic to spacewalk-
  oracle.
- Replace nvl with coalesce in user_permissions.
- Removing unused import and fixed checkstyle. (slukasik@redhat.com)
- Added missing javadoc (internal class) (lzap+git@redhat.com)

* Thu Oct 07 2010 Jan Pazdziora 1.2.55-1
- Use current_timestamp instead of the Oracle-specific sysdate in
  schedule_pkg_for_delete_from_set.
- PostgreSQL NVL2 function (CASE WHERE) typo fix. (lzap+git@redhat.com)
- Removed unnecessary rhn.jar Ant dependency in a unit test
  (lzap+git@redhat.com)
- Replace Oracle outer join syntax with ANSI syntax for
  Channel.findCustomBaseChannels (lzap+git@redhat.com)
- Need to make the select a subselect, to be able to use the column alias in
  order by.
- Use the global function evr_t_as_vre_simple in package_ids_in_set instead of
  method .as_vre_simple; this works on PostgreSQL as well.

* Thu Oct 07 2010 Tomas Lestach <tlestach@redhat.com> 1.2.54-1
- 640520 - removing default/rhn_taskomatic.conf file (tlestach@redhat.com)

* Thu Oct 07 2010 Lukas Zapletal 1.2.53-1
- 640926 - commons-logging library is now explicitly configured in Jasper2
- PostgreSQL does not have NVL2 function and we have to use CASE WHERE.

* Wed Oct 06 2010 Jan Pazdziora 1.2.52-1
- Use the global function evr_t_as_vre_simple instead of method .as_vre_simple;
  this works on PostgreSQL as well.
- Remove all from cache, not only rpm specific metadata. (slukasik@redhat.com)
- Implement isChannelRepodataStale for debian channels. (slukasik@redhat.com)
- Rpm and Deb metadata creation differs, moving to separate classes.
  (slukasik@redhat.com)

* Wed Oct 06 2010 Tomas Lestach <tlestach@redhat.com> 1.2.51-1
- 640520 - removing old taskomatic static configuration (tlestach@redhat.com)

* Tue Oct 05 2010 Jan Pazdziora 1.2.50-1
- Replace Oracle outer join syntax with ANSI syntax for
  Channel.findAllBaseChannels and Channel.findByIdAndUserId.
- Use current_timestamp instead of the Oracle-specific sysdate in
  request_repo_regen.
- Avoid using rhn_repo_regen_queue_id_seq.nextval Oracle syntax in
  request_repo_regen.
- spacewalk-java.spec now check for spelling errors in build time.
  (lzap+git@redhat.com)

* Mon Oct 04 2010 Justin Sherrill <jsherril@redhat.com> 1.2.49-1
- 639999 - removing management entitlement requirment from a bunch of user
  pages (jsherril@redhat.com)
- 639134 - use proper function when searching package using id
  (tlestach@redhat.com)
- Port /network/account/activation_keys/child_channels.pxt
  (coec@war.coesta.com)
- Create cache directory for both rpm and deb channels. (slukasik@redhat.com)
- Use US spelling of 'organisation' (coec@war.coesta.com)
- Port /network/systems/ssm/system_list.pxt (coec@war.coesta.com)
- SSM System migration (coec@war.coesta.com)
- distinguish spacewalk and satellite email body, when certificate expires
  (tlestach@redhat.com)
- Hardware Refresh - Create only one action (coec@war.coesta.com)
- Package Refresh - Create only one action (coec@war.coesta.com)
- Port SSM Package Refresh Page (coec@war.coesta.com)
- Port /network/systems/ssm/index.pxt (colin.coe@gmail.com)
- Implement schedule.archiveActions (coec@war.coesta.com)

* Thu Sep 30 2010 Lukas Zapletal 1.2.48-1
- jspf pages are now precompiled too
- deleted jpsf that was no longer in use
- known error (628555) is solved by jspf precompilation

* Wed Sep 29 2010 Shannon Hughes <shughes@redhat.com> 1.2.47-1
- fix incorrect adding of trust set for system migrate (shughes@redhat.com)

* Tue Sep 28 2010 Shannon Hughes <shughes@redhat.com> 1.2.46-1
- checkstyle fixes (shughes@redhat.com)
- 636610 alternative set add due to ibm jvm issue (shughes@redhat.com)
- fixing possible ISE where a cobbler system record already exists, but is not
  associated to a system when re-provisioning is initiated
  (jsherril@redhat.com)
- fixing issue where kickstarts woudl not show up for provisioning if the
  distro was created since the last tomcat restart (jsherril@redhat.com)
- adding ext4 support for duplicate systems (jsherril@redhat.com)
- 637696 - fixing issue where kickstart could hang, either because of a rhel
  5.5 kernel panic, or because RHEL 6 does not allow pre-scripts to continue
  running in the background (jsherril@redhat.com)

* Mon Sep 27 2010 Miroslav Suchý <msuchy@redhat.com> 1.2.45-1
- Revert "591291 - added new API calls
  channel.software.mergeErrataWithPackages" (aparsons@redhat.com)
- fixing unit tests (jsherril@redhat.com)
- fixing some strings associated with repo syncing (jsherril@redhat.com)
- 636442 - fixing issue where calling packages.removePackage() api call could
  result in a unique constraint exception (jsherril@redhat.com)
- Fixed mroe checkstyle errors (paji@redhat.com)
- Fixed a checkstyle error (paji@redhat.com)
- 634230 - fixing issue where errata mailer would run continuously and never
  mark the notification queue as being finished (jsherril@redhat.com)
- 636610 - Small fix for the migration jsp bug (paji@redhat.com)
- redundancy is the spice of life, adding back rhnServer to table joins since
  its not so redundant.  Reverts 9f09cf8bb9854c9f8bc6f4e497a49abec3affee2
  (jsherril@redhat.com)
- 629971 - added two county codes, better Localizer error message
  (lzap+git@redhat.com)

* Thu Sep 23 2010 Michael Mraka <michael.mraka@redhat.com> 1.2.44-1
- fixed erratamailer_fill_work_queue
- resource spelling script and several typo corrections

* Thu Sep 23 2010 Lukas Zapletal 1.2.43-1
- 636740 - asterisks in package search fixed
- 636120 - fixed an ISE in the org.listSystemEntitlements call to deal with null
  Used/Allocated entitlements
- 630877 - XMLRPC Documentation fix
- 634230 - fixing slowness in email sending
- 636587- Fixed a query showing the system counts in the Software Entitleements
  page
- 630585 - about-chat string correction
- 634263 - Fix to allow guests to register across orgs + UI fixes for the
  Virtual systems page

* Tue Sep 21 2010 Aron Parsons <aparsons@redhat.com> 1.2.42-1
- added new API call channel.software.removeErrata (aparsons@redhat.com)
- 591291 - added new API calls channel.software.mergeErrataWithPackages
  (aparsons@redhat.com)
- added a new variation of channel.software.mergeErrata API call that allows
  the user to pass in a list of advisory names (aparsons@redhat.com)
- 630585 - about-chat now points to proper channel (branding)
  (lzap+git@redhat.com)
- 634834 - fixing ISE when putting in invalid day of week (jsherril@redhat.com)
- 634910 - fixing permission denied error on manage channel errata that should
  not have been denied (jsherril@redhat.com)
- checkstyle fix for previous commit (lzap+git@redhat.com)
- various checkstyle fixes for previous commit (lzap+git@redhat.com)
- 634884 - managing repositories within channels through XMLRPC API disabled
  (lzap+git@redhat.com)
- fixed NPE when spacewalk_reposync_logpath is set to nonexisting dir
  (lzap+git@redhat.com)
- 633956 -fixing error popup on YourRhn when a warning or critical probe exists
  (jsherril@redhat.com)

* Thu Sep 16 2010 Lukas Zapletal 1.2.41-1
- 595500 - added contents_enc64 param to createOrUpdatePath XMLAPI
- making taskmoatic work with the rkbloom driver
- 633535 - added RHEL 5 subrepos as well as stopped showing repos not valid for
  a particular release
- adding configchannel.lookupFileInfo() taking a revision id
- implement <label> for form fields - systems/probes/edit.jsp
- implement <label> for form fields - systems/systemsearch.jsp
- 627920 - Added a larger config file icon for symlinks. Thanks to Joshua Roys.

* Tue Sep 14 2010 Justin Sherrill <jsherril@redhat.com> 1.2.40-1
- 630980 - fixing ise on package details page (jsherril@redhat.com)

* Tue Sep 14 2010 Michael Mraka <michael.mraka@redhat.com> 1.2.39-1
- 632561 - two typos in string resource xml (en_US)
- 580998 - making deprecatedVersion become deprecatedReason
- don't fail if service is already running

* Fri Sep 10 2010 Tomas Lestach <tlestach@redhat.com> 1.2.38-1
- 606555 - provide more information into the XmlRpcFault when method not found
  (tlestach@redhat.com)

* Thu Sep 09 2010 Partha Aji <paji@redhat.com> 1.2.37-1
- 625730 - Fixed the create config file/dir javascript to work with google
  chrome (paji@redhat.com)

* Thu Sep 09 2010 Partha Aji <paji@redhat.com> 1.2.36-1
- 627874 - Quick fix to disable Macro Delims for Config Directories
  (paji@redhat.com)
- 629974 - fixing ISE on select all on the channel repos page
  (jsherril@redhat.com)
- 630595 - fixing issue where a taskomatic restart was required for distros to
  be synced (jsherril@redhat.com)
- widening text file upon user request (jsherril@redhat.com)
- 623447 - improving speed of providing_channles call, which is only used
  through the api, and so its ok to just use org id and not go through the
  rhNAvailableChannels view which seems very slow for large satellites.  We
  should improve this in the future (jsherril@redhat.com)
- let sandbox task log when removing some files/channels (tlestach@redhat.com)
- 570393 - return empty map as DMI in case no hardware info is available
  (tlestach@redhat.com)
- 570393 - return empty map as CPU in case no hardware info is available
  (tlestach@redhat.com)

* Thu Sep 09 2010 Tomas Lestach <tlestach@redhat.com> 1.2.35-1
- add None as channel checksum type option on the webUI (tlestach@redhat.com)

* Wed Sep 08 2010 Shannon Hughes <shughes@redhat.com> 1.2.34-1
- bug fixes for audit tab and proxy installer additions (shughes@redhat.com)
- 630876 - fixing ISE if viewing the hardware of a system registered with no
  hardware (jsherril@redhat.com)

* Wed Sep 08 2010 Shannon Hughes <shughes@redhat.com> 1.2.33-1
- 589728 hide audit functionality for satellite product (shughes@redhat.com)

* Wed Sep 08 2010 Partha Aji <paji@redhat.com> 1.2.32-1
- 630877 - Updated a couple of documentation comments in the get/setVariables
  XMLRPC call (paji@redhat.com)

* Wed Sep 08 2010 Partha Aji <paji@redhat.com> 1.2.31-1
- 630877 - Improved the documentation on get/set Variables call
  (paji@redhat.com)
- 617044 - enabling reprovisioning for KVM and fully virt XEN guests
  (jsherril@redhat.com)
- xliff fixes for previous translations commit (enUS) (shughes@redhat.com)
- checkstyle fixes,  hit 150 line limit on a method, got around it, but we
  should either change the limit or refactor this method (jsherril@redhat.com)
- fixing common typo pacakges -> packages (tlestach@redhat.com)
- translated xliff string update (shughes@redhat.com)
- handle repo generation when channel checksum not set (tlestach@redhat.com)

* Tue Sep 07 2010 Michael Mraka <michael.mraka@redhat.com> 1.2.30-1
- fixed errataqueue_find_autoupdate_servers
- removign srcjars from java
- fix latest errata cache changes

* Tue Sep 07 2010 Tomas Lestach <tlestach@redhat.com> 1.2.29-1
- update method name to make the code compilable (tlestach@redhat.com)

* Tue Sep 07 2010 Michael Mraka <michael.mraka@redhat.com> 1.2.28-1
- 573630 - reused pl/sql implementation of update_needed_cache in java
- newPackages() is dead since update_needed_cache move to pl/sql
- improved errataqueue_find_autoupdate_servers

* Mon Sep 06 2010 Tomas Lestach <tlestach@redhat.com> 1.2.27-1
- removing hibernate commit from the populateWorkQueue (tlestach@redhat.com)
- fix query for errata mailer (tlestach@redhat.com)

* Mon Sep 06 2010 Michael Mraka <michael.mraka@redhat.com> 1.2.26-1
- fixed imports

* Mon Sep 06 2010 Michael Mraka <michael.mraka@redhat.com> 1.2.25-1
- 573630 - reuse pl/sql implementation of update_needed_cache in java
- file attribute was removed from the wrong method in PackageHelper
- 614918 - Made SSM Select Systems to work with I18n languages
- 598845 - fixing issue where syncing errata would fail with a Hibernate
  NonUniqueObjectException because keywords on errata were being duplicated
  durign sync

* Fri Sep 03 2010 Tomas Lestach <tlestach@redhat.com> 1.2.24-1
- 567178 - adding Pacific/Auckland time zone (tlestach@redhat.com)
- 495973 - adding America/Regina time zone (tlestach@redhat.com)
- 623447 - making errata.listPackages maintain api compatibility since it is to
  be backported to 5.3 (jsherril@redhat.com)
- 623447 - speeding up errata.listPackages api call (jsherril@redhat.com)
- 591291 - do not touch packages in mergeErrata api call (tlestach@redhat.com)
- make null checks for cron expressions (tlestach@redhat.com)
- add sanity check for predefined tasks (tlestach@redhat.com)
- check only active schedules when checking DB for initialization
  (tlestach@redhat.com)

* Wed Sep 01 2010 Partha Aji <paji@redhat.com> 1.2.23-1
- 518664 - Made spacewalk search deal with other locales (paji@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 616570 - adding support for looking up debuginfo rpms if they are located on
  the satellite itself (jsherril@redhat.com)
- fixing kickstart %post script logging to actually work and not break
  kickstarts (jsherril@redhat.com)
- fix ClearLogHistory (tlestach@redhat.com)

* Wed Sep 01 2010 Tomas Lestach <tlestach@redhat.com> 1.2.22-1
- 627905 - taskomatic requires jakarta-commons-dbcp (tlestach@redhat.com)

* Tue Aug 31 2010 Partha Aji <paji@redhat.com> 1.2.21-1
- 577921 - Removed references to redhat-release package (paji@redhat.com)

* Tue Aug 31 2010 Partha Aji <paji@redhat.com> 1.2.20-1
- 628097 - Removed kickstart partition validation logic (paji@redhat.com)

* Tue Aug 31 2010 Tomas Lestach <tlestach@redhat.com> 1.2.19-1
- 626741 - do not allow two repos with same label or repository url
  (tlestach@redhat.com)
- As 00-spacewalk-mod_jk.conf which referenced workers.properties is gone,
  remove it now as well. (jpazdziora@redhat.com)

* Mon Aug 30 2010 Partha Aji <paji@redhat.com> 1.2.18-1
- 628100 - fix for Activation Keys - Config channels issue (paji@redhat.com)
- cleaned up KickstartData object a bit (paji@redhat.com)
- 591291 - list errata packages only associated to the given channel
  (tlestach@redhat.com)
- checkstyle fix (tlestach@redhat.com)
- 627149 - do not return installtime via xmlrpc when not defined
  (tlestach@redhat.com)
- better create a separate method than override an existing in this case
  (tlestach@redhat.com)
- do not log if queue is empty for queue tasks (tlestach@redhat.com)
- 529232 - add 'no base' and 'ignore missing' options to kickstart
  (coec@war.coesta.com)
- Removed unnecessary NVLs from a config query (paji@redhat.com)
- 624377 - restore original functionality and information (coec@war.coesta.com)
- Fix hardware page (colin.coe@gmail.com)

* Fri Aug 27 2010 Tomas Lestach <tlestach@redhat.com> 1.2.17-1
- add repo type to the RepoSyncTask (tlestach@redhat.com)
- fix user email notification (tlestach@redhat.com)
- fix ChannelSoftwareHandlerTest.testMergeErrataByDate test
  (tlestach@redhat.com)
- 484895 - Stop the release link giving a 404 (colin.coe@gmail.com)

* Thu Aug 26 2010 Tomas Lestach <tlestach@redhat.com> 1.2.16-1
- 591291 - faster handling of mergeErrata API call (tlestach@redhat.com)
- fix ErrataQueueTest unit test (tlestach@redhat.com)
- 580939 - fixing invalid html with alter channels page (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)
- Fixed struts form bloopered entry (paji@redhat.com)
- making taskoamtic api handler be ignored by the api doc generation
  (jsherril@redhat.com)
- a bunch of unit test fixes (jsherril@redhat.com)

* Tue Aug 24 2010 Partha Aji <paji@redhat.com> 1.2.15-1
- checkstyle error fix (jsherril@redhat.com)
- Making repo sync screen display an error if taskomatic isnt up, and disable
  the buttons (jsherril@redhat.com)
- removing serializer entry for removed serializer (jsherril@redhat.com)

* Tue Aug 24 2010 Partha Aji <paji@redhat.com> 1.2.14-1
- 593896 - Moved Kickstart Parition UI logic (paji@redhat.com)
- remove updateSchedule method (tlestach@redhat.com)
- rename mathod names to match taskomatic terms (tlestach@redhat.com)
- reschedule = unschedule + schedule (tlestach@redhat.com)
- fix just log formatting (tlestach@redhat.com)
- do not email when tasko job get skipped (tlestach@redhat.com)
- adding the rest of the recurring event picker to the reposync stuff
  (jsherril@redhat.com)
- more work on reposync/taskomatic UI (jsherril@redhat.com)
- fixing path for chrooted post script log file (jsherril@redhat.com)
- introduce interface to get active schedules by bunch name
  (tlestach@redhat.com)
- change log info for skipped queue tasks (tlestach@redhat.com)
- change path for taskomatic logs (tlestach@redhat.com)
- enable repo sync schedule from web ui (tlestach@redhat.com)
- rewrite RepoSyncTask (tlestach@redhat.com)
- adding missing import (tlestach@redhat.com)
- checking in some missing files (jsherril@redhat.com)
- making the sync repos page do different things depending on the button
  (jsherril@redhat.com)
- Fixed a compile error (paji@redhat.com)
- Removed a bunch of duplicate dynaforms to use no_scrub and no_paren_scrub
  (paji@redhat.com)
- adding early draft of recurring event picker (jsherril@redhat.com)

* Thu Aug 19 2010 Tomas Lestach <tlestach@redhat.com> 1.2.13-1
- Fix typo (joshua.roys@gtri.gatech.edu)
- 601656 - fix user permission check for errata.create call
  (tlestach@redhat.com)

* Thu Aug 19 2010 Tomas Lestach <tlestach@redhat.com> 1.2.12-1
- return only information, run has /(not) a log (provide no file path)
  (tlestach@redhat.com)
- just call satellite-sync without sudo (tlestach@redhat.com)
- fix comparism of log outputs (tlestach@redhat.com)
- fix check whether a run is associated with the given org
  (tlestach@redhat.com)
- enable taskomatic logging in the correct file (tlestach@redhat.com)
- better uncomment used code (tlestach@redhat.com)

* Wed Aug 18 2010 Partha Aji <paji@redhat.com> 1.2.11-1
- 623683-Fixed a dupes bug where config channels were not getting shown..
  (paji@redhat.com)

* Wed Aug 18 2010 Tomas Lestach <tlestach@redhat.com> 1.2.10-1
- requires simple-core instead of obsolete (tlestach@redhat.com)

* Wed Aug 18 2010 Tomas Lestach <tlestach@redhat.com> 1.2.9-1
- status has to be saved (tlestach@redhat.com)
- fix check if a run belong to a certain org (tlestach@redhat.com)

* Wed Aug 18 2010 Tomas Lestach <tlestach@redhat.com> 1.2.8-1
- serialize dataMap even if empty (tlestach@redhat.com)
- enable task logging to files (tlestach@redhat.com)

* Tue Aug 17 2010 Partha Aji <paji@redhat.com> 1.2.7-1
- Added API calls to create/update symlinks (paji@redhat.com)
- Fixed the manage config file page to not show 'upload' for symlinks
  (paji@redhat.com)

* Tue Aug 17 2010 Tomas Lestach <tlestach@redhat.com> 1.2.6-1
- rename, update and schedule ClearLogHistory (tlestach@redhat.com)
- email support (tlestach@redhat.com)
- Fix missing functionality on System Hardware page (colin.coe@gmail.com)

* Mon Aug 16 2010 Tomas Lestach <tlestach@redhat.com> 1.2.5-1
- fix ErrataQueueTest unit test (tlestach@redhat.com)
- do not print stacktrace, when logging disabled (tlestach@redhat.com)
- do not use TaskoFactory inside of the start() and finish() methods
  (tlestach@redhat.com)
- load errata after closing session to be used later on (tlestach@redhat.com)
- add simple-core dependecies (tlestach@redhat.com)
- chekstyle fix (tlestach@redhat.com)

* Sun Aug 15 2010 Tomas Lestach <tlestach@redhat.com> 1.2.4-1
- taskomatic enhancements (tlestach@redhat.com)
- 620149 - Restore Users tab for Org Admins (colin.coe@gmail.com)
- System Notes pages PXT to java (colin.coe@gmail.com)

* Thu Aug 12 2010 Justin Sherrill <jsherril@redhat.com> 1.2.3-1
- fixing compile errors (jsherril@redhat.com)

* Wed Aug 11 2010 Partha Aji <paji@redhat.com> 1.2.2-1
- 562555 - Added code to scrub activation key names and descriptions
  (paji@redhat.com)
- Removed a stupid class that was unused (paji@redhat.com)

* Tue Aug 10 2010 Partha Aji <paji@redhat.com> 1.2.1-1
- 622715 - Fixed dups profile bug where unentitled systems were being wrongly
  reported as entitled (paji@redhat.com)
- 620463 - Fixed a KS bug (paji@redhat.com)
- fixing issue where "guests consuming regular entitlement page" would show
  guests that were recieving free entitlements because their host had a virt
  entitlement (jsherril@redhat.com)
- bumping package versions for 1.2 (mzazrivec@redhat.com)

* Tue Aug 10 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.50-1
- 621528 - Fixed dupes sys compare page to deal with unentitled systems

* Mon Aug 09 2010 Partha Aji <paji@redhat.com> 1.1.49-1
- 620341 - Fixed a dupes query (paji@redhat.com)
- 576779 - fixing issue where selecting systems to apply a single errata to
  would only work on the first page ful (jsherril@redhat.com)
- 619301 - Fixed a ypo in a i18n string (paji@redhat.com)

* Mon Aug 09 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.48-1
- Massaged the sys ents page a little more (paji@redhat.com)
- Added some tool tips on the Multi Org System Entitlements page
  (paji@redhat.com)
- fixing unit test that was written incorrectly to start with
  (jsherril@redhat.com)
- I18nized Manage and Clear (paji@redhat.com)

* Thu Aug 05 2010 Partha Aji <paji@redhat.com> 1.1.47-1
- 621520 - Fixed a bug where the 'clear' box ignored extra request parameters
  (paji@redhat.com)
- Fixed a couple of dup queries to use having (paji@redhat.com)
- making the editarea not highlight by default (jsherril@redhat.com)
- 616041 - fixing issue where deploying config files for multiple servers
  scheduled multiple actions instead of one (jsherril@redhat.com)
- 596831 - fixing issue where non-internationalized strings were stored and
  displayed for the SSM operations pages (jsherril@redhat.com)

* Thu Aug 05 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.46-1
- 616785 - fixing issue where selecting "update Properties" on the system
  details edit page would set "Auto Update Errata" to no, even if it had been
  previously set to yes
- 601058 - fixing issue where hitting update on the kickstart operating system
  tab would overwrite the custom url
- 575981 - fixing issue where non-user scheduled actions wouldnt show up in the
  scheduled list
- convert hardware.pxt to Java

* Tue Aug 03 2010 Partha Aji <paji@redhat.com> 1.1.45-1
- Fixed byte[] -> string conversion bugs that were created during the
  blob->binary commit (paji@redhat.com)

* Tue Aug 03 2010 Shannon Hughes <shughes@redhat.com> 1.1.44-1
- we need to use epoch of 1 for 1.6.0 and greater according to fedora java package rules (shughes@redhat.com)

* Mon Aug 02 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.43-1
- use objectweb-asm for Fedora-13 and beyond

* Mon Aug 02 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.42-1
- point taskomatic to slf4j jars

* Fri Jul 30 2010 Justin Sherrill <jsherril@redhat.com> 1.1.41-1
- 619381 - fixing issue where reprovisioning a system would cause registration
  to fail in the %post section resulting in the system not being registered at
  all. (jsherril@redhat.com)

* Fri Jul 30 2010 Shannon Hughes <shughes@redhat.com> 1.1.40-1
- modify build requires java for epoc 1:1.6.0 

* Fri Jul 30 2010 Justin Sherrill <jsherril@redhat.com> 1.1.39-1
- few more changes for asm vs objectweb-asm detection (jsherril@redhat.com)

* Fri Jul 30 2010 Justin Sherrill <jsherril@redhat.com> 1.1.38-1
- taking a stab at alternating between asm.jar and objectweb-asm/asm.jar to
  handle errors with taskomatic on fedora13 (jsherril@redhat.com)

* Thu Jul 29 2010 Partha Aji <paji@redhat.com> 1.1.37-1
- Config Management schema update + ui + symlinks (paji@redhat.com)
- 603133 - fixing issue where system within a group that were unentitled would
  still factor into whether the group would show up with an exclamation point
  (jsherril@redhat.com)
- Symlink /var/www/html/pub in devel environment (coec@spacey.coesta.com)
- Fix checkstyle errors (coec@spacey.coesta.com)
- 563797 - changing behavior of lookup exceptions to print a smaller error as
  well as not send an email by default (jsherril@redhat.com)
- 533190 - fixing issue where deleting more than 1000 errata would throw a
  database error (jsherril@redhat.com)
- 514426 - changing list tag behavior to show fliter box even if the user has
  filtered something and got no results (jsherril@redhat.com)
- 595524 - changing improper accesses to /ks/dist to return a file not found
  (jsherril@redhat.com)
- getting rid of tabs (jsherril@redhat.com)
- 591863 - making pre and post logging work for scripts that are not bash
  scripts (jsherril@redhat.com)
- fixing missing escaped command that broke kickstart rendering
  (jsherril@redhat.com)
- System currency phase 2 (coec@spacey.coesta.com)
- Fix 'Duplicate message key found in XML Resource file' message
  (coec@spacey.coesta.com)
- added new API functions system.listPackageProfiles and
  system.deletePackageProfile (aparsons@redhat.com)
- fixed the system counts in the *_action_list queries (aparsons@redhat.com)
- 580086 - cleaning up some code related with system group intersection and
  fixing one possible cause of not calculating the intersection correctly
  (jsherril@redhat.com)
- checkstyle fixes (jsherril@redhat.com)
- checkstyle fixes (jsherril@redhat.com)
- 582085 - fixing issue where renaming an errata with keywords would fail
  (jsherril@redhat.com)
- 582995 - fixing the automatic escaping of dollar signs within a raw kickstart
  (jsherril@redhat.com)
- removing mistakenly included debug message (jsherril@redhat.com)
- 616267 - fixing issue where system.listPackages api call would return nothing
  if the client had not uploaded the arch for the installed packages (older
  rhel 4 clients) (jsherril@redhat.com)

* Mon Jul 26 2010 Tomas Lestach <tlestach@redhat.com> 1.1.36-1
- alter the return type of system.listLatestAvailablePackage
  (aparsons@redhat.com)
- added new API call system.listLatestAvailablePackage that will list the
  latest available version of a package for each system in the list
  (aparsons@redhat.com)
- add counts for the number of completed/failed/inprogress systems to the
  ScheduledAction DTO and schedule.list*Actions API calls (aparsons@redhat.com)
- added new API call schedule.rescheduleActions (aparsons@redhat.com)

* Fri Jul 23 2010 Michael Mraka <michael.mraka@redhat.com> 1.1.35-1
- fixing new connection stuff to allow for the thin client
- Add system migration to webUI

* Thu Jul 22 2010 Michael Mraka <michael.mraka@redhat.com> 1.1.34-1
- modified java to use global database information
- fixed asm for Fedora 13

* Tue Jul 20 2010 Justin Sherrill <jsherril@redhat.com> 1.1.33-1
- Initial set of changes to show the 'files' include info on dirs and symlinks
  (paji@redhat.com)
- Making spacewalk-java build correctly for fedora 13 (jsherril@redhat.com)
* Tue Jul 20 2010 Justin Sherrill <jsherril@redhat.com> 1.1.32-1
- fixing java build scripts to use objectweb-asm library if it exists versus
  the normal asm (jsherril@redhat.com)
- add path to oracle xe library for taskomatic (msuchy@redhat.com)
- converting hibernate blobs to binary data types to hopefully work better in
  postgresql (jsherril@redhat.com)

* Tue Jul 20 2010 Tomas Lestach <tlestach@redhat.com> 1.1.31-1
- checkstyle fix (tlestach@redhat.com)
- 584860 - do not return empty partition strings (tlestach@redhat.com)
- 584860 - kickstart.profile.system.getPartitioningScheme does not return
  include statements (aparsons@redhat.com)
- 584864 - added API method kickstart.profile.downloadRenderedKickstart
  (aparsons@redhat.com)
- 584852 - added API configchannel.listSubscribedSystems (aparsons@redhat.com)
- Added a nice org updated message for the org config page (paji@redhat.com)
- 599612 - making the SSM able to subscripe systems to shared channels
  (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- making kickstarts not fail if multiple of the same NVREA are in the same
  channel (jsherril@redhat.com)
- 600502 - speeding up system.getId() api call (jsherril@redhat.com)

* Mon Jul 19 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.30-1
- use db_* options from rhn.conf to retrieve database connection info
- Added unit tests for SystemHandlerTest.convertToFlex
- unit test fix
- fixing un-escaped dollar sign in %post script that deals with rewriting
  /etc/sysconfig/rhn/up2date

* Fri Jul 16 2010 Justin Sherrill <jsherril@redhat.com> 1.1.29-1
- fixing compile breakage (jsherril@redhat.com)

* Fri Jul 16 2010 Partha Aji <paji@redhat.com> 1.1.28-1
- Forgot to add Exception Message ... (paji@redhat.com)

* Fri Jul 16 2010 Milan Zazrivec <mzazrivec@redhat.com> 1.1.27-1
- fixed typo in system_currency query
- Added a convert to flex api call and misc improvements on unit tests

* Thu Jul 15 2010 Justin Sherrill <jsherril@redhat.com> 1.1.26-1
- adding a couple of temp jars back for build system builds
  (jsherril@redhat.com)

* Thu Jul 15 2010 Justin Sherrill <jsherril@redhat.com> 1.1.25-1
* Thu Jul 15 2010 Justin Sherrill <jsherril@redhat.com> 1.1.24-1
- moving temp jars to ivy, and adding needed slf4j jars for quartz unit tests
  (jsherril@redhat.com)
- fix checksum info across mulitorg grant actions (shughes@redhat.com)
- fixed system_currency query (michael.mraka@redhat.com)

* Thu Jul 15 2010 Tomas Lestach <tlestach@redhat.com> 1.1.23-1
- [PATCH] allow multiple systems to be scheduled for an erratum via the API
  (aron@redhat.com)
- checkstyle fixes (tlestach@redhat.com)
- [PATCH] alter system.scheduleRunScript API call to schedule multiple systems
  (aron@redhat.com)
- removed dead file not used anywhere (michael.mraka@redhat.com)
- oracle client has been removed from /opt/oracle ages ago
  (michael.mraka@redhat.com)
- Add system currency report (colin.coe@gmail.com)
- Added API to list flex guests and eligible flex guests (paji@redhat.com)
- Added a Configuration page to Orgs to handle maintenance windows
  (paji@redhat.com)
- Added the lookupAndBind org to RequestContext so it could be used in various
  actions (paji@redhat.com)
- added a simple test to check for stagin content (paji@redhat.com)
- adding flex guest support for some of the org-entitlement apis
  (jsherril@redhat.com)
- making Channel package add page much faster (jsherril@redhat.com)
- Cleaned up web_customer, rhnPaidOrgs, and rhnDemoOrgs inaddition to moving
  OrgImpl- Org. These are unused tables/views/columns.. Added upgrade scripts
  accordingly (paji@redhat.com)
- fixed a goof up on preferences jspf that didn;t escape content
  (paji@redhat.com)
- fixed a comment typo (paji@redhat.com)
- Added an extra column mapping to OrgImpl object (paji@redhat.com)
- updating api doc for system.getScriptResults (adding serverId)
  (tlestach@redhat.com)
- add serverId to structure returned by system.getScriptResults() API call
  (aparsons@redhat.com)
- Corrected a couple of jsp pages where 'label for' was not used
  (paji@redhat.com)
- Fix checkstyle errors (colin.coe@gmail.com)
- Use correct tomcat version (colin.coe@gmail.com)
- Remove println used in testing (colin.coe@gmail.com)
- Display calina.out in admin tab, part 2 (colin.coe@gmail.com)
- Display calina.out in admin tab (colin.coe@gmail.com)

* Fri Jul 09 2010 Justin Sherrill <jsherril@redhat.com> 1.1.22-1
- 576139 - fixing issue where auto-application of errata would be triggered
  before the new repodata was generated. (jsherril@redhat.com)

* Thu Jul 08 2010 Shannon Hughes <shughes@redhat.com> 1.1.21-1
- removing log5j until we get fedora approval; removed velocity since its in
  tempjars; adding new versions of quartz for cron taskomatic scheduler
  (shughes@redhat.com)

* Thu Jul 08 2010 Justin Sherrill <jsherril@redhat.com> 1.1.20-1
- 603258 - fixing issue where channel.software.mergeErrata and mergePackages
  would not populate the errata/package cache corerctly (jsherril@redhat.com)

* Thu Jul 08 2010 Tomas Lestach <tlestach@redhat.com> 1.1.19-1
- CobblerSyncTask fix (tlestach@redhat.com)
- Made entitlement logic handle flex guests when the host is virt (un)entitled
  (paji@redhat.com)
- 608811 - fixing issue where virt guest creation would not create the guests
  to use a virtual bridge. (jsherril@redhat.com)

* Fri Jul 02 2010 Jan Pazdziora 1.1.18-1
- Use the { call ... } syntax instead of the direct PL/SQL.
- fix broken repo sync download log file logic (shughes@redhat.com)
- fixed a couple of issues with the sat scrubber test (paji@redhat.com)

* Thu Jul 01 2010 Tomas Lestach <tlestach@redhat.com> 1.1.17-1
- replacing ExceptionTranslator for SqlExceptionTranslator and its convert()
  method for sqlException() (tlestach@redhat.com)
- Added a sat scrubber test that wipes out old test artifactsw
  (paji@redhat.com)
- Added an automatic db test cleanup script as a part of tests
  (paji@redhat.com)
- fix bug Validation i18n key (shughes@redhat.com)
- bug fixing for reposync (shughes@redhat.com)
- junit modification for repo sync (shughes@redhat.com)
- checkstyle fix, extra java import (shughes@redhat.com)
- hook to call create repo sync task in taskomatic (shughes@redhat.com)
- remove call to repo task from the channel edit/update cmds
  (shughes@redhat.com)
- add last log repo sync to edit channel (shughes@redhat.com)
- remove old repo fields from channel edit page, clean up i18n strings
  (shughes@redhat.com)
- making links between repo objects and taskomatic (shughes@redhat.com)
- lots of checkstyle fixes (shughes@redhat.com)
- add channel count access for repo objects (shughes@redhat.com)
- general repo cleanup, bugfixing (shughes@redhat.com)
- new page: list of repos to sync (session sets) (shughes@redhat.com)
- struts support for repo sync action (shughes@redhat.com)
- adding new sync nav, moving add/remove to new tab (shughes@redhat.com)
- remove debug messages, add extra i18n update string (shughes@redhat.com)
- db mapping logic for channel repos (shughes@redhat.com)
- preselect set channel repo logic (shughes@redhat.com)
- initial jsp support for channel to repo mapping (shughes@redhat.com)
- change from rhnset to sessionset for repo maps (shughes@redhat.com)
- intial strut action for channel repository mapping (shughes@redhat.com)
- strut support for channel repository mapping (shughes@redhat.com)
- channel nav support for repository mapping (shughes@redhat.com)
- modify verbage for repo list summary (shughes@redhat.com)
- logic to delete content sources from db (shughes@redhat.com)
- minor syntax issue with i18n repo delete strings (shughes@redhat.com)
- initial files to support Repo delete (shughes@redhat.com)
- bug fixes for EditRepo, strut path fixes (shughes@redhat.com)
- RepoEdit page cleanup, jsp fixes (shughes@redhat.com)
- fix hibernate content obj named queries for Edit Repo (shughes@redhat.com)
- starting checking content objects off id and org for security; also fix query
  for taskomatic (shughes@redhat.com)
- commit before master merge (shughes@redhat.com)
- adding repo edit commands (shughes@redhat.com)
- refactoring repo commands to use base class (shughes@redhat.com)
- more repo content obj clean up (shughes@redhat.com)
- fix link for repo edit (shughes@redhat.com)
- quick fix to remove sync query from content source obj (shughes@redhat.com)
- update channel to handle sync date; remove from content source
  (shughes@redhat.com)
- fix incorrect reference to sync column of content source (shughes@redhat.com)
- adding org id mapping to content source objects (shughes@redhat.com)
- ise fixes for repo create (shughes@redhat.com)
- adding url field to repo details form/jsp (shughes@redhat.com)
- pushing changes to prepare for master merge (shughes@redhat.com)
- fixed incorrect url syntax for repocreate (shughes@redhat.com)
- adding repo domain creation logic to manager/action layer
  (shughes@redhat.com)
- pushing minor changes before master merge (shughes@redhat.com)
- repo struts action fnd jsp or creating repo objects. (shughes@redhat.com)
- support classes for adding a Repo object (shughes@redhat.com)
- repo validation xsd schema (shughes@redhat.com)
- adding nav entries for repo create and edit (shughes@redhat.com)
- struts entries for repo create and edit pages (shughes@redhat.com)
- adding dynaform for content source creation (shughes@redhat.com)
- fixing toolbar syntax for repo (shughes@redhat.com)
- minor tweaks to struts url path and hibernate fix (shughes@redhat.com)
- adding repolist page to struts (shughes@redhat.com)
- datasource queries for repolist listtag page (shughes@redhat.com)
- adding ContentSource DTO object for repo listtags (shughes@redhat.com)
- setting up ContentSource queries (shughes@redhat.com)
- fixing compile errors on RepoLister (shughes@redhat.com)
- initial classes for Repolisting (shughes@redhat.com)
- adding repo list jsp page (shughes@redhat.com)
- Revert "fixing accidental branch creation, removing cobbler stubs"
  (shughes@redhat.com)
- fixing accidental branch creation, removing cobbler stubs
  (shughes@redhat.com)
- new jsp for the repo list (shughes@redhat.com)
- adding nav menu for external repo management (shughes@redhat.com)
- minor changes to tests (shughes@redhat.com)
- more compiliation fixes to support many2many (shughes@redhat.com)
- fixing breakage after adding many2many objects for yum repo sync
  (shughes@redhat.com)
- minor updates to Channel object to add repos (shughes@redhat.com)
- initial hibernate changes to support many2many relationships of channel to
  repos (shughes@redhat.com)
- hibernate changes for existing content source objects (shughes@redhat.com)
- Fixed some checkstyle errors (paji@redhat.com)
- 605383 - fixing issue where adding errata to a channel with 'package
  association' unchecked wouldn't handle arches correctly (jsherril@redhat.com)

* Wed Jun 30 2010 Tomas Lestach <tlestach@redhat.com> 1.1.16-1
- 591291 - fix also mergeErrata with given start and end date
  (tlestach@redhat.com)
- remove exceptions from method definitions that aren't thrown
  (tlestach@redhat.com)
- More unit test fixes (paji@redhat.com)
- Cleared more unit test (paji@redhat.com)
- Fixed another checkstyle issue (paji@redhat.com)
- Speeded up a unit test .... (paji@redhat.com)
- Fixed a checkstyle issue (paji@redhat.com)
- Fixed fve unit tests Hopefully... (paji@redhat.com)
- Fixed a dupe key issue (paji@redhat.com)
- if file is rpm package, use checksum from db, otherwise read whole file
  (msuchy@redhat.com)
- Fixed a compile error.... (paji@redhat.com)
- Added more tests on Orphaned gets entitlements (paji@redhat.com)
- Added unit tests for VirtEntitlementsManager (paji@redhat.com)
- Fixed some typos (paji@redhat.com)
- Added page sizes to flex multiorg pages (paji@redhat.com)
- fixed a line typo where I forgot to clear the map create in session
  (paji@redhat.com)
- Added sorting to channel family-> orgs page (paji@redhat.com)
- Added flex magic to ChannelFamily -> Orgs page (paji@redhat.com)
- Added alphabar columns for the mutli org pages (paji@redhat.com)
- More verbiage on software entitlements page (paji@redhat.com)
- Updated the software entitlements page to deal with FVE (paji@redhat.com)
- Added a couple of enhancements on the Org software subs pager
  (paji@redhat.com)
- Fixed checkstyle errors (paji@redhat.com)
- Added code to get multiorgs org -> software channel ents page work with flex
  entitlements (paji@redhat.com)
- Forgot to commit EligibleFlexGuestAction (paji@redhat.com)
- Added the convert to flex plsql operation (paji@redhat.com)
- More updates to the UI (paji@redhat.com)
- More UI updates on the Flex Guest Pages added Nav stuff (paji@redhat.com)
- Made the Flexguest page show entitlements (paji@redhat.com)
- Initial cut to list eligible flex guests page (paji@redhat.com)
- Slight refactoring of Virtual Enttitlements (paji@redhat.com)
- Initial cut of the Flex Guests Page (paji@redhat.com)
- adding flex guest entitlement columns on the org entitlments page
  (jsherril@redhat.com)
- updating rhn_entitlement package for cert activation (jsherril@redhat.com)
- having setters do the right thing (jsherril@redhat.com)
- matching hosteds column names for flex guests (jsherril@redhat.com)
- adding hibernate mapping for flex guests (jsherril@redhat.com)

* Wed Jun 23 2010 Jan Pazdziora 1.1.15-1
- Fixed a couple of checkstyle errors (paji@redhat.com)

* Mon Jun 21 2010 Jan Pazdziora 1.1.14-1
- updating rhnPackageRepodata table to not use a reserved word.
  (jsherril@redhat.com)
- Fixed a typo in the previous commit (paji@redhat.com)
- Good Bye Channel License Code (paji@redhat.com)

* Fri Jun 18 2010 Miroslav Suchý <msuchy@redhat.com> 1.1.13-1
- implement <label> for form fields - sdc/details.jsp (msuchy@redhat.com)
- implement <label> for form fields - user/create/usercreate.jsp
  (msuchy@redhat.com)
- implement <label> for form fields - activationkeys/details.jspf
  (msuchy@redhat.com)
- implement <label> for form fields - edit.jsp (msuchy@redhat.com)
- implement <label> for form fields - orgcreate.jsp (msuchy@redhat.com)
- implement <label> for form fields - probe-edit.jsp (msuchy@redhat.com)
- implement <label> for form fields - filter-form.jspf (msuchy@redhat.com)
- implement <label> for form fields - restart.jsp (msuchy@redhat.com)
- implement <label> for form fields - monitoring.jsp (msuchy@redhat.com)
- implement <label> for form fields - bootstrap.jsp (msuchy@redhat.com)
- implement <label> for form fields - general.jsp (msuchy@redhat.com)
- 585176 - changing the behavior of the SSM package upgrade screen to handle
  system and their packages for upgrade invidually, so only packages needed on
  a system will be installed.  This means that each system is scheduled
  individually, but at least it is correct (jsherril@redhat.com)

* Thu Jun 17 2010 Miroslav Suchý <msuchy@redhat.com> 1.1.12-1
- Made the duplicate compares page do confirm delete differently
  (paji@redhat.com)
- Added a sort of 'confirm' logic for delete systems in dup compares page
  (paji@redhat.com)
- 602591 - "Content-Length" added to response header for different download
  contents (tlestach@redhat.com)
- 603890 - fix/rewrite system.listSubscribableBaseChannels API
  (tlestach@redhat.com)
- 576314 - fix for errata being added to the email queue multiple times before
  it can be run (jsherril@redhat.com)
- bumping up heap to 512m for jsp compiles (shughes@redhat.com)
- bumping up build heap to 512m (shughes@redhat.com)
- Removed an unnecessary abstraction for VirtEntitlements (paji@redhat.com)
- 591291 - associate packages also (when mergeing errata) (tlestach@redhat.com)
- 601656 - fix channel permission check for errata.clone (tlestach@redhat.com)
- 601656 - fix channel permission check for channel.software.mergePackages
  (tlestach@redhat.com)
- fixing issue where package summary could be null, causing NPE
  (jsherril@redhat.com)
- 601656 - fix channel permission check (tlestach@redhat.com)
- 591291 - clone errata instead of associating them to custom channels
  (tlestach@redhat.com)
- fixing hashCode for Errata (tlestach@redhat.com)
- 529359: Fixed a couple of bugs related to Remote Command Package upgrade
  (paji@redhat.com)
- 595473 525588 - fixing small query issue and moving the ssm operation
  creation to before the (jsherril@redhat.com)
- 595473 525588 - fixing issue where child channel subscription changes would
  not use the stored procedure and would instead update rhnServerChannel table
  directly, bypassing all entitelment logic (jsherril@redhat.com)
- 525588 - changing SSM child channel subscription page to not use hibernate
  when doing subscribng (jsherril@redhat.com)
- Correct 'checkstyle' errors (colin.coe@gmail.com)
- checkstyle fixes (jsherril@redhat.com)
- Update errata.setDetails to allow setting CVEs (colin.coe@gmail.com)
- Allow CVEs to be set on unpublished errata (colin.coe@gmail.com)
- 585176 - fixing issue where packages were excluded from update on SSM
  upgradable packages page when the packages had multiple arches
  (jsherril@redhat.com)
- 585965 - fixing issue with multilib packages and errata-cache generation,
  where updating one arch of a package would indicate that the other one was
  updated as well (jsherril@redhat.com)
- 563859 - fixing issue where adding errata to x86_64 channels would only get
  packages of one arch, even if the errata had two (lib packages)
  (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)
- Adding the correct checkstyle for inactive systems (paji@redhat.com)
- 576953 - fixing errata search case sensitivity and not searching on partial
  cve name (jsherril@redhat.com)
- 588367 - introducing systemgroup.scheduleApplyErrataToActive API call
  (tlestach@redhat.com)
- 588367 move applyErrataHelper to ErrataManager (tlestach@redhat.com)
- Added the dupe compare css and javascript magic (paji@redhat.com)
- 590204 - fixing issue where pagination wasnt working properly on normal user
  list page (jsherril@redhat.com)
- Made the default dups compare page preselect a bunch of items
  (paji@redhat.com)
- Improved a error message on Dups systems page (paji@redhat.com)
- Fix style of commit c4e387bbb1c5cf16f54a2fa968a5613121bc1d7a
  (lukas.durfina@gmail.com)
- A more functional dupes compare page (paji@redhat.com)
- adding distro deletion to cleanup script (jsherril@redhat.com)
- Removed a no white space after a type cast check since we are not enforcing
  it anywhere (paji@redhat.com)
- unit test fix (jsherril@redhat.com)
- Generate Debian repository (lukas.durfina@gmail.com)
- Fixed broken unit tests (paji@redhat.com)
- checkstyle fix (joshua.roys@gtri.gatech.edu)
- Updated a typo in the  string (paji@redhat.com)
- Updated a resource string (paji@redhat.com)
- Added i18n strings for the systemdetails page (paji@redhat.com)
- Limit automatic config comparisons to diff enabled systems
  (joshua.roys@gtri.gatech.edu)

* Mon May 10 2010 Partha Aji <paji@redhat.com> 1.1.11-1
- Added an option to selectively delete instead of reactivate when a system is
  being reprovisioned (paji@redhat.com)
- Made ssm operations use OperationDetailsDto instead of just dealing with
  plain maps and random attributes (paji@redhat.com)
- unit tset fix (jsherril@redhat.com)
- 528884 - fixing issue where cloning ks profiles wouldnt clone virt info
  (jsherril@redhat.com)
- Added stubs for the duplicate profiles compare page (paji@redhat.com)
- Fixed a hibernate bug on capabilities object. Removed created and modified
  from mapping (paji@redhat.com)
- 568962 - get correct set of errata to merge (tlestach@redhat.com)
- Fix a NPE in the Audit code (joshua.roys@gtri.gatech.edu)
- Added the import tree.js part to the expansion decorator so its used on a
  need to use bases (paji@redhat.com)
- Added the logic to handle Delete from the Dup Systems page (paji@redhat.com)
- Made the dup systems page use ssm (paji@redhat.com)
- Made the expansion decorator show the show all|hide all correctly
  (paji@redhat.com)
- queuing channel repo generation for new channels (jsherril@redhat.com)
- Fixed a pagination issue that occured on first page load (paji@redhat.com)
- ignoring virt bonded interfaces, changing dups page to not sure the same set,
  and fixing inactive counts on mac and hostname pages (jsherril@redhat.com)
- 585901 - add an extra null condition (tlestach@redhat.com)
- Added a form var to keep track of inactive count (paji@redhat.com)
- Added logic for all the 3 tabs to use the same set as they refer to the same
  list (paji@redhat.com)
- Added Nav Tabs + hostname /mac address functionality + cleaned up the i18n
  Strings (paji@redhat.com)
- adding inactive drop down box and select inactive button
  (jsherril@redhat.com)
- Changed the tree behaviour to always expand (paji@redhat.com)
- Fixed checkstyle (paji@redhat.com)
- Commiting the Select All magic stuff (paji@redhat.com)
- 588901 - fix to_package_id (joshua.roys@gtri.gatech.edu)

* Wed May 05 2010 Tomas Lestach <tlestach@redhat.com> 1.1.10-1
- 585901 - recursive comps search (tlestach@redhat.com)
- More work on select all magic (paji@redhat.com)
- 588901 - Fix listLatestUpgradablePackages API results
  (joshua.roys@gtri.gatech.edu)
- Fixed an accidental compile error that occured due to a previous commit
  (paji@redhat.com)
- Added some magic to show the system names and url instead of ids in the dups
  page (paji@redhat.com)
- added an nbsp to space the text better (paji@redhat.com)
- Added a new tag attribute to filter by ip address (paji@redhat.com)
- More list tag enhancements (paji@redhat.com)
- Updated the list tag to deal with parent vs child filtering (paji@redhat.com)
- More changes to properly handle selection javascript magic (paji@redhat.com)
- Needed to add more JS magic to get selections to work (paji@redhat.com)
- Quick fix to deal with a null pointer that would ve occued on a logdebg
  (paji@redhat.com)
- Added code to get checkbox grouping to work (paji@redhat.com)
- Got the tree filters working (paji@redhat.com)
- Fixed a checkstyle error (paji@redhat.com)
- fixing RowRenderer, to do coloring more like the mockups
  (jsherril@redhat.com)
- Made the post reactivation key logic more fail safe.. (paji@redhat.com)

* Thu Apr 29 2010 Partha Aji <paji@redhat.com> 1.1.9-1
- Added new cobbler snippets to enable sytem reactivation on bare metal reprovisioning
  (paji@redhat.com)
- Added code to show general snippets created in spacewalk.
- Remove spammy audit types from default search (joshua.roys@gtri.gatech.edu)

* Thu Apr 29 2010 Tomas Lestach <tlestach@redhat.com> 1.1.8-1
- introducing DistChannelHandler (tlestach@redhat.com)
- add 2 new DistChannelMap related queries with appropriate methods
  (tlestach@redhat.com)
- rename {lookup,find}ByOsReleaseAndChannelArch ->
  ByProductNameReleaseAndChannelArch (tlestach@redhat.com)
- Added all the javascript macgic needed to show and hide stuff
  (paji@redhat.com)
- Fixed a Compile typo to work with 1.5 compiler (paji@redhat.com)

* Wed Apr 28 2010 Jan Pazdziora 1.1.7-1
- Added new expandable and non-expandable columns. Also UI improvements
  (paji@redhat.com)
- adding expandable row renderer and adding it to duplicate page
  (jsherril@redhat.com)
- Added an 'expandable' tag function to differentiate between parent/child
  (paji@redhat.com)
- Got the new treeable list tag in a more stable state (paji@redhat.com)
- Better looking Duplicate Ips page (paji@redhat.com)
- The relativeFilename in rhnChannelComps is really relative, need to join with
  slash.
- converting Duplicate dtos to use new expandable interface
  (jsherril@redhat.com)
- Added initial entry point for duplicate ip page (paji@redhat.com)
- Added initial mods to list tag to deal with simple trees (paji@redhat.com)
- adding row renderer (jsherril@redhat.com)
- creating RowRenderer to provide alternate ways to render the styles of each
  row (jsherril@redhat.com)
- remove @Override, since it is not an Override (tlestach@redhat.com)
- Change from nested select to inner join (colin.coe@gmail.com)
- Got the delete systems  confirm page completed. (paji@redhat.com)
- Make bash the default for syntax highlighting (colin.coe@gmail.com)

* Fri Apr 23 2010 Justin Sherrill <jsherril@redhat.com> 1.1.6-1
- adding duplicate system manager layer and api calls (jsherril@redhat.com)
- adding server delete event for duplicate profiles (shughes@redhat.com)
- Moved SSM System DeleteConfirm page to java to facilitate Deletion using the
  message queue infrastructure (paji@redhat.com)
- allowing the period character is cobbler system records (jsherril@redhat.com)

* Wed Apr 21 2010 Justin Sherrill <jsherril@redhat.com> 1.1.5-1
- adding feature to preselect a kickstart profile for provisioning if the
  cobbler system record for that system has it selected (jsherril@redhat.com)
- 580927 - sorting advanced options (jsherril@redhat.com)
- fixing broken unit tests and properly picking the right exception
  (jsherril@redhat.com)
- Addition of channel.software.getChannelLastBuildById API call
  (james.hogarth@gmail.com)

* Mon Apr 19 2010 Michael Mraka <michael.mraka@redhat.com> 1.1.4-1
- 576211 - fixed server name replacement pattern
- removing log5j stuff
- fix issue with PSQLException

* Fri Apr 16 2010 Justin Sherrill <jsherril@redhat.com> 1.1.2-1
- bumping spec files to future 1.1 packages (shughes@redhat.com)
- 516983 - making it clearer that a distro cannot be deleted if profiles are
  associated with it. Also fixing the nav for that page (jsherril@redhat.com)
- Fix the SELinux regex to handle MLS categories better
  (joshua.roys@gtri.gatech.edu)
- Fix SSM 'Select All' button on configuration pages
  (joshua.roys@gtri.gatech.edu)
- xmlrpc: Put the symlink target in 'contents' (joshua.roys@gtri.gatech.edu)
- adding velocity dep (jsherril@redhat.com)
- Add 'arch' to channel.list*Channels (colin.coe@gmail.com)
- Fix xmlrpc file-type for symlinks (joshua.roys@gtri.gatech.edu)
- adding log5j to ivy stuff, and moving the repo to parthas fedorapeople
  account (jsherril@redhat.com)
- 576907 - making same display changes for system sync (tlestach@redhat.com)
- Move systemlogs directory out of /var/satellite (joshua.roys@gtri.gatech.edu)
- 580227 - displaying dates in the same format (tlestach@redhat.com)

* Wed Apr 07 2010 Tomas Lestach <tlestach@redhat.com> 0.9.17-1
- introducing kickstart.cloneProfile API call (tlestach@redhat.com)

* Wed Apr 07 2010 Justin Sherrill <jsherril@redhat.com> 0.9.16-1
- 573153 - improving performance of the systems group overview page
  considerably (jsherril@redhat.com)
- adding NVL to query which needed it (jsherril@redhat.com)
- fixing small issue with query that resulted in odd error, inconsistent
  datatypes: expected UDT got CHAR (jsherril@redhat.com)
- Implement 'channel.software.listChildren' API call (colin.coe@gmail.com)

* Fri Apr 02 2010 Tomas Lestach <tlestach@redhat.com> 0.9.15-1
- 576907 - supporting multilib packages for syncing systems/profiles
  (tlestach@redhat.com)
- fixing taskomatic problem (tlestach@redhat.com)
- 577074 - Fix to remove invalid characters from a cobbler system record name
  (paji@redhat.com)
- 574594 - Fixed date based sorting issues on 4 User List pages.
  (paji@redhat.com)
- 577224 - Fixed an issue where when cloning KS profiles variables were not
  getting copied (paji@redhat.com)

* Wed Mar 31 2010 Justin Sherrill <jsherril@redhat.com> 0.9.14-1
- 531122 - fixing issue where system records created with cobbler would not use
  all the correct activation keys once keys were changed from a profile
  (jsherril@redhat.com)
- 522497 - Fixed a ks system details bug (paji@redhat.com)
- Remove audit review cruft from spacewalk-setup (joshua.roys@gtri.gatech.edu)

* Fri Mar 26 2010 Justin Sherrill <jsherril@redhat.com> 0.9.13-1
- 576301, 576314 - fixing issues where auto-apply of errata was applying even
  for systems that did not need the errata and was being scheduled multiple
  times for systems (once for every channel that contained that errata)
  (jsherril@redhat.com)
- changing cobbler call to use automated user since it could go through
  taskomatic (jsherril@redhat.com)
- API to list API (tlestach@redhat.com)
- 559693 - fixing apidoc (tlestach@redhat.com)
- 559693 - allow channel.software.listAllPackages to return the checksum
  (colin.coe@gmail.com)
- added packages no more automaticaly required in tomcat6
  (michael.mraka@redhat.com)

* Fri Mar 26 2010 Tomas Lestach <tlestach@redhat.com> 0.9.12-1
- API to list API (tlestach@redhat.com)
- 559693 - fixing apidoc (tlestach@redhat.com)
- 559693 - allow channel.software.listAllPackages to return the checksum
  (colin.coe@gmail.com)

* Wed Mar 24 2010 Michael Mraka <michael.mraka@redhat.com> 0.9.11-1
- fixed Requires for tomcat6
- test case fix for SystemHandlerTest

* Mon Mar 22 2010 Tomas Lestach <tlestach@redhat.com> 0.9.10-1
- 575796 - make system.get_name API call faster (tlestach@redhat.com)
- 529359 - attempting to fix issue where solaris packages couldnt be installed,
  may break unit test, we will see (jsherril@redhat.com)
- 529359 - Fix for this error (paji@redhat.com)
- Basically removed the listAllSystems call in SystemManager (paji@redhat.com)
- 574197 - making cobbler name seperator configurable (jsherril@redhat.com)

* Wed Mar 17 2010 Michael Mraka <michael.mraka@redhat.com> 0.9.9-1
- 568958 - package removal and verify
- 516048 - syncing java stack with perl stack on channel naming convention
- 510383 - Create/Update user commands use the max_user_len and min_user_len values
- 574065 - shared channel couldnt properly be used as a distros channel
- fixed syntax highliging in editarea textareas
- 510383 - fixes on the UI side for password length issue 
- 572277 - package profile sync
- added an API function: errata.listUnpublishedErrata
- 559551 - ISE fixed for SyncSystems.do
- making Channel.getPackages() much more verbose
- 570560 - fixing misleading channel creation warning message
- 514554 - adding back the ability to delete virt guests
- 529962 - nav not showing the current tab
- 531122 - <<inherit>> would appear within system records when modifying activation key
- 493176 - kickstart.tree.getDetails
- 562881 - save cobbler object after setting kickstart variables
- 562881 - cobbler system record check

* Fri Feb 19 2010 Tomas Lestach <tlestach@redhat.com> 0.9.8-1
- 566434 - manage base entitlements with system.add/removeEntitlements API call
  (tlestach@redhat.com)
- combine several API call params to a single Map parameter
  (tlestach@redhat.com)

* Tue Feb 16 2010 Justin Sherrill <jsherril@redhat.com> 0.9.7-1
- fixing issue with conflict between javamail package and classpathx-mail
  (which provides javamail as a provides).  The fedora 12 build was building
  against the javamail package which broke the deployment when it wasnt
  installed (jsherril@redhat.com)

* Mon Feb 15 2010 Justin Sherrill <jsherril@redhat.com> 0.9.6-1
- changing new rev number to be one more than latest, not one more than current
  (jsherril@redhat.com)
-  510100 - adding the ability to set a config file to a certain revision
  (jsherril@redhat.com)
- making timezone still null errors a bit quieter.  Maybe once we really add
  all the timezones we can really do a warning (jsherril@redhat.com)
- Automatic commit of package [spacewalk-java] release [0.9.4-1].
  (jsherril@redhat.com)
- fixing rhn.xml for tomcat6 (jsherril@redhat.com)
- 562881 - new api calls introduced (tlestach@redhat.com)

* Thu Feb 11 2010 Justin Sherrill <jsherril@redhat.com> 0.9.4-1
- adding snippet api unit tests (jsherril@redhat.com)

* Wed Feb 10 2010 Justin Sherrill <jsherril@redhat.com> 0.9.2-1
- initial tomcat6 stuff (jsherril@redhat.com)
- change checkstyle Header to RegexpHeader (tlestach@redhat.com)
- change copyright preferencies for newly created java files
  (tlestach@redhat.com)
- updated copyrights in all java files to make hudson happy
  (michael.mraka@redhat.com)
- adding createOrUpdate and delete to snippet handler as well as tests
  (jsherril@redhat.com)
- 558628 - fixing issue with configure-proxy script as well as making /cblr
  rewrites work over SSL too (jsherril@redhat.com)
- commiting missing files from previous commit that converted target systems
  page to java (jsherril@redhat.com)
- adding kickstart.snippet.list* (jsherril@redhat.com)
- fixing issue where select all and update set would clear the set before
  redisplaying the page (jsherril@redhat.com)
- fixing issue where probe suite probe list was not generating probe links
  correctly resulting in an error when trying to edit or view the probe
  (jsherril@redhat.com)
- let's start Spacewalk 0.9 (michael.mraka@redhat.com)

* Sat Feb 06 2010 Michael Mraka <michael.mraka@redhat.com> 0.8.11-1
- Fix a NPE in CompareConfigFilesTask

* Thu Feb 04 2010 Michael Mraka <michael.mraka@redhat.com> 0.8.10-1
- updated copyrights
- 556956 - fixed listSubscribedSystems api call would error
- 559015 - fixed target systems page
- removed handler org_has_scouts
- 531454 - provide architecture even for downgrade/upgrade
- removed config values web.public_errata_*
- 561068 - fixed api breakage with new cobbler version

* Fri Jan 29 2010 Miroslav Suchý <msuchy@redhat.com> 0.8.9-1
- 539159 - offering only ssm systems with appropriate permissions for config channel unsubscription (tlestach@redhat.com)
- 539159 - offering only ssm systems with appropriate permissions for config channel subscription (tlestach@redhat.com)
- 538435 - fixing issue where cloning a channel wouldnt properly clone the activation keys, and wouldnt update the default session key properly (jsherril@redhat.com)
- 506950 - fixing issue where RedHat channels tab would show up for spacewalk users (jsherril@redhat.com)
fixing issue that kept spacewalk from working with the newest cobbler (jsherril@redhat.com)
- 559284 - fixing issue where _ & - characters were being removed from cobbler names (jsherril@redhat.com)

* Wed Jan 27 2010 Justin Sherrill <jsherril@redhat.com> 0.8.8-1
- fixing api doc (jsherril@redhat.com)

* Wed Jan 27 2010 Michael Mraka <michael.mraka@redhat.com> 0.8.7-1
- 529460 - fixing detection of disconnected satellite
- 530177 - moving cobbler snippet usage before user %post scripts
- 543879 - support for downloading kickstart profiles through a proxy
- 493176 - introducing kickstart.tree.getDetails API call
- 382561 - fixing daily status message to be formatted correctly
- 543184 - ability to change logging on a kickstart file from the api
- 513716 - prefix check simplification
- 506279 - speeding up channel.software.addPackages
- 518127 - adding a configchannel.deployAllSystems api call

* Fri Jan 15 2010 Tomas Lestach <tlestach@redhat.com> 0.8.6-1
- removing logic for channel checksum type completion (tlestach@redhat.com)
- 549752 - fix for check "channel in set" in UpdateChildChannelsCommand
  (tlestach@redhat.com)
- 555212 - changing the path we use for downloading package updates in
  kickstarts from $http_server to $redhat_management_server so that distros can
  be located externally without breaking this functionality
  (jsherril@redhat.com)
- 549752 - throwing exception, if subscribing system to a wrong child via api
  (tlestach@redhat.com)
- 537147 - removign unused row in column on user details page
  (jsherril@redhat.com)
- 514759 - stripping space chars from activation keys (jsherril@redhat.com)
- 554516 - adding better formatting for config file diffs (jsherril@redhat.com)
- 513716 - prefix validation added when creating a user (tlestach@redhat.com)
- 554767 - fixing issue where file preservation list details wouldnt always
  show up under the correct tab (jsherril@redhat.com)
- 543461 - fixing issue where csv downloader for systems errata list was not
  showing up (jsherril@redhat.com)
- 549553 - speeding up package removal from channel (jsherril@redhat.com)
- 553262 - fixing issue where kickstart label wasnt printed on software profile
  page (jsherril@redhat.com)

* Fri Jan 08 2010 Justin Sherrill <jsherril@redhat.com> 0.8.5-1
- 553265 - fixing issue where stored profile list wasnt sorted by name
  (jsherril@redhat.com)
- 552900 - fixing issue where variables would have a newline on the end
  (jsherril@redhat.com)
- Update copyright years to end with 2010. (jpazdziora@redhat.com)
- adding "Yum Repository Checksum Type" info to the channels/ChannelDetail.do
  page (tlestach@redhat.com)
- 526823 - improving speed of scheduling package installs for 1000s of systems
  (jsherril@redhat.com)
- 549391 - ISE when audit searching without any machine information
  (tlestach@redhat.com)

* Fri Dec 18 2009 Tomas Lestach <tlestach@redhat.com> 0.8.4-1
- fixed exception handling (tlestach@redhat.com)
- modifying Checksum.toString() for easier debugging (tlestach@redhat.com)
- sha256 changes for taskomatic (tlestach@redhat.com)
- adding checksum type for rhn/errata/details/Packages.do page
  (tlestach@redhat.com)
- displaying checkum type on rhn/software/packages/Details.do page
  (tlestach@redhat.com)
- download_packages.pxt was in the second rhn-tab-url in both
  channel_detail.xmls, and not referenced from anywhere else, removing.
  (jpazdziora@redhat.com)
- The webapp.conf is not used anywhere. (jpazdziora@redhat.com)
- adding channel.software.regenerateYumCache() api call (jsherril@redhat.com)
- making selinux not required for server.config.createOrUpdate() api call, also
  adding selinux_ctx to the documentation (jsherril@redhat.com)
- changing mock request to default to a POST request (jsherril@redhat.com)

* Wed Dec 16 2009 Tomas Lestach <tlestach@redhat.com> 0.8.3-1
- modifying spacewalk-java build propetries to enable f12 builds
  (tlestach@redhat.com)
- Remove the spacewalk-moon (sub)package as it is not used anywhere.
  (jpazdziora@redhat.com)
- correcting the action that the POST check was done for errata add package
  (jsherril@redhat.com)
- adding post checking to a couple of pages (jsherril@redhat.com)
- 545995 - adding package signing key to the package details page
  (jsherril@redhat.com)
- The email.verify.body trans-unit is not used anywhere, removing as dead text.
  (jpazdziora@redhat.com)

* Thu Dec 10 2009 Michael Mraka <michael.mraka@redhat.com> 0.8.2-1
- fixed support for SHA256 rpms

* Fri Dec  4 2009 Miroslav Suchý <msuchy@redhat.com> 0.8.1-1
- sha256 support

* Wed Dec 02 2009 Tomas Lestach <tlestach@redhat.com> 0.7.24-1
- 537094 - yum list-sec CVE's on cloned channels doesn't work
  (tlestach@redhat.com)
- fixing checksum empty string in the repo metadata (tlestach@redhat.com)
- checking return value of channel.getChecksum() (tlestach@redhat.com)
- 543347 - Security errata with enhancement advisory icons
  (tlestach@redhat.com)
- fixing ISE when cloning channel (tlestach@redhat.com)
- fixing ISE when adding Red Hat Errata to custom channel (tlestach@redhat.com)

* Tue Dec  1 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.23-1
- 542830 - fixing three api calls that were using very inefficient queries to use the same queries that were used in sat 5.2 (jsherril@redhat.com)
- converting old hibernate max in clause limit fix to use new fix (jsherril@redhat.com)
- 538559 - fixing issue where about 300 errata could not be applied to a system due to inefficient hibernate usage (jsherril@redhat.com)
- fixing list borders on errata apply confirm page (jsherril@redhat.com)
- Fix creating new config-managed symlinks (joshua.roys@gtri.gatech.edu)

* Mon Nov 30 2009 Tomas Lestach <tlestach@redhat.com> 0.7.21-1
- checking return value of channel.getChecksum() (tlestach@redhat.com)
- adding checkstyle build dependency (tlestach@redhat.com)
- updating ant-contrib path (tlestach@redhat.com)

* Wed Nov 25 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.19-1
- improving the system channels page by increasing the base channel selector box size and having the custom channels sorted by name (jsherril@redhat.com)
- another small display issue fix for list (jsherril@redhat.com)
- fixing sort on channel manage page to sort by name and not id (jsherril@redhat.com)
- fixing a bunch of list display issues that have bugged me for a while (jsherril@redhat.com)
- 519788 - fixing set selection on two config management lists (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- unit test fixes (jsherril@redhat.com)
- unit test fix - reloading the "Action" hibernate object seemed to cause issues with the user object that it was associated with, so instead lets try refreshing (jsherril@redhat.com)

* Fri Nov 20 2009 Tomas Lestach <tlestach@redhat.com> 0.7.18-1
- some columns not filled on webui for non-cve errata (tlestach@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 512844 - fixing inefficient query in package set clenaup
  (jsherril@redhat.com)
- unit test fix - we no longer do validation checking on kickstart partitions,
  so no need to test it (jsherril@redhat.com)
- unit test fix - kickstart compare packages was not working correctly
  (jsherril@redhat.com)
- 537491 - fixing issue with cloned kickstart profiles losing the package list
  during cloning (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)

* Thu Nov 12 2009 Tomas Lestach <tlestach@redhat.com> 0.7.17-1
- 536825 - storing "@ Base" KickstartPackage into DB (tlestach@redhat.com)
- java code enhancements according to jsherrill's comments
  (tlestach@redhat.com)
- unit test fix (jsherril@redhat.com)

* Tue Nov 10 2009 Tomas Lestach <tlestach@redhat.com> 0.7.16-1
- WebUI Errata & CVEs enhancements (tlestach@redhat.com)
- unit test fixes (jsherril@redhat.com)
- 531649 - fixed issue where confirmation message was not displayed after using
  channel merge/compare feature (jsherril@redhat.com)
- 531645 - fixing query with mistaken id reference (jsherril@redhat.com)
- standart Red Hat header added to CompareConfigFilesTask.java
  (tlestach@redhat.com)
- Show number of differing config files in overview
  (joshua.roys@gtri.gatech.edu)
- Set CompareConfigFilesTask to run at 11pm (joshua.roys@gtri.gatech.edu)
- Add task to schedule config file comparisons (joshua.roys@gtri.gatech.edu)
- Fix two more fd leaks (joshua.roys@gtri.gatech.edu)
- Plug fd leak (joshua.roys@gtri.gatech.edu)
- Fix system comparison file/dir/symlink counts (joshua.roys@gtri.gatech.edu)
- 508771 - fixing incorrect sort on channel errata list page
  (jsherril@redhat.com)
- 531091 - fixing issue that would result in odd hibernate errors due to
  hibernate objects being used across hibernate sessions (jsherril@redhat.com)
- 531059 - fixing issue where certain characters in the org name would cause
  errors when trying to create things in cobbler (jsherril@redhat.com)

* Tue Oct 27 2009 Tomas Lestach <tlestach@redhat.com> 0.7.15-1
- replacing HashSet with TreeSet (tlestach@redhat.com)
- checkstyle errors removed (tlestach@redhat.com)
- 525561 - fixing issue where ksdata without associated kickstart defaults
  would try to be synced to cobbler and fail (jsherril@redhat.com)

* Mon Oct 26 2009 Tomas Lestach <tlestach@redhat.com> 0.7.13-1
- 527724 - fix for kickstart upgrade issue (tlestach@redhat.com)
- 449167 - it looks better when architecture column is not thin column
  (msuchy@redhat.com)

* Fri Oct 23 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.10-1
- 449167 - show rpm install date in webui
- 144325 - recommiting this without the unintended sql commit  <jsherril@redhat.com>
- 144325 - moving probes and probe suite pages over to new list tag <jsherril@redhat.com>

* Tue Oct 20 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.9-1
- Make spacewalk use the editarea RPM and remove supplied editarea files (colin.coe@gmail.com)

* Tue Oct 20 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.8-1
- reverting parthas patch that was trying to automatically get connection info, but cause too many issues (jsherril@redhat.com)
- 522526 - fixing small issue where updating advanced options page would remove custom partitioning script (jsherril@redhat.com)
- 522526 - fixing issue where snippets couldnt be used in the partitioning section of the kickstart wizard (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 523624 - fixing issue where snippets were written with a carraige return (jsherril@redhat.com)
- 526823 - fixing issue where SSM package removal pages were taking way too long and timing out with 11000 systems (jsherril@redhat.com)
- 525575 - imporoving performance of system group overview query (michaels fix) (jsherril@redhat.com)

* Thu Oct  1 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.7-1
- 476851 - removing column "ENVIRONMENT" from ConfigMacro
- workaround for hibernate not handling in caluses of more than 1000 <jsherril@redhat.com>
- 523673 - generate repomd for zstreams too
- adding workaround for hibernate oddity/bug <jsherril@redhat.com>
- checkstyle fixes <jsherril@redhat.com>
- 525549 - fixing issue where SSM package operations would run out of memory <jsherril@redhat.com>
- adding script to help diagnose spacewalk-cobbler login issues <jsherril@redhat.com>
- Fix audit machine listing/paginatio <joshua.roys@gtri.gatech.edu>
- Make reviewing empty audit sections possible <joshua.roys@gtri.gatech.edu>
- Display 'File Type' as 'Symlink' in file details <joshua.roys@gtri.gatech.edu>
- 523926 - fixing issue with schedule event package list not paginating properly <jsherril@redhat.com>

* Thu Sep 17 2009 Miroslav Suchý <msuchy@redhat.com> 0.7.6-1
- 523631 - Files in /etc/rhn/default should not be "noreplace"
- fixing broken path in eclipse classpath generation
- 523146 - fix typo in name of column
- 476851 - removal of tables: rhn_db_environment, rhn_environment
- Made hibernate configs use new configs.
- fixing issue where repo_sync tasks would not get removed under certain conditions
- fixing issue where errata cache task was pulling ALL tasks out of the queue and not just the two it actually was using

* Wed Sep 02 2009 Michael Mraka <michael.mraka@redhat.com> 0.7.5-1
- Add symlink capability to config management (joshua.roys@gtri.gatech.edu)

* Tue Sep 01 2009 Michael Mraka <michael.mraka@redhat.com> 0.7.4-1
- 498661 - added missing oracle/monitoring translation

* Tue Sep 01 2009 Michael Mraka <michael.mraka@redhat.com> 0.7.3-1
- moved database specific files to subpackages
- 518227 - missing repo label would result in invalid summary error
- 498009 - kickstart label would not show up on kickstart variables page
- setting the default checksum type for channels to be sha1 instead of sha256
- making RepoSyncTask use the --quiet flag for repo syncing
- new way of waiting on process for RepoSync task.  Hopefully this does not
  bail out after a long time

* Thu Aug 20 2009 jesus m. rodriguez <jesusr@redhat.com> 0.7.2-1
- fix duplicate base channels listed in the "Parent Channel" dropdown (jesusr@redhat.com)
- Log files should be ghosted rather than belonging to a package (m.d.chappell@bath.ac.uk)

* Wed Aug 19 2009 jesus m. rodriguez <jesusr@redhat.com> 0.7.1-1
- add the Chat graphic as an advertisement to the layouts. (jesusr@redhat.com)
- allow users to chat with spacewalk members on IRC via the web.
  (jesusr@redhat.com)
- 518342 - adding workaround for RHEL5u4 bug failing to register when dbus and
  hal are not running (jsherril@redhat.com)
- Checkstyle fix (jason.dobies@redhat.com)
- 518262 - Fixed select all buttons when selecting erratum packages to push to
  a channel. (jason.dobies@redhat.com)
- 516863 - Fix Schedule page date sorting. (dgoodwin@redhat.com)
- adding config option for disabling the ability to access child channel repo
  through kickstart (jsherril@redhat.com)
- adding support for child channel repos during kickstart (jsherril@redhat.com)
- 517567 - fixing issue with ISE with page sort on org trust page
  (jsherril@redhat.com)
- 517551 - fixing issue where a migrated system couldnt provision a guest
  (jsherril@redhat.com)
- unit test (jsherril@redhat.com)
- 517421 - allow shared channels as parents to child channels
  (jesusr@redhat.com)
- 494409 - Update TrustAction to removed shared subscriptions before removing
  trusts (jortel@redhat.com)
- fixing the cloned channel creation to use the original channels checksum type
  and set to db. Once the cloned logic is converted from perl to java we can do
  this more nicely. (pkilambi@redhat.com)
- 509430 - fixing issue where the provisioning tab would ISE on 2.1 systems
  (jsherril@redhat.com)
- 517076 - Added association of servers in the SSM to the package upgrade task
  log. See comment in the code for more information. (jason.dobies@redhat.com)
- 517086 - Added note to indicate the types of SSM tasks to expect to see on
  that page to minimize confusion. (jason.dobies@redhat.com)
- 514305 - switching the algorithm for reading the file into memory.
  (mmccune@redhat.com)
- 517074 - Systems were pulled from the SSM rhnSet without being scoped to a
  specific user ID. Updated the query to take user IDs into account.
  (jason.dobies@redhat.com)
- Fixed typo. (jason.dobies@redhat.com)
- 483606 - Added clause to SSM system retrieval query to filter out proxies.
  (jason.dobies@redhat.com)
- fixing checkstyle (pkilambi@redhat.com)
- fixing unit test breakage (pkilambi@redhat.com)
- 509364 - Fix to show Package Arch name correctly in SSM Package isntall
  (paji@redhat.com)
- 516220 - Fixed bug in SSM query that was looking for systems in any set, not
  just the SSM specific rhnSet. (jason.dobies@redhat.com)
- Reapplying accidentally reverted commit: "Revert "478397 - fixing issue where
  rhnpush would schedule a taskomatic task to regenerate needed cache and was
  using a query that didnt generate for all channels (even though it was
  deleting from all channels)"" (jason.dobies@redhat.com)
- 443500 - Made sure the call to complete the SSM async operation always takes
  place. Added hook to associate servers with the operation.
  (jason.dobies@redhat.com)
- Revert "478397 - fixing issue where rhnpush would schedule a taskomatic task
  to regenerate needed cache and was using a query that didnt generate for all
  channels (even though it was deleting from all channels)"
  (jason.dobies@redhat.com)
- 478397 - fixing issue where rhnpush would schedule a taskomatic task to
  regenerate needed cache and was using a query that didnt generate for all
  channels (even though it was deleting from all channels)
  (jsherril@redhat.com)
- adding reposync task to taskomatic config (jsherril@redhat.com)
- bumping versions to 0.7.0 (jmatthew@redhat.com)

* Wed Aug 05 2009 John Matthews <jmatthew@redhat.com> 0.6.41-1
- 509474 - make sure we symlink to stringtree-json (mmccune@redhat.com)
- 509474 - fixing NPE (joshua.roys@gtri.gatech.edu)
- 509474 - removing un-needed check now that RPM installs this dir
  (mmccune@redhat.com)
- 509474 - adding directory to RPM installation and fixing jsps
  (joshua.roys@gtri.gatech.edu)
- 509474 - switching to exists() check (mmccune@redhat.com)
- 509474 - integration of Joshua's audit feature. (joshua.roys@gtri.gatech.edu)

* Wed Aug 05 2009 Pradeep Kilambi <pkilambi@redhat.com> 0.6.40-1
- Merge branch 'master' of ssh://pkilambi@git.fedorahosted.org/git/spacewalk
  (joshua.roys@gtri.gatech.edu)
- bugfix patch on selinux config file deploy (joshua.roys@gtri.gatech.edu)

* Wed Aug 05 2009 Jan Pazdziora 0.6.39-1
- Fixed unit tests (paji@redhat.com)
- 514291 - Fix for KS by IP (paji@redhat.com)
- enhancing logging mechanism for spacewalk-repo-sync (jsherril@redhat.com)
- 514800 - added logic to check for channel managers per cid
  (shughes@redhat.com)
- 514291 - Fix to properly schedule ssm ks over IP range (paji@redhat.com)
- adding last_boot to system.getDetails() api call, per user request (jlsherri
  @justin-sherrills-macbook-2.local)
- 514994 - added logic to keep channel family name lengh at 128 or lower
  (shughes@redhat.com)
- 514792 - fix spelling error for form var on jsp page (shughes@redhat.com)
- Merge branch 'master' into repo-sync (jsherril@redhat.com)
- Patch: Selinux Context support for config files (joshua.roys@gtri.gatech.edu)
- merge conflict (jsherril@redhat.com)
- 515219 - We can have a channel with null description. In the
  packagedetailsaction we call replace on description  without checking if its
  a valid string resulting in Null Pointer Exception. (pkilambi@redhat.com)
- 496080 - fixing issue where if the rhn tools beta channel was synced, you
  would get an ISE when trying to give the virt entitlement within an org that
  did not have access to that channel (jsherril@redhat.com)
- check style fixes (jsherril@redhat.com)
- 494409 - fix to unsubscribe child channels during trust removal
  (shughes@redhat.com)
- 514591 - fixing issue where empty string being passed in for some values on
  errata.create api would result in ISE 500 (jsherril@redhat.com)
- unit test fixes (jsherril@redhat.com)
- some repo sync task fixes (jsherril@redhat.com)
- updating task to include log file and more logging (jsherril@redhat.com)
- adding sync repo option to channel details, and taskomatic task
  (jsherril@redhat.com)
- 51455, 513683, 514291, 513539 - Fixed a bunch of bugs related to KS
  provisioning. (paji@redhat.com)
- adding repo sync task and other UI bits for spacewalk repo sync
  (jsherril@redhat.com)
- merge conflict (jsherril@redhat.com)
- adding sync repo option to UI for yum repos (jsherril@redhat.com)
- initial yum repo sync schema and UI work (jsherril@redhat.com)

* Tue Jul 28 2009 Pradeep Kilambi <pkilambi@redhat.com> 0.6.38-1
-  Adding a new create channel api using checksumtype as a params.
  (pkilambi@redhat.com)
- 513786 - api - org.create - update api to support pam authentication
  (bbuckingham@redhat.com)

* Mon Jul 27 2009 John Matthews <jmatthew@redhat.com> 0.6.37-1
- 513683 - Added 'link' as a network device option (paji@redhat.com)
- 515539 - Made the cobbler create system record command always delete and
  create a new version of system (paji@redhat.com)
- 510299 & 510785- Fixed issues pertaining to static network and upgrade.
  (paji@redhat.com)

* Thu Jul 23 2009 Pradeep Kilambi <pkilambi@redhat.com> 0.6.35-1
-  Sha256 support for channel creation: (pkilambi@redhat.com)
- checkstyle (mmccune@redhat.com)
- 512814 - unit test fix (mmccune@redhat.com)

* Wed Jul 22 2009 John Matthews <jmatthew@redhat.com> 0.6.34-1
- 512814 - adding spot to add 'upgrade' logic to our startup of tomact.
  (mmccune@redhat.com)

* Tue Jul 21 2009 John Matthews <jmatthew@redhat.com> 0.6.33-1
- 512679 - Fix to guess a sensible default virt path for Xen/KVM virt type
  (paji@redhat.com)
- 510785 - Removed the 'valid' column from the ks profiles list
  (paji@redhat.com)
- 512396 - Cobbler's KS meta can store ints while our code was expecting them
  to be all  strings (paji@redhat.com)
- Fixed unit tests (paji@redhat.com)
- 510785 - Handled an edge case where there are NO valid trees available in KS
  raw mode.. (paji@redhat.com)
- 510785 - Major commit to deal with KS/Distro upgrade scenarios
  (paji@redhat.com)
- 509409 - rewrote package file naming when pushed from proxy
  (shughes@redhat.com)
- 510785 - modifying query to now show profiles on provisioning schedule pages
  if the profiles cobbler id is null (jsherril@redhat.com)
- 512224 - improving handling of invalid network interfaces when adding them to
  cobbler (jsherril@redhat.com)
- 510785 - updating cobbler sync tasks to ignore kickstarts and trees when the
  tree is not able to be synced to cobbler (jsherril@redhat.com)
- 511963 - fixing issue where changing distro  from non-para virt to paravirt
  would not update cobbler objects correctly (or vice-versa)
  (jsherril@redhat.com)
- 510785 - Initial stab on the Invalid KS Distro Base Path issue.
  (paji@redhat.com)
- 508331 - sha256 checksum support for yum repo generation stuff through
  taskomatic. (pkilambi@redhat.com)
- 510329 - Fix SSM package operations UI timeout. (dgoodwin@redhat.com)
- 509589 - fix for org counts (shughes@redhat.com)
- 510299 - Big commit to get static networking to work (paji@redhat.com)
- 509409 - correct package display for rhn_package_manager (shughes@redhat.com)

* Thu Jul 09 2009 John Matthews <jmatthew@redhat.com> 0.6.32-1
- 510122 -  ErrataSearch now filters results so it won't display errata from a
  non-sharing Org (jmatthew@redhat.com)
- 509589 - fixing ise on single default org sys ent page (shughes@redhat.com)
- 509215 - update SDC packages->upgrade to show pkg arch when available
  (bbuckingham@redhat.com)
- checkstyle (jsherril@redhat.com)
- 510334 - Fix the comps.xml timestamp in repomd.xml to compute the timestamp
  value correctly. (pkilambi@redhat.com)
- 510146 - Fix 2002-08 to 2002-09 copyright in non-English resource bundles.
  (dgoodwin@redhat.com)
- 510146 - Update copyright years from 2002-08 to 2002-09.
  (dgoodwin@redhat.com)
- 509268 - Fixed incorrect filterattr values (jason.dobies@redhat.com)
- 509589 - clean up software and system entitlement subscription pages
  (shughes@redhat.com)
- 496174 - removing usage of rhnPrivateErrataMail view and tuning query
  (mmccune@redhat.com)
- 508931 - bumping taskomatic default max memory to 512 and min to 256 to avoid
  OutOfMemoryError's on s390 (pkilambi@redhat.com)
- fix prads oops (shughes@redhat.com)
- 509911 - Dont compute date if the file is missing that way we dont show 1969
  for last build. Also changing the jsp logic to only show as complete if both
  last build and status are not null (pkilambi@redhat.com)
- 509394 - update System/Profile comparison to not display duplicate error
  messages (bbuckingham@redhat.com)
- 508980 - converting SSM kickstart to java (jsherril@redhat.com)
- small request to add orgid for pkilambi (shughes@redhat.com)
- 509457 - incorrectly using user id twice in channel query
  (shughes@redhat.com)
- 509377 - confirmation pgs for Pkg Install & Remove updated to include pkg
  arch (bbuckingham@redhat.com)

* Mon Jul 06 2009 John Matthews <jmatthew@redhat.com> 0.6.30-1
- 509444 - remove delete action system from virt page (shughes@redhat.com)
- 509371 - SSM->Install,Remove,Verify - minor fixes to Package Name and Arch
  (bbuckingham@redhat.com)
- 509411 - make sure we delete the ks template when we delete a profile
  (mmccune@gibson.pdx.redhat.com)
- 509364 - fix SSM->Upgrade arch that being listed (bbuckingham@redhat.com)
- 509376 - add Shared Channels to side navigation of Channels tab
  (bbuckingham@redhat.com)
- 509270 - clarify text on Channels -> All Channels page
  (bbuckingham@redhat.com)
- 509019 - adding tooltip on howto copypaste (mmccune@gibson.pdx.redhat.com)
- 509221 - System->Package->Install incorrectly using arch name vs label
  (bbuckingham@redhat.com)
- 509213 - fixed channel provider column, don't link red hat inc
  (shughes@redhat.com)
- 509027 - kickstart profile edit - update length of supported kernel and post
  kernel options (bbuckingham@redhat.com)
- 509011 - apidoc - kickstart.deleteProfile - update kslabel description
  (bbuckingham@redhat.com)
- refactor config constants to their own class with statics and methods.
  (mmccune@gibson.pdx.redhat.com)
- 509037 - fixing issue where looking for packages in child channels would
  result in base channels (jsherril@redhat.com)
- 508790 - switch to /var/lib/libvirt/images for our default path
  (mmccune@gibson.pdx.redhat.com)
- 508966 - fixed issue where could not set package profile for a kickstart,
  rewrote to new list tag (jsherril@redhat.com)
- 508789 - Block deletion of last remaining Satellite Administrator.
  (dgoodwin@redhat.com)
- Bumping timeout on Message Queue Test. (dgoodwin@redhat.com)
- 508962 - Fixed KS software edit page to hide repo section if tree is not rhel
  5 (paji@redhat.com)
- 508790 - use virbr0 for KVM guest defaults (mmccune@gibson.pdx.redhat.com)
- 508705 - Fixed KS details page to hide virt options if virt type is none
  (paji@redhat.com)
- 508885 - fixed ks schedule pages to remember proxy host (paji@redhat.com)
- Made the radio button in schedule ks page choose scheduleAsap by default
  (paji@redhat.com)
- 508736 - Corrected spec to properly  set the cobbler/snippets/spacewalk
  symlink (paji@redhat.com)
- 508141 - api - system.config.deployAll updated w/ better exception when
  system not config capable (bbuckingham@redhat.com)
- 508323 - fixing issue with creating cobbler system records with spaces (which
  would fail) (jsherril@redhat.com)
- 508220 - fixed channel sharing syntax error on english side
  (shughes@redhat.com)
- Fix API call to remove server custom data value. (dgoodwin@redhat.com)
- ErrataSearch, add "synopsis" to ALL_FIELDS (jmatthew@redhat.com)

* Thu Jun 25 2009 John Matthews <jmatthew@redhat.com> 0.6.29-1
- Remove catch/log return null of HibernateExceptions. (dgoodwin@redhat.com)
- Fix server migration when source org has > 1000 org admins.
  (dgoodwin@redhat.com)
- Fix to make sure kernel param entries don;t get duplicated (paji@redhat.com)
- 492206 - Fixed kickstart template error (paji@redhat.com)
- 507533 - added catch around unhandled exception for pkg in mutiple channels
  (shughes@redhat.com)
- 507862 - Fixed an ise that occured when config deploy was selected on a
  profile (paji@redhat.com)
- 507863 - fixing issue where enabling remote commands would not be saved
  (jsherril@redhat.com)
- 507888 - Set the default virt mem value to 512 instead of 256
  (paji@redhat.com)
- hopeflly fixing unit test (jsherril@redhat.com)
- Fixed a unit test (paji@redhat.com)
- 506702 - Converted probe details page to use the new list to get the correct
  csv (paji@redhat.com)
- Fixed a nitpick that memory didnt sya memMb (paji@redhat.com)
- 507097 - Fixed guest provisioning virt settings (paji@redhat.com)
- Adding repodata details for a given channel to channelDetails page.
  (pkilambi@redhat.com)
- 506816 - fixing issue where virt hosts that begin to use sat 5.3 could not
  install spacewalk-koan (jsherril@redhat.com)
- 506693 - removed more contact.pxt references (shughes@redhat.com)
- 507046 & 507048 - Fixed a couple of cobbler issues (paji@redhat.com)
- Added a fix to master to ignore profiles that have not yet been synced to
  cobbler.. (paji@redhat.com)
- Fix for html:errors and html:messages to be consitently viewed in the UI
  (paji@redhat.com)
- 506726 - do not allow links for null org channel management
  (shughes@redhat.com)
- 506705 - removed invalid rhn require tag (shughes@redhat.com)
- 506693 - remove contact.pxt link from 404 message (shughes@redhat.com)
- 506509 - Fixed an ssm query.. Accidental typo.. (paji@redhat.com)
- 506509 - Fixed ISE on Config Deploy pages (paji@redhat.com)
- Checkstyle fix. (dgoodwin@redhat.com)
- 506608 - fixing issue where source packages could not be downloaded from the
  package details page (jsherril@redhat.com)
- Fix monitoring action unit tests. (dgoodwin@redhat.com)
- Attempt to fix ChannelManagerTest.testListErrata. (dgoodwin@redhat.com)
- 506342 - fix system count for consumed channel sharing (shughes@redhat.com)
- 506341 - fix system count for provided shared channels (shughes@redhat.com)
- 495406 - Changed package arch lookup for ACLs to use arch labels instead of
  hibernate objects. (jason.dobies@redhat.com)
- 506489 - remove the link associated with the org name present in the UI
  header (bbuckingham@redhat.com)
- Adding missed EusReleaseComparator file. (dgoodwin@redhat.com)
- 506492, 506139 - PackageSearch default quick search to searching all arches &
  fix no result if systems aren't registered (jmatthew@redhat.com)
- 506296 - Repair EUS logic after removal of is_default column.
  (dgoodwin@redhat.com)
- 506144 - apidoc - packages.search - adding missing files to return value
  (bbuckingham@redhat.com)
- fix unit test cases (shughes@redhat.com)
- removed a duplicate string resources entry (paji@redhat.com)
- Fix some of the failing EUS unit tests. (dgoodwin@redhat.com)
- 505616 - Fixing the eus logic that gets the latest and the default eus
  channels to not depend on is_default column. Thanks to jsherril for his help
  on this. (pkilambi@redhat.com)
- Fixed a set of unit tests which owere looking for ActtionMessagess instead of
  ActionErrors (paji@redhat.com)
- Unit test fix (paji@redhat.com)
- Fixed unit test: was looking for errors as part of action messages
  (jason.dobies@redhat.com)
- Remove hibernate mappings for rhnReleaseChannelMap is_default column.
  (dgoodwin@redhat.com)
- unit test fix (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)
- 431673 - reworking rhnServerNeededView for performance fixes.
  (mmccune@gmail.com)
- 505170 - api - proxy.deactivateProxy - was generating internal exception
  (bbuckingham@redhat.com)
- 505327 - fixing url parse for advanced kickstart options (shughes@redhat.com)
- 498650 - HTML escape monitoring data before displaying. (dgoodwin@redhat.com)
- Revert "498650 - html escape of monitoring data before displaying on the
  WEBUI" (dgoodwin@redhat.com)
- 498650 - html escape of monitoring data before displaying on the WEBUI
  (tlestach@redhat.com)
- 492206 - Fixed cobbler error url to point to KS file download page which has
  better info on cheetah stacktrace (paji@redhat.com)
- 505188 - fixing issues causing rhel2.1 provisioning to not work
  (jsherril@redhat.com)
- 490960 - ErrataSearch, fix for multiorg channel permissions
  (jmatthew@redhat.com)
- fix to shwo the correct error message css (paji@redhat.com)
- 504804 - Need to stuff the relevant flag back into the request so it's used
  in the package name URLs. (jason.dobies@redhat.com)

* Wed Jun 10 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.26-1
- 504806 - Added missing channel_filter attribute that was being lost during
  pagination. (jason.dobies@redhat.com)
- 487014 - SystemSearch remove score requirement to redirect to SDC on 1 result
  (jmatthew@redhat.com)
- 490770 - Skip and warn if multiple virt channels are found.
  (dgoodwin@redhat.com)
- 503801 - update channel details edit to not refresh package cache
  (bbuckingham@redhat.com)

* Tue Jun 09 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.25-1
- 470991 - spacewalk-java requires jakarta-commons-io and spacewalk-branding.
  (jesusr@redhat.com)
- 501388 - Fixed the guest provisioning side of things also to conform to the
  new UI (paji@redhat.com)
- 501388 - fixing kernel options on profile and scheduling pages to use newer
  CobblerObject based parsing (jsherril@redhat.com)
- 504652 - remove default column from rhnchanneldist map query
  (shughes@redhat.com)
- Update for python 2.5+ (jmatthew@redhat.com)
- 501388 - kernel options and post kernel options redesign (paji@redhat.com)
- Fix to include html:errors wherever html:messages is used so that errors can
  be reported. (paji@redhat.com)
- 504049 - adding functionality to keep the  cobbler profile and system records
  redhat managemnet keys in line with whats set in the Kickstart Profile on
  satellite (jsherril@redhat.com)
- 499471 - list default org in subscription list (shughes@redhat.com)
- 504014 - Fix to show an error message on No Kicktstart tree on KS OS page
  (paji@redhat.com)
- 504227 - apidoc - kickstart handler - add 'none' as a supported virt type
  (bbuckingham@redhat.com)
- 500505 - apidoc - packages.findByNvrea - update docs (bbuckingham@redhat.com)

* Fri Jun 05 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.24-1
- good bye StrutsDelegateImpl and StrutsDelegateFactory (paji@redhat.com)
- 502959 - skip null date values for taskomatic status (shughes@redhat.com)
- Fixed code that would show up even error messages as good messages in the UI
  (paji@redhat.com)
- 504054 - api - errata.getOval - commenting out api (bbuckingham@redhat.com)
- 502941 - Now that 495506 is verified, removing the log message spam.
  (jason.dobies@redhat.com)
- Restore ChannelManager.getLatestPackageEqualInTree. (dgoodwin@redhat.com)
- 484294 - Fix to complain a channel with distros cant be deleted.
  (paji@redhat.com)
- 499399 - api call proxy.createMonitoringScout now return scout shared key
  (msuchy@redhat.com)
- Revert "adding better support for kickstart cent, whereby we install/udpate
  the client packages on all distros and not just RHEL-2,3,4"
  (dgoodwin@redhat.com)
- 499399 - save scout to db (msuchy@redhat.com)
- 504023 - fixing repodata generation to skip solaris custom channels
  (pkilambi@redhat.com)
- 495594, 504012 - Fixed issue where invert flag disappeared on pagination;
  fixed ISE when search produces no results. (jason.dobies@redhat.com)
- 503642 - update KickstartScheduleCommand to store action id after the action
  has been saved to the db (bbuckingham@redhat.com)
- 502905 - fixing issue where non virt kickstarts would show up on virt
  provisioning page (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 502259 - fixing query error that prevented solaris patch clusters from being
  installed (jsherril@redhat.com)
- 503545 - api - system.migrateSystems - update to handle systems that are in a
  system group (bbuckingham@redhat.com)
- 435043 - adding errata sync page for syncing out of date errata (that have
  been updated by red hat) (jsherril@redhat.com)
- 502646 - Fixed list tag filter issue hitting the enter key in IE
  (paji@redhat.com)
- 501224 - api - enhance system.listSystemEvents to include more detail on
  events executed (bbuckingham@redhat.com)
- Made default virt options in a profile configurable and other anomalies
  related to virt options (paji@redhat.com)

* Mon Jun 01 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.23-1
- 496933 - update the errata index when publishing an errata. (jesusr@redhat.com)
- 492206 - Fixed an issue ' bad cobbler template' parsing (paji@redhat.com)
- PackageSearchHandler apidoc cleanup (jmatthew@redhat.com)
- 457316 - Added search for packages in a particular channel. (jason.dobies@redhat.com)
- 502076 - Fixed kickstarting using a system profile (paji@redhat.com)
- 487014 - SystemSearch reducing scrore threshold for a single result to
  redirect to SDC page (jmatthew@redhat.com)
- 501797 - no need to install Monitoring service (msuchy@redhat.com)
- 502923 - Fixed a null pointer that occured on saving non existent xen distro. (paji@redhat.com)
- 490960 - ErrataSearch limit returned results to current or trusted orgs (jmatthew@redhat.com)
- remove todo indicator from code (bbuckingham@redhat.com)
- 501358 - api - channel.software.create - update to provide more detail on
  label/name errors (bbuckingham@redhat.com)
- 499399 - create new api call proxy.createMonitoringScout (msuchy@redhat.com)
- 502848 - adding hooks to better assist automation with the systems channel
  subscription page (jsherril@redhat.com)
- 496105 - Fix for setting up activaiton key for para-host provisioning (paji@redhat.com)
- 498467 - A few changes related to the channel name limit increase. (jason.dobies@redhat.com)
- 502099 - api - update systemgroup.addOrRemoveAdmins to not allow changes to
  access for sat/org admins (bbuckingham@redhat.com)
- Fix tests and actions broken by recent change to set clearing logic. (dgoodwin@redhat.com)
- 472545 - update to the webui translation strings (shughes@redhat.com)
- 502853 - improving support for CentOS by not looking only in the base channel
  for the UPDATE pacakges (jsherril@redhat.com)
- 501387 - adding kernel opts and post kernel opts  to distro edit/create page (jsherril@redhat.com)

* Tue May 26 2009 Devan Goodwin <dgoodwin@redhat.com> 0.6.22-1
- 500366 - ssm pkg verify - fix string in resource bundle
  (bbuckingham@redhat.com)
- 501389 - splitting up virt types none and kvm guests, as well as improving
  virt type names (jsherril@redhat.com)
- 500444 - Clear system set when beginning a new config deploy pageflow.
  (dgoodwin@redhat.com)
- 492902 - Updated a config target systems query to include unprovisioned
  machines (paji@redhat.com)
- 502146 - Added validation to custom system info key label to line up with
  macro argument validation. (jason.dobies@redhat.com)
- 502186 - Added missing resource key for solaris patches
  (jason.dobies@redhat.com)
- adding missing slash on paths (jsherril@redhat.com)
- 502068 - having cobbler distro create/edit/sync use correct kernel and initrd
  for ppc distros (jsherril@redhat.com)
- 457350 - adding api for package search with activation key
  (jmatthew@redhat.com)

* Thu May 21 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.21-1
- cleanup duplicate changelog entry
- 501837 - api - doc - update channel.software.listAllPackages / listAllPackagesByDate returns
  (bbuckingham@redhat.com)
- 500501 - improving message displayed when trying to delete a kickstart (jsherril@redhat.com)

* Thu May 21 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.17-1
- Added a comment to the spec (paji@redhat.com)
- 496254 - now requires commons-io (because of fileupload) (paji@redhat.com)
- 457350 - added api for advanced search filtered by channel (jmatthew@redhat.com)
- 501376 - deprecate system.applyErrata (bbuckingham@redhat.com)
- 457350 - added package search apis to match functionality webui provides (jmatthew@redhat.com)
- 501077 - preferences.locale.setTimeZone - fix signature (bbuckingham@redhat.com)
- 501392 - system.schedulePackageRefresh - fix return docs (bbuckingham@redhat.com)
- fixing issue introduced by the recent rewrite of the profile list on
  provisioning wizard pages (jsherril@redhat.com)
- 501065 - fixing issue where guest provisioning would fail if host had a
  system record (jsherril@redhat.com)
- Fixed a null check while sorting for '' attributes (paji@redhat.com)
- changing download file processing to look in a distro path, if the file is an
  rpm and it is not in the channel (jsherril@redhat.com)
- Fixed sorting to use javascript (paji@redhat.com)
- 500895 - allowing creation of kickstart variables with spaces (jsherril@redhat.com)
- 500719 - Ported delete channel page to Java; success/failure messages now
  properly displayed on manage channels page. (jason.dobies@redhat.com)
- 498251 - add new api proxy.listAvailableProxyChannels (msuchy@redhat.com)
- 497404 - Ported KS schedule page to new list tag (paji@redhat.com)
- SearchServer - refactoring package search-server interactions into a helper class (jmatthew@redhat.com)
- SearchServer - fixes free-form search for Documentation Search (jmatthew@redhat.com)
- SearchServer - Fixing "free form" search.  Adding a boolean flag which when passed (jmatthew@redhat.com)
- Added a Radio Column tag to be used with the New List Tag (paji@redhat.com)
- 251920 - fixed small issue where errata status message after being picked up
  (but before finishing) was still showing as pending (jsherril@redhat.com)
- 501074 - fixing issue where ks profile url option was being generated with
  the entire hostname and not just the path (jsherril@redhat.com)
- checkstyle fix, and changing dates to be localized (jsherril@redhat.com)
- 500499 - fixed issue where task engine times were not displayed, the old perl
  code had been ripped out, so i converted it to java (jsherril@redhat.com)
- 491361 - Added note to error messages to check the log for error messages. (jason.dobies@redhat.com)
- 500891 - fixed an unescaped string on snippets delete confirm page (paji@redhat.com)
- 500887 -Fix to not escape contents in cobbler snippet detials page (paji@redhat.com)
- 5/14 update of webui translation strings (shughes@redhat.com)
- 500727 - Just noticed this was flagged as NOTABUG since we don't want to
  allow this functionality, so removing checkbox. (jason.dobies@redhat.com)
- 491361 - Added ability to pass the --ignore-version-mismatch flag to the
  certificate upload page. (jason.dobies@redhat.com)
- 489902 - add help link to Systems->ActivationKeys (bbuckingham@redhat.com)
- 489902 - fix broken help link on ManageSoftwareChannels pg (bbuckingham@redhat.com)
- Fixed unit tests (paji@redhat.com)
- 432412 - update context help link for Config Mgmt page (bbuckingham@redhat.com)
- 497424 - Slight redesign of the KS Virt UI to deal with duplicate virt paths (paji@redhat.com)
- 500160 - fix precision on org trust details page for date (shughes@redhat.com)
- Fixed incorrect message key (jason.dobies@redhat.com)
- 499980 - Clear the set after adding the packages in case the user hits the
  back button and tries to submit it twice. (jason.dobies@redhat.com)
- 500482 - deprecate kickstart.listKickstartableTrees (bbuckingham@redhat.com)
- 500147 - update update errata list/remove to use advisoryName vs advisory (bbuckingham@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- fixing issue where kickstart file was not written during Cobbler Profile creation (jsherril@redhat.com)
- 500415 - api - deprecating errata.listByDate (bbuckingham@redhat.com)
- 495506 - Added temporary verbose logging in case of failed ACL checks for
  package details page to debug this issue in the next QA build; will remove
  afterwards. (jason.dobies@redhat.com)
- 497119 - channel changes - update to use hibernate refresh vs reload (bbuckingham@redhat.com)
- major cleanup of build files: reformat, remove old targets, etc. (jesusr@redhat.com)
- removing duplicate query and fixing small issue with errata add page (jsherril@redhat.com)
- Added new 'rhn:required-field' tag to help with displayed required fields in UI. (paji@redhat.com)
- 494930 - distros of the same label cannot exist in 2 different orgs fixed (jsherril@redhat.com)
- 500169 - changing cobbler path doesn't change distro kernel and initrd paths (jsherril@redhat.com)
- 472545 - updated  translations strings for java webui (shughes@redhat.com)
- 499537 - removing references to faq links (shughes@redhat.com)
- 499515 - fix ISEs with Solaris patch install/remove and cluster install (bbuckingham@redhat.com)
- Fixed a compile error that occured with 1.5 compilers (paji@redhat.com)
- 499473 - api - added 2 new api calls to org for listing entitlements (bbuckingham@redhat.com)
- 499508 - Removed Run Remote Command buttons from package install/upgrade (jason.dobies@redhat.com)

* Thu May 07 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.16-1
- remove @Override for java 1.5 builds (jesusr@redhat.com)

* Thu May 07 2009 Justin Sherrill <jsherril@redhat.com> 0.6.15-1
- Split log4.properties files into two so taskomatic and tomcat are using different ones 

* Thu May 07 2009 Tomas Lestach <tlestach@redhat.com> 0.6.14-1
- 499038 - channel list doesn't contain non globablly subscribable channels
  (tlestach@redhat.com)

* Wed May 06 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.13-1
- 469937 - Fixed a deactivateProxy issue. (s/reload/refresh) (paji@redhat.com)
- 499258 - update Alter Channel Subscriptions to not ISE when base channel is
  changed (bbuckingham@redhat.com)
- 499037 - fixing issue wher errata cache entires werent being generated if an
  errata publication did not cause packages to be pushed to a channel
  (jsherril@redhat.com)
- 495789 - fixing issue where taskomtaic would create the api log first,
  thereby stopping tomcat from being able to write to it (jsherril@redhat.com)
- 437361 - Added all orgs (except default org) to the entitlement's org subtab.
  (jason.dobies@redhat.com)
- unit test fixes (jlsherri@justin-sherrills-macbook-2.local)
- 499233 - Download CSV link on monitoring page should have the same look as on
  others pages (msuchy@redhat.com)
- unit test fix (jsherril@redhat.com)
- 499258 - update Alter Channel Subscriptions to not ISE when base channel is
  changed (bbuckingham@redhat.com)
- compile fix (jsherril@redhat.com)
- Fixed an accidental removal of a string resource entry (paji@redhat.com)
- Applying changes suggested by zeus (paji@redhat.com)
- 499046 - making it so that pre/post scripts can be templatized or not,
  defaulting to not (jsherril@redhat.com)
- Changed the gen-eclipse script to add things like tools.jar and ant-junit &
  ant.jar (paji@redhat.com)
- 433660 - Removed the restriction in the UI that prevents orgs with 0
  entitlements from being shown on the org page of an entitlement.
  (jason.dobies@redhat.com)

* Mon May 04 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.12-1
- add BuildRequires for jakarta-commons-codec (jesusr@redhat.com)
- remove our requirement on commons-configuration (jesusr@redhat.com)
- 498455 - fixing tooltip for guests alter channel subscription page
  (jsherril@redhat.com)
- fixing junit breakage for ChannelFactoryTest (shughes@redhat.com)
- unit test fix (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)
- fixing unit test by fixing bad hibernate mapping (jsherril@redhat.com)
- unit test fix (jsherril@redhat.com)
- changing junit tests to use joust (jsherril@redhat.com)
- fixing unit test (jsherril@redhat.com)
- 497122 - Fixed error message where no selected organizations would appear as
  a selection error. (jason.dobies@redhat.com)
- 498441 - fixing issue where removing package from a channel didnt regenerate
  repo cache (jsherril@redhat.com)
- 498275 - api - system.obtainReactivationKey updated to replace existing key
  (bbuckingham@redhat.com)

* Thu Apr 30 2009 Tomas Lestach <tlestach@redhat.com> 0.6.10-1
- 454876 - not setting cookie domain (tlestach@redhat.com)
- 497458 - fixing ISE with errata cloning (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 219179 - setting redhat_management_server for the system records like we do
  for server (jsherril@redhat.com)
- 480011 - Added organization to the top header near the username.
  (jason.dobies@redhat.com)
- 497867 - fixed bug in logic after changing hibernate mappings
  (jsherril@redhat.com)
- 497917 - fixing issue where select all did not work on errata list/remove
  packages (jsherril@redhat.com)
- 497867 - fixing reboots taking place even if provisioning fails
  (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 219179 - fixed some issues related to reprovisioning through proxy
  (jsherril@redhat.com)
- 481578 - Ported manage software channels page from perl to java
  (jason.dobies@redhat.com)
- 498208 - cobbler webui string correction (shughes@redhat.com)
- 461704 - clean time_series when deleting a monitoring probe
  (mzazrivec@redhat.com)
- 497925 - we search and replace the cobbler host with proxy
  (mmccune@gmail.com)
- Added code to ensure name is required .... (paji@redhat.com)
- 497872 - skip 'fake' interfaces when looking up system records.
  (mmccune@gmail.com)
- Updated the Kickstart Advanced mode page to include edit area instead of the
  standard text area for uploading kicktstart information.. (paji@redhat.com)
- 497964 - Made the config file create and file details page use edit area..
  Fancy editor... (paji@redhat.com)
- 444221 - Updated the Create/Modify and the delete snippets pages based on
  Mizmo's suggestions (paji@redhat.com)
- 489902 - fix help links to work with rhn-il8n-guides (bbuckingham@redhat.com)
- Checkstyle fixes (jason.dobies@redhat.com)
- 494627 - Added more fine grained error messages for invalid channel data.
  (jason.dobies@redhat.com)
- 485849 - merging RELEASE-5.1 bug into spacewalk (mmccune@gmail.com)
- 496259 - greatly improved errata deletion time (jsherril@redhat.com)
- 444221 - Cobbler Snippet Create page redesign (paji@redhat.com)
- 444221 - Initial improvement on Cobbler Snippets List page based on the bug..
  (paji@redhat.com)

* Fri Apr 24 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.8-1
- removing some debug statements (jsherril@redhat.com)
- 495961 - greatly improving performance of add errata page (jsherril@redhat.com)
- Removed outdated @version requirement (jason.dobies@redhat.com)
- 497119 - support to remove child channel subscriptions from orgs that have
  systems subscribed when denied access to protected channel (shughes@redhat.com)
- 495846 - Oops, missed a file (jason.dobies@redhat.com)
- 495847 - New ListTag 3 functionality to add selected servers to SSM.
  (jason.dobies@redhat.com)
- 497538 - remove shared child channel subscriptions when removing subscription
  from parent (shughes@redhat.com)

* Thu Apr 23 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.7-1
- 496080 - Fix channel with package lookup to filter on org.
  (dgoodwin@redhat.com)

* Wed Apr 22 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.6-1
- 496719 - generate error for invalid keys in input maps (bbuckingham@redhat.com)
- 494976 - adding missing file (jsherril@redhat.com)
- 496303 - 'select all' button fixed on errata list/remove packages page (jsherril@redhat.com)
- 480010 - minor syntax changes to organization channel sharing consumption (shughes@redhat.com)
- Fixed a couple of bugs related to the snippets page. (paji@redhat.com)
- 496272 - Updates/clean up to relogin text. (jason.dobies@redhat.com)
- 496710 - system.listSystemEvents - convert dates in return to use Date (bbuckingham@redhat.com)
- 494976 - adding cobbler system record name usage to reprovisioning (jsherril@redhat.com)
- 495506 - Fixed issue when determining package ACLs. (jason.dobies@redhat.com)
- Removed a couple of needless if statements (paji@redhat.com)
- Added some unit tests for the cobbler snippets (paji@redhat.com)
- 495946 - Rewrite of Cobbler Snippets. (paji@redhat.com)
- 496318 - api - unable to register system using key generated by
  system.obtainReactivationKey (bbuckingham@redhat.com)
- 467063 - Fixed issue where the form variables were reset when the page size
  was changed. (jason.dobies@redhat.com)
- 496666 - apidoc - add some deprecations to the activation key handler
  (bbuckingham@redhat.com)
- 443500 - Changed logic to determine packages to remove to include the
  server's current package information. (jason.dobies@redhat.com)
- 495897 - Fix broken Activated Systems links. (dgoodwin@redhat.com)
- adding fallbackAppender for log4j (jsherril@redhat.com)
- fixing checkstyle and a commit that did not seem to make it related with
  log4j (jsherril@redhat.com)
- 496104 - fixing double slash and downloads with ++ in the filename. (mmccune@gmail.com)
- 495616 - throw permission error if url is modified (jesusr@redhat.com)
- fixing error in specfile after accidental commit of
  d8903258b897c9d6527a1a64b70b8a2610c2e3ce (jsherril@redhat.com)

* Mon Apr 20 2009 Partha Aji <paji@redhat.com> 0.6.5-1
- 495946 - Got a workable edition of cobbler snippets.

* Fri Apr 17 2009 Devan Goodwin <dgoodwin@redhat.com> 0.6.4-1
- 495789 - changing the way apis are logged to fall back to RootAppender if
  there is an error (jsherril@redhat.com)
- logrotate (jsherril@redhat.com)
- 496161 - fixing broken system group links (jsherril@redhat.com)
- 495789 - enabling api logging by default (jsherril@redhat.com)
- 494649 - fix resource bundle text for changing channel to protected
  (bbuckingham@redhat.com)
- 496003 - api - fix system.isNvreInstalled(n,v,r) to properly handle packages
  that have an epoch (bbuckingham@redhat.com)
- 494450 - api - add permissions_mode to ConfigRevisionSerializer & fix doc on
  system.config.createOrUpdatePath (bbuckingham@redhat.com)
- 493163 - fixing ISE when renaming distros and profiles (jsherril@redhat.com)

* Thu Apr 16 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.3-1
- remove Proxy Release Notes link and unused Developer's area. (jesusr@redhat.com)
- 487209 - enhanced system search for hardware devices (jmatthew@redhat.com)
- 450954 - changing reprovisioning to allow reactivation with an activation key
  of a conflicting base channel (jsherril@redhat.com)
- 487185 - Fixed system-search by needed package (jmatthew@redhat.com)
- 494920 - fixing ISE when cloning errata, after channel was cloned
  (jsherril@redhat.com)
- Fix null pointer in scheduleAutoUpdates(). (jortel@redhat.com)
- SystemSearch lowering threshold of a single match to cause a redirect to SDC.
  (jmatthew@redhat.com)
- 495133 - changing send notifications button to populate channel id as well
  (jsherril@redhat.com)
- 495133 - fixing errata mailer such that mails are only sent for a particular
  channel that was changed (jsherril@redhat.com)
- 495065 - channel name appears on private/protected confirm page
  (jesusr@redhat.com)
- 492906 - Fixed spacewalk reference in cobbler config (paji@redhat.com)
- 491130 - improved a kickstart edit page message a little more..
  (paji@redhat.com)
- 491130 - improved a kickstart edit page message.. (paji@redhat.com)
- 494673 - update system migration to support null config channels
  (bbuckingham@redhat.com)
- Clarifying that search must be restarted after running cleanindex
  (jmatthew@redhat.com)
- 487158 - SystemSearch fixed search by customInfo (jmatthew@redhat.com)
- 458205 - Fixed KS Ipranges URL (paji@redhat.com)
- 495786 - fixing issue where some updates were being ignored for RHEL 4
  systems (jsherril@redhat.com)
- 487192 - Fixed system search, search by registration (jmatthew@redhat.com)
- 490904 - change all references to /rhn/help/*/en/ -> /rhn/help/*/en-US/
  (jesusr@redhat.com)
- fix duplicate string resource entry (jesusr@redhat.com)
- 480674 - allow shared channels to appear in act. keys creation
  (jesusr@redhat.com)
- 495585 - fixing Errata Search by Issue Date (jmatthew@redhat.com)
- SystemSearch fix hwdevice result gathering.  Keep highest scoring match per
  system-id (jmatthew@redhat.com)
- 488603 - Fix to deal with blank space interpreter for post scripts
  (paji@redhat.com)
- 234449 - moved block of code to only count real downloads (mmccune@gmail.com)
- 488603 - KickstartFileFormat fix, to deal with blank space interpreter
  (paji@redhat.com)
- 492902 - Fixed 2 queries for Config Target Systems page (paji@redhat.com)
- 486029 - being more consistent with the kickstart label  string
  (jsherril@redhat.com)
- 493163 - fixing ise on update distro page with RHEL 4 distros
  (jsherril@redhat.com)
- 494884 - sub class needs to have protected method to behave as desired
  (jsherril@redhat.com)
- checkstyle fix (jsherril@redhat.com)
- 493647 - Fix for unselect all malfunction... (paji@redhat.com)
- 443500 - Refactored SSM remove packages to only create a single action for
  all servers/packages selected. (jason.dobies@redhat.com)
- 494914 - fix to create a network interface for cobbler system records on
  guest provisioning (jsherril@redhat.com)
- 493718 - minor syntax message change for private channel access
  (shughes@redhat.com)
- 493110 - Changed package installation through SSM to only create one action
  (jason.dobies@redhat.com)
- 494686 - changing it such that you have to provide a virt guest name, not
  letting koan make one (jsherril@redhat.com)
- Fixed the cobbler MockConnection to work with find_* calls (paji@redhat.com)
- api doclet - enhanced to support a 'since' tag, tagged snapshot apis and
  bumped api version (bbuckingham@redhat.com)
- 487566 - fix broken junit in ServerFactoryTest (bbuckingham@redhat.com)
- 442439 - internationalize strings for system search csv export
  (jmatthew@redhat.com)
- 442439 - enhancing csv for systemsearch (jmatthew@redhat.com)
- 494593 - fixing the repofile compare to use the right type for java date
  object obtained through hibernate (pkilambi@redhat.com)
- Updated documentation (jason.dobies@redhat.com)
- 493744 - Added configuration admin ACL to configuration tab
  (jason.dobies@redhat.com)
- 487566 - api/script - initial commit of snapshot script and mods to snapshot
  apis (bbuckingham@redhat.com)
- bumping the protocol version on exporter (pkilambi@redhat.com)
- 492206-Fix for Kickstart Profile Template parse error. (paji@redhat.com)
- 492206-Fix for Kickstart Profile Template parse error. (paji@redhat.com)
- 484435 - add union to query to allow shared child channel subscription access
  (shughes@redhat.com)
- 442439 - system search CSV update to dataset name (jmatthew@redhat.com)
- Removing the last bastions of 1.4 code.. Where logic went like if cobbler
  version < 1.6 do one set else do other wise... (paji@redhat.com)
- Made the configuraiton manager instance static final instead of just static..
  Made no sense for it to be static... (paji@redhat.com)
- 494409 - unsubscribe affected systems after trust removal
  (shughes@redhat.com)
- 494475,460136 - remove faq & feedback code which used customerservice emails.
  (jesusr@redhat.com)
- 487189 -  System Search fixed search by checkin (jmatthew@redhat.com)
- fixing small NPE possibility (jsherril@redhat.com)
- 492949 - setting cobblerXenId appropriately (jsherril@redhat.com)
- 492949 - having CobblerSync task, reuse existing distros if they already
  exist (by name) (jsherril@redhat.com)
- adding single page doclet supporting macros (jsherril@redhat.com)
- 443132 - couple of small fixes for the revamped action pages
  (jsherril@redhat.com)

* Sun Apr 05 2009 jesus m. rodriguez <jesusr@redhat.com> 0.6.2-1
- 470991 - remove unused jar files from taskomatic_daemon.conf (jesusr@redhat.com)
- 437547 - include instructions for regenerating indexes (jmatthew@redhat.com)
- 483611 - Remove search links from YourRhn tasks module (jmatthew@redhat.com)
- 480060 - improve performance of All and Relevant (mmccune@gmail.com)
- 494066 - removed the trailing \n from strings returned from cobbler. (mmccune@gmail.com)
- 489792 - listErrata api docuementation corrected (jsherril@redhat.com)
- 484659 - taskmoatic no longer throws cobbler errors on restart (jsherril@redhat.com)
- 221637 - Removed no-op channels from SSM subscribe config channels (jason.dobies@redhat.com)
- 490866 - distros now properly synced after sat-sync (jsherril@redhat.com)
- 493173 - add redirect in struts config for errata/manage/Delete (bbuckingham@redhat.com)
- 487418 - Added a 'None' option to the available virt type (paji@redhat.com)
- 493187 - Changed empty list message to be a variable and set in calling pages specific to need (published v. unpublished) (jason.dobies@redhat.com)
- fix junit assertion error in testDeleteTreeAndProfiles (bbuckingham@redhat.com)
- 485317 - phantom kickstart sessions no longer show up on kickstart overview (jsherril@redhat.com)

* Thu Apr 02 2009 Devan Goodwin <dgoodwin@redhat.com> 0.6.1-1
- 481130 - Move preun scriptlet to taskomatic subpackage. (dgoodwin@redhat.com)
- 487393 - fixed issue where list count was wrong on provisioning page
  (jsherril@redhat.com)
- 493111 - api - errata.delete added & fixed add/removePackages & setDetails to
  only modify custom errata (bbuckingham@redhat.com)
- 493421 - api - kickstart.tree.deleteTreeAndProfiles fixed to delete
  associated profiles (bbuckingham@redhat.com)
- 487688 - adding text during ks tree creation to explain more detail of what
  is needed (jsherril@redhat.com)
- 462593 - fixing issue where creating or renaming a profile with a name that
  already exists would give ISE (jsherril@redhat.com)
- 492903 - api - channel.software.create - updates so that new channels will
  show on Channel tab (bbuckingham@redhat.com)
- 492980 - api - errata.getDetails - add release, product and solution to
  return and clarify last_modified_date in docs (bbuckingham@redhat.com)
- 458838 - adding new files for kickstart exception 404 (jsherril@redhat.com)
- 490987 - fixed issue where errata files werent being refreshed, by removing
  the need for errata files (jsherril@redhat.com)
- 458838 - changing kickstart download 404s to have a descriptive message
  (jsherril@redhat.com)
- removed jasper5* from run time dependencies and made them build time
  instead. (paji@redhat.com)
- 489532 - unsubscribe multiorg shared channel when moving access from public
  to protected with deny selection (shughes@redhat.com)

* Mon Mar 30 2009 Mike McCune <mmccune@gmail.com> 0.5.44-1
- 472595 - ported query forgot to check child channels
- 144325 - converting system probe list to the new list tag, featuring all the bells and 
  whistles the new list tag has to offer
- 492478 - modifying the system applicable errata page so that you can filter on the 
  type of errata you want to see, also linking a couple of critical errata li
- 467063 - Port of clone errata functionality to new list tag
- 492418 - adding missing channel title when creating new software channels
- 492476 - fixing issue where critical  plus non-critical errata for a system (on the system details page) did not  total errata
- 492146 - fixing issue where system icons are not clickable


* Thu Mar 26 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.41-1
- 437359 - redirect org creation to the orgsystemsubscription page
- 489007 - add system.getConnectionPath for listing proxies a server connected through
- 489736 - generate non-expiring kickstart package download url
- 489736 - download_url_lifetime of 0 disables expiration server wide
- 489736 - can disable expiration by package name by non_expirable_package_urls
- 489486 - added updated message when changing channel access from public to private
- Adding support for comps info to be added to repomd.xml.
- Updated documentation

* Thu Mar 26 2009 Mike McCune <mmccune@gmail.com> 0.5.40-1
- 492137 - fixing ISE for virt 

* Thu Mar 26 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.39-1
- 484852 - user taken to meaningful error pages instead of ISEs.

* Wed Mar 25 2009 Partha Aji <paji@redhat.com> 0.5.38-1
- Added code to take advantage of cobbler 1.6 perf enhancements
- if the customer has that installed.

* Wed Mar 25 2009 Mike McCune <mmccune@gmail.com> 0.5.37-1
- 491978 - fixing status reporting in webui for kickstarts.
- Added resource bundle entries for admin/config/Cobbler.do
- 467063 - Ported published and unpublished errata to new list tag to get new navigation features
- 446269 - fixed issue where you could not remove a package from a system 

* Fri Mar 20 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.36-1
- bring over jta from satellite build.
- fix the jfreechart requires to be 0:1.0.9 everywhere

* Thu Mar 19 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.34-1
- ServerFactory - fix wording in method header
- 486212 - api - added system.deleteCustomValues

* Thu Mar 19 2009 Mike McCune <mmccune@gmail.com> 0.5.33-1
- 474774 - adding jfreechart 1.0 version requires

* Wed Mar 18 2009 Mike McCune <mmccune@gmail.com> 0.5.31-1
- 486186 - Update spacewalk spec files to require cobbler >= 1.4.3

* Thu Mar 12 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.30-1
- fixed iprange delete URLs weren't being correctly rendered
- 480432 - fixed kickstart urls: .../rhn/kickstart/ks/cfg/org/1/org_default
- 489792 - fixing incorrect api return types
- 489775 - fixing listErrata api due to bad query
- 481180 - update KickstartFormatter to use StringUtils on --interpreter check

* Wed Mar 11 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.29-1
- 489760 - used cheetah's #errorCatcher Echo to handle escaping in ks files.
- 249459 - fixing issue where org trust page was busted
- 488137 - refer to cobbler_api instead of cobbler_api_rw to support cobbler >= 1.6
- update deprecated methods in ChannelSoftwareHandler to be more consistent
- 484463 - added more cobbler bits to the kickstart formatter that were missing
- 488830 - api - auth handler - remove the public doc for checkAuthToken
- apidoc generation now ignores an individual call using @xmlrpc.ignore
- added taskomatic task to regenerate deleted kickstart wizard files
- Fixed the ks-setup.py script to function correctly w.r.t space05 changes
- 481180 - do not include --interpreter in profile for scripts without scripting lang
- fix indentations to make it more readable
- Removed code that was getting ignored.
- 489577 - fixing issue that caused taskomatic tracebacks when talking to cobbler
- 489363 - add missing exception class...
- 489363 - api - system.createPackageProfile did not include pkg arch in profile
- 489426 - fixing cloning of kickstarts for regular and raw style
- 489347 - fixing "File Location" field on OS tab to show the --url param
- 483287 - Added ability to do a cobbler sync thru the UI
- adding missing param, for channel name to show up in header
- 483776 - fixing ISE (NPE) on clone errata page
- 462079 - fixed issue where an auto-scheduled errata had name of  "null - null"
- 467265 - fixing issue where errata list was sorting date incorrectly
- fixing package delete to delete from a couple more tables
- 489042 - api - org.setSystemEntitlements - supports setting base entitlements.
- added list of supported entitlements to the api doc
- 488999 - c.s.setUserSubscribable documented value as string while impl
- expected a primitive boolean as input instead of Boolean
- 488148 - test fixes related to bugzilla
- 488148 - use pre-existing system record if there is one.
- 489033 - correcting type of trustOrgId in org.trust.addTrust and removeTrust
- 488990 - api - remove addTrust, removeTrust, listTrusts apis from org handler.
- 488548 - api - org.migrateSystems - fix reactivationkeys, custom info and config
- 488348 - use channel org_id to prevent returning RH channels in addition to custom
- Fixed variable name typo.
 
* Fri Mar 06 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.28-1
- added ExcludeArch: ia64

* Thu Mar 05 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.27-1
- revert commit ba62c229
- changing MockConnection and MockXmlrpcInvoker to handle multiple entities
- 488723 - handling ise for channel packages listing
- 488379 - Syntax error in sql query causing ISE corrected
- 487317 - entitlement verbage change for error message
- 484284 - fixing create/updates messages for custom channel edit actions
- 488622 - api - kickstart.profile.addIpRange updated to validate input
- 487563 - switching take_snapshots to enable_snapshots
- 193788 - converting a few pages to java, so we can sort better
- adding check to looking up cobbler id if its null
- 466195 - apis - rename system.listBaseChannels and system.listChildChannels
- 488277 - remove rhn-highlight from href address
- 485313 - update string to remove extra space
- 484305 - Refactored to keep the package deletion heavy lifting in the DB, avoids OutOfMemoryErrors.
- 480012 - allow sharing org to see shared errata.
- 487234 - fix the query used by the system->software->upgrade page

* Mon Mar 02 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.26-1
- add bcel to BuildRequires

* Fri Feb 27 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.25-1
- Profile rename has been finally fixed
- 469921 - system.scheduleSyncPackagesWithSystems generated a NullPointerException
- fixing mistake in method name
- 485120 - fixed issue where changing org
- name or changing profile name breaks kickstarts (including raw).  Also moved kickstart file location

* Thu Feb 26 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.24-1
- removing listScripts, addScript, removeScript and downloadKickstart APIs from KickstartHandler
- 486749 - Add symlinks for jakarta-commons-collections and jta jars.
- 484942 - "Satellite" is in monitoring schema and have to be translated to product name

* Thu Feb 26 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.23-1
- modifying list tag to not clear set during a select all()
- fixing some issues with converting rhnset to implement set
- Fix to a cobbler rename profile issue...
- making edit command a bit more relaxed if there is no associated cobbler profile
- 486606 - Changed query and page to load/display arch for each package selected
- 487066 - change create link to be lowercase (create new key).
- 482879 - fixing compile error and syncing whenever we update a ksdata
- 482879 - make sure we add all the activation keys to the cobbler profile
- 486982 - fixed ise on software upgrade list
- 480191 - fix query used by systems->software->packages->install
- 487174 - fixing issue where clearing the filter, resulted in the page being submitted
- 241070 - select all on filtered list would select the entire list and not just what was filtered.
- 483555 - Ported to new list tag to get Select All functionality correct when a filter is active.

* Tue Feb 24 2009 Pradeep Kilambi <pkilambi@redhat.com> 0.5.22-1
- fixing the repodata task queries to avoid tempspace issues
 
* Thu Feb 19 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.21-1
- 486502 - Changed order when list a group of systemIds so top result is highest.
- Fixing problem which broke unique documents in the lucene index.
- 486502 - Sort similar results by systemId with highest ID on the bottom
- SystemSearch change redirect behavior if only 1 result is found.

* Thu Feb 19 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.20-1
- 484768 - Basically fixed a query and DTO and a Translator to correctly 
- 486174 - Was using the incorrect key in the filterattr attribute on the
- kickstart session status where ks is syncing to a profile has an correc
- 456315 - refixing this bug, changing kickstart commands to be a Collect
- Changed the hard coded 500 value to BATCH size :)
- 444517 - Added snapshot hook to configuration channel subscription via 
- 485047 - adding back the Task_queries find_channel_in_task_queue query
- 437547, 485313 - Added exception message for when index files are missi
- Adding 'Errata' search to Tasks under YourRhn.do
- 483607 -  Adding documentation as an option to the search bar
- 219844 -  Add 'legend' for Errata Search
- Cleanup, removed commented out code

* Wed Feb 18 2009 Dave Parker <dparker@redhat.com> 0.5.19-1
- 486186 - Update spacewalk spec files to require cobbler >= 1.4.2

* Mon Feb 16 2009 Pradeep Kilambi <pkilambi@redhat.com> 0.5.18-1
- yum repodata regen changes to taskomatic

* Mon Feb 16 2009 Miroslav Suchý <msuchy@redhat.com> 0.5.16-1
- 458355 - show Monitoring tabs only if Monitoring Backend or Monitoring Scout is enabled
- 481766 - Corrected the text on Ks Distribution page to reflect the exact nature of the value to be
- 483796 - fixed bug where ip address would show up as 0
- 469957 - Updated getDetails to use first_name instead of first_names
- 485500 - fixed ISE when deleting errata
- 469957 - Added translation in XMLRPC API layer to accept first_name instead of "first_names"
- handler-manifest.xml used by xmlrpc api was pointing to wrong location for a class...:(
- 466295 - Added date format as description on the property
- Removing duplicate setKickstartTree API

* Thu Feb 12 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.13-1
- 484312 - more cleanup for kickstart AUTO virt type removal
- 484312 - massive cleanup of virt types.  getting rid of useless AUTO type.

* Thu Feb 12 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.12-1
- 484911 - fixed issue where taskomatic won't sync to cobbler newly sat-synced
- Moving SystemDetailsHandler.java and its junit test out of kickstart.profile
- 199560 - Fix epoch being returned as ' ' in channel.software.list_all_package
- 484262 - Updated documentation as per the bz
- 483815 - minor messaging change for custom channel pkg removal
- 452956 - Need to check to make sure the DMI actually contains data before at
- 484435 - needed parent_channel is null when selecting from rhnsharedchannelv
- 480674 - fixed query in Channel.hbm.xml to know about shared channels. Chang
- 485122 - api - kickstart.profile.system.getPartitioningScheme was incorrectl
- 485039 - apidoc - channel.software.removePackages - fix wording on return va
- remove + which hoses the urls in org trusts page

* Wed Feb 11 2009 Dave Parker <dparker@redhat.com> 0.5.11-1
- 484659 remove error messages due to incorrect startup sequences from sysv and from the rhn-satellite tool
* Thu Feb 05 2009 jesus m. rodriguez <jesusr@redhat.com> 0.5.10-1
- Properly run the status through the message bundle for i18n

* Thu Feb 05 2009 Mike McCune <mmccune@gmail.com> 0.5.9-1
- 481767 - be more forgiving of busted kickstart distros during a sync and also report errors in an email.
- 442601 - api - adding access to server lock/unlock
- Restructured to an inversion of control pattern to make it more clear that the mode/summary key are not meant to be attributes.
- 443718 - fixing a view mistage and having a query just use the view
- 483603 - Added details page for listing servers involved in a particular SSM operation
- update the header to 2009 and fix the very annoying whitespace after the *.
- fixing Action classes that have non-final member variables
- 251767 - api - channel.software.setSystemChannels - throw better exception when user passes multiple base channels as input
- 467063 - Added page decorator to allow variable amount of items to be shown
- 437872 - added multiorg messaging suggestion for entitlement warnings
- 483603 - First pass at display of async SSM operations in the UI
- 437563 - adding success message for sat admin toggles
- 479541, 483867 - replaced runuser with /sbin/runuser
- 483603 - Renamed query file; added ability to retrieve servers associated with an operation
- 481200 - api - fix minor issues in apidoc for activationkey apis
- 483689 - api doc updates for channel.software listAllPackages and listAllPackagesByDate apis
- 483806 - updating more iso country codes
- 482929 - fixing messaging with global channel subscriptions per user
- 480016 - adding ID to org details page for information (assist with migration scripts)
- 443718 - improving errata cache calcs when pushing a single errata

* Mon Feb  2 2009 Miroslav Suchý <msuchy@redhat.com> 0.5.8-1
- 480126 - deactivate proxy different way
- 477532 - fixed issue where channels would dissappear after hiding the children

* Fri Jan 30 2009 Mike McCune <mmccune@gmail.com> 0.5.7-1
- removing requirement for spacewalk-branding-jar

* Fri Jan 30 2009 Miroslav Suchý <msuchy@redhat.com> 0.5.6-1
- 483058 - subscribe to proxy channel if requested
- 482923 - splitting out the java branding jar file into its own subpackage
- 459085 - Added (and defaulted) option for Do Nothing
- 469984 - Restructuring to avoid DB hits entirely if there are no channels selected to either subscribe or unsubscribe.

* Wed Jan 28 2009 Miroslav Suchý <msuchy@redhat.com> 0.5.5-1
- 468052 - throw exception if proxy do not has provisioning entitlement
- 481671 - improved the performance of a query
- 469984 - speeding up the bulk channel subscription changes
- 481778 - fix NPE when deleting an unpublished errata
- 480003 - minor grammar change for private channel access
- 428419 - always use the cobbler server when showing URLs for kickstarts
- added ks-setup.py script to add a profile, channel, distro and activation key ..

* Thu Jan 22 2009 Dennis Gilmore <dennis@ausil.us> 0.5.4-1
- update java and java-devel Requires and BuildRequires to 1.6.0

* Wed Jan 21 2009 Devan Goodwin <dgoodwin@redhat.com> 0.5.3-1
- Remove dependency on spacewalk-taskomatic and spacewalk-search.

* Wed Jan 21 2009 Michael Mraka <michael.mraka@redhat.com> 0.5.2-1
- fixed branding stuff

* Tue Jan 20 2009 Mike McCune <mmccune@gmail.com> 0.4.17-1
- 480636 - simplifying the commands vs options into one real collection 
  managed by hibernate vs 2 that both contained the same things

* Thu Jan 15 2009 jesus m. rodriguez <jesusr@redhat.com> 0.4.16-1
- 456467 - Fixed bug where the set of packages to remove was being cleared
- before scheduling

* Wed Jan 14 2009 Mike McCune <mmccune@gmail.com> 0.4.15-1
- 461162 - properly fetch guest name from form

* Tue Jan 13 2009 Mike McCune <mmccune@gmail.com> 0.4.14-1
- 461162 - adding org to system record name
- 461162 - unit test fixes.

* Mon Jan 12 2009 Mike McCune <mmccune@gmail.com> 0.4.12-1
- Boatload of changes from end of 0.4 set of bugs/features

* Tue Jan 06 2009 Mike McCune <mmccune@gmail.com> 0.4.11-1
- Latest spacewalk 0.4 changes.

* Tue Dec 23 2008 Michael Mraka <michael.mraka@redhat.com> 0.4.10-1
- modified layout decorators

* Mon Dec 22 2008 Mike McCune <mmccune@gmail.com> 0.4.9-1
- Adding proper cobbler requirement with version

* Fri Dec 19 2008 Mike McCune <mmccune@gmail.com> 0.4.8-1
- latest changes

* Thu Dec 11 2008 Michael Mraka <michael.mraka@redhat.com> 0.4.7-1
- resolved #471225 - moved rhn-sat-restart-silent to /usr/sbin

* Mon Dec  8 2008 Michael Mraka <michael.mraka@redhat.com> 0.4.6-1
- fixed Obsoletes: rhns-* < 5.3.0

* Fri Dec  5 2008 Michael Mraka <michael.mraka@redhat.com> 0.4.5-1
- removed rhn-oracle-jdbc

* Thu Nov 20 2008 Miroslav Suchy <msuchy@redhat.com> 0.4.2-1
- 472346 - Bump up API version and make the versioning independent on web.version

* Tue Nov  4 2008 Miroslav Suchy <msuchy@redhat.com>
- 461517 - password and db name are swapped

* Fri Oct 31 2008 Jesus M. Rodriguez <jesusr@redhat.com> 0.3.7-1
- 467945 - fixed issue where part of the ssm required you to be an org admin

* Thu Oct 23 2008 Jesus M. Rodriguez <jesusr@redhat.com> 0.3.6-1
- comment the logdriver statements again.
- Fixed some set related issues.
- Updated query to only count outranked channels if the channel
- contains the file.

* Wed Oct 22 2008 Jesus M. Rodriguez <jesusr@redhat.com> 0.3.5-1
- fix stringtree-spec Requires

* Wed Oct 22 2008 Jesus M. Rodriguez <jesusr@redhat.com> 0.3.4-1
- add stringtree-spec (Build)Requires

* Tue Oct 21 2008 Michael Mraka <michael.mraka@redhat.com> 0.3.3-1
- resolves #467717 - fixed sysvinit scripts
- resolves #467877 - use runuser instead of su

* Wed Sep 17 2008 Devan Goodwin <dgoodwin@redhat.com> 0.3.1-1
- Re-version for 0.3.x.
- Add BuildRequires: jsp for RHEL 4.

* Fri Sep  5 2008 Jan Pazdziora 0.2.7-1
- add BuildRequires: javamail, needed on RHEL 4.

* Tue Sep  2 2008 Devan Goodwin <dgoodwin@redhat.com> 0.2.6-1
- Rebuild to include new kickstart profile options.

* Fri Aug 29 2008 Jesus M. Rodriguez <jesusr@redhat.com> 0.2.5-1
- Remove dependency on jsch and ant-jsch.

* Fri Aug 29 2008 Devan Goodwin <dgoodwin@redhat.com> 0.2.4-1
- Remove dependency on bouncycastle and wsdl4j.

* Wed Aug 27 2008 Devan Goodwin <dgoodwin@redhat.com> 0.2.2-1
- Build fix for velocity.jar.

* Tue Aug 26 2008 Devan Goodwin <dgoodwin@redhat.com> 0.2.1-1
- Bumping to 0.2.0.

* Mon Aug 25 2008 Mike McCune 0.2-1
- remove ivy BuildRequires and adding jakarta-commons-cli

* Tue Aug 20 2008 Mike McCune <mmccune@redhat.com> 0.2-1
- more work on rename to spacewalk-java

* Tue Aug  5 2008 Miroslav Suchy <msuchy@redhat.com> 0.2-0
- Renamed to spacewalk-java
- cleanup spec

* Thu May 22 2008 Jan Pazdziora 5.2.0-5
- weaken hibernate3 version requirement

* Fri May 16 2008 Michael Mraka <michael.mraka@redhat.com> 5.2.0-3
- fixed file ownership
- fixed optimizer settings for Oracle 10g

* Thu May 15 2008 Jan Pazdziora - 5.2.0-1
- spec updated for brew builds
