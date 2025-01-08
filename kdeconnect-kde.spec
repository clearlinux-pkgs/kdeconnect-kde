#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdeconnect-kde
Version  : 24.12.0
Release  : 63
URL      : https://download.kde.org/stable/release-service/24.12.0/src/kdeconnect-kde-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/kdeconnect-kde-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/kdeconnect-kde-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Adds communication between KDE and your smartphone
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kdeconnect-kde-bin = %{version}-%{release}
Requires: kdeconnect-kde-data = %{version}-%{release}
Requires: kdeconnect-kde-lib = %{version}-%{release}
Requires: kdeconnect-kde-license = %{version}-%{release}
Requires: kdeconnect-kde-locales = %{version}-%{release}
BuildRequires : ModemManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcrash-dev
BuildRequires : kio-dev
BuildRequires : kirigami2-dev
BuildRequires : kpeople-dev
BuildRequires : kservice-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : kwayland-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libfakekey-dev
BuildRequires : modemmanager-qt-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libfakekey)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pulseaudio-qt-dev
BuildRequires : qca-dev
BuildRequires : qqc2-desktop-style-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
BuildRequires : qtwayland-dev
BuildRequires : wayland-protocols-dev plasma-wayland-protocols-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
When the user moves his on the phone, dx and dy (The difference between the last movement and the current movement of the X and Y Axis respectively)
is sent inside a NetworkPackage QCursor is used to move mouse cursor according to its relative position.

%package bin
Summary: bin components for the kdeconnect-kde package.
Group: Binaries
Requires: kdeconnect-kde-data = %{version}-%{release}
Requires: kdeconnect-kde-license = %{version}-%{release}

%description bin
bin components for the kdeconnect-kde package.


%package data
Summary: data components for the kdeconnect-kde package.
Group: Data

%description data
data components for the kdeconnect-kde package.


%package doc
Summary: doc components for the kdeconnect-kde package.
Group: Documentation

%description doc
doc components for the kdeconnect-kde package.


%package lib
Summary: lib components for the kdeconnect-kde package.
Group: Libraries
Requires: kdeconnect-kde-data = %{version}-%{release}
Requires: kdeconnect-kde-license = %{version}-%{release}

%description lib
lib components for the kdeconnect-kde package.


%package license
Summary: license components for the kdeconnect-kde package.
Group: Default

%description license
license components for the kdeconnect-kde package.


%package locales
Summary: locales components for the kdeconnect-kde package.
Group: Default

%description locales
locales components for the kdeconnect-kde package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kdeconnect-kde-24.12.0
cd %{_builddir}/kdeconnect-kde-24.12.0
pushd ..
cp -a kdeconnect-kde-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735236442
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735236442
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdeconnect-kde
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kdeconnect-app
%find_lang kdeconnect-cli
%find_lang kdeconnect-core
%find_lang kdeconnect-fileitemaction
%find_lang kdeconnect-indicator
%find_lang kdeconnect-interfaces
%find_lang kdeconnect-kcm
%find_lang kdeconnect-kded
%find_lang kdeconnect-kio
%find_lang kdeconnect-nautilus-extension
%find_lang kdeconnect-plugins
%find_lang kdeconnect-settings
%find_lang kdeconnect-sms
%find_lang kdeconnect-urlhandler
%find_lang plasma_applet_org.kde.kdeconnect
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kdeconnect-app
/V3/usr/bin/kdeconnect-cli
/V3/usr/bin/kdeconnect-handler
/V3/usr/bin/kdeconnect-indicator
/V3/usr/bin/kdeconnect-settings
/V3/usr/bin/kdeconnect-sms
/V3/usr/bin/kdeconnectd
/usr/bin/kdeconnect-app
/usr/bin/kdeconnect-cli
/usr/bin/kdeconnect-handler
/usr/bin/kdeconnect-indicator
/usr/bin/kdeconnect-settings
/usr/bin/kdeconnect-sms
/usr/bin/kdeconnectd

