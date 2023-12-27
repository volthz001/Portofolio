import streamlit as st
#import plotly.express as px
#from streamlit_javascript import st_javascript
import random
import pandas as pd
import numpy as np
#st.write("""
#<script> 
#x= document.getElementsByClassName('st-emotion-cache-10trblm e1nzilvr1')[0]
#x.innerText='telah berganti'
#</script>
#""",unsafe_allow_html=True)
program = st.sidebar.selectbox('select program',['Manipulated Data','Order Drive','Extract-Transform-Load','Chat-Ai','Buat PDF','Cari Properti','Cari barang second','test'])
code = st.sidebar.checkbox('display code')
if program == "Manipulated Data":
    ax= st.file_uploader('Input your File...') 
    if ax:
        st.success('Data berhasil Diupload')
        if ax.name[-5:-1] == '.xls':
            df = pd.read_excel(ax)
        if ax.name[-4:] == '.csv':
            df = pd.read_csv(ax)
        st.write(df)
        lings = {
        'No':[i for i in range(0,3)],
        'Ubah nama kolom':df.columns,
        }
    #,df.columns[0:],[df.columns[-1]]
    xi=pd.DataFrame(lings,index=lings['No'])
    #print(xi)
    nama_provinsi =st.multiselect('Pilih perintah yang diinginkan...',xi.columns[1:])
    if nama_provinsi:
        nama_kolom = st.multiselect('Masukkan nama kolom',xi['Ubah nama kolom'])
        x = st.chat_input('Masukkan nama kolom baru...')
        if st.button('Submit'):
            if nama_kolom in df.columns:
                st.write(df.columns)
            st.write(df)
    if st.button("Lakukan pencarian"):
        st.success("yahahahahah pal pal e pal pale pal ")
        #if ax[-5:] == '.xlsx':
        #    df = pd.read_excel(ax)  
if program == 'Order Drive':
    st.title('Order Drive')
    wass=st_javascript(
    """
    
    if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(showPosition,showError);
        }else{
            console.log("Geeolocation is not supported")
        }
        function showPosition(position){
            x = {'Latitude:':position.coords.latitude,'longitude':position.coords.longitude}
            return JSON.stringify(x);
        }
        function showError(error){
            switch(error.code){
                case error.PERMISSION_DENIED:
                    console.log('User Denied the request for geolocation');
                    break;
                case error.POSITION_UNAVAIBLE:
                    console.log('Location information is unavaible');
                    break;
                case error.TIMEOUT:
                    console.log('the request to get user location time out');
                    break;
                case error.UNKNOWN_ERROR:
                    console.log('An unknown error occurated.');
                    break;
            }
        } 
    """,)
    print(f"{wass}")
    st.write('hasil dari javascript: ',wass)
    st.warning('Izinkan lokasi untuk mengetahui driver terdekat...')
    st.write('Khusus Daerah Jakarta-Tanggerang-Tanggerang Selatan')
    st.image('../downloads/carbon.png',caption='Ayla')
    st.text('Khusus daerah jakarta-Tanggerang-Tanggerang selatan')
    st.link_button('Order Now','http://whatsapp.me/+6282175733644')
    #st.write("""\n<script>
   # x=document.getElementsByClassName("st-emotion-cache-1vbkxwb e1nzilvr5")[1]
    #x.querySelector('p').innerText='Order'
    #</script>
   # """,unsafe_allow_html=True)
if program == 'Extract-Transform-Load':
    ax= st.file_uploader('Input your File...') 
    if ax is not None:  
        st.succes("File berhasil diunggah...")
    df = pd.read_excel(ax)
    st.write(df)   
