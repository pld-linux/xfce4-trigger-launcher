Summary:	Trigger launcher
Summary(pl):	Trigger launcher
Name:		xfce4-trigger-launcher
Version:	3.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://linux.imp.mx/xfce4/rc2/xfce4-rc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	750f1b959eb6f6d30831507d5a7c4da4
URL:		http://www.xfce.org/
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce4-panel >= 3.99.2
Requires:	xfce4-panel-devel >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trigger launcher

%description -l pl
Trigger launcher

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
%doc README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
