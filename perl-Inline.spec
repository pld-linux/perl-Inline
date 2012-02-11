%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
Summary:	Inline Perl module - write Perl subroutines in other programming languages
Summary(pl.UTF-8):	Moduł Perla Inline - tworzenie funkcji perlowych w innych językach programowania
Name:		perl-Inline
Version:	0.50
Release:	1
Epoch:		1
# same as perl (but C-Cookbook is Artistic-only)
License:	GPL v1+ (except C-Cookbook) or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{version}.tar.gz
# Source0-md5:	cb9377b494819924bddf2de20c90f3ab
URL:		http://search.cpan.org/dist/Inline/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-Parse-RecDescent >= 1.78
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# false requires found by rpm
%define		_noautoreq	'perl(of)'

%description
The Inline module allows you to put source code from other programming
languages directly "inline" in a Perl script or module. The code is
automatically compiled as needed, and then loaded for immediate access
from Perl.

%description -l pl.UTF-8
Moduł Inline pozwala umieszczać kod źródłowy w innych językach
programowania bezpośrednio wewnątrz skryptu lub modułu perlowego. Kod
jest w razie potrzeby automatycznie kompilowany, a następnie ładowany
w celu bezpośredniego dostępu z poziomu Perla.

%package C
Summary:	Inline::C Perl module - write Perl subroutines in C
Summary(pl.UTF-8):	Moduł Perla Inline::C - tworzenie funkcji Perla w C
Group:		Development/Languages/Perl
License:	Artistic
Requires:	%{name} = %{epoch}:%{version}
Requires:	gcc

%description C
Inline::C is a module that allows you to write Perl subroutines in C.

%description C -l pl.UTF-8
Inline::C to moduł pozwalający pisać funkcje Perla w C.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/*.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Inline/*.pod

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
