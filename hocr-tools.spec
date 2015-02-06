Name:		hocr-tools
Version:	20091007
Release:	2
Summary:	Tools for manipulating and evaluating the hOCR format
Group:		Office
License:	Apache License
URL:		https://code.google.com/p/hocr-tools/
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	python

%description
OCR is a format for representing OCR output, including layout information,
character confidences, bounding boxes, and style information. It embeds this
information invisibly in standard HTML. By building on standard HTML, it
automatically inherits well-defined support for most scripts, languages,
and common layout options. Furthermore, unlike previous OCR formats,
the recognized text and OCR-related information co-exist in the same file
and survives editing and manipulation. hOCR markup is independent
of the presentation.

Included command line programs:

 -  hocr-check -- check the hOCR file for errors
 -  hocr-combine -- combine pages in multiple hOCR files into a single document
 -  hocr-eval -- compute number of segmentation and OCR errors
 -  hocr-eval-geom -- compute over, under, and mis-segmentations
 -  hocr-eval-lines -- compute OCR errors of hOCR output relative to text
ground truth
 -  hocr-split -- split an hOCR file into individual pages
 -  hocr-merge-dc -- merge Dublin Core meta data into the hOCR HTML header

%prep
%setup -q

%build

%install
for file in hocr-*
do
install -D -m 0755 $file %{buildroot}%{_bindir}/$file
done

%files
%doc README
%{_bindir}/hocr-*


%changelog
* Fri Nov 11 2011 Andrey Smirnov <asmirnov@mandriva.org> 20091007-1
+ Revision: 730075
- imported package hocr-tools

