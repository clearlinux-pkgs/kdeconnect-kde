#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdeconnect-kde
Version  : 23.04.0
Release  : 35
URL      : https://download.kde.org/stable/release-service/23.04.0/src/kdeconnect-kde-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/kdeconnect-kde-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/kdeconnect-kde-23.04.0.tar.xz.sig
Summary  : Adds communication between KDE and your smartphone
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kdeconnect-kde-bin = %{version}-%{release}
Requires: kdeconnect-kde-data = %{version}-%{release}
Requires: kdeconnect-kde-lib = %{version}-%{release}
Requires: kdeconnect-kde-license = %{version}-%{release}
Requires: kdeconnect-kde-locales = %{version}-%{release}
BuildRequires : ModemManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kirigami2-dev
BuildRequires : kpackage-dev
BuildRequires : kpeople-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libfakekey-dev
BuildRequires : modemmanager-qt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libfakekey)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : qca-qt5-dev
BuildRequires : qqc2-desktop-style-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This plugin allows to control the system volume.

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
%setup -q -n kdeconnect-kde-23.04.0
cd %{_builddir}/kdeconnect-kde-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682115670
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682115670
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdeconnect-kde
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdeconnect-kde-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdeconnect-kde/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
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

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kdeconnectd

%files bin
%defattr(-,root,root,-)
/usr/bin/kdeconnect-app
/usr/bin/kdeconnect-cli
/usr/bin/kdeconnect-handler
/usr/bin/kdeconnect-indicator
/usr/bin/kdeconnect-settings
/usr/bin/kdeconnect-sms

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
/usr/share/applications/org.kde.kdeconnect_open.desktop
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
/usr/share/kdeconnect/kdeconnect_runcommand_config.qml
/usr/share/kdeconnect/kdeconnect_sendnotifications_config.qml
/usr/share/kdeconnect/kdeconnect_share_config.qml
/usr/share/knotifications5/kdeconnect.notifyrc
/usr/share/kservices5/plasma-kdeconnect.desktop
/usr/share/metainfo/org.kde.kdeconnect.appdata.xml
/usr/share/metainfo/org.kde.kdeconnect.metainfo.xml
/usr/share/nautilus-python/extensions/kdeconnect-share.py
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Battery.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Connectivity.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/DeviceDelegate.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/FindMyPhone.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Photo.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/RemoteCommands.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/SMS.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Sftp.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/Share.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/VirtualMonitor.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.kdeconnect/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.kdeconnect/metadata.json
/usr/share/qlogging-categories5/kdeconnect-kde.categories
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
/usr/lib64/libkdeconnectcore.so.23
/usr/lib64/libkdeconnectcore.so.23.04.0
/usr/lib64/libkdeconnectinterfaces.so.23
/usr/lib64/libkdeconnectinterfaces.so.23.04.0
/usr/lib64/libkdeconnectpluginkcm.so.23
/usr/lib64/libkdeconnectpluginkcm.so.23.04.0
/usr/lib64/qt5/plugins/kdeconnect/kcms/kdeconnect_clipboard_config.so
/usr/lib64/qt5/plugins/kdeconnect/kcms/kdeconnect_runcommand_config.so
/usr/lib64/qt5/plugins/kdeconnect/kcms/kdeconnect_sendnotifications_config.so
/usr/lib64/qt5/plugins/kdeconnect/kcms/kdeconnect_share_config.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_battery.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_bigscreen.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_clipboard.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_connectivity_report.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_contacts.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_findmyphone.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_lockdevice.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_mmtelephony.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_mousepad.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_mpriscontrol.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_mprisremote.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_notifications.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_photo.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_ping.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_presenter.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_remotecommands.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_remotecontrol.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_remotekeyboard.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_remotesystemvolume.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_runcommand.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_screensaver_inhibit.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_sendnotifications.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_sftp.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_share.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_sms.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_telephony.so
/usr/lib64/qt5/plugins/kdeconnect/kdeconnect_virtualmonitor.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/kdeconnectfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kio/kdeconnect.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kdeconnect.so
/usr/lib64/qt5/qml/org/kde/kdeconnect/DBusProperty.qml
/usr/lib64/qt5/qml/org/kde/kdeconnect/PluginChecker.qml
/usr/lib64/qt5/qml/org/kde/kdeconnect/RemoteKeyboard.qml
/usr/lib64/qt5/qml/org/kde/kdeconnect/libkdeconnectdeclarativeplugin.so
/usr/lib64/qt5/qml/org/kde/kdeconnect/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdeconnect-kde/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdeconnect-kde/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdeconnect-kde/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdeconnect-kde/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdeconnect-kde/6f1f675aa5f6a2bbaa573b8343044b166be28399
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

