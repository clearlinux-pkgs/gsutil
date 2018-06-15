#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsutil
Version  : 4.28
Release  : 21
URL      : https://pypi.debian.net/gsutil/gsutil-4.28.tar.gz
Source0  : https://pypi.debian.net/gsutil/gsutil-4.28.tar.gz
Summary  : A command line tool for interacting with cloud storage services.
Group    : Development/Tools
License  : Apache-2.0
Requires: gsutil-bin
Requires: gsutil-python3
Requires: gsutil-python
Requires: SocksiPy-branch
Requires: argcomplete
Requires: boto
Requires: crcmod
Requires: gcs-oauth2-boto-plugin
Requires: google-apitools
Requires: httplib2
Requires: oauth2client
Requires: pyOpenSSL
Requires: python-gflags
Requires: retry_decorator
Requires: six
BuildRequires : SocksiPy-branch
BuildRequires : crcmod
BuildRequires : gcs-oauth2-boto-plugin
BuildRequires : google-apitools
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python-gflags
BuildRequires : python3-dev
BuildRequires : retry_decorator
BuildRequires : setuptools
Patch1: versions.patch

%description
gsutil is a Python application that lets you access Google Cloud Storage from
        the command line. You can use gsutil to do a wide range of bucket and object

%package bin
Summary: bin components for the gsutil package.
Group: Binaries

%description bin
bin components for the gsutil package.


%package python
Summary: python components for the gsutil package.
Group: Default
Requires: gsutil-python3

%description python
python components for the gsutil package.


%package python3
Summary: python3 components for the gsutil package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gsutil package.


%prep
%setup -q -n gsutil-4.28
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528564569
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsutil

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
