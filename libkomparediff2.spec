%define major 4
%define libname %mklibname komparediff2_ %{major}
%define devname %mklibname komparediff2 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE library to compare files and strings
Name:		libkomparediff2
Version:	14.12.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
KDE library to compare files and strings.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Kompare shared library
Group:		System/Libraries

%description -n %{libname}
Kompare shared library.

%files -n %{libname}
%doc COPYING
%{_kde_libdir}/libkomparediff2.so.%{major}*

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
%{_kde_includedir}/%{name}
%{_kde_libdir}/cmake/%{name}/
%{_kde_libdir}/libkomparediff2.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:14.12.0-1
- New version 14.12.0

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- Split from Kompare package as upstream did
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
