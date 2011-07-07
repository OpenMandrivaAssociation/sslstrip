%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           sslstrip
Version:        0.9
Release:        %mkrel 2
Summary:        Tool that provides a demonstration of HTTPS stripping attacks
Group:          Monitoring
License:        GPLv3+
URL:            http://www.thoughtcrime.org/software/sslstrip/
Source0:        http://www.thoughtcrime.org/software/sslstrip/%{name}-%{version}.tar.gz
BuildRequires:  python >= 2.5
Requires:       python-twisted-web
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Tool that provides a demonstration of HTTPS stripping attacks that were 
presented at Black Hat DC 2009 by Moxie Marlinspike. It will transparently 
hijack HTTP traffic on a network, watch for HTTPS links and redirects, then map 
those links into either look-alike HTTP links or homograph-similar HTTPS links.
It also supports modes for supplying a favicon which looks like a lock icon, 
selective logging, and session denial

%prep
%setup -q

# Make COPYING and README not executable
chmod -x COPYING
chmod -x README

%build
python setup.py build

%install
python setup.py install --root %{buildroot}

# Remove duplicate doc files
rm %{buildroot}/usr/share/%{name}/README
rm %{buildroot}/usr/share/%{name}/COPYING

%clean
rm -rf %{buildroot}

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

