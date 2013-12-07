# revision 17362
# category Package
# catalog-ctan /macros/latex/contrib/isonums
# catalog-date 2010-03-09 13:05:51 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-isonums
Version:	1.0
Release:	3
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752812
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718739
- texlive-isonums
- texlive-isonums
- texlive-isonums
- texlive-isonums

