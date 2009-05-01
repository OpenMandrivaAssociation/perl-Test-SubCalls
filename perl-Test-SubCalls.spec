
%define realname   Test-SubCalls
%define version    1.09
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Track the number of times subs are called
Source:     http://www.cpan.org/modules/by-module/Test/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Hook::LexWrap)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
There are a number of different situations (like testing caching code)
where you want to want to do a number of tests, and then verify that some
underlying subroutine deep within the code was called a specific number of
times.

This module provides a number of functions for doing testing in this way in
association with your normal the Test::More manpage (or similar) test
scripts.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*


