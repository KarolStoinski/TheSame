# TheSame
Analiza posiedzenia Sejmu RP z 29 listopada 2023 roku w oparciu o embedding stworzony z poszczególnych wypowiedzi.

## Motywacja
Oglądając posiedzenia Sejmu można zauważyć, że wiele wypowiedzi jest do siebie podobnych.
Dzięki narzędziom powszechnym w tematyce AI można pokusić się o zbudowanie narzędzia, które wizualizuje te podobieństwa.
Projekt ten jest Proof of Concept stworzonym, aby sprawdzić jak takie narzędzie może wyglądać i działać.

## Dojście do wynikowej prezentacji w TensorBoard
Poniższy filmik YouTube pokazuje jak wygląda wynik procesu przetwarzania danych, którego źródła znajdują się w tym repozytorium.

[![TheSame - Analiza posiedzenia Sejmu RP w oparciu o narzędzia AI](http://img.youtube.com/vi/dnV5fTl4jM8/0.jpg)](http://www.youtube.com/watch?v=dnV5fTl4jM8 "TheSame - Analiza posiedzenia Sejmu RP w oparciu o narzędzia AI")
http://www.youtube.com/watch?v=dnV5fTl4jM8

### UWAGA
Do zobaczenia samej prezentacji wystarczy przeskoczyć do kroku 7go mając zainstalowany u siebie TensorBoard. Wszystkie dane pośrednie i wynikowe znajdują się w tym repozytorium i nie trzeba wykonywać wszystkich poniższych kroków. Opisane są jedynie dla udokumentowania tego, co poszczególne skrypty robią.

### 1. Zamiana PDF na tekst
Plik PDF
http://orka2.sejm.gov.pl/StenoInter10.nsf/0/5EA2FC331EDABAFDC1258A760079790B/%24File/01_f_ksiazka.pdf
ze stenogramem posiedzenia sejmu przetworzony został narzędziem onlineowym https://pdftotext.com/pl/
na plik tekstowy 01_f_ksiazka.txt

### 2. Uruchomienie split.py
Plik split.py dzieli plik 01_f_ksiazka.txt na fragmenty przy pomocy słów kluczowych
> keywords = ["Poseł", "Marszałek", "Przedstawiciel Komitetu", "Wicemarszałek", "Minister", "Zastępca Przedstawiciela", "Podsekretarz Stanu", "Prezes Rady Ministrów"]

### 3. Uruchomienie embedding.py
Dla każdego pliku z katalogu "splitted" wyliczany jest embedding, który ląduje w katalogu "embeddings"

### 4. Uruchomienie tensor.py
Przygotowuje plik tensor/vectors.tsv ze wszystkimi embeddingami oraz tensor/metadata.tsv z treścią wypowiedzi

### 5. Uruchomienie load.py
Zamienia plik tensor/vectors.tsv na format zrozumiały dla TensorBoard https://www.tensorflow.org/tensorboard?hl=pl i umieszcza pliki wyjściowe w katalogu "logs"

### 6. Skopiowanie metadata.tsv do katalogu logs
Pozwala na zobaczenie treści wypowiedzi w TensorBoard

### 7. Uruchomienie TensorBoard
Skrypt board.sh uruchamia TensorBoard z danymi z katalogu "logs". Korzystając z zakładki Projector widzimy wizyalizację powiązań między wypowiedziami.
