Name:		texlive-pgf-umlcd
Version:	63386
Release:	2
Summary:	Some LaTeX macros for UML Class Diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-umlcd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlcd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlcd.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/pgf-umlcd
%doc %{_texmfdistdir}/doc/latex/pgf-umlcd

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
