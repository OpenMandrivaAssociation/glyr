%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:		Search engine for music related metadata
Name:		glyr
Version:		1.0.10
Release:		4
License:	LGPL-3.0-or-later
Group:		Sound/Utilities
Url:			https://github.com/sahib/glyr
Source0:	https://github.com/sahib/glyr/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
# PATCH-FIX-OPENSUSE glyr-0.9.4-optflags.patch lazy.kent@opensuse.org -- use default openSUSE optimization flags.
Patch0:		glyr-0.9.4-optflags.patch
Patch1:		glyr-1.0.10-link-curl.patch
# CMakeLists.txt, config.h: Fix version
Patch2:		glyr-1.0.10-fix-version-numbering.patch
Patch3:		glyr-1.0.10-update-liricswiki.patch
# The build needs curl/curl.h, but does not include it
Patch4:		glyr-1.0.10-add-missing-header.patch
#BuildSystem:	cmake
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	curl
BuildRequires:	git
BuildRequires:	sqlite-tools
BuildRequires:	glibc-devel
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sqlite3)

%description
This is a cli search engine for music related metadata. It comes both in a
command-line interface tool (glyrc) and as a C library, both with an easy to
use interface.
The sort of metadata glyr is searching (and downloading) is usually the data
you see in your musicplayer. And indeed, originally it was written to serve
as internally library for a musicplayer, but has been extended to work
as a standalone program which is able to download:
* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example links
   to Wikipedia;
* similar artists;
* similar songs.

%files
%license COPYING
%{_bindir}/%{name}c
%doc AUTHORS CHANGELOG README.textile state_of_providers.txt


#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Search engine for music related metadata
Group:		System/Libraries/C_C++
%rename	%{_lib}glyr

%description -n %{libname}
This is a cli search engine for music related metadata. It comes both in a
command-line interface tool (glyrc) and as a C library, both with an easy to
use interface.
This package contains the shared library used by %{name}.

%files -n %{libname}
%license COPYING
%{_libdir}/lib%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C and C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The C and C++ development files needed for use %{name}.

%files -n %{devname}
%license COPYING
%doc AUTHORS CHANGELOG README.textile
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Do not inject bogus dependencies into the library's pkgconfig file
sed -i -e '/Requires: glib-2.0 libcurl sqlite3/Requires: sqlite3/' libglyr.pc.in


%build
%cmake -G Ninja
%ninja_build


%install
%ninja_install -C build
