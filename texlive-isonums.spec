# revision 17362
# category Package
# catalog-ctan /macros/latex/contrib/isonums
# catalog-date 2010-03-09 13:05:51 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-isonums
Version:	1.0
Release:	1
Summary:	Display numbers in maths mode according to ISO 31-0
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isonums
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isonums.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isonums.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package makes a quick hack to ziffer to display numbers in
maths mode according to ISO 31-0, regardless of input format
(European $1.235,7$ or Anglo-American $1,235.7$). The options
[euro, anglo] control the global input format. Default input
format is anglo. Documentation is included as comments to the
text source.

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
%{_texmfdistdir}/tex/latex/isonums/isonums.sty
%doc %{_texmfdistdir}/doc/latex/isonums/isonums.pdf
%doc %{_texmfdistdir}/doc/latex/isonums/isonums.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
