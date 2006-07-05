Summary:	Trigger launcher - a launcher with two states
Summary(pl):	Trigger launcher - dwustanowy prze³±cznik
Name:		xfce4-trigger-launcher
Version:	4.2.3
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	af3c0356862af8a37e90ec18ad008918
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel >= 4.1.0
Requires:	xfce4-panel >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trigger launcher - a launcher with two states.

%description -l pl
Trigger launcher - dwustanowy prze³±cznik.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
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
