%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.02-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Quechua
%define languagecode qu
# FIXME: no locale yet
%define lc_ctype qu_PE

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       20040424.1
Release:       %mkrel 12
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
#Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 20040424.1-10mdv2011.0
+ Revision: 662862
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 20040424.1-9mdv2011.0
+ Revision: 603455
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 20040424.1-8mdv2010.1
+ Revision: 518956
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 20040424.1-7mdv2010.0
+ Revision: 413098
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 20040424.1-6mdv2009.1
+ Revision: 350090
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 20040424.1-5mdv2009.0
+ Revision: 220440
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 20040424.1-4mdv2008.1
+ Revision: 182629
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 20040424.1-2mdv2007.0
+ Revision: 123353
- Import aspell-qu

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 20040424.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 20040424.1-1mdk
- first version

