#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : absl-py
Version  : 0.4.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/a7/86/67f55488ec68982270142c340cd23cd2408835dc4b24bd1d1f1e114f24c3/absl-py-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a7/86/67f55488ec68982270142c340cd23cd2408835dc4b24bd1d1f1e114f24c3/absl-py-0.4.1.tar.gz
Summary  : Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
Group    : Development/Tools
License  : Apache-2.0
Requires: absl-py-python3
Requires: absl-py-python
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
This repository is a collection of Python library code for building Python
        applications. The code is collected from Google's own Python code base, and has
        been extensively tested and used in production.
        
        ## Features
        
        * Simple application startup
        * Distributed commandline flags system
        * Custom logging module with additional features
        * Testing utilities
        
        ## Getting Started
        
        ### Installation

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
%setup -q -n absl-py-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535549082
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
