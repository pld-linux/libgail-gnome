Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl):	Implementacja u³atwiania pracy niepe³nosprawnym dla GTK+ i GNOME
Name:		libgail-gnome
Version:	1.0.2
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
URL:		http://developer.gnome.org/projects/gap
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+2-devel >= 2.1.3-2
BuildRequires:	libgnomecanvas-devel >= 2.0.2
BuildRequires:	atk-devel >= 1.1.0
BuildRequires:	at-spi-devel >= 1.1.5-4
BuildRequires:	libbonoboui-devel >= 2.1.0
BuildRequires:	gail-devel >= 1.1.2
BuildRequires:	libbonoboui >= 2.1.0
Requires:	gnome-common >= 1.2.4
Requires:	atk >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as at-spi to
access those GUIs.

%description -l pl
GAIL jest implementacj± abstrakcyjnych interfejsów z ATK dla bibliotek
GTK+ i GNOME, umo¿liwiaj±c± korzystanie z technik takich jak at-spi,
aby u³atwiæ niepe³nosprawnym korzystanie z tych GUI.

%package devel
Summary:	Header files to compile applications that use libgail-gnome
Summary(pl):	Pliki nag³ówkowe libgail-gnome
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires: 	pkgconfig >= 0.14.0

%description devel
gail-devel contains the header files required to compile applications
against the GAIL libraries.

%description devel -l pl
Pakiet gail-devel zawiera pliki nag³ówkowe potrzebne do kompilowania
aplikacji u¿ywaj±cych bibliotek GAIL.


%package static
Summary:	Static GAIL libraries
Summary(pl):	Statyczne biblioteki GAIL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gail-static contains the static GAIL libraries.

%description static -l pl
Pakiet gail-static zawiera statyczne biblioteki GAIL.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.??

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/gtk-2.0/modules/*.a
