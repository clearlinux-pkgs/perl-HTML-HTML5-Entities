#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-HTML5-Entities
Version  : 0.004
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Entities-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Entities-0.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-html5-entities-perl/libhtml-html5-entities-perl_0.004-1.debian.tar.xz
Summary  : 'drop-in replacement for HTML::Entities'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-HTML5-Entities-license = %{version}-%{release}
Requires: perl-HTML-HTML5-Entities-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
HTML::HTML5::Entities - drop-in replacement for HTML::Entities
SYNOPSIS
use HTML::Entities;
my $enc = encode_entities('fish & chips');
print "$enc\n";   # fish &amp; chips
my $dec = decode_entities($enc);
print "$dec\n";   # fish & chips

%package dev
Summary: dev components for the perl-HTML-HTML5-Entities package.
Group: Development
Provides: perl-HTML-HTML5-Entities-devel = %{version}-%{release}
Requires: perl-HTML-HTML5-Entities = %{version}-%{release}

%description dev
dev components for the perl-HTML-HTML5-Entities package.


%package license
Summary: license components for the perl-HTML-HTML5-Entities package.
Group: Default

%description license
license components for the perl-HTML-HTML5-Entities package.


%package perl
Summary: perl components for the perl-HTML-HTML5-Entities package.
Group: Default
Requires: perl-HTML-HTML5-Entities = %{version}-%{release}

%description perl
perl components for the perl-HTML-HTML5-Entities package.


%prep
%setup -q -n HTML-HTML5-Entities-0.004
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-html5-entities-perl_0.004-1.debian.tar.xz
cd %{_builddir}/HTML-HTML5-Entities-0.004
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-HTML5-Entities-0.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-HTML5-Entities
cp %{_builddir}/HTML-HTML5-Entities-0.004/COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-HTML-HTML5-Entities/fe8305f6e0407ec483da7f3dc3579e9877d207ba
cp %{_builddir}/HTML-HTML5-Entities-0.004/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTML-HTML5-Entities/34f5e12514b91055de4b164a1f2327ef5c30ba53
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-HTML5-Entities/e926d13c344c3699392b67e066091c01ffec5087
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::HTML5::Entities.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-HTML5-Entities/34f5e12514b91055de4b164a1f2327ef5c30ba53
/usr/share/package-licenses/perl-HTML-HTML5-Entities/e926d13c344c3699392b67e066091c01ffec5087
/usr/share/package-licenses/perl-HTML-HTML5-Entities/fe8305f6e0407ec483da7f3dc3579e9877d207ba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTML/HTML5/Entities.pm
