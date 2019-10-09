#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : absl-py
Version  : 0.8.1
Release  : 30
URL      : https://files.pythonhosted.org/packages/3b/72/e6e483e2db953c11efa44ee21c5fdb6505c4dffa447b4263ca8af6676b62/absl-py-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/72/e6e483e2db953c11efa44ee21c5fdb6505c4dffa447b4263ca8af6676b62/absl-py-0.8.1.tar.gz
Summary  : Abseil Python Common Libraries
Group    : Development/Tools
License  : Apache-2.0
Requires: absl-py-license = %{version}-%{release}
Requires: absl-py-python = %{version}-%{release}
Requires: absl-py-python3 = %{version}-%{release}
Requires: enum34
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : enum34
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

%description python3
python3 components for the absl-py package.


%prep
%setup -q -n absl-py-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570638995
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
cp LICENSE %{buildroot}/usr/share/package-licenses/absl-py/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/absl-py/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
