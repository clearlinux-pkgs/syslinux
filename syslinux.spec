#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : syslinux
Version  : 6.03
Release  : 6
URL      : https://www.kernel.org/pub/linux/utils/boot/syslinux/syslinux-6.03.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/boot/syslinux/syslinux-6.03.tar.xz
Summary  : Kernel loader which uses a FAT, ext2/3 or iso9660 filesystem or a PXE network
Group    : Development/Tools
License  : BSD-2-Clause-NetBSD BSD-3-Clause GPL-2.0 Libpng MIT
Requires: syslinux-bin
Requires: syslinux-data
BuildRequires : asciidoc
BuildRequires : nasm-bin
BuildRequires : pkgconfig(uuid)
Patch1: 0035-SYSAPPEND-Fix-space-stripping.patch
Patch2: fix-alignment-change-gcc-5.patch
Patch3: dont-guess-section-alignment.patch

%description
SYSLINUX is a suite of bootloaders, currently supporting DOS FAT
filesystems, Linux ext2/ext3 filesystems (EXTLINUX), PXE network boots
(PXELINUX), or ISO 9660 CD-ROMs (ISOLINUX).  It also includes a tool,
MEMDISK, which loads legacy operating systems from these media.

%package bin
Summary: bin components for the syslinux package.
Group: Binaries
Requires: syslinux-data

%description bin
bin components for the syslinux package.


%package data
Summary: data components for the syslinux package.
Group: Data

%description data
data components for the syslinux package.


%package dev
Summary: dev components for the syslinux package.
Group: Development
Requires: syslinux-bin
Requires: syslinux-data
Provides: syslinux-devel

%description dev
dev components for the syslinux package.


%package extras
Summary: extras components for the syslinux package.
Group: Default

%description extras
extras components for the syslinux package.


%prep
%setup -q -n syslinux-6.03
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/man/man1/extlinux.1
/usr/man/man1/gethostip.1
/usr/man/man1/isohybrid.1
/usr/man/man1/lss16toppm.1
/usr/man/man1/memdiskfind.1
/usr/man/man1/ppmtolss16.1
/usr/man/man1/syslinux.1
/usr/man/man1/syslinux2ansi.1

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/isohybrid.pl
%exclude /usr/bin/keytab-lilo
%exclude /usr/bin/lss16toppm
%exclude /usr/bin/md5pass
%exclude /usr/bin/mkdiskimage
%exclude /usr/bin/ppmtolss16
%exclude /usr/bin/pxelinux-options
%exclude /usr/bin/sha1pass
%exclude /usr/bin/syslinux2ansi
/usr/bin/extlinux
/usr/bin/gethostip
/usr/bin/isohybrid
/usr/bin/memdiskfind
/usr/bin/syslinux

