%global commit0 aecaf4a0947e1cd184440008b5a1f13657ca268c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           openshot
Version:        2.4.2
Release:        2%{?gver}%{dist}
Summary:        Create and edit videos and movies

Group:          Applications/Multimedia
License:        GPLv3+
URL:            http://www.openshotvideo.com/
Source0:	https://github.com/OpenShot/openshot-qt/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	gpl-2.0.txt

BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  libopenshot >= 0.2.0
BuildRequires:  libopenshot-audio >= 0.1.6
BuildRequires:  desktop-file-utils
BuildRequires:	python3-setuptools
# To fix icon
BuildRequires:  ImageMagick

Requires:       mlt
Requires:       mlt-python
Requires:       ladspa
Requires:       notify-python
Requires:       pygoocanvas
Requires:       pygtk2-libglade
Requires:       python3-pillow
Requires:       python3-httplib2
Requires:       pyxdg
Requires:       SDL
Requires:       sox
#Requires:       librsvg2
Requires:       frei0r-plugins
Requires:       fontconfig
Requires:       python3-libopenshot >= 0.2.0
Requires:       libopenshot-audio >= 0.1.6
Requires:       qt5-qtsvg
Requires:       qt5-qtwebkit
Requires:       python3-qt5
Requires:       python3-zmq
# Needed because it owns icon directories
Requires:       hicolor-icon-theme
Requires:       python3-qt5-webkit
Recommends:     ffmpeg
Recommends:     blender
Recommends:     vid.stab


%description
OpenShot Video Editor is a free, open-source, non-linear video editor. It
can create and edit videos and movies using many popular video, audio,
image formats.  Create videos for YouTube, Flickr, Vimeo, Metacafe, iPod,
Xbox, and many more common formats!

Features include:
* Multiple tracks (layers)
* Compositing, image overlays, and watermarks
* Support for image sequences (rotoscoping)
* Key-frame animation
* Video and audio effects (chroma-key)
* Transitions (lumas and masks)
* 3D animation (titles and simulations)
* Upload videos (YouTube and Vimeo supported)


%prep
%autosetup -n %{name}-qt-%{commit0} 
sed -i 's/^ROOT =.*/ROOT = False/' setup.py


%build

%py3_build

# FIX lang
cd src/locale/
for dir in *;do echo "%lang($dir) %{python3_sitelib}/openshot_qt/locale/$dir" >> %{_builddir}/%{name}-qt-%{commit0}/OpenShot.lang
done

%install
%py3_install 


# Validate desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f OpenShot.lang
%{_bindir}/openshot-qt
%{_prefix}/lib/mime/packages/openshot-qt
%{python3_sitelib}/%{name}_qt*-py*.egg-info/
%{_datadir}/applications/openshot-qt.desktop
%{_datadir}/mime/packages/openshot-qt.xml
%{_datadir}/pixmaps/openshot-qt.svg
%{python3_sitelib}/%{name}_qt/blender/  
%{python3_sitelib}/%{name}_qt/images/     
%{python3_sitelib}/%{name}_qt/presets/      
%{python3_sitelib}/%{name}_qt/settings/  
%{python3_sitelib}/%{name}_qt/titles/       
%{python3_sitelib}/%{name}_qt/windows/
%{python3_sitelib}/%{name}_qt/classes/  
%{python3_sitelib}/%{name}_qt/launch.py  
%{python3_sitelib}/%{name}_qt/profiles/     
%{python3_sitelib}/%{name}_qt/tests/     
%{python3_sitelib}/%{name}_qt/transitions/
%{python3_sitelib}/%{name}_qt/effects/       
%{python3_sitelib}/%{name}_qt/__pycache__/  
%{python3_sitelib}/%{name}_qt/timeline/  
#{python3_sitelib}/%{name}_qt/uploads/
%{python3_sitelib}/%{name}_qt/locale/__pycache__/


%changelog

* Fri Jul 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.2-2.gitaecaf4a
- Rebuilt for Python 3.7

* Sat Jun 30 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.2-1.gitaecaf4a
- Updated to 2.4.2-1.gitaecaf4a

* Thu Nov 16 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.1-2.git4bdea37
- Updated to 2.4.1-2.git4bdea37

* Fri Sep 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.0-2.gita170fb4
- Updated to 2.4.0-2.gita170fb4

* Tue Jun 06 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.3.4-2.gitaa79cd6 
- Updated to 2.3.4-2.gitaa79cd6 

* Thu May 25 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.3.3-3.git0c838ef  
- Rebuilt for libopenshot-audio

* Wed May 24 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.3.3-2.git0c838ef  
- Updated to 2.3.3-2.git0c838ef

* Sun Apr 02 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.3.1-2-20170402gitf677f30
- Updated to 2.3.1-2-20170402gitf677f30

* Sat Mar 18 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.2.0-2-20170318gitac2d084
- Updated to 2.2.0-2-20170318gitac2d084

* Thu Mar 16 2017 Pavlo Rudyi <paulcarroty at riseup net> - 2.2.0-1
- Updated to 2.2

* Sat Sep 03 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.1.0-2
- Disabled "tutorial first"
- Solved local issues

* Wed Aug 31 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 2.1.0-1
- Updated to 2.1
- New source URL

* Tue Jul 12 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.0.7-6
- Massive rebuild 

* Sun Jun 26 2016 The UnitedRPMs Project (Key for UnitedRPMs infrastructure) <unitedrpms@protonmail.com> - 2.0.7-5
- Rebuild with new ffmpeg

* Thu Jun  9 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 2.0.7-4
- Added the depends python3-qt5-webkit.

* Fri May 27 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.0.7-3
- Added missing dependencies
- Sanitize tabs.

* Mon Apr 18 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-2
- Update to require python3-libopenshot.

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-1
- Update to latest upstream release.

* Fri Mar  4 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.6-1
- Update to latest upstream release.

* Mon Jan 11 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.4-1
- Update to latest upstream release.

* Mon Apr  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4.3-3
- Fix broken icon file (BZ#3546).
- Add ladspa as a install requirement (BZ#3472).

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Oct 26 2012 Richard Shaw <hobbes1069@gmail.com> - 1.4.3-1
- Update to latest upstream release.

* Mon Feb 20 2012 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-4
- Fix small packaging bug with icon.

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 06 2012 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-2
- Update to latest release.
- Fixed small build problem with the buildroot path finding it's way into
  a packaged file.

* Mon Feb 06 2012 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-1
- Update to latest release.

* Mon Jan 30 2012 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-1
- Update to latest release.
