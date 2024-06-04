default:
	@cat makefile

get_texts: pg17192.txt 932.txt 1063.txt 1064-0.txt 51060-8.txt 50852-0.txt 32037.txt 2147-0.txt 2148-0.txt 2149-0.txt

pg17192.txt:
	@wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
932.txt:
	@wget https://www.gutenberg.org/files/932/932.txt
1063.txt:
	@wget https://www.gutenberg.org/files/1063/1063.txt
1064-0.txt:
	@wget https://www.gutenberg.org/files/1064/1064-0.txt
51060-8.txt:
	@wget https://www.gutenberg.org/files/51060/51060-8.txt
50852-0.txt:
	@wget https://www.gutenberg.org/files/50852/50852-0.txt
32037.txt:
	@wget https://www.gutenberg.org/files/32037/32037.txt
2147-0.txt:
	@wget https://www.gutenberg.org/files/2147/2147-0.txt
2148-0.txt:
	@wget https://www.gutenberg.org/files/2148/2148-0.txt
2149-0.txt:
	@wget https://www.gutenberg.org/files/2149/2149-0.txt

# this runs all of the data processing tasks
data_processing:
	@bash data_processing.sh	
