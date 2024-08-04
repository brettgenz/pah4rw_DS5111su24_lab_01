default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

get_texts: book_Raven.txt book_FallHouseUsher.txt book_CaskAmontillado.txt book_Poems.txt book_LeCorbeau.txt

test: get_texts
	. env/bin/activate; pytest -vvx -m "not integration" tests

lint: test
	. env/bin/activate; pylint src/data_prep.py

book_Raven.txt:
	@wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
book_FallHouseUsher.txt:
	@wget https://www.gutenberg.org/files/932/932.txt
book_CaskAmontillado.txt:
	@wget https://www.gutenberg.org/files/1063/1063.txt
book_Poems.txt:
	@wget https://www.gutenberg.org/files/10031/10031-0.txt
book_LeCorbeau.txt:
	@wget https://www.gutenberg.org/cache/epub/14082/pg14082.txt
#1064-0.txt:
#	@wget https://www.gutenberg.org/files/1064/1064-0.txt
#51060-8.txt:
#	@wget https://www.gutenberg.org/files/51060/51060-8.txt
#50852-0.txt:
#	@wget https://www.gutenberg.org/files/50852/50852-0.txt
#32037.txt:
#	@wget https://www.gutenberg.org/files/32037/32037.txt
#2147-0.txt:
#	@wget https://www.gutenberg.org/files/2147/2147-0.txt
#2148-0.txt:
#	@wget https://www.gutenberg.org/files/2148/2148-0.txt
#2149-0.txt:
#	@wget https://www.gutenberg.org/files/2149/2149-0.txt

# this will run all of the data processing tasks
#data_processing:
#	@bash data_processing.sh

raven_line_count:
	@bash raven_line_count.sh

raven_word_count:
	@bash raven_word_count.sh

raven_counts:
	@bash raven_counts.sh

total_lines:
	@bash total_lines.sh

total_words:
	@bash total_words.sh	

delete_texts:
	@rm 10031-0.txt* 1063.txt* 932.txt* pg14082.txt* pg17192.txt*
