# revision 19714
# category Package
# catalog-ctan /fonts/punknova
# catalog-date 2010-09-13 12:44:18 +0200
# catalog-license other-free
# catalog-version 1.002
Name:		texlive-punknova
Version:	1.002
Release:	1
Summary:	OpenType version of Knuth's Punk font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/punknova
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The font was generated from a MetaPost version of the sources
of the 'original' punk font. Knuth's original fonts generated
different shapes at random. This isn't actually possible in an
OpenType font; rather, the font contains several variants of
each glyph, and uses the OpenType randomize function to select
a variant for each invocation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-bold.otf
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-boldslanted.otf
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-regular.otf
%{_texmfdistdir}/fonts/opentype/public/punknova/punknova-slanted.otf
%doc %{_texmfdistdir}/doc/fonts/punknova/NEWS
%doc %{_texmfdistdir}/doc/fonts/punknova/README
%doc %{_texmfdistdir}/doc/fonts/punknova/documentation/documentation-sources/sample.tex
%doc %{_texmfdistdir}/doc/fonts/punknova/documentation/sample.pdf
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-bold.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-boldslanted.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-characters.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-definitions.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont-slanted.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/source/punkfont.mp
%doc %{_texmfdistdir}/doc/fonts/punknova/tools/build.py
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
