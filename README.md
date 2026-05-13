# Tři automatizované testy

## Playwright Testy pro Engeto.cz
Tento projekt obsahuje základní automatizované testy pro web engeto.cz pomocí frameworku Playwright a testovacího runneru Pytest.
## 📋 Co se testuje?
Skript pokrývá tři základní scénáře:

   1. Ověření titulku stránky: Kontroluje, zda se hlavní stránka načte se správným názvem.
   2. Interakce s cookies: Testuje, zda po kliknutí na tlačítko "Přijmout" zmizí cookie lišta.
   3. Validace newsletteru: Ověřuje, že systém správně rozpozná neplatný formát e-mailu a zobrazí příslušnou chybovou hlášku.

## 🛠 Požadavky
Před spuštěním se ujisti, že máš nainstalovaný Python a potřebné balíčky:

# Instalace pytest a playwright pluginu
pip install pytest-playwright
# Instalace prohlížečů (Firefox, Chromium, atd.)
playwright install

## 🚀 Jak testy spustit
Testy spustíš jednoduše z terminálu v kořenovém adresáři projektu:

pytest jmeno_tveho_souboru.py

## Užitečné parametry:

* $env:PWDEBUG=1; pytest: Pokud chceš vidět prohlížeč v akci.
* -v: Podrobnější výpis výsledků (verbose).



