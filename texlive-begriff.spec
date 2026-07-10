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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines maths mode commands for typesetting Frege's
Begriffschrift.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/begriff
%dir %{_datadir}/texmf-dist/tex/latex/begriff
%doc %{_datadir}/texmf-dist/doc/latex/begriff/COPYING
%doc %{_datadir}/texmf-dist/doc/latex/begriff/README
%doc %{_datadir}/texmf-dist/doc/latex/begriff/examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/begriff/examples.tex
%{_datadir}/texmf-dist/tex/latex/begriff/begriff.sty
