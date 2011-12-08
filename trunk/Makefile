all:	book.tex
	pdflatex book
	makeindex book
	mv book.pdf pythonhydro.pdf
	evince pythonhydro.pdf

hevea:	book.tex header.html footer.html
	rm -rf html
	mkdir html
	hevea -O -e latexonly htmlonly book
	imagen -png book
	hacha book.html
	cp up.png next.png back.png html
	mv index.html book.css book*.html book*.png *motif.gif html

DEST = /home/downey/public_html/greent/pythonhydro

epub:
	cd html; ebook-convert index.html pythonhydro.epub

distrib:
	rm -rf dist
	rsync -a pythonhydro.pdf pythonhydro.html $(DEST)
	rsync -a images/cover_small.png $(DEST)/images
	chmod -R o+r $(DEST)/*

clean:
	rm -f *~ *.aux *.log *.dvi *.idx *.ilg *.ind *.toc



