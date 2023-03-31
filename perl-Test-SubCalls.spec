%define modname	Test-SubCalls
%define modver	1.10

Summary:	Track the number of times subs are called
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(inc::Module::Install::DSL)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Hook::LexWrap)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
There are a number of different situations (like testing caching code)
where you want to want to do a number of tests, and then verify that some
underlying subroutine deep within the code was called a specific number of
times.

This module provides a number of functions for doing testing in this way in
association with your normal the Test::More manpage (or similar) test
scripts.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

