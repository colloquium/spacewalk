# Macros

%define cvs_package scdb_accessor_perl


# Package specific stuff
Name:         %cvs_package
Version:      1.3.0
Release:      1
Packager:     Karen Jacqmin-Adams <kja@redhat.com>
Summary:      NOCpulse SCDB perl client
Source:	      %name-%PACKAGE_VERSION.tar.gz
BuildArch:    noarch
Group:        unsorted
Copyright:    (c) 2001-2003 Red Hat, Inc. All rights reserved.
Vendor:       Red Hat, Inc.
Buildroot:    %{_tmppath}/%cvs_package

%description

perl library for accessing the SCDB

%prep
%entirely_abstract_build_step


%build
echo "Nothing to build"

%install
cd $RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION

%find_perl_installsitelib
perl_lib=$installsitelib/NOCpulse/SCDB

mkdir -p $RPM_BUILD_ROOT$perl_lib
cp NOCpulse/SCDB/Accessor.pm $RPM_BUILD_ROOT$perl_lib

%point_scripts_to_correct_perl
%make_file_list


%files -f %{name}-%{version}-%{release}-filelist

%clean
%abstract_clean_script
