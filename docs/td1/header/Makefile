PDF = header.pdf
TPL = tpl.tex
SRC = # List of markdown files
HEADER = 
BEFORE = resume.tex header.tex

FLAGS = --chapters --template=$(TPL) $(HEADER:%=-H %) $(BEFORE:%=-B %)

DEPS = $(TPL) $(HEADER) $(BEFORE) commands.tex revisions.tex

GEN = $(PDF)

$(PDF):	$(SRC) $(DEPS)
	pandoc $(SRC) -o $@ $(FLAGS)

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
