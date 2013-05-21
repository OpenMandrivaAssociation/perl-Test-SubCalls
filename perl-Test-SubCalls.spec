%define upstream_name    Test-SubCalls
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Track the number of times subs are called
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Hook::LexWrap)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
There are a number of different situations (like testing caching code)
where you want to want to do a number of tests, and then verify that some
underlying subroutine deep within the code was called a specific number of
times.

This module provides a number of functions for doing testing in this way in
association with your normal the Test::More manpage (or similar) test
scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-5mdv2012.0
+ Revision: 765750
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-4
+ Revision: 764255
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-3
+ Revision: 676845
- rebuild

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.90.0-2
+ Revision: 658458
- rebuild for updates rpm-setup

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 401518
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.09-1mdv2010.0
+ Revision: 369785
- update to new version 1.09

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 1.08-1mdv2009.1
+ Revision: 329107
- import perl-Test-SubCalls


* Tue Jan 13 2009 cpan2dist 1.08-1mdv
- initial mdv release, generated with cpan2dist