%files data
%defattr(-,root,root,-)
/usr/share/Thunar/sendto/kdeconnect-thunar.desktop
/usr/share/applications/kcm_kdeconnect.desktop
/usr/share/applications/org.kde.kdeconnect-settings.desktop
/usr/share/applications/org.kde.kdeconnect.app.desktop
/usr/share/applications/org.kde.kdeconnect.daemon.desktop
/usr/share/applications/org.kde.kdeconnect.handler.desktop
/usr/share/applications/org.kde.kdeconnect.nonplasma.desktop
/usr/share/applications/org.kde.kdeconnect.sms.desktop
/usr/share/contractor/kdeconnect.contract
/usr/share/dbus-1/services/org.kde.kdeconnect.service
/usr/share/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop
/usr/share/icons/hicolor/16x16/status/laptopconnected.svg
/usr/share/icons/hicolor/16x16/status/laptopdisconnected.svg
/usr/share/icons/hicolor/16x16/status/laptoptrusted.svg
/usr/share/icons/hicolor/16x16/status/smartphoneconnected.svg
/usr/share/icons/hicolor/16x16/status/smartphonedisconnected.svg
/usr/share/icons/hicolor/16x16/status/smartphonetrusted.svg
/usr/share/icons/hicolor/16x16/status/tabletconnected.svg
/usr/share/icons/hicolor/16x16/status/tabletdisconnected.svg
/usr/share/icons/hicolor/16x16/status/tablettrusted.svg
/usr/share/icons/hicolor/16x16/status/tvconnected.svg
/usr/share/icons/hicolor/16x16/status/tvdisconnected.svg
/usr/share/icons/hicolor/16x16/status/tvtrusted.svg
/usr/share/icons/hicolor/22x22/status/laptopconnected.svg
/usr/share/icons/hicolor/22x22/status/laptopdisconnected.svg
/usr/share/icons/hicolor/22x22/status/laptoptrusted.svg
/usr/share/icons/hicolor/22x22/status/smartphoneconnected.svg
/usr/share/icons/hicolor/22x22/status/smartphonedisconnected.svg
/usr/share/icons/hicolor/22x22/status/smartphonetrusted.svg
/usr/share/icons/hicolor/22x22/status/tabletconnected.svg
/usr/share/icons/hicolor/22x22/status/tabletdisconnected.svg
/usr/share/icons/hicolor/22x22/status/tablettrusted.svg
/usr/share/icons/hicolor/22x22/status/tvconnected.svg
/usr/share/icons/hicolor/22x22/status/tvdisconnected.svg
/usr/share/icons/hicolor/22x22/status/tvtrusted.svg
/usr/share/icons/hicolor/32x32/status/laptopconnected.svg
/usr/share/icons/hicolor/32x32/status/laptopdisconnected.svg
/usr/share/icons/hicolor/32x32/status/laptoptrusted.svg
/usr/share/icons/hicolor/32x32/status/smartphoneconnected.svg
/usr/share/icons/hicolor/32x32/status/smartphonedisconnected.svg
/usr/share/icons/hicolor/32x32/status/smartphonetrusted.svg
/usr/share/icons/hicolor/32x32/status/tabletconnected.svg
/usr/share/icons/hicolor/32x32/status/tabletdisconnected.svg
/usr/share/icons/hicolor/32x32/status/tablettrusted.svg
/usr/share/icons/hicolor/32x32/status/tvconnected.svg
/usr/share/icons/hicolor/32x32/status/tvdisconnected.svg
/usr/share/icons/hicolor/32x32/status/tvtrusted.svg
/usr/share/icons/hicolor/scalable/apps/kdeconnect.svg
/usr/share/icons/hicolor/scalable/apps/kdeconnectindicator.svg
/usr/share/icons/hicolor/scalable/apps/kdeconnectindicatordark.svg
/usr/share/kdeconnect/kdeconnect_clipboard_config.qml
/usr/share/kdeconnect/kdeconnect_findthisdevice_config.qml
/usr/share/kdeconnect/kdeconnect_pausemusic_config.qml
/usr/share/kdeconnect/kdeconnect_runcommand_config.qml
/usr/share/kdeconnect/kdeconnect_sendnotifications_config.qml
/usr/share/kdeconnect/kdeconnect_share_config.qml
/usr/share/knotifications6/kdeconnect.notifyrc
/usr/share/metainfo/org.kde.kdeconnect.appdata.xml
/usr/share/metainfo/org.kde.kdeconnect.metainfo.xml
/usr/share/nautilus-python/extensions/kdeconnect-share.py
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Battery.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Clipboard.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Connectivity.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/DeviceDelegate.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/FindMyPhone.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/RemoteCommands.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/SMS.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Sftp.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Share.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/VirtualMonitor.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/metadata.json
/usr/share/qlogging-categories6/kdeconnect-kde.categories
/usr/share/xdg/autostart/org.kde.kdeconnect.daemon.desktop
/usr/share/zsh/site-functions/_kdeconnect

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/ca/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/de/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/de/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/en/kdeconnect/index.cache.bz2
/usr/share/doc/HTML/en/kdeconnect/index.docbook
/usr/share/doc/HTML/es/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/es/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/id/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/id/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/it/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/it/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/nl/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/nl/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/pt/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/pt/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/pt_BR/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/ru/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/ru/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/sl/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/sl/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/sv/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/sv/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/tr/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/tr/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/uk/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/uk/kdeconnect-kde/index.docbook
/usr/share/doc/HTML/zh_CN/kdeconnect-kde/index.cache.bz2
/usr/share/doc/HTML/zh_CN/kdeconnect-kde/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkdeconnectcore.so.24.12.0
/V3/usr/lib64/libkdeconnectpluginkcm.so.24.12.0
/V3/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_clipboard_config.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_findthisdevice_config.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_pausemusic_config.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_runcommand_config.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_sendnotifications_config.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_share_config.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_battery.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_bigscreen.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_clipboard.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_connectivity_report.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_contacts.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_findmyphone.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_findthisdevice.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_lockdevice.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mmtelephony.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mousepad.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mpriscontrol.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mprisremote.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_notifications.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_pausemusic.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_ping.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_presenter.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotecommands.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotecontrol.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotekeyboard.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotesystemvolume.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_runcommand.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_screensaver_inhibit.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_sendnotifications.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_sftp.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_share.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_sms.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_systemvolume.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_telephony.so
/V3/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_virtualmonitor.so
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/kdeconnectfileitemaction.so
/V3/usr/lib64/qt6/plugins/kf6/kio/kdeconnect.so
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kdeconnect.so
/V3/usr/lib64/qt6/qml/org/kde/kdeconnect/libkdeconnectdeclarativeplugin.so
/V3/usr/lib64/qt6/qml/org/kde/kdeconnect/private/findthisdevice/libkdeconnect_findthisdevice_qmlhelper.so
/usr/lib64/libkdeconnectcore.so.24
/usr/lib64/libkdeconnectcore.so.24.12.0
/usr/lib64/libkdeconnectpluginkcm.so.24
/usr/lib64/libkdeconnectpluginkcm.so.24.12.0
/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_clipboard_config.so
/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_findthisdevice_config.so
/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_pausemusic_config.so
/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_runcommand_config.so
/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_sendnotifications_config.so
/usr/lib64/qt6/plugins/kdeconnect/kcms/kdeconnect_share_config.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_battery.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_bigscreen.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_clipboard.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_connectivity_report.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_contacts.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_findmyphone.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_findthisdevice.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_lockdevice.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mmtelephony.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mousepad.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mpriscontrol.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_mprisremote.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_notifications.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_pausemusic.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_ping.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_presenter.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotecommands.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotecontrol.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotekeyboard.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_remotesystemvolume.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_runcommand.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_screensaver_inhibit.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_sendnotifications.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_sftp.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_share.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_sms.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_systemvolume.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_telephony.so
/usr/lib64/qt6/plugins/kdeconnect/kdeconnect_virtualmonitor.so
/usr/lib64/qt6/plugins/kf6/kfileitemaction/kdeconnectfileitemaction.so
/usr/lib64/qt6/plugins/kf6/kio/kdeconnect.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kdeconnect.so
/usr/lib64/qt6/qml/org/kde/kdeconnect/DBusProperty.qml
/usr/lib64/qt6/qml/org/kde/kdeconnect/PluginChecker.qml
/usr/lib64/qt6/qml/org/kde/kdeconnect/RemoteKeyboard.qml
/usr/lib64/qt6/qml/org/kde/kdeconnect/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kdeconnect/kdeconnectdeclarativeplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kdeconnect/libkdeconnectdeclarativeplugin.so
/usr/lib64/qt6/qml/org/kde/kdeconnect/private/findthisdevice/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kdeconnect/private/findthisdevice/kdeconnect_findthisdevice_qmlhelper.qmltypes
/usr/lib64/qt6/qml/org/kde/kdeconnect/private/findthisdevice/libkdeconnect_findthisdevice_qmlhelper.so
/usr/lib64/qt6/qml/org/kde/kdeconnect/private/findthisdevice/qmldir
/usr/lib64/qt6/qml/org/kde/kdeconnect/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdeconnect-kde/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdeconnect-kde/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdeconnect-kde/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdeconnect-kde/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdeconnect-kde/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdeconnect-kde/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593
/usr/share/package-licenses/kdeconnect-kde/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdeconnect-kde/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kdeconnect-kde/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/kdeconnect-kde/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kdeconnect-kde/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kdeconnect-app.lang -f kdeconnect-cli.lang -f kdeconnect-core.lang -f kdeconnect-fileitemaction.lang -f kdeconnect-indicator.lang -f kdeconnect-interfaces.lang -f kdeconnect-kcm.lang -f kdeconnect-kded.lang -f kdeconnect-kio.lang -f kdeconnect-nautilus-extension.lang -f kdeconnect-plugins.lang -f kdeconnect-settings.lang -f kdeconnect-sms.lang -f kdeconnect-urlhandler.lang -f plasma_applet_org.kde.kdeconnect.lang
%defattr(-,root,root,-)

