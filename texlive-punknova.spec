# revision 24649
# category Package
# catalog-ctan /fonts/punknova
# catalog-date 2011-11-23 11:34:47 +0100
# catalog-license other-free
# catalog-version 1.003
Name:		texlive-punknova
Version:	1.003
Release:	5
Summary:	OpenType version of Knuth's Punk font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/punknova
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font was generated from a MetaPost version of the sources
of the 'original' punk font. Knuth's original fonts generated
different shapes at random. This isn't actually possible in an
OpenType font; rather, the font contains several variants of
each glyph, and uses the OpenType randomize function to select
a variant for each invocation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-bold.otf
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-boldslanted.otf
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-regular.otf
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-slanted.otf
%doc %{_texmfdistdir}/doc/fonts/punknova/Makefile
%doc %{_texmfdistdir}/doc/fonts/punknova/NEWS
%doc %{_texmfdistdir}/doc/fonts/punknova/README
%doc %{_texmfdistdir}/doc/fonts/punknova/documentation/documentation-sources/sample.tex
%doc %{_texmfdistdir}/doc/fonts/punknova/documentation/sample.pdf
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-bold.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-boldslanted.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-regular.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-slanted.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/tools/build.py

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.003-2
+ Revision: 755527
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.003-1
+ Revision: 739873
- texlive-punknova

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.002-1
+ Revision: 719414
- texlive-punknova
- texlive-punknova
- texlive-punknova
- texlive-punknova

