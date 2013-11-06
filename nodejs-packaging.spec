%define debug_package %{nil}
%define _rpmconfigdir %{_prefix}/lib/rpm

%define dist %{expand:%%(/usr/lib/rpm/redhat/dist.sh --dist)}

Name:           nodejs-packaging
Version:        4
Release:        3.ptin%{?dist}
Summary:        RPM Macros and Utilities for Node.js Packaging
BuildArch:      noarch
Group:         Development/Libraries
License:        MIT
URL:            https://fedoraproject.org/wiki/Node.js/Packagers
Source0:        https://fedorahosted.org/released/%{name}/%{name}-el6-%{version}.tar.xz
Patch0: python24.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{rpm_name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
#ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

#nodejs-devel before 0.10.12 provided these macros and owned /usr/share/node
Requires:       nodejs(engine) >= 0.10.12
Requires:       redhat-rpm-config, python, python-simplejson

#%global debug_package %{nil}

%description
This package contains RPM macros and other utilities useful for packaging
Node.js modules and applications in RPM-based distributions.

%prep
%setup -qn %{name}-el6-%{version}
%patch0 -p1

%build
#nothing to do

%install
install -Dpm0644 macros.nodejs %{buildroot}%{_sysconfdir}/rpm/macros.nodejs
install -Dpm0755 nodejs.prov %{buildroot}%{_rpmconfigdir}/nodejs.prov
install -pm0755 nodejs.req %{buildroot}%{_rpmconfigdir}/nodejs.req
install -pm0755 nodejs-symlink-deps %{buildroot}%{_rpmconfigdir}/nodejs-symlink-deps
install -pm0755 nodejs-fixdep %{buildroot}%{_rpmconfigdir}/nodejs-fixdep
install -Dpm0644 multiver_modules %{buildroot}%{_datadir}/node/multiver_modules

%files
%{_sysconfdir}/rpm/macros.nodejs
%{_rpmconfigdir}/nodejs*
%{_datadir}/node/multiver_modules
%doc LICENSE

%changelog
* Wed Nov  6 2013 Sergio Freire <sergio-s-freire@ptinovacao.pt> - 4-3.ptin
- added missing dependency of python-simplejson
* Wed Nov  6 2013 Sergio Freire <sergio-s-freire@ptinovacao.pt> - 4-2.ptin
- made it compatible with Python 2.4 and RHEL5
* Mon Jul 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4-1
- handle cases where the symlink target exists gracefully

* Wed Jul 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3-1
- dependencies and engines can be lists or strings too
- handle unversioned dependencies on multiply versioned modules correctly
  (RHBZ#982798)
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2-1
- move multiple version list to /usr/share/node
- bump nodejs Requires to 0.10.12
- add Requires: redhat-rpm-config

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1-1
- initial package
