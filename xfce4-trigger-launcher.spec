Summary:	Trigger launcher - a launcher with two states
Summary(pl):	Trigger launcher - dwustanowy przełącznik
Name:		xfce4-trigger-launcher
Version:	4.0.4
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	104e1c6abfcc30a036673c15f66b2d03
URL:		http://www.xfce.org/
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce4-panel-devel >= %{version}
Requires:	xfce4-panel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trigger launcher - a launcher with two states.

%description -l pl
Trigger launcher - dwustanowy przełącznik.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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
