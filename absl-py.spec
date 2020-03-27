#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : absl-py
Version  : 0.9.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/1a/53/9243c600e047bd4c3df9e69cfabc1e8004a82cac2e0c484580a78a94ba2a/absl-py-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1a/53/9243c600e047bd4c3df9e69cfabc1e8004a82cac2e0c484580a78a94ba2a/absl-py-0.9.0.tar.gz
Summary  : Abseil Python Common Libraries
Group    : Development/Tools
License  : Apache-2.0
Requires: absl-py-license = %{version}-%{release}
Requires: absl-py-python = %{version}-%{release}
Requires: absl-py-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
# Abseil Python Common Libraries
This repository is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

%package license
Summary: license components for the absl-py package.
Group: Default

%description license
license components for the absl-py package.


%package python
Summary: python components for the absl-py package.
Group: Default
Requires: absl-py-python3 = %{version}-%{release}

%description python
python components for the absl-py package.


%package python3
Summary: python3 components for the absl-py package.
Group: Default
Requires: python3-core
Provides: pypi(absl_py)
Requires: pypi(six)

%description python3
python3 components for the absl-py package.


%prep
%setup -q -n absl-py-0.9.0
cd %{_builddir}/absl-py-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585319246
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/absl-py
cp %{_builddir}/absl-py-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/absl-py/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/absl-py/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
