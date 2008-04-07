# TODO:
# - package examples
#
# Conditional build:
%bcond_without	static_libs # don't build static library
#
%define		realname	libgdamm
Summary:	C++ wrappers for libgda 3.x
Summary(pl.UTF-8):	Interfejsy C++ dla libgda 3.x
Name:		libgdamm3
Version:	3.0.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdamm/3.0/%{realname}-%{version}.tar.bz2
# Source0-md5:	f1ab9b9fad1ab02eb3e580911ce5e702
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	glibmm-devel >= 2.12.8
BuildRequires:	libgda3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.12.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgda 3.x.

%description -l pl.UTF-8
Interfejsy C++ dla libgda 3.x.

%package devel
Summary:	Header files for libgdamm3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdamm3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.12.8
Requires:	libgda3-devel >= 3.0.0

%description devel
Header files for libgdamm3 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgdamm3.

%package static
Summary:	Static libgdamm3 library
Summary(pl.UTF-8):	Statyczna biblioteka libgdamm3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdamm3 library.

%description static -l pl.UTF-8
Statyczna biblioteka libgdamm3.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
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
%attr(755,root,root) %ghost %{_libdir}/libgdamm-3.0.so.10

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
