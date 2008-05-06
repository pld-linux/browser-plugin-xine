Summary:	XINE browser plugin
Summary(pl.UTF-8):	Wtyczka XINE dla przeglądarek WWW
Name:		browser-plugin-xine
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xine/xine-plugin-%{version}.tar.bz2
# Source0-md5:	56f826f5ca85543df114d25591147970
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	xine-lib-devel >= 2:1.1.0
BuildRequires:	xorg-lib-libX11-devel
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# directory where you store the plugin
%define		_plugindir	%{_libdir}/browser-plugins

%description
This is a very simple Netscape/Mozilla browser plugin using the XINE
engine to display multimedia streams.

Features:
- embedded display on browser window
- streaming playback directly from XINE engine
- playback control using keyboard
- relative paths supported
- on screen display of buffering and stream information
- playlists and references support
- loop and repeat mode
- multiple instances within the same page
- JavaScript support

%description -l pl.UTF-8
Bardzo prosta wtyczka dla przeglądarek Netscape/Mozilla używająca
silnika XINE do wyświetlania strumieni multimedialnych.

Możliwości:
- wyświetlanie osadzone w okienku przeglądarki
- odtwarzanie strumieni bezpośrednio z silnika XINE
- sterowanie odtwarzaniem przy użyciu klawiatury
- obsługa względnych ścieżek
- wyświetlanie na ekranie (OSD) informacji o buforowaniu i strumieniu
- obsługa playlist i własnych ustawień
- tryb pętli i powtarzania
- wiele instancji na tej samej stronie
- obsługa JavaScriptu

%prep
%setup -q -n xine-plugin-%{version}

%build
%configure \
	--with-plugindir=%{_plugindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = "0" ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_plugindir}/xineplugin.so
%{_plugindir}/xine-logo.ogg
