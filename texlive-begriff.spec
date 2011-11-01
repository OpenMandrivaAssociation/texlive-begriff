Name:		texlive-begriff
Version:	1.6
Release:	1
Summary:	Typeset Begriffschrift
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/begriff
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines maths mode commands for typesetting Frege's
Begriffschrift.

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
%{_texmfdistdir}/tex/latex/begriff/begriff.sty
%doc %{_texmfdistdir}/doc/latex/begriff/COPYING
%doc %{_texmfdistdir}/doc/latex/begriff/README
%doc %{_texmfdistdir}/doc/latex/begriff/examples.pdf
%doc %{_texmfdistdir}/doc/latex/begriff/examples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
