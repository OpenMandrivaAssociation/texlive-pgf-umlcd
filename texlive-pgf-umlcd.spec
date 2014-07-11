# revision 33307
# category Package
# catalog-ctan /graphics/pgf/contrib/pgf-umlcd
# catalog-date 2014-03-28 18:05:25 +0100
# catalog-license gpl
# catalog-version 0.2.1.1
Name:		texlive-pgf-umlcd
Version:	0.2.1.1
Release:	2
Summary:	Some LaTeX macros for UML Class Diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-umlcd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlcd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlcd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Some LaTeX macros for UML Class Diagrams.pgf.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgf-umlcd/pgf-umlcd.sty
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/COPYING
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/README
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/abstract-class.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/abstract-factory.svg
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/abstract-factory.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/aggregation.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/association.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/class.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/composition.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/implement-interface.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/inheritance.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/interface.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/note.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/object-include-methods.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/object.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/package.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/unidirectional-association.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/demo/visibility.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/logo.png
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/pgf-umlcd-manual.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd/pgf-umlcd-manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
