%define upstream_name    Perl-Critic-Compatibility
%define upstream_version 1.001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Don't allow three-argument open unless version of perl supports it
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The included policies are:

* the Perl::Critic::Policy::Compatibility::ProhibitColonsInBarewordHashKeys
  manpage

  Perls after 5.8 don't support having colons in unquoted hash keys.
  [Severity: 5]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.1.0-2mdv2011.0
+ Revision: 655607
- rebuild for updated spec-helper

* Fri Aug 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 573474
- import perl-Perl-Critic-Compatibility

