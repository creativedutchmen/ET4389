FILE=report

pdf:
	Rscript -e "require(knitr); require(markdown); knit('$(FILE).rmd', '$(FILE).md');"
clean:
	rm report.md
