#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Output
Summary:	Test::Output - Utilities to test STDOUT and STDERR messages.
#Summary(pl):	
Name:		perl-Test-Output
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dcf67296e04a41a9f73f70c10fe5f825
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Tester) >= 0.103
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Output provides a simple interface for testing output sent to STDOUT
or STDERR. A number of different utilies are included to try and be as
flexible as possible to the tester.

Originally this module was designed not to have external requirements, 
however, the features provided by Sub::Exporter over what Exporter
provides is just to great to pass up.

Test::Output ties STDOUT and STDERR using Test::Output::Tie.


# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%dir %{perl_vendorlib}/Test/Output
%{perl_vendorlib}/Test/Output/Tie.pm
%{_mandir}/man3/*