if program =='Chat-Ai':
   st.title('Chat Ai')

    pairs = [
    ['hi', 'hai', 'hallo', 'hello'],
    ['nama kamu siapa', 'kamu siapa'],
    ['apa itu hipotesis statistik', 'hipotesis statistik', 'hipotesis statistik adalah'],
    ['sebutkan bagian hipotesis statistik', 'sebutkan hipotesis statistik', 'bagian bagian hipotesis statistik',
     'bagian-bagian hipotesis statistik'],
    ['agi', 'agi adalah', 'apa itu agi']
    ]

    reflec = [
    ['hello', 'hallo', 'hai', 'hi'],
    ['nama saya Galdyn', 'nama saya effraine'],
    ['hipotesis statistik adalah pernyataan atau asumsi yang diajukan dalam analisis statistik untuk diuji melalui pengumpulan dan analisis data'],
    ["""\n-Hipotesis nol (H0): ini adalah hipotesis yang menyatakan bahwa tidak ada perbedaan, tidak ada hubungan, atau tidak ada efek yang signifikan dalam data. Ini sering kali menggambarkan keadaan dasar atau status quo yang akan diuji.\n
    -Hipotesis alternatif (H1): ini adalah hipotesis yang berlawanan dengan hipotesis nol. Ini menyatakan bahwa ada perbedaan, ada hubungan, atau efek yang signifikan dalam data.
    """],
    ['Artificial General Intelligence']
    ]

    def response(prompt):
        xt = False
        for i in range(0, len(pairs)):
            if prompt.lower() in pairs[i]:
                x = st.chat_message("ai")
                x.write(str(reflec[i][random.randrange(0, len(reflec[i]))]))
                xt = True
        if not xt:
            w = st.chat_message('ai')
            w.write(f'Maaf yang anda maksudkan ~{prompt}~ belum dapat saya pahami...')

    chat_history = st.session_state.setdefault('chat_history', [])

    def add_message(message):
        chat_history.append(message)

    def display_chat():
        for message in chat_history:
            st.text(message)

    prompt = st.text_input("Say something")
    if st.button("Send"):
        add_message(prompt)
        if prompt:
            if 'hitunglah' in prompt.lower():
                prompt = prompt.split(" ")
                w = st.chat_message('ai')
                w.write(eval(prompt[-1]))
                add_message(eval(prompt[-1]))

            else:
                response(prompt)

    display_chat()

# Save chat history to session state
st.session_state['chat_history'] = chat_history
if program == "Buat PDF":

    oxp = []
    cs = ['Table data','line plot','histogram plot','scatter plot']
    data_x= st.multiselect('Data X',cs[0:],[cs[-1]])
    data_y= st.multiselect('Data Y',cs[0:],[cs[-1]])
    st.subheader('Cetak Pdf...')
    text_=st.chat_input('Tambahkan kalimat')
    if text_:
        oxp.append(str(text_))
        print(text_)
        if oxp:
            st.success('teks berhasil ditambahkan')
    lis_cs_= st.multiselect('Pilih bagian yang diikut sertakan dalam pdf...',cs[0:],[cs[-1]])
    if st.button('preview'):
        print(oxp)
        st.write(f'{oxp}')
    st.button('Cetak sekarang...')
                #st.line_chart(np.random.randn(30,3))
if program=="Cari Properti":
    st.title('Order Drive')
    prov = {
        'No':[i for i in range(0,3)],
        'Dki Jakarta':['Jakarta Barat','Jakarta selatan','Jakarta timur'],
        'Jawa Timur':['Surabaya','Malang','Jancuk'],
        'Banten':['Tanggerang','Pandeglang','Tanggerang selatan'],
        'Sumatera Selatan':['Ogan komering Ulu','Ogan Komering Ilir','Lubuklinggau'],
        'sumatera utara':['medan','sibolga','sipahutar']
        }
    #,df.columns[0:],[df.columns[-1]]
    xi=pd.DataFrame(prov,index=prov['No'])
    #print(xi)
    nama_provinsi =st.multiselect('Masukkan Nama provinsi:',xi.columns[1:])
    if nama_provinsi:
        nama_daerah = st.multiselect('Masukkan nama daerah',xi[nama_provinsi])
    if st.button("Lakukan pencarian"):
        st.success("yahahahahah pal pal e pal pale pal ")
if program=="Cari barang second":
    st.title('Cari kendaraan Favoritmu disini')
    prov = {
        'No':[i for i in range(0,3)],
        'Dki Jakarta':['Jakarta Barat','Jakarta selatan','Jakarta timur'],
        'Jawa Timur':['Surabaya','Malang','Jancuk'],
        'Banten':['Tanggerang','Pandeglang','Tanggerang selatan'],
        'Sumatera Selatan':['Ogan komering Ulu','Ogan Komering Ilir','Lubuklinggau'],
        'sumatera utara':['medan','sibolga','sipahutar']
        }
    typek ={
        "Type":["Motor","Mobil","Sepeda","Elektronik"]
    }
 
    xi=pd.DataFrame(prov,index=prov['No'])
    xi_=pd.DataFrame(typek,index=[i for i in range(4)])
    nama_provinsi =st.multiselect('Masukkan Nama provinsi:',xi.columns[1:])
    if nama_provinsi:
        nama_daerah = st.multiselect('Masukkan nama daerah',xi[nama_provinsi])
        if nama_daerah:
            nama_provinsi =st.multiselect('Masukkan Type Barang...',xi_.Type)
    
    if st.button("Lakukan pencarian"):
        st.success("yahahahahah pal pal e pal pale pal ")
if program =='test':
    async def test(nama='google'):
        st.write(nama)
    test()
