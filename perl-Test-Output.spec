#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Output
Summary:	Test::Output - Utilities to test STDOUT and STDERR messages
Summary(pl.UTF-8):	Test::Output - narzędzia do terowania komunikatów STDOUT i STDERR
Name:		perl-Test-Output
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	903485edb382f5a18a5029978d1febf6
URL:		http://search.cpan.org/dist/Test-Output/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Capture-Tiny >= 0.17
BuildRequires:	perl-File-Temp >= 0.21
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Tester >= 0.107
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Output provides a simple interface for testing output sent to
STDOUT or STDERR. A number of different utilies are included to try
and be as flexible as possible to the tester.

%description -l pl.UTF-8
Test::Output udostępnia prosty interfejs do testowania komunikatów
wysyłanych na STDOUT lub STDERR. Załączonych jest wiele różnych
narzędzi do wypróbowania, mających być jak najbardziej elastycznymi
dla testera.

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
%{perl_vendorlib}/Test/Output.pm
%{_mandir}/man3/Test::Output.3pm*
