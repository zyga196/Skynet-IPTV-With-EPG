# Skynet-IPTV-With-EPG

# Kas čia?

  Tai Skynet IPTV kanalų (ir kelių kitų ISP) sąrašas. Šiuo playlist siekiame suvienodinti ir turėti vieną bendrą sąrašą kuriuo gali naudotis visi ir visi gali prisidėti prie jo tobulinimo.


# Kaip pasileisti šitą "playlist'ą"?

Playlist failas yra prieinamas per šią nuorodą: [skynet-pl-local.m3u][playlist-link]

  Tiesiog nusikopijuokite nuorodą ir įdėkite į savo IPTV programą.  Atsiradus naujiems pakeitimas jie automatiškai atsiras ir pas jus televizoriuje



# Kas yra EPG ir kaip gauti šių kanalų programą?

Norint matyti šio playlisto kanalų programą galite naudotis [guide.xml][epg-link]
 failu,
šis failas yra elektronio programos gido (EPG) standartas ir turėtų veikti
su įvairiais iptv įrenginiais. Šis *EPG* buvo išbandytas ir veikia su
`Kodi Simple IPTV` klientu.

# Kaip dažnai yra atnaujinamas Elektroninis Progamų Gidas (EPG)?

Šiai dienai EPG yra generuojamas 3 dienas į priekį ir yra išnaujo sugeneruojamas,
kas dieną `04:00` ryto.



# Ką dar turėčiau žinoti apie EPG?

- Šis EPG savyje saugo ir kanalų logotipus
- Programa yra sugeneruota `UTC±00:00` todėl programų gidą reikęs atsukti 2 valandas (žiemos laiku) ir 3 valandas [(vasaros laiku)][apie-laiko-juostas]
- Playlistas ir EPG veikia ir buvo išbandyti su `Kodi "Simple IPTV Client"`



# Su kokiu interneto tiekėju veikia šis playlist?

  Visi kanalai šiame grojarašyje yra prieinami jei naudojatės `Skynet` paslaugomis ir nesvarbu ar esate užsisakęs IPTV ar ne.


# EPG laiko pasukimas

## Kodi: Simple IPTV Client

![pasukimas][epg-simple-shift]

Simple IPTV turi bug kuris leidžia atlikti `EPG Time Shift (hours)` tik
EPG pridėjimo metu, todėl jei norite pastumti EPG laiką jau pridėtam
playlist atlikite šiuos žingsnius:

---

1. Ištrinkite: XMLTV URL
2. Reboot Kodi
3. Nueikite: IPTV Simple Client nustatymus
4. Pridėkite: XMLTV URL [iš čia][epg-link]
5. Nustatykite į +2 arba +3: EPG Time shift (hours)
6. Nustatykite: Apply Time Shift to All Channels
7. Nuspauskite mygtuką: OK
7. Reboot Kodi`


---


# Kaip prisidėti prie šio playlist tobulinimo?

## Noriu prisidėti prie `skynet-pl-public.m3u` failo keitimo

1. Pasidarykite šitos repozitorijos `public fork (master branch)`
2. Padarykite pakeitimus savo repozitorijoje (rekomenduojame per web interface). 
3. Padarykite `Pull Request` į šios repozitorijos `master branch`
4. Kai pridedate naują kanalą jo vardas turi būti toks pat kaip šiame sąraše: [kanalų vardai][channel-names]
> ⚠️ Teisingi kanalų vardai yra būtini EPG generavimui

## Noriu prisidėti prie `guide.xml` tobūlinimo

...

 

[channel-names]: http://www.webgrabplus.com/epg-channels#sFA
[playlist-link]: https://raw.githubusercontent.com/Povilas1/Skynet-IPTV-With-EPG/master/skynet-pl-local.m3u
[epg-link]: https://raw.githubusercontent.com/Povilas1/Skynet-IPTV-With-EPG/master/guide.xml
[apie-laiko-juostas]: http://www.mintysposakiai.lt/tikslus-laikas/#laiko-juosta
[epg-simple-shift]: docs/how-to-shift.jpg