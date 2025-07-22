%define major 6
%define libname %mklibname komparediff2-kf6
%define devname %mklibname komparediff2-kf6 -d
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240524
%define gitbranch kf6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	KDE library to compare files and strings
Name:		libkomparediff2
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/libkomparediff2/-/archive/%{gitbranch}/libkomparediff2-%{gitbranchd}.tar.bz2#/libkomparediff2-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkomparediff2-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
# Really conflicts with the plasma5 version
BuildRequires:	plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%rename plasma6-libkomparediff2

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE library to compare files and strings.

%files -f %{name}.lang
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
%{_libdir}/cmake/KompareDiff2
%{_libdir}/libkomparediff2.so
