# Macros

%define cvs_package PerlModules/NP/Spread

# Package specific stuff
Name:         NOCpulse-Spread
Version:      1.10.0
Release:      1
Packager:     Karen Jacqmin-Adams <kja@redhat.com>
Summary:      %{name} network utilities
Source:	      %{name}-%PACKAGE_VERSION.tar.gz
BuildArch:    noarch
Group:        unsorted
Copyright:    (c) 2002-2003 Red Hat, Inc. All rights reserved.
Vendor:       Red Hat, Inc.
Buildroot:    %{_tmppath}/%cvs_package
Prefix:       %{_our_prefix}

%description

NOCpulse-Spread provides NP authored libraries and utilities for the
Spread network.

%prep
%entirely_abstract_build_step

%build
echo "Nothing to build"

%install
cd $RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION

%find_perl_installsitelib

mkdir -p $RPM_BUILD_ROOT$installsitelib/NOCpulse

cp SpreadNetwork.pm $RPM_BUILD_ROOT$installsitelib/NOCpulse
cp SpreadServers.pm $RPM_BUILD_ROOT$installsitelib/NOCpulse
cp Filters.pm $RPM_BUILD_ROOT$installsitelib/NOCpulse

%point_scripts_to_correct_perl

%make_file_list

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root,-)


%clean

%abstract_clean_script
