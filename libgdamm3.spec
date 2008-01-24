#
# Conditional build:
%bcond_without	static_libs # don't build static library
#
%define		realname	libgdamm
Summary:	C++ wrappers for libgda 3.x
Summary(pl.UTF-8):	Interfejsy C++ dla libgda 3.x
Name:		libgdamm3
Version:	2.9.81
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdamm/2.9/%{realname}-%{version}.tar.gz
# Source0-md5:	ef07649a9da29f6ecf3f6ab5bb843f97
BuildRequires:	glibmm-devel >= 2.12.8
BuildRequires:	libgda3-devel >= 3.0.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.12.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgda 3.x.

%description -l pl.UTF-8
Interfejsy C++ dla libgda 3.x.

%package devel
Summary:	Header files for libgdamm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdamm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.12.8
Requires:	libgda3-devel >= 3.0.0

%description devel
Header files for libgdamm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgdamm.

%package static
Summary:	Static libgdamm library
Summary(pl.UTF-8):	Statyczna biblioteka libgdamm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdamm library.

%description static -l pl.UTF-8
Statyczna biblioteka libgdamm.

%prep
%setup -q -n %{realname}-%{version}

%build
%configure \
	%{?with_static_libs:--enable-static=yes}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgdamm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdamm-3.0.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdamm-3.0.so
%{_libdir}/libgdamm-3.0.la
%{_libdir}/libgdamm-3.0
%{_includedir}/libgdamm-3.0
%{_pkgconfigdir}/libgdamm-3.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdamm-3.0.a
%endif
