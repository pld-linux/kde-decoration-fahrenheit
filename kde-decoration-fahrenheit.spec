%define		_decoration 	fahrenheit
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.1
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/2108-%{_decoration}-%{version}.tar.bz2
# Source0-md5:	4e8651c81098e2b0941076a58f920411
URL:		http://www.kde-look.org/content/show.php?content=2108
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fahrenheit is an innovative kwin decoration which does not follow the
old and overused ideas of WinXP or MacOsX.

%description -l pl
fahrenheit to innowacyjna dekoracja kwin, która nie pod±¿a za
pomys³ami zrealizowanymi w WinXP czy MacOsX.

%prep
%setup -q -n %{_decoration}-%{version}

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp -f %{_datadir}/automake/config.sub admin
sed -i -e "s,\$(TOPSUBDIRS),client," Makefile.am

export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop
%{_datadir}/apps/kwin/fahrenheit
