deadline 
7.12

#### wymagania
1. opis projektu, wskazujący na zrozumienie problemu
2. precyzyjny opis algorytmów, które będą wykorzystane
3. plan eksperymentów, który może się zmienić - nie musi być ostateczny
4. dokładnie opisane zbiory danych, które będą używane do badań.

#### temat
Zaimplementować zmodyfikowaną wersję algorytmu generowania lasu losowego, w której do generowania kolejnych drzew losowane są cześciej elementy ze zbioru uczącego, na których dotychczasowy model sie mylił.



#### 1. opis projektu
*można doczytać*
- idea RF
- idea AdaBoost https://www.analyticsvidhya.com/blog/2021/09/adaboost-algorithm-a-complete-guide-for-beginners/
- weighted RF - weigh drawing attributes or specif tree weights - *maybe*

*draft*
robimy RFa, ale boost-ujemy iteracyjnie tak jak w AdaBoost 

#### 2. opis algorytmów
opis RF oraz funkcji do losowania

główny algorytm
```
powtarzaj n razy:
	zbuduj RF (z naszym losowaniem)
	ewalucja na U
	zaktuliazuji wagi przykładów do losowania
```

nasze losowanie
- init: każda klasa 1 ticket
- losuj przykład proporcjonalnie to ticket-ów 
- *(jakieś przekształcenie regulujące preference wyżej notowanych przykładów*)
	- selekcja ruletkowa/progowa/turniejowa
	- min max i alternatywy

#### 3. opis eksperymentów
- porównanie metryk na dataset
- wybór selekcji
- wybór ważenia poszczególnych przykładów vs wybór ważenia klas

#### 4. datasets
binary
- uci mashrooms
- uci breast cancer
- titanic *small/simple*


todo
- formatowanie i ładny opis alg
- czytanie o algorytmach dla siebie
- datasety doszukać
- pytania do SK
	- gotowa funkcja do RF/decision tree
	- jak wiążące so wybory dataset-ów, czy trzeba EDA czy tylko wybór?



