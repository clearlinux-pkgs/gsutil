#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsutil
Version  : 4.37
Release  : 45
URL      : https://files.pythonhosted.org/packages/c9/86/b2eef9a5e677ec7f5e512bb0de6278cb041b87b266942900c3c67137d307/gsutil-4.37.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/86/b2eef9a5e677ec7f5e512bb0de6278cb041b87b266942900c3c67137d307/gsutil-4.37.tar.gz
Summary  : A command line tool for interacting with cloud storage services.
Group    : Development/Tools
License  : Apache-2.0
Requires: gsutil-bin = %{version}-%{release}
Requires: gsutil-license = %{version}-%{release}
Requires: gsutil-python = %{version}-%{release}
Requires: gsutil-python3 = %{version}-%{release}
Requires: PySocks
Requires: argcomplete
Requires: boto
Requires: crcmod
Requires: fasteners
Requires: gcs-oauth2-boto-plugin
Requires: google-apitools
Requires: google-reauth
Requires: httplib2
Requires: monotonic
Requires: oauth2client
Requires: pyOpenSSL
Requires: python-gflags
Requires: python-mock
Requires: retry_decorator
Requires: six
BuildRequires : PySocks
BuildRequires : argcomplete
BuildRequires : boto
BuildRequires : buildreq-distutils3
BuildRequires : crcmod
BuildRequires : fasteners
BuildRequires : gcs-oauth2-boto-plugin
BuildRequires : google-apitools
BuildRequires : google-reauth
BuildRequires : httplib2
BuildRequires : monotonic
BuildRequires : oauth2client
BuildRequires : pyOpenSSL
BuildRequires : python-gflags
BuildRequires : python-mock
BuildRequires : retry_decorator
BuildRequires : six
Patch1: 0001-Force-use-of-PySocks.patch
Patch2: 0002-Remove-versioned-dependency-on-python-mock.patch

%description
gsutil is a Python application that lets you access Google Cloud Storage from
        the command line. You can use gsutil to do a wide range of bucket and object

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
Requires: pypi(oauth2client)
Requires: pypi(pyopenssl)
Requires: pypi(retry_decorator)
Requires: pypi(six)

%description python3
python3 components for the gsutil package.


%prep
%setup -q -n gsutil-4.37
cd %{_builddir}/gsutil-4.37
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587770797
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
cp %{_builddir}/gsutil-4.37/LICENSE %{buildroot}/usr/share/package-licenses/gsutil/2b8b815229aa8a61e483fb4ba0588b8b6c491890
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