%files data
%defattr(-,root,root,-)
%exclude /usr/share/syslinux/altmbr.bin
%exclude /usr/share/syslinux/altmbr_c.bin
%exclude /usr/share/syslinux/altmbr_f.bin
%exclude /usr/share/syslinux/cat.c32
%exclude /usr/share/syslinux/chain.c32
%exclude /usr/share/syslinux/cmd.c32
%exclude /usr/share/syslinux/cmenu.c32
%exclude /usr/share/syslinux/com32/com32.ld
%exclude /usr/share/syslinux/com32/include/gplinclude/README
%exclude /usr/share/syslinux/com32/libgpl.c32
%exclude /usr/share/syslinux/config.c32
%exclude /usr/share/syslinux/cptime.c32
%exclude /usr/share/syslinux/cpu.c32
%exclude /usr/share/syslinux/cpuid.c32
%exclude /usr/share/syslinux/cpuidtest.c32
%exclude /usr/share/syslinux/debug.c32
%exclude /usr/share/syslinux/dhcp.c32
%exclude /usr/share/syslinux/diag/geodsp1s.img.xz
%exclude /usr/share/syslinux/diag/geodspms.img.xz
%exclude /usr/share/syslinux/diag/handoff.bin
%exclude /usr/share/syslinux/disk.c32
%exclude /usr/share/syslinux/dmi.c32
%exclude /usr/share/syslinux/dmitest.c32
%exclude /usr/share/syslinux/dosutil/copybs.com
%exclude /usr/share/syslinux/dosutil/eltorito.sys
%exclude /usr/share/syslinux/dosutil/mdiskchk.com
%exclude /usr/share/syslinux/efi32/cat.c32
%exclude /usr/share/syslinux/efi32/chain.c32
%exclude /usr/share/syslinux/efi32/cmd.c32
%exclude /usr/share/syslinux/efi32/cmenu.c32
%exclude /usr/share/syslinux/efi32/config.c32
%exclude /usr/share/syslinux/efi32/cptime.c32
%exclude /usr/share/syslinux/efi32/cpu.c32
%exclude /usr/share/syslinux/efi32/cpuid.c32
%exclude /usr/share/syslinux/efi32/cpuidtest.c32
%exclude /usr/share/syslinux/efi32/debug.c32
%exclude /usr/share/syslinux/efi32/dhcp.c32
%exclude /usr/share/syslinux/efi32/disk.c32
%exclude /usr/share/syslinux/efi32/dmi.c32
%exclude /usr/share/syslinux/efi32/dmitest.c32
%exclude /usr/share/syslinux/efi32/elf.c32
%exclude /usr/share/syslinux/efi32/ethersel.c32
%exclude /usr/share/syslinux/efi32/gfxboot.c32
%exclude /usr/share/syslinux/efi32/gpxecmd.c32
%exclude /usr/share/syslinux/efi32/hdt.c32
%exclude /usr/share/syslinux/efi32/hexdump.c32
%exclude /usr/share/syslinux/efi32/host.c32
%exclude /usr/share/syslinux/efi32/ifcpu.c32
%exclude /usr/share/syslinux/efi32/ifcpu64.c32
%exclude /usr/share/syslinux/efi32/ifmemdsk.c32
%exclude /usr/share/syslinux/efi32/ifplop.c32
%exclude /usr/share/syslinux/efi32/kbdmap.c32
%exclude /usr/share/syslinux/efi32/kontron_wdt.c32
%exclude /usr/share/syslinux/efi32/ldlinux.e32
%exclude /usr/share/syslinux/efi32/lfs.c32
%exclude /usr/share/syslinux/efi32/libcom32.c32
%exclude /usr/share/syslinux/efi32/libgpl.c32
%exclude /usr/share/syslinux/efi32/liblua.c32
%exclude /usr/share/syslinux/efi32/libmenu.c32
%exclude /usr/share/syslinux/efi32/libutil.c32
%exclude /usr/share/syslinux/efi32/linux.c32
%exclude /usr/share/syslinux/efi32/ls.c32
%exclude /usr/share/syslinux/efi32/lua.c32
%exclude /usr/share/syslinux/efi32/mboot.c32
%exclude /usr/share/syslinux/efi32/meminfo.c32
%exclude /usr/share/syslinux/efi32/menu.c32
%exclude /usr/share/syslinux/efi32/pci.c32
%exclude /usr/share/syslinux/efi32/pcitest.c32
%exclude /usr/share/syslinux/efi32/pmload.c32
%exclude /usr/share/syslinux/efi32/poweroff.c32
%exclude /usr/share/syslinux/efi32/prdhcp.c32
%exclude /usr/share/syslinux/efi32/pwd.c32
%exclude /usr/share/syslinux/efi32/pxechn.c32
%exclude /usr/share/syslinux/efi32/reboot.c32
%exclude /usr/share/syslinux/efi32/rosh.c32
%exclude /usr/share/syslinux/efi32/sanboot.c32
%exclude /usr/share/syslinux/efi32/sdi.c32
%exclude /usr/share/syslinux/efi32/sysdump.c32
%exclude /usr/share/syslinux/efi32/syslinux.c32
%exclude /usr/share/syslinux/efi32/syslinux.efi
%exclude /usr/share/syslinux/efi32/vesa.c32
%exclude /usr/share/syslinux/efi32/vesainfo.c32
%exclude /usr/share/syslinux/efi32/vesamenu.c32
%exclude /usr/share/syslinux/efi32/vpdtest.c32
%exclude /usr/share/syslinux/efi32/whichsys.c32
%exclude /usr/share/syslinux/efi32/zzjson.c32
%exclude /usr/share/syslinux/efi64/cat.c32
%exclude /usr/share/syslinux/efi64/chain.c32
%exclude /usr/share/syslinux/efi64/cmd.c32
%exclude /usr/share/syslinux/efi64/cmenu.c32
%exclude /usr/share/syslinux/efi64/config.c32
%exclude /usr/share/syslinux/efi64/cptime.c32
%exclude /usr/share/syslinux/efi64/cpu.c32
%exclude /usr/share/syslinux/efi64/cpuid.c32
%exclude /usr/share/syslinux/efi64/cpuidtest.c32
%exclude /usr/share/syslinux/efi64/debug.c32
%exclude /usr/share/syslinux/efi64/dhcp.c32
%exclude /usr/share/syslinux/efi64/disk.c32
%exclude /usr/share/syslinux/efi64/dmi.c32
%exclude /usr/share/syslinux/efi64/dmitest.c32
%exclude /usr/share/syslinux/efi64/elf.c32
%exclude /usr/share/syslinux/efi64/ethersel.c32
%exclude /usr/share/syslinux/efi64/gfxboot.c32
%exclude /usr/share/syslinux/efi64/gpxecmd.c32
%exclude /usr/share/syslinux/efi64/hdt.c32
%exclude /usr/share/syslinux/efi64/hexdump.c32
%exclude /usr/share/syslinux/efi64/host.c32
%exclude /usr/share/syslinux/efi64/ifcpu.c32
%exclude /usr/share/syslinux/efi64/ifcpu64.c32
%exclude /usr/share/syslinux/efi64/ifmemdsk.c32
%exclude /usr/share/syslinux/efi64/ifplop.c32
%exclude /usr/share/syslinux/efi64/kbdmap.c32
%exclude /usr/share/syslinux/efi64/kontron_wdt.c32
%exclude /usr/share/syslinux/efi64/ldlinux.e64
%exclude /usr/share/syslinux/efi64/lfs.c32
%exclude /usr/share/syslinux/efi64/libcom32.c32
%exclude /usr/share/syslinux/efi64/libgpl.c32
%exclude /usr/share/syslinux/efi64/liblua.c32
%exclude /usr/share/syslinux/efi64/libmenu.c32
%exclude /usr/share/syslinux/efi64/libutil.c32
%exclude /usr/share/syslinux/efi64/linux.c32
%exclude /usr/share/syslinux/efi64/ls.c32
%exclude /usr/share/syslinux/efi64/lua.c32
%exclude /usr/share/syslinux/efi64/mboot.c32
%exclude /usr/share/syslinux/efi64/meminfo.c32
%exclude /usr/share/syslinux/efi64/menu.c32
%exclude /usr/share/syslinux/efi64/pci.c32
%exclude /usr/share/syslinux/efi64/pcitest.c32
%exclude /usr/share/syslinux/efi64/pmload.c32
%exclude /usr/share/syslinux/efi64/poweroff.c32
%exclude /usr/share/syslinux/efi64/prdhcp.c32
%exclude /usr/share/syslinux/efi64/pwd.c32
%exclude /usr/share/syslinux/efi64/pxechn.c32
%exclude /usr/share/syslinux/efi64/reboot.c32
%exclude /usr/share/syslinux/efi64/rosh.c32
%exclude /usr/share/syslinux/efi64/sanboot.c32
%exclude /usr/share/syslinux/efi64/sdi.c32
%exclude /usr/share/syslinux/efi64/sysdump.c32
%exclude /usr/share/syslinux/efi64/syslinux.c32
%exclude /usr/share/syslinux/efi64/vesa.c32
%exclude /usr/share/syslinux/efi64/vesainfo.c32
%exclude /usr/share/syslinux/efi64/vesamenu.c32
%exclude /usr/share/syslinux/efi64/vpdtest.c32
%exclude /usr/share/syslinux/efi64/whichsys.c32
%exclude /usr/share/syslinux/efi64/zzjson.c32
%exclude /usr/share/syslinux/elf.c32
%exclude /usr/share/syslinux/ethersel.c32
%exclude /usr/share/syslinux/gfxboot.c32
%exclude /usr/share/syslinux/gptmbr_c.bin
%exclude /usr/share/syslinux/gptmbr_f.bin
%exclude /usr/share/syslinux/gpxecmd.c32
%exclude /usr/share/syslinux/gpxelinux.0
%exclude /usr/share/syslinux/gpxelinuxk.0
%exclude /usr/share/syslinux/hdt.c32
%exclude /usr/share/syslinux/hexdump.c32
%exclude /usr/share/syslinux/host.c32
%exclude /usr/share/syslinux/ifcpu.c32
%exclude /usr/share/syslinux/ifcpu64.c32
%exclude /usr/share/syslinux/ifmemdsk.c32
%exclude /usr/share/syslinux/ifplop.c32
%exclude /usr/share/syslinux/isohdpfx.bin
%exclude /usr/share/syslinux/isohdpfx_c.bin
%exclude /usr/share/syslinux/isohdpfx_f.bin
%exclude /usr/share/syslinux/isohdppx.bin
%exclude /usr/share/syslinux/isohdppx_c.bin
%exclude /usr/share/syslinux/isohdppx_f.bin
%exclude /usr/share/syslinux/isolinux-debug.bin
%exclude /usr/share/syslinux/isolinux.bin
%exclude /usr/share/syslinux/kbdmap.c32
%exclude /usr/share/syslinux/kontron_wdt.c32
%exclude /usr/share/syslinux/ldlinux.c32
%exclude /usr/share/syslinux/lfs.c32
%exclude /usr/share/syslinux/libcom32.c32
%exclude /usr/share/syslinux/libgpl.c32
%exclude /usr/share/syslinux/liblua.c32
%exclude /usr/share/syslinux/libmenu.c32
%exclude /usr/share/syslinux/libutil.c32
%exclude /usr/share/syslinux/linux.c32
%exclude /usr/share/syslinux/lpxelinux.0
%exclude /usr/share/syslinux/ls.c32
%exclude /usr/share/syslinux/lua.c32
%exclude /usr/share/syslinux/mboot.c32
%exclude /usr/share/syslinux/mbr.bin
%exclude /usr/share/syslinux/mbr_c.bin
%exclude /usr/share/syslinux/mbr_f.bin
%exclude /usr/share/syslinux/memdisk
%exclude /usr/share/syslinux/meminfo.c32
%exclude /usr/share/syslinux/menu.c32
%exclude /usr/share/syslinux/pci.c32
%exclude /usr/share/syslinux/pcitest.c32
%exclude /usr/share/syslinux/pmload.c32
%exclude /usr/share/syslinux/poweroff.c32
%exclude /usr/share/syslinux/prdhcp.c32
%exclude /usr/share/syslinux/pwd.c32
%exclude /usr/share/syslinux/pxechn.c32
%exclude /usr/share/syslinux/pxelinux.0
%exclude /usr/share/syslinux/reboot.c32
%exclude /usr/share/syslinux/rosh.c32
%exclude /usr/share/syslinux/sanboot.c32
%exclude /usr/share/syslinux/sdi.c32
%exclude /usr/share/syslinux/sysdump.c32
%exclude /usr/share/syslinux/syslinux.c32
%exclude /usr/share/syslinux/syslinux.com
%exclude /usr/share/syslinux/vesa.c32
%exclude /usr/share/syslinux/vesainfo.c32
%exclude /usr/share/syslinux/vesamenu.c32
%exclude /usr/share/syslinux/vpdtest.c32
%exclude /usr/share/syslinux/whichsys.c32
%exclude /usr/share/syslinux/zzjson.c32
/usr/share/syslinux/efi64/syslinux.efi
/usr/share/syslinux/gptmbr.bin

