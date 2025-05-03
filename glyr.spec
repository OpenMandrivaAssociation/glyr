%define major 1
%define libname %mklibname %{name}
%define devname %mklibname -d %{name}


Name:		glyr
Version:	1.0.10
Release:	3
Summary:	Search engine for music related metadata
License:	LGPL-3.0-or-later
Group:		Sound/Utilities
URL:			https://github.com/sahib/glyr
Source0:	https://github.com/sahib/glyr/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE glyr-0.9.4-optflags.patch lazy.kent@opensuse.org -- use default openSUSE optimization flags.
Patch0:		glyr-0.9.4-optflags.patch
Patch1:		glyr-1.0.10-link-curl.patch
# CMakeLists.txt, config.h: Fix version
Patch2:		glyr-1.0.10-fix-version-numbering.patch

BuildSystem:	cmake
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	curl
BuildRequires:	git
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	sqlite-tools

%description
glyr is a cli search engine for music related metadata

It comes both in a command-line interface tool (glyrc) and as a C library,
both with an easy to use interface.

The sort of metadata glyr is searching (and downloading) is usually
the data you see in your musicplayer.

And indeed, originally it was written to serve as internally library
for a musicplayer, but has been extended to work as a standalone
program which is able to download:

  cover art;
  lyrics;
  bandphotos;
  artist biography;
  album reviews;
  tracklists of an album;
  a list of albums from a specific artist;
  tags, either related to artist, album or title relations, for example
  links to Wikipedia;
  similar artists;
  similar songs.

%package -n %libname
Summary:	Search engine for music related metadata
Group:		System/Libraries/C_C++

%description -n %libname
The glyr shared library.

%package -n %devname
Summary:	Development files for the glyr music metadata search engine
Group:		Development/C and C++
Requires:	%libname = %{version}-%{release}

%description -n %devname
The glyr C and C++ development files.

%prep
%autosetup -p1
# do not inject bogus dependencies into the library's pkgconfig file
sed -i -e '/Requires: glib-2.0 libcurl sqlite3/Requires: sqlite3/' libglyr.pc.in

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}c
%doc AUTHORS
%doc CHANGELOG
%doc README.textile
%doc state_of_providers.txt
%license COPYING

%files -n %libname
%{_libdir}/lib%{name}.so.%{major}*
%license COPYING

%files -n %devname
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%doc AUTHORS
%doc CHANGELOG
%doc README.textile
%doc state_of_providers.txt
%license COPYING

