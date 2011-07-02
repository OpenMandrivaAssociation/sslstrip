%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           sslstrip
Version:        0.9
Release:        %mkrel 1
Summary:        Tool that provides a demonstration of HTTPS stripping attacks
Group:          System/Servers
License:        GPLv3+
URL:            http://www.thoughtcrime.org/software/sslstrip/
Source0:        http://www.thoughtcrime.org/software/sslstrip/%{name}-%{version}.tar.gz
#Patch0:         sslstrip0.7-version_num.patch
#Patch1:         sslstrip0.7-version_num-setuppy.patch

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch

BuildRequires:  python >= 2.5
Requires:       python-twisted-web

%description
Tool that provides a demonstration of HTTPS stripping attacks that were 
presented at Black Hat DC 2009 by Moxie Marlinspike. It will transparently 
hijack HTTP traffic on a network, watch for HTTPS links and redirects, then map 
those links into either look-alike HTTP links or homograph-similar HTTPS links.
It also supports modes for supplying a favicon which looks like a lock icon, 
selective logging, and session denial

%prep
%setup -q

# Patch out the incorrect version in both the setup.py and main source file
##fixed in 0.9 upstream release
#patch0
#patch1

# Make COPYING and README not executable
chmod -x COPYING
chmod -x README

%build
python setup.py build

%install
python setup.py install --root $RPM_BUILD_ROOT

# Remove duplicate doc files
rm $RPM_BUILD_ROOT/usr/share/%{name}/README
rm $RPM_BUILD_ROOT/usr/share/%{name}/COPYING


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/*.py
#{python_sitelib}/%{name}/*.pyc
#{python_sitelib}/%{name}/*.pyo
%{python_sitelib}/*.egg-info
%{_datadir}/%{name}/*
%{_bindir}/%{name}

