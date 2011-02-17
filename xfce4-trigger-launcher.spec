Summary:	Trigger launcher - a launcher with two states
Summary(pl.UTF-8):	Trigger launcher - dwustanowy przełącznik
Name:		xfce4-trigger-launcher
Version:	4.2.4.1
Release:	3
License:	BSD
Group:		X11/Applications
#Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	8d35a75cb7bbaec78a9a2f171dfa5571
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trigger launcher - a launcher with two states.

%description -l pl.UTF-8
Trigger launcher - dwustanowy przełącznik.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po

%build
%{__intltoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-trigger-launcher-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-trigger-launcher.desktop
