# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/stubs
# catalog-date 2008-08-23 22:26:13 +0200
# catalog-license gpl
# catalog-version 0.1.1
Name:		texlive-stubs
Version:	0.1.1
Release:	5
Summary:	Create tear-off stubs at the bottom of a page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stubs
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stubs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stubs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The \stubs command creates as many repetitions as possible of
its argument, at the bottom of the page; these stubs may be
used (for example) for contact information.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stubs/stubs.sty
%doc %{_texmfdistdir}/doc/latex/stubs/COPYING
%doc %{_texmfdistdir}/doc/latex/stubs/README
%doc %{_texmfdistdir}/doc/latex/stubs/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/stubs/changelog.txt
%doc %{_texmfdistdir}/doc/latex/stubs/stubs_ex.pdf
%doc %{_texmfdistdir}/doc/latex/stubs/stubs_ex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-2
+ Revision: 756266
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-1
+ Revision: 719597
- texlive-stubs
- texlive-stubs
- texlive-stubs
- texlive-stubs

