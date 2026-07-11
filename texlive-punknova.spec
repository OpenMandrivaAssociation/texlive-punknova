%global tl_name punknova
%global tl_revision 24649

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.003
Release:	%{tl_revision}.1
Summary:	OpenType version of Knuths Punk font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/punknova
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/punknova.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The font was generated from a MetaPost version of the sources of the
'original' punk font. Knuth's original fonts generated different shapes
at random. This isn't actually possible in an OpenType font; rather, the
font contains several variants of each glyph, and uses the OpenType
randomize function to select a variant for each invocation.

