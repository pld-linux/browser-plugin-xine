Summary:	XINE browser plugin
Summary(pl):	Wtyczka XINE dla przegl±darek WWW
Name:		browser-plugin-xine
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xine/xine-plugin-%{version}.tar.bz2
# Source0-md5:	05498789ac11990d5ddd05269671ad0d
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	xine-lib-devel >= 2:1.0.0
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

%description -l pl
Bardzo prosta wtyczka dla przegl±darek Netscape/Mozilla u¿ywaj±ca
silnika XINE do wy¶wietlania strumieni multimedialnych.

Mo¿liwo¶ci:
- wy¶wietlanie osadzone w okienku przegl±darki
- odtwarzanie strumieni bezpo¶rednio z silnika XINE
- sterowanie odtwarzaniem przy u¿yciu klawiatury
- obs³uga wzglêdnych ¶cie¿ek
- wy¶wietlanie na ekranie (OSD) informacji o buforowaniu i strumieniu
- obs³uga playlist i w³asnych ustawieñ
- tryb pêtli i powtarzania
- wiele instancji na tej samej stronie
- obs³uga JavaScriptu

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
