%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
Summary:	Inline perl module
Summary(pl):	Modu³ perla Inline
Name:		perl-Inline
Version:	0.43
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-Parse-RecDescent >= 1.78
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
Requires:	%{name} = %{version}
Requires:	gcc

%description C
Inline::C - Write Perl subroutines in C.

%description C -l pl
Modu³ Inline::C - pozwalaj±cy pisaæ funkcje Perla w C.

%prep
%setup -q -n %{pdir}-%{version}

%build
echo "y" | perl Makefile.PL
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
%{perl_sitelib}/Inline.pm
%{perl_sitelib}/Inline/denter.pm
%{perl_sitelib}/Inline/Foo.pm
%{perl_sitelib}/Inline/MakeMaker.pm
%{perl_sitelib}/auto/Inline
%{_mandir}/man3/Inline.3pm*
%{_mandir}/man3/Inline-*.3pm*

%files C
%defattr(644,root,root,755)
%doc C/Changes C/README
%{perl_sitelib}/Inline/C.pm
%{perl_sitelib}/Inline/C
%{_mandir}/man3/Inline::C*.3pm*
