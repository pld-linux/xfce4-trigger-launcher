
%define		_snap 20040816

Summary:	Trigger launcher - a launcher with two states
Summary(pl):	Trigger launcher - dwustanowy prze³±cznik
Name:		xfce4-trigger-launcher
Version:	4.1.0
Release:	0.%{_snap}
License:	BSD
Group:		X11/Applications
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	28619171c6438cf6e2afc2e96b985b20
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce4-panel-devel >= 4.1.0
Requires:	xfce4-panel >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trigger launcher - a launcher with two states.

%description -l pl
Trigger launcher - dwustanowy prze³±cznik.

%prep
%setup -q -n %{name}
%patch0 -p1

mv -f po/{fa_IR,fa}.po
mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I m4
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
