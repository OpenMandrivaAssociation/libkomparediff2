%define major 5
%define libname %mklibname komparediff2_ %{major}
%define devname %mklibname komparediff2 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE library to compare files and strings
Name:		libkomparediff2
Version:	22.04.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
Requires: %{libname} = %{EVRD}

%description
KDE library to compare files and strings.

%files -f libkomparediff2.lang
%{_datadir}/qlogging-categories5/libkomparediff2.categories

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
Conflicts:	kdesdk4-devel < 1:1.4.11.0
Conflicts:	kompare-devel < 1:1.4.12.0

%description -n %{devname}
This package includes the header files you will need to compile applications
based on libkomparediff2 library.

%files -n %{devname}
%doc COPYING
%{_includedir}/%{name}
%{_libdir}/cmake/LibKompareDiff2
%{_libdir}/libkomparediff2.so

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkomparediff2
