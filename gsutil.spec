#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsutil
Version  : 4.64
Release  : 55
URL      : https://files.pythonhosted.org/packages/5b/fa/2a048d4307b2819e9998b4082a9d17d4bf6805aa2fa70422ac8d827f3b8d/gsutil-4.64.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/fa/2a048d4307b2819e9998b4082a9d17d4bf6805aa2fa70422ac8d827f3b8d/gsutil-4.64.tar.gz
Summary  : A command line tool for interacting with cloud storage services.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: gsutil-bin = %{version}-%{release}
Requires: gsutil-license = %{version}-%{release}
Requires: gsutil-python = %{version}-%{release}
Requires: gsutil-python3 = %{version}-%{release}
Requires: PySocks
Requires: PyYAML
Requires: argcomplete
Requires: crcmod
Requires: fasteners
Requires: gcs-oauth2-boto-plugin
Requires: google-apitools
Requires: google-reauth
Requires: httplib2
Requires: httpretty
Requires: monotonic
Requires: paramiko
Requires: pyOpenSSL
Requires: pyasn1
Requires: pyasn1-modules
Requires: python-mock
Requires: requests
Requires: retry_decorator
Requires: rsa
Requires: simplejson
Requires: six
BuildRequires : PySocks
BuildRequires : PyYAML
BuildRequires : argcomplete
BuildRequires : buildreq-distutils3
BuildRequires : crcmod
BuildRequires : fasteners
BuildRequires : gcs-oauth2-boto-plugin
BuildRequires : google-apitools
BuildRequires : google-reauth
BuildRequires : httplib2
BuildRequires : httpretty
BuildRequires : monotonic
BuildRequires : paramiko
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : python-gflags
BuildRequires : python-mock
BuildRequires : requests
BuildRequires : retry_decorator
BuildRequires : rsa
BuildRequires : simplejson
BuildRequires : six
Patch1: 0001-Remove-versioned-dependency-on-python-mock.patch

%description
This directory contains library code used by gsutil. Users are cautioned not
to write programs that call the internal interfaces defined in here; these
interfaces were defined only for use by gsutil, and are subject to change
without notice. Moreover, Google supports this library only when used by
gsutil, not when the library interfaces are called directly by other programs.

%package bin
Summary: bin components for the gsutil package.
Group: Binaries
Requires: gsutil-license = %{version}-%{release}

%description bin
bin components for the gsutil package.


%package license
Summary: license components for the gsutil package.
Group: Default

%description license
license components for the gsutil package.


%package python
Summary: python components for the gsutil package.
Group: Default
Requires: gsutil-python3 = %{version}-%{release}

%description python
python components for the gsutil package.


%package python3
Summary: python3 components for the gsutil package.
Group: Default
Requires: python3-core
Provides: pypi(gsutil)
Requires: pypi(argcomplete)
Requires: pypi(crcmod)
Requires: pypi(fasteners)
Requires: pypi(gcs_oauth2_boto_plugin)
Requires: pypi(google_apitools)
Requires: pypi(google_reauth)
Requires: pypi(httplib2)
Requires: pypi(mock)
Requires: pypi(monotonic)
Requires: pypi(pyopenssl)
Requires: pypi(retry_decorator)
Requires: pypi(six)

%description python3
python3 components for the gsutil package.


%prep
%setup -q -n gsutil-4.64
cd %{_builddir}/gsutil-4.64
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624027263
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gsutil
cp %{_builddir}/gsutil-4.64/LICENSE %{buildroot}/usr/share/package-licenses/gsutil/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/gsutil-4.64/gslib/vendored/boto/LICENSE %{buildroot}/usr/share/package-licenses/gsutil/875c7866415e9e58a4c515bd052d001ac5107943
cp %{_builddir}/gsutil-4.64/gslib/vendored/oauth2client/LICENSE %{buildroot}/usr/share/package-licenses/gsutil/a7b6feb97b476557d3d699fa1f20090fb956d662
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
sitedir=$(python -c "import sys; print(sys.path[-1])")
rm -rfv %{buildroot}/${sitedir}/test
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsutil

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gsutil/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/gsutil/875c7866415e9e58a4c515bd052d001ac5107943
/usr/share/package-licenses/gsutil/a7b6feb97b476557d3d699fa1f20090fb956d662

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
