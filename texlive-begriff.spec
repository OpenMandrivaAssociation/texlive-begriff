%global tl_name begriff
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Typeset Begriffschrift
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/begriff
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines maths mode commands for typesetting Frege's
Begriffschrift.

