class Script(object):

    START_MSG = """<b>Hy {},

I'm an advanced filter bot with many capabilities!
There are no practical limits for my filtering capacity :)

<i>/help</i> yazarak detaylı bilgi alabilirsiniz.</b>
"""


    HELP_MSG = """
<i>Beni grubunuza yönetici olarak ekleyin ve filtrelemeye başlayın :)</i>


<b>Basit Komutlar;</b>

/start - Hayatta olup olmadığımı kontrol et!
/help - Komut yardımı
/about - Benimle ilgili bir şey!


<b>Filter Komutları;</b>

<code>/add selam as</code>  -  Filtre ekle

<code>/del name</code>  -  Filtre Sil

<code>/delall</code>  -  Tüm filtreleri sil. (Grup Sahibi) 

<code>/viewfilters</code>  -  Tüm filtreleri görüntüle.


<b>Bağlanma Komutu;</b>

<code>/connect groupid</code>  -  Grubunuzu başbakanıma bağlayın. Ayrıca basitçe kullanabilirsiniz,
<code>/connect</code> gruba gönder

<code>/connections</code>  -  Bağlantılarınızı yönetin.


<b>Extra;</b>

/status  -  Botunuzun geçerli durumunu gösterir (Yalnızca Kimlik Doğrulama Kullanıcısı)

/id  -  Kimlik bilgilerini gösterir

<code>/info userid</code>  -  Kullanıcı Bilgilerini Gösterir. <code>/info</code> ayrıntıları için bazı iletilere yanıt olarak!


<b>© @Saygisizlar</b>
"""


    ABOUT_MSG = """⭕️<b>My Name : Saygısızlar Filter Bot</b>

⭕️<b>Creater :</b> @SaygisizlarSahip  

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
