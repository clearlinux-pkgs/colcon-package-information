#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-package-information
Version  : 0.2.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/2d/34/3571034051350571b4c885258ddb9b600ddd6abcd8cf94799f314e97a961/colcon-package-information-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/2d/34/3571034051350571b4c885258ddb9b600ddd6abcd8cf94799f314e97a961/colcon-package-information-0.2.2.tar.gz
Summary  : Extension for colcon to output package information.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-package-information-python = %{version}-%{release}
Requires: colcon-package-information-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3

%description
colcon-package-information
==========================
An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to provide information about the packages.

%package python
Summary: python components for the colcon-package-information package.
Group: Default
Requires: colcon-package-information-python3 = %{version}-%{release}

%description python
python components for the colcon-package-information package.


%package python3
Summary: python3 components for the colcon-package-information package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-package-information package.


%prep
%setup -q -n colcon-package-information-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547690445
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
