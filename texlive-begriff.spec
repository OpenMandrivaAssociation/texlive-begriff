Name:		texlive-begriff
Version:	15878
Release:	2
Summary:	Typeset Begriffschrift
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/begriff
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines maths mode commands for typesetting Frege's
Begriffschrift.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/begriff/begriff.sty
%doc %{_texmfdistdir}/doc/latex/begriff/COPYING
%doc %{_texmfdistdir}/doc/latex/begriff/README
%doc %{_texmfdistdir}/doc/latex/begriff/examples.pdf
%doc %{_texmfdistdir}/doc/latex/begriff/examples.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
