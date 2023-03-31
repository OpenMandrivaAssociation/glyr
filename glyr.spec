%define major   1
%define libname %mklibname glyr
%define devname %mklibname -d glyr

Name:           glyr
Version:        1.0.10
Release:        2
Summary:        Search engine for music related Metadata
License:        GPLv3+
Group:          System/Libraries
Url:            https://github.com/sahib/glyr
Source0:        https://github.com/sahib/glyr/archive/refs/tags/%{version}.tar.gz
# PATCH-FIX-OPENSUSE glyr-0.9.4-optflags.patch lazy.kent@opensuse.org -- use default openSUSE optimization flags.
Patch1:         glyr-0.9.4-optflags.patch
Patch2:		glyr-1.0.10-link-curl.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sqlite3)

%description
Glyr CLI tool.

The sort of metadata glyr is searching (and downloading) is usually the
data you see in your musicplayer. And indeed, originally it was written
to serve as internally library for a musicplayer, but has been extended
to work as a standalone program which is able to download:

* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example
  links to wikipedia;
* similar artists;
* similar songs.

%package -n	%{libname}
Summary:        Searcheninge for Musicrelated Metadata
Group:          System/Libraries

%description -n %{libname}
Glyr shared library.

%package -n	%{devname}
Summary:        Searcheninge for Musicrelated Metadata
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
Glyr development files.

%prep
%autosetup -p1
%cmake

%build
%make_build -C build

%install
%make_install -C build

%files
%doc AUTHORS CHANGELOG COPYING README.textile
%{_bindir}/glyrc

%files -n %{libname}
%{_libdir}/libglyr.so.%{major}*

%files -n %{devname}
%doc src/examples
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

