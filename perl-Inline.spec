%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
Summary:	Inline perl module
Summary(pl):	Modu³ perla Inline
Name:		perl-Inline
Version:	0.44
Release:	2
Epoch:		1
# same as perl (but C-Cookbook is Artistic-only)
License:	GPL v1+ (except C-Cookbook) or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	840f47d9b6cef39e68370faf9dceab2c
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-Parse-RecDescent >= 1.78
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# false requires found by rpm
%define		_noautoreq	'perl(of)'

%description
Inline.pm - Write Perl subroutines in other programming languages.

%description -l pl
Modu³ Inline.pm - pozwala tworzyæ procedury Perla w innych jêzykach
programowania.

%package C
Summary:	Inline::C perl module
Summary(pl):	Modu³ perla Inline::C
Group:		Development/Languages/Perl
License:	Artistic
Requires:	%{name} = %{epoch}:%{version}
Requires:	gcc

%description C
Inline::C - Write Perl subroutines in C.

%description C -l pl
Modu³ Inline::C - pozwalaj±cy pisaæ funkcje Perla w C.

%prep
%setup -q -n %{pdir}-%{version}

%build
echo "y" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline.pm
%{perl_vendorlib}/Inline/denter.pm
%{perl_vendorlib}/Inline/Foo.pm
%{perl_vendorlib}/Inline/MakeMaker.pm
%{perl_vendorlib}/auto/Inline
%{_mandir}/man3/Inline.3pm*
%{_mandir}/man3/Inline-*.3pm*

%files C
%defattr(644,root,root,755)
%doc C/Changes C/README
%{perl_vendorlib}/Inline/C.pm
%{perl_vendorlib}/Inline/C
%{_mandir}/man3/Inline::C*.3pm*
