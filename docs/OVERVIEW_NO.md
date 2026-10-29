# Compulsory 2: hva vi har laget

Dette er Group 12 sitt utgangspunkt for prosjektet som fortsetter til eksamen. Gruppen består av Kai Arne Hage og Mohammad Almojtaba Elhajj A Elhajj. Fristen Kai har oppgitt fra Canvas er 7. november 2026 kl. 23.59.

## Problemet

En innbygger i Hamar vil raskt forstå et planvarsel: hva som foreslås, hvor det gjelder, hvilken fase saken er i, når innspill må sendes, og hvordan man svarer. Vi undersøker om en kort forklaring med sporbare kildeutdrag kan hjelpe. Vi har foreløpig ikke intervjuet innbyggere eller vist at løsningen faktisk forbedrer forståelsen.

## Hva den fungerende prototypen gjør

```text
Utvalgt tekst + kildeopplysninger
             |
             v
Lokal modell foreslår strukturerte fakta og kildebelegg
             |
             v
Python lager et norsk utkast fra en fast mal
             |
             v
Kontrollerer format, belegg og datoer
             |
             v
Lagrer utkast til menneskelig gjennomgang, eller en feilrapport
```

Det er ett modellkall. Modellen får instruksjonsfilen og det valgte utdraget. Den får ingen nettleser, tilgang til andre filer eller mulighet til å publisere. Python styrer prosessen. Den norske teksten formateres med en mal, slik at vi unngår et ekstra modellkall som kan introdusere nye påstander.

## Eksemplet vi har testet

Vi bruker tre korte, adskilte utdrag fra Hamar kommunes varsel om Ringgata. Utdraget inneholder forslaget om sykkelveg med fortau, strekningen mellom Solvangvegen og Disenvegen, oppstart av planarbeidet og fristen 18. november 2026. Det er kun 21 ord og gir derfor en svært begrenset test. Innsendingsveien er utelatt. Da skal modellen svare at den er ukjent, ikke finne på en e-postadresse.

Kilden og utdraget er kontrollert av Codex. Din og partnerens gjennomgang er fortsatt en faktisk oppgave, ikke noe vi har krysset av automatisk.

## Hva resultatene viser

Den endelige forsøksserien har fem kjøringer med Qwen på det samme utdraget. Alle lagret et utkast som bestod kodekontrollene, og de smale referansekontrollene fant de forventede feltene i 5 av 5 kjøringer. Serien brukte 3 645 modelltoken og totalt 37,971 sekunder målt fra klienten. Dette er ikke bevis for at systemet virker på alle varsler.

En tidligere Llama-kjøring feilet og inneholdt oppdiktede sitater. Den er bevart. Vi har også et syntetisk tilfelle der en ondsinnet dato kan slippe gjennom hvis datoen faktisk står i teksten. At sitatet finnes, beviser ikke at sitatet støtter påstanden. Det er en viktig del av risikoanalysen.

Alle 12 tester bestod, og en fersk klone fra GitHub kjørte både testene og et reelt eksempel. Syntetiske tester med ferdiglagde modellsvar tester programmet, ikke modellens evne til å motstå angrep.

## Dette leverer vi for Compulsory 2

- En engelsk rapport med fire sider hovedtekst og to sider referanser og vedlegg.
- Lenke til det offentlige GitHub-repositoryet inne i rapporten.
- Et repository med kode, instruksjoner, kontekstfil, input, tester og lagrede forsøksresultater.
- Et ærlig vedlegg med promptutdrag og faktiske arbeidsøkter. Møter med partneren skal føres når de faktisk skjer.

Rapporten er et redaksjonelt utkast. Begge må lese, kontrollere og bearbeide teksten før innlevering. Det er ikke krav om en innspilt video til dette arbeidskravet; den obligatoriske demonstrasjonen kommer senere.

## Dette må utvikles før eksamen

Et større testsett, virkelige feilinjeksjoner, dokumenterte reparasjoner og regresjonstester, tydeligere tilgangskontroll, samlet tokenbudsjett og en målbar stoppregel. Vi planlegger å teste både ondsinnet eller feilaktig input og svikt i modelltilkoblingen. Eksamen inkluderer live demonstrasjon i uke 46-47, en rapport på 7-8 hovedsider og minst åtte ekte møtereferater. Fristen for eksamensrapporten i oppgavebeskrivelsen er 3. desember 2026 kl. 11.59.

Start gjennomgangen i docs/DEMONSTRATION.md. Åpne originalkilden og ett lagret utkast ved siden av hverandre før vi går gjennom koden.