%files dev
%defattr(-,root,root,-)
/usr/share/syslinux/com32/include/alloca.h
/usr/share/syslinux/com32/include/assert.h
/usr/share/syslinux/com32/include/bitsize/limits.h
/usr/share/syslinux/com32/include/bitsize/stddef.h
/usr/share/syslinux/com32/include/bitsize/stdint.h
/usr/share/syslinux/com32/include/bitsize/stdintconst.h
/usr/share/syslinux/com32/include/bitsize/stdintlimits.h
/usr/share/syslinux/com32/include/bitsize32/limits.h
/usr/share/syslinux/com32/include/bitsize32/stddef.h
/usr/share/syslinux/com32/include/bitsize32/stdint.h
/usr/share/syslinux/com32/include/bitsize32/stdintconst.h
/usr/share/syslinux/com32/include/bitsize32/stdintlimits.h
/usr/share/syslinux/com32/include/bitsize64/limits.h
/usr/share/syslinux/com32/include/bitsize64/stddef.h
/usr/share/syslinux/com32/include/bitsize64/stdint.h
/usr/share/syslinux/com32/include/bitsize64/stdintconst.h
/usr/share/syslinux/com32/include/bitsize64/stdintlimits.h
/usr/share/syslinux/com32/include/bufprintf.h
/usr/share/syslinux/com32/include/byteswap.h
/usr/share/syslinux/com32/include/cli.h
/usr/share/syslinux/com32/include/colortbl.h
/usr/share/syslinux/com32/include/com32.h
/usr/share/syslinux/com32/include/console.h
/usr/share/syslinux/com32/include/cpufeature.h
/usr/share/syslinux/com32/include/ctype.h
/usr/share/syslinux/com32/include/dev.h
/usr/share/syslinux/com32/include/dhcp.h
/usr/share/syslinux/com32/include/dirent.h
/usr/share/syslinux/com32/include/dprintf.h
/usr/share/syslinux/com32/include/elf.h
/usr/share/syslinux/com32/include/endian.h
/usr/share/syslinux/com32/include/errno.h
/usr/share/syslinux/com32/include/fcntl.h
/usr/share/syslinux/com32/include/getopt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/acpi.h
/usr/share/syslinux/com32/include/gplinclude/acpi/boot.h
/usr/share/syslinux/com32/include/gplinclude/acpi/dsdt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/ecdt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/facs.h
/usr/share/syslinux/com32/include/gplinclude/acpi/fadt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/hpet.h
/usr/share/syslinux/com32/include/gplinclude/acpi/madt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/mcfg.h
/usr/share/syslinux/com32/include/gplinclude/acpi/rsdp.h
/usr/share/syslinux/com32/include/gplinclude/acpi/rsdt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/sbst.h
/usr/share/syslinux/com32/include/gplinclude/acpi/slic.h
/usr/share/syslinux/com32/include/gplinclude/acpi/ssdt.h
/usr/share/syslinux/com32/include/gplinclude/acpi/structs.h
/usr/share/syslinux/com32/include/gplinclude/acpi/tcpa.h
/usr/share/syslinux/com32/include/gplinclude/acpi/xsdt.h
/usr/share/syslinux/com32/include/gplinclude/cpuid.h
/usr/share/syslinux/com32/include/gplinclude/disk/bootloaders.h
/usr/share/syslinux/com32/include/gplinclude/disk/common.h
/usr/share/syslinux/com32/include/gplinclude/disk/errno_disk.h
/usr/share/syslinux/com32/include/gplinclude/disk/error.h
/usr/share/syslinux/com32/include/gplinclude/disk/geom.h
/usr/share/syslinux/com32/include/gplinclude/disk/mbrs.h
/usr/share/syslinux/com32/include/gplinclude/disk/msdos.h
/usr/share/syslinux/com32/include/gplinclude/disk/partition.h
/usr/share/syslinux/com32/include/gplinclude/disk/read.h
/usr/share/syslinux/com32/include/gplinclude/disk/swsusp.h
/usr/share/syslinux/com32/include/gplinclude/disk/util.h
/usr/share/syslinux/com32/include/gplinclude/disk/write.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_base_board.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_battery.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_bios.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_cache.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_chassis.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_ipmi.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_memory.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_processor.h
/usr/share/syslinux/com32/include/gplinclude/dmi/dmi_system.h
/usr/share/syslinux/com32/include/gplinclude/memory.h
/usr/share/syslinux/com32/include/gplinclude/vpd/vpd.h
/usr/share/syslinux/com32/include/gplinclude/zzjson/zzjson.h
/usr/share/syslinux/com32/include/hw/vga.h
/usr/share/syslinux/com32/include/ilog2.h
/usr/share/syslinux/com32/include/inttypes.h
/usr/share/syslinux/com32/include/klibc/archsetjmp.h
/usr/share/syslinux/com32/include/klibc/compiler.h
/usr/share/syslinux/com32/include/klibc/diverr.h
/usr/share/syslinux/com32/include/klibc/endian.h
/usr/share/syslinux/com32/include/klibc/extern.h
/usr/share/syslinux/com32/include/klibc/i386/archsetjmp.h
/usr/share/syslinux/com32/include/klibc/sysconfig.h
/usr/share/syslinux/com32/include/klibc/x86_64/archsetjmp.h
/usr/share/syslinux/com32/include/libansi.h
/usr/share/syslinux/com32/include/limits.h
/usr/share/syslinux/com32/include/linux/list.h
/usr/share/syslinux/com32/include/math.h
/usr/share/syslinux/com32/include/menu.h
/usr/share/syslinux/com32/include/minmax.h
/usr/share/syslinux/com32/include/netinet/in.h
/usr/share/syslinux/com32/include/png.h
/usr/share/syslinux/com32/include/pngconf.h
/usr/share/syslinux/com32/include/refstr.h
/usr/share/syslinux/com32/include/setjmp.h
/usr/share/syslinux/com32/include/sort.h
/usr/share/syslinux/com32/include/stdarg.h
/usr/share/syslinux/com32/include/stdbool.h
/usr/share/syslinux/com32/include/stddef.h
/usr/share/syslinux/com32/include/stdint.h
/usr/share/syslinux/com32/include/stdio.h
/usr/share/syslinux/com32/include/stdlib.h
/usr/share/syslinux/com32/include/string.h
/usr/share/syslinux/com32/include/suffix_number.h
/usr/share/syslinux/com32/include/sys/bitops.h
/usr/share/syslinux/com32/include/sys/cpu.h
/usr/share/syslinux/com32/include/sys/dirent.h
/usr/share/syslinux/com32/include/sys/elf32.h
/usr/share/syslinux/com32/include/sys/elf64.h
/usr/share/syslinux/com32/include/sys/elfcommon.h
/usr/share/syslinux/com32/include/sys/exec.h
/usr/share/syslinux/com32/include/sys/fpu.h
/usr/share/syslinux/com32/include/sys/gpxe.h
/usr/share/syslinux/com32/include/sys/i386/bitops.h
/usr/share/syslinux/com32/include/sys/i386/cpu.h
/usr/share/syslinux/com32/include/sys/i386/module.h
/usr/share/syslinux/com32/include/sys/io.h
/usr/share/syslinux/com32/include/sys/module.h
/usr/share/syslinux/com32/include/sys/pci.h
/usr/share/syslinux/com32/include/sys/stat.h
/usr/share/syslinux/com32/include/sys/time.h
/usr/share/syslinux/com32/include/sys/times.h
/usr/share/syslinux/com32/include/sys/types.h
/usr/share/syslinux/com32/include/sys/x86_64/bitops.h
/usr/share/syslinux/com32/include/sys/x86_64/cpu.h
/usr/share/syslinux/com32/include/sys/x86_64/module.h
/usr/share/syslinux/com32/include/syslinux/adv.h
/usr/share/syslinux/com32/include/syslinux/advconst.h
/usr/share/syslinux/com32/include/syslinux/align.h
/usr/share/syslinux/com32/include/syslinux/boot.h
/usr/share/syslinux/com32/include/syslinux/bootpm.h
/usr/share/syslinux/com32/include/syslinux/bootrm.h
/usr/share/syslinux/com32/include/syslinux/config.h
/usr/share/syslinux/com32/include/syslinux/debug.h
/usr/share/syslinux/com32/include/syslinux/disk.h
/usr/share/syslinux/com32/include/syslinux/firmware.h
/usr/share/syslinux/com32/include/syslinux/idle.h
/usr/share/syslinux/com32/include/syslinux/io.h
/usr/share/syslinux/com32/include/syslinux/keyboard.h
/usr/share/syslinux/com32/include/syslinux/linux.h
/usr/share/syslinux/com32/include/syslinux/loadfile.h
/usr/share/syslinux/com32/include/syslinux/memscan.h
/usr/share/syslinux/com32/include/syslinux/movebits.h
/usr/share/syslinux/com32/include/syslinux/pmapi.h
/usr/share/syslinux/com32/include/syslinux/pxe.h
/usr/share/syslinux/com32/include/syslinux/pxe_api.h
/usr/share/syslinux/com32/include/syslinux/reboot.h
/usr/share/syslinux/com32/include/syslinux/resolve.h
/usr/share/syslinux/com32/include/syslinux/sysappend.h
/usr/share/syslinux/com32/include/syslinux/version.h
/usr/share/syslinux/com32/include/syslinux/vesacon.h
/usr/share/syslinux/com32/include/syslinux/video.h
/usr/share/syslinux/com32/include/syslinux/zio.h
/usr/share/syslinux/com32/include/time.h
/usr/share/syslinux/com32/include/tinyjpeg.h
/usr/share/syslinux/com32/include/unistd.h
/usr/share/syslinux/com32/include/zconf.h
/usr/share/syslinux/com32/include/zlib.h

%files extras
%defattr(-,root,root,-)
/usr/bin/isohybrid.pl
/usr/bin/keytab-lilo
/usr/bin/lss16toppm
/usr/bin/md5pass
/usr/bin/mkdiskimage
/usr/bin/ppmtolss16
/usr/bin/pxelinux-options
/usr/bin/sha1pass
/usr/bin/syslinux2ansi
