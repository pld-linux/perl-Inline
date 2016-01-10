%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
Summary:	Inline Perl module - write Perl subroutines in other programming languages
Summary(pl.UTF-8):	Moduł Perla Inline - tworzenie funkcji perlowych w innych językach programowania
Name:		perl-Inline
Version:	0.80
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{version}.tar.gz
# Source0-md5:	510bbac46e727bcaf240b7feac2646c9
URL:		http://search.cpan.org/dist/Inline/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-Parse-RecDescent >= 1.80
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Warn >= 0.23
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n %{pdir}-%{version}

%{__mv} lib/Inline/MakeMaker/Changes Changes.Inline_MakeMaker

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
%doc Changes Changes.Inline_MakeMaker README
%{perl_vendorlib}/Inline.pm
%{perl_vendorlib}/Inline/denter.pm
%{perl_vendorlib}/Inline/Foo.pm
%{perl_vendorlib}/Inline/MakeMaker.pm
%{_mandir}/man3/Inline.3pm*
%{_mandir}/man3/Inline::API.3pm*
%{_mandir}/man3/Inline::FAQ.3pm*
%{_mandir}/man3/Inline::Support.3pm*
