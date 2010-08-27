%define upstream_name    Perl-Critic-Compatibility
%define upstream_version 1.001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Don't allow three-argument open unless the code uses a version of perl that supports it
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The included policies are:

* the Perl::Critic::Policy::Compatibility::ProhibitColonsInBarewordHashKeys
  manpage

  Perls after 5.8 don't support having colons in unquoted hash keys.
  [Severity: 5]

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
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


