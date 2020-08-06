Name:      goto-ups-server
Version:   2.1.2
Release:   0
Url:       https://github.com/warwick-one-metre/gotoupsd
Summary:   Pyro frontend for monitoring the GOTO UPSes via SNMP.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-power
Requires:  observatory-log-client, net-snmp-utils, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

gotoupsd is a Pyro frontend for monitoring the GOTO UPSes via SNMP.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/gotoupsd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/gotoupsd.service %{buildroot}%{_unitdir}

%post
%systemd_post gotoupsd.service

%preun
%systemd_preun gotoupsd.service

%postun
%systemd_postun_with_restart gotoupsd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/gotoupsd
%defattr(-,root,root,-)
%{_unitdir}/gotoupsd.service

%changelog
