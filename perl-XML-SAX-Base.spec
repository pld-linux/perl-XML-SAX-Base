#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	XML
%define		pnam	SAX-Base
Summary:	XML::SAX::Base - Base class SAX Drivers and Filters
Summary(pl.UTF-8):	XML::SAX::Base - klasa bazowa dla sterowników i filtrów SAX
Name:		perl-XML-SAX-Base
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec347a14065dd7aec7d9fb181b2d7946
URL:		https://metacpan.org/dist/XML-SAX-Base
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Conflicts:	perl-XML-SAX < 0.99
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX::Base is intended for use as a base class for SAX filter
modules and XML parsers generating SAX events.

%description -l pl.UTF-8
Moduł XML::SAX::Base jest przeznaczony do używania jako klasa bazowa
dla modułów filtrów SAX oraz analizatorów XML generujących zdarzenia
SAX.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/XML/SAX
%{perl_vendorlib}/XML/SAX/Base.pm
%{perl_vendorlib}/XML/SAX/Exception.pm
%{perl_vendorlib}/XML/SAX/BuildSAXBase.pl
%{_mandir}/man3/XML::SAX::Base.3pm*
%{_mandir}/man3/XML::SAX::BuildSAXBase.3pm*
%{_mandir}/man3/XML::SAX::Exception.3pm*
