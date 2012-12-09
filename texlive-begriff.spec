# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/begriff
# catalog-date 2007-01-29 23:57:18 +0100
# catalog-license gpl
# catalog-version 1.6
Name:		texlive-begriff
Version:	1.6
Release:	2
Summary:	Typeset Begriffschrift
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/begriff
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begriff.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 749563
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 717904
- texlive-begriff
- texlive-begriff
- texlive-begriff
- texlive-begriff
- texlive-begriff

