%define upstream_name    Date-Pcalc
%define upstream_version 6.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Pure-Perl drop-in replacement for Date::Calc
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Bit::Vector)
BuildRequires: perl(Carp::Clan)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
* *

  'use Date::Pcalc qw( Days_in_Year Days_in_Month ... );'

* *

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


