Name:          wxsvg
Version:       1.0.8
Release:       1%{?dist}
Summary:       C++ library to create, manipulate and render SVG files

Group:         System Environment/Libraries
License:       wxWidgets
URL:           http://www.wxsvg.org/
Source0:       http://downloads.sourceforge.net/wxsvg/wxsvg-%{version}-1.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtool, gettext
BuildRequires: expat-devel
BuildRequires: ffmpeg-devel
BuildRequires: freetype-devel
BuildRequires: libart_lgpl-devel
BuildRequires: pango-devel
BuildRequires: wxGTK-devel

%description
wxSVG is C++ library to create, manipulate and render SVG files.

%package devel
Summary: Development files for the wxSVG library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: wxGTK-devel

%description devel
wxSVG is C++ library to create, manipulate and render SVG files. This package
provides the files required to develop programs that use wxsvg.

%prep
%setup -q -n wxsvg-%{version}-1

%build
./autogen.sh
%configure \
    --disable-dependency-tracking \
    --disable-static
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

# Get rid of those .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/wxSVG/
%{_includedir}/wxSVGXML/
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Mon May 2 2011 Stewart Adam <s.adam at diffingo.com> - 1.0.8-1
- Update to 1.0.8

* Sat Nov 20 2010 Stewart Adam <s.adam at diffingo.com> - 1.0.7_1-1
- Update to 1.0.7_1 release

* Wed May 19 2010 Stewart Adam <s.adam at diffingo.com> - 1.0.4-1
- Update to 1.0.4 release

* Mon Jan 18 2010 Stewart Adam <s.adam at diffingo.com> - 1.0.2_1-1
- Update to 1.0.2_1 release

* Wed Oct 21 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0-8
- rebuild for new ffmpeg

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0-7
- rebuild for new F11 features

* Wed Jan 21 2009 Stewart Adam <s.adam at diffingo.com> - 1.0-6
- Add libtool and ffmpeg-devel BR
- Package headers & binaries again

* Tue Jan 20 2009 Stewart Adam <s.adam at diffingo.com> - 1.0-5
- Bump for correct upgrade path from Fedora

* Tue Jan 20 2009 Stewart Adam <s.adam at diffingo.com> - 1.0-4
- Rename wxsvg-freeworld to wxsvg and remove soname patch
- Update description

* Thu Dec 11 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-3
- Change soname to wxsvg_freeworld
- Update expat patch, rm -rf internal expat sources
- BR: expat should be BR: expat-devel

* Thu Nov 13 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-2
- Split off a devel package

* Thu Nov 13 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-1
- Update to 1.0 final
- Remove requires on /etc/ld.so.conf.d
- Patch out the internal expat build
- Remove requires on wxsvg
- Own %%{_libdir}/wxsvg-freeworld

* Fri Oct 17 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.11.b11
- Remove useless -devel subpackage

* Thu Oct 16 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.10.b11
- Remove binaries and include files; these are the same as the originals
- Remove ffmpeg-devel requirement on -devel package
- Get rid of %%configure hack (CFLAGS/CXXFLAGS)
- Require wxsvg and wxsvg-devel so the proper binaries and headers are
  pulled in
- Add patch to use LIBAVFORMAT_{CFLAGS,LDFLAGS} in Makefile.am

* Wed Oct 15 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.9.b11
- Make devel package require ffmpeg-devel
- Edit #include statements to append -freeworld
- Add README.Fedora

* Sat Sep 27 2008 Stewart Adam <s.adam at diffingo.com> - 1.0-0.8.b11
- New package based from Fedora's spec
- Update to 1.0b11, enable ffmpeg
- Use ld.so.conf.d to override non-ffmpeg enabled libraries

* Wed Mar  5 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.8.b10
- Update to 1.0b10.
- Build with dependency tracking disabled.

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 1.0-0.8.b7_3
- Downgrade to 1.0b7_3 since 1.0b8_1 requires ffmpeg and disabling it doesn't
  seem to work properly and it has never avtually been built.
- Update URL field.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Matthias Saou <http://freshrpms.net/> 1.0-0.6.b8_1
- Update to 1.0b8_1.
- Replace shipping our own ltmain.sh with running libtoolize.
- Disable new ffmpeg option (which is enabled by default).
- Still needs work (doesn't compile!), since ffmpeg seems to be mandatory now.

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.5.b7_3
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.4.b7_3
- Update License field.

* Wed Jun  6 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.3.b7_3
- Update to 1.0b7_3.
- Pass -p to install.
- Remove no longer needed freetype patch, but...
- ...include our own ltmain.sh because it's missing...
- ...run ./autogen.sh since Makefile.in files are missing too.

* Wed May  9 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.2.b7
- Remove rpath on 64bit.
- Update sf.net download URL.
- Add missing wxGTK-devel requirement to the devel package.

* Fri Jan 19 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.1.b7
- Initial RPM release.

