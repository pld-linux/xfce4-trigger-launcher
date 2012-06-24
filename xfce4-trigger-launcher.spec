Summary:	Trigger launcher - a launcher with two states
Summary(pl):	Trigger launcher - dwustanowy prze��cznik
Name:		xfce4-trigger-launcher
Version:	4.0.2
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	c842c85f2d6d2cb72c5d0aaff9363d62
URL:		http://www.xfce.org/
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce4-panel-devel >= %{version}
Requires:	xfce4-panel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trigger launcher - a launcher with two states.

%description -l pl
Trigger launcher - dwustanowy prze��cznik.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
