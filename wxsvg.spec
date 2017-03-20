Name:          wxsvg
Version:       1.5.11
Release:       2%{?dist}
Summary:       C++ library to create, manipulate and render SVG files

Group:         System Environment/Libraries
License:       wxWidgets
URL:           http://sourceforge.net/projects/wxsvg
Source0:       http://downloads.sourceforge.net/wxsvg/wxsvg-%{version}.tar.bz2
Patch1:        wxsvg-wxwin.m4.patch
BuildRequires: autoconf automake libtool gettext
BuildRequires: expat-devel
BuildRequires: ffmpeg-devel
BuildRequires: freetype-devel
BuildRequires: libart_lgpl-devel
BuildRequires: pango-devel
BuildRequires: compat-wxGTK3-gtk2-devel
BuildRequires: libexif-devel

%description
wxSVG is C++ library to create, manipulate and render SVG files.

%package devel
Summary: Development files for the wxSVG library
Group: Development/Libraries

%description devel
wxSVG is C++ library to create, manipulate and render SVG files. This package
provides the files required to develop programs that use wxsvg.

%prep
%setup -q
%patch1 -p1

%build
#clean autogenerated files before run autoreconf
rm install-sh mkinstalldirs missing depcomp config.sub ltmain.sh config.guess compile aclocal.m4 Makefile.in configure
rm m4/libtool.m4 m4/lt~obsolete.m4 m4/ltoptions.m4 m4/ltsugar.m4 m4/ltversion.m4
autoreconf -i
%configure \
    --disable-dependency-tracking \
    --disable-static --with-wx-config=/usr/bin/wx-config-3.0-gtk2
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

# Get rid of those .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%{_libdir}/*.so
%{_includedir}/wxSVG/
%{_includedir}/wxSVGXML/
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Sérgio Basto <sergio@serjux.com> - 1.5.11-1
- Update wxsvg to 1.5.11

* Mon Oct 24 2016 Sérgio Basto <sergio@serjux.com> - 1.5.10-1
- Update to 1.5.10, added support of EXIF metadata.

* Tue Sep 27 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-4
- Let try compat-wxGTK3-gtk2, rfbz#4267

* Tue Aug 16 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-3
- Remove Requires old wxGTK-devel in wxsvg-devel, also don't need Requires wxsvg

* Mon Aug 15 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-2
- Upstream suggested to use wxGTK 3.x.

* Tue Aug 09 2016 Sérgio Basto <sergio@serjux.com> - 1.5.9-1
- Update to 1.5.9
- Remove patch0, patch is already in source.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.5.8-4
- Rebuilt for ffmpeg-3.1.1

* Sat Jul 30 2016 Sérgio Basto <sergio@serjux.com> - 1.5.8-3
- Try fix rfbz#4137 , with upstream fixes.

* Fri Jul 08 2016 Sérgio Basto <sergio@serjux.com> - 1.5.8-2
- Cleanup spec and add License tag

* Wed Jun 22 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.5.8-1
- Update to 1.5.8

* Tue Oct 27 2015 Sérgio Basto <sergio@serjux.com> - 1.5.5-1
- Update to 1.5.5.
- Use autoreconf -i instead autogen.sh

* Thu Apr 09 2015 Sérgio Basto <sergio@serjux.com> - 1.5.4-1
- Update to 1.5.4.

* Fri Jan 23 2015 Sérgio Basto <sergio@serjux.com> - 1.5.3-1
- Update to 1.5.3.

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 1.5-3
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.5-2
- Rebuilt for FFmpeg 2.4.x

* Sun Aug 10 2014 Sérgio Basto <sergio@serjux.com> - 1.5-1
- Update to 1.5

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.3-2
- Rebuilt for ffmpeg-2.3

* Sat May 10 2014 Sérgio Basto <sergio@serjux.com> - 1.3-1
- New upstream release .

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.2.1-2
- Rebuilt for ffmpeg-2.2

* Thu Oct 17 2013 Sérgio Basto <sergio@serjux.com> - 1.2.1-1
- Update to 1.2.1

* Mon Oct 07 2013 Sérgio Basto <sergio@serjux.com> - 1.2-1
- Update to 1.2

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.15-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.15-2
- Rebuilt for x264/FFmpeg

* Sat May 11 2013 Sérgio Basto <sergio@serjux.com> - 1.1.15-1
- Update to 1.1.15

* Mon Apr 08 2013 Sérgio Basto <sergio@serjux.com> - 1.1.14-1
- Update to 1.1.14

* Wed Feb 20 2013 Sérgio Basto <sergio@serjux.com> - 1.1.13-1
- Update to 1.1.13

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.12-2
- Rebuilt for ffmpeg

* Mon Jan 21 2013 Sérgio Basto <sergio@serjux.com> - 1.1.12-1
- Update to 1.1.12
- re-use ./autogen.sh
- minor clean ups 

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.9-2
- Rebuilt for FFmpeg 1.0

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.9-1
- Update to 1.1.9
- Use SF URL

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-2
- Rebuilt for FFmpeg

* Thu May 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 28 2011 Stewart Adam <s.adam at diffingo.com> - 1.1.2-1
- Update to 1.1.2

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.8-2
- Update to FFmpeg-0.8

* Mon May 2 2011 Stewart Adam <s.adam at diffingo.com> - 1.0.8-1
- Update to 1.0.8

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

