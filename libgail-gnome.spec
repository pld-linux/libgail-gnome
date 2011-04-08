Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl.UTF-8):	Implementacja ułatwiania pracy niepełnosprawnym dla GTK+ i GNOME
Name:		libgail-gnome
Version:	1.20.4
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgail-gnome/1.20/%{name}-%{version}.tar.bz2
# Source0-md5:	b29bf1c8f2cd8652ec827c9f5b8baa14
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	GConf2-devel
BuildRequires:	at-spi-devel >= 1.24.0
BuildRequires:	atk-devel >= 1:1.24.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-panel-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	libbonoboui-devel >= 2.24.0
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	atk >= 1:1.24.0
Requires:	libgnomeui >= 2.24.0
Obsoletes:	libgail-gnome-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as at-spi to
access those GUIs.

%description -l pl.UTF-8
GAIL jest implementacją abstrakcyjnych interfejsów z ATK dla bibliotek
GTK+ i GNOME, umożliwiającą korzystanie z technik takich jak at-spi,
aby ułatwić niepełnosprawnym korzystanie z tych GUI.

%package devel
Summary:	Header files to compile applications that use libgail-gnome
Summary(pl.UTF-8):	Pliki nagłówkowe libgail-gnome
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atk-devel >= 1:1.24.0
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libbonoboui-devel >= 2.24.0

%description devel
gail-devel contains the header files required to compile applications
against the GAIL libraries.

%description devel -l pl.UTF-8
Pakiet gail-devel zawiera pliki nagłówkowe potrzebne do kompilowania
aplikacji używających bibliotek GAIL.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install libgail-gnome.schemas

%preun
%gconf_schema_uninstall libgail-gnome.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libgail-gnome.so
%{_sysconfdir}/gconf/schemas/libgail-gnome.schemas

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/libgail-gnome.pc
