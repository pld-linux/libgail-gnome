Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl.UTF-8):	Implementacja ułatwiania pracy niepełnosprawnym dla GTK+ i GNOME
Name:		libgail-gnome
Version:	1.1.3
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgail-gnome/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	1d12c5375b3404f4f20b214b763e5225
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	at-spi-devel >= 1.1.5-4
BuildRequires:	atk-devel >= 1.8.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel
BuildRequires:	gnome-panel-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libbonoboui-devel >= 2.14.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	atk >= 1.8.0
Requires:	libgnomeui >= 2.14.0
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
Requires:	atk-devel >= 1.8.0
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	libbonoboui-devel >= 2.1.0

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
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
