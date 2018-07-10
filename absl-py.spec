#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : absl-py
Version  : 0.1.13
Release  : 16
URL      : https://pypi.python.org/packages/f4/bc/b19223874bf38e1f5ae6d1297b56cf87838985e87a96488c3058a8677bd3/absl-py-0.1.13.tar.gz
Source0  : https://pypi.python.org/packages/f4/bc/b19223874bf38e1f5ae6d1297b56cf87838985e87a96488c3058a8677bd3/absl-py-0.1.13.tar.gz
Summary  : Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
Group    : Development/Tools
License  : Apache-2.0
Requires: absl-py-python3
Requires: absl-py-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
# Abseil Python Common Libraries
This repository is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

%package python
Summary: python components for the absl-py package.
Group: Default
Requires: absl-py-python3

%description python
python components for the absl-py package.


%package python3
Summary: python3 components for the absl-py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the absl-py package.


%prep
%setup -q -n absl-py-0.1.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529089843
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
