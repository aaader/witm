#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#Copyright © Võru Instituut 
#Copyright © Ants Aader
#Edasiturustamine või -levitamine ning tarkvara lähtekoodi ja binaarsete vormide kasutamine modifitseeritud või modifitseerimata kujul on lubatud, kui on täidetud järgmised tingimused:
#Tarkvara lähtekoodi edasiturustamisel või -levitamisel tuleb säilitada ülaltoodud autoriõigusemärge, käesolev tingimuste loetelu ja alljärgnev loobumisteade.
#
#Tarkvara binaarse vormi edasiturustamisel või -levitamisel tuleb dokumentatsioonis ja/või teistes turustamisel või levitamisel üleantavates materjalides reprodutseerida ülaltoodud autoriõigusemärge, käesolev tingimuste loetelu ja alljärgnev loobumisteade:
#
#SELLE TARKVARA ON VALMISTANUD VÕRU INSTITUUT KOOS KAASVALMISTAJATEGA KASUTAMISEKS SELLISENA „NAGU SEE ON“ NING SEE EI ANNA MINGIT SÕNASTATUD VÕI EELDATAVAT GARANTIID, SEALHULGAS TURUSTATAVUSE, TEATUD OTSTARBEKS SOBIVUSE EGA MUUD GARANTIID. MITTE MINGIL JUHUL EI OLE VÕRU INSTITUUT EGA TARKVARA KAASVALMISTAJAD KOHUSTATUD VASTUTAMA ÜKSKÕIK MILLISE OTSESE, KAUDSE, JUHUSLIKU, ERILISE, ÜHEKORDSE EGA TULENEVA KAHJU (SEALHULGAS ASENDUSTOODETE VÕI -TEENUSTE HANKIMISE KUJUL, KASUTAMISE, ANDMETE VÕI TULUDE KAOTUSE KUJUL; VÕI ÄRITEGEVUSE KATKEMISE KUJUL) EEST PÕHJUSTATUNA ÜKSKÕIK KUIDAS JA ÜKSKÕIK MISSUGUSE KOHUSTUSTE PÕHJENDUSEGA, ÜKSKÕIK KAS SEE TEKIB LEPINGULISE KOHUSTUSE, RANGE VASTUTUSE VÕI ÕIGUSERIKKUMISE (SEALHULGAS HOOLETUSE VÕI MUU KUJUL) TÕTTU, KUI SEE TEKIB ÜKSKÕIK MISSUGUSEL TEEL SELLE TARKVARA KASUTAMISE TAGAJÄRJEL, ISEGI KUI ON TEATAVAKS TEHTUD SELLISE KAHJU VÕIMALUS.
#
#Copyright © Võru Institute 
#Copyright © Ants Aader
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution:
#
#THIS SOFTWARE IS PROVIDED BY THE VÕRU INSTITUTE AND CONTRIBUTORS "AS IS" AND  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import cgi, cgitb, sys, codecs
import html as h
import funk_sn as fsn

cgitb.enable()
writer = codecs.getwriter('utf8')(sys.stdout.buffer)
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

h.kr("\r\n")

h.pais('WI Võro kiil, sõnaraamat')
h.kr("<div id=\"keha\">")
h.kr("<div id=\"kast\">")
h.kr("<div id=\"yl\">")
h.kr("<h3>Võro keele sõnaraamat(ud)</h3>")
h.kr("</div>")
h.viide('sn.py?z=avatekst','Pikemalt ja kirjeldused | ')
h.viide('sn.py?z=etvro','Eesti-Võru sõnaraamat | ')
h.viide('sn.py?z=vroet','Võru-Eesti sõnaraamat | ')
form = cgi.FieldStorage()
if form.getvalue('z'):
	z = form.getvalue('z')
	z = cgi.escape(z)
	if (z == "koikkaandsonad"):
		fsn.kaanded()
	elif (z == "yhesugusedkaandelopud"):
		fsn.yhesugusedkaandelopud()
	elif (z == "kaandeloppuderuhmad"):
		fsn.kaandeloppuderuhmad()
	elif (z == "vroen"):
		fsn.vro_en_koik()
	elif (z == "etvro"):
		fsn.etvro()
	elif (z == "vroet"):
		fsn.vroet()
	elif (z == "puhasvro"):
		fsn.puhasvro()
	elif (z == "avatekst"):
		fsn.avatekst()
h.kr("</div>")
h.kr("</div>")
h.jalus()
