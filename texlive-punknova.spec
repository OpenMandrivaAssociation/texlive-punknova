Name:		texlive-punknova
Version:	24649
Release:	2
Summary:	OpenType version of Knuth's Punk font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/punknova
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
