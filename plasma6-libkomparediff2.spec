%define major 5
%define libname %mklibname komparediff2-kf6
%define devname %mklibname komparediff2-kf6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230807

Summary:	KDE library to compare files and strings
Name:		plasma6-libkomparediff2
Version:	24.00.0
Release:	%{?git:0.%{git}.}1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/libkomparediff2/-/archive/master/libkomparediff2-master.tar.bz2#/libkomparediff2-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
Requires: %{libname} = %{EVRD}

%description
KDE library to compare files and strings.

%files -f libkomparediff2.lang
%{_datadir}/qlogging-categories6/libkomparediff2.categories

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Kompare shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Kompare shared library.

%files -n %{libname}
%{_libdir}/libkomparediff2.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for libkomparediff2
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package includes the header files you will need to compile applications
based on libkomparediff2 library.

%files -n %{devname}
%doc COPYING
%{_includedir}/KompareDiff2
%{_libdir}/cmake/LibKompareDiff2
%{_libdir}/libkomparediff2.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkomparediff2-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang libkomparediff2
