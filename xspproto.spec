Summary:	Xsp extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xsp
Name:		xspproto
Version:	1.2
Release:	1
License:	MIT-like
Group:		Development/Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/x11proto-xsp_%{version}-1.tar.gz
# Source0-md5:	90cab4074681d90da6ba997303e12a0f
URL:		http://maemo.org/
# just for dir
Requires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains header files for the Xsp extension. There are
two users for Xsp: end-user calibration application, and the media
player.

%description -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe rozszerzenia Xsp. Są dwa
zastosowania Xsp: aplikacja użytkownika do kalibracji i odtwarzacz
multimedialny.

%prep
%setup -q -n x11proto-xsp-%{version}

%build
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
%doc AUTHORS COPYING README
%{_includedir}/X11/extensions/xspproto.h
%{_includedir}/X11/extensions/xspwire.h
%{_pkgconfigdir}/xspproto.pc
