Name:		texlive-isonums
Version:	17362
Release:	2
Summary:	Display numbers in maths mode according to ISO 31-0
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isonums
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isonums.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isonums.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes a quick hack to ziffer to display numbers in
maths mode according to ISO 31-0, regardless of input format
(European $1.235,7$ or Anglo-American $1,235.7$). The options
[euro, anglo] control the global input format. Default input
format is anglo. Documentation is included as comments to the
text source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isonums/isonums.sty
%doc %{_texmfdistdir}/doc/latex/isonums/isonums.pdf
%doc %{_texmfdistdir}/doc/latex/isonums/isonums.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
