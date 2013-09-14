PDF = 2015_AA2_FR_onitu.pdf
TPL = tpl.tex
SRC = title.md introduction.md taille_et_performance.md qualite.md
HEADER = resume.tex header.tex

FLAGS = --chapters --toc --template=$(TPL) $(HEADER:%=-B %)

PICTURES = 

GEN = $(PDF)

$(PDF):	$(SRC) $(TPL) $(HEADER) $(PICTURES)
	pandoc $(SRC) -o $@ $(FLAGS)

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
