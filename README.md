# Uczenie Maszynowe - projekt

### Etap 2

- Tomasz Owienko
- Wojciech Zarzecki


### Cel projektu

Celem projektu jest implementacja zmodyfikowanej wersji algorytmu generowania lasu losowego, w której do generowania kolejnych drzew losowane są częściej elementy ze zbioru uczącego, na których dotychczasowy model się mylił.

Istotą metody lasu losowego w problemach regresji i klasyfikacji jest redukcja wariancji i nadmiernego dopasowania osiąganego przez pojedyncze drzewa decyzyjne. W klasycznych algorytmach generowania lasu losowego każde z $B$ drzew generowane jest na podstawie $\sqrt{B}$ przykładów ze zbioru trenującego wylosowanych ze zwracaniem, zazwyczaj ograniczonych (w problemach klasyfikacji) do $\sqrt{|D|}$ atrybutów wylosowanych bez zwracania, gdzie $D$ jest zbiorem atrybutów. Proces ten odbywa się w jednej iteracji - algorytm kończy pracę po wygenerowaniu $B$ drzew. Taka koncepcja to tzw. $\textit{bagging}$, który ma na celu ograniczenie wariancji modelu po przez agreację wielu prostszych modeli - w tym przypadku drzew decyzyjnych.

Realizowany projekt zakłada zbadanie możliwości zastosowania metod $\textit{boostingu}$ oraz $\textit{stackingu}$. Wdrożenie metod boostingowych polega na uwzględnianiu błędów wygenerowanych już drzew decyzyjnych przy budowanie kolejnych. W takim podejściu nowe drzewa są nieustannie dołączane są do istniejącego już lasu. Natomiast stacking zakłada utworzenie nowego zbioru danych na bazie wyników wytrenowanego modelu oraz wytrenowanie na nowym zbiorze $\textit{metamodelu}$. Co istotne, w podejściu stackingowym las wygenerowany w iteracji $n+1$ w pełni zastępuje las z iteracji $n$.



### Modele
Porównujemy i opusujemy następujące model:
- Boosted RF
- Stacking RF
- IterativeRandomForrestClassBased
- IterativeRandomForrestSampleBased
- Classic RF


Ich opis i eksperymenty można znaleźć w folderze `./experiments` a ich listing w folderze `./src`.



### Wykorzystywane zbiory danych

Ocena jakości modeli wykonywana była w oparciu o dwa zbiory danych:

- UCI Breast Cancer - 569 przykładów, 31 atrybutów numerycznych ciągłych
- UCI Spambase - 4601 przykładów, 57 atrybutów ciągłych i dyskretnych
- UCI Statlog (German Credit Data) - 1000 przykładów, 20 atrybutów dyskretnych, kategoryzacyjnych i binarnych
