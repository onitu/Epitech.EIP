PDF = 2015_TD4_FR_onitu.pdf
TPL = tpl.tex
SRC =	presentation.md \
	architecture.md \
	architecture_fonctionnement.md \
	architecture_technologies.md \
	architecture_core.md \
	architecture_drivers.md \
	architecture_api.md \
	architecture_webui.md \
	architecture_client.md \
	configuration.md \
	tests.md \
	contribution.md \
	liens.md
HEADER = print_json.tex
BEFORE = resume.tex header.tex

FLAGS = --chapters --toc --template=$(TPL) $(HEADER:%=-H %) $(BEFORE:%=-B %)

DEPS = $(TPL) $(HEADER) $(BEFORE) commands.tex revisions.tex imgs/global_archi.png

GEN = $(PDF)

$(PDF):	$(SRC) $(DEPS)
	pandoc $(SRC) -o $@ $(FLAGS)

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
