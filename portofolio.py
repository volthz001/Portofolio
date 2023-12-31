import streamlit as st
import plotly.express as px
from streamlit_javascript import st_javascript
from streamlit_option_menu import option_menu
import random
import base64
import pandas as pd
import numpy as np
#st.write("""'''
    #import requests
    #from bs4 import BeautifulSoup
    #lelang = requests.get('https://lelang.go.id')
    #soup = BeautifulSoup(lelang.content,'html.parser')
    #x = soup.find(id='container-lot-lelang')
    #w = x.find_all('li')
    #v = []
    #for i in range(int(len(w))):
    #    print(f'{(w[i]).find("div",class_="product").div.h2.text}')    
    #    print(f'{(w[i]).find("div",class_="product").a.img.attrs["src"]}')
    ##    print(f'{(w[i]).find("div",class_="product").div.div.span.text}')
    #    print(f'{(w[i]).find("div",class_="product").small.text}')
    #    print('\n')
    #'''
#<script> 
#x= document.getElementsByClassName('st-emotion-cache-10trblm e1nzilvr1')[0]
#x.innerText='telah berganti'
#</script>
#""",unsafe_allow_html=True)

#img = get_img(r'')

st.markdown(r'''
<script>
alert("hello world")</script>
<style>
#class="stDeployButton"{visibility: hidden}
[data-testid=stAppViewContainer]{
    background-image: url("psm 1.jpg");
    background-size:cover
}
[data-testid=stSidebar]{
    background-image: url("psm 1.jpg");
}
footer{visibility:hidden};

</style>
''',unsafe_allow_html=True)
selected = option_menu(
    menu_title = None,
    options=['Program','Chat-Ai'],
    icons=['House','books'],
    menu_icon = "cast",
    default_index=0,
    orientation="horizontal",
    styles={
        'container':{'padding':"0!important","background-color": "#3333ff"},
        "icon":{"color":"orange","font-size":"25px"},
        "nav-link":{
            "font-size":"25px",
            "text-align":"left"
        }
    }
)
program = st.sidebar.selectbox('select program',['Manipulated Data','Order Drive','Extract-Transform-Load','Chat-Ai','Buat PDF','Cari Properti','Cari barang second','test','Crypto Prices'])
code = st.sidebar.checkbox('display code')
#[data-testid="baseButton-headerNoPadding"]{visibility: hidden}
if program == "Manipulated Data":
    try:
        ax= st.file_uploader('Input your File...') 
        if ax:
            st.success('Data berhasil Diupload')
            global df
            if ax.name[-5:-1] == '.xls':
                df = pd.read_excel(ax)
            if ax.name[-4:] == '.csv':
                df = pd.read_csv(ax)
            st.write(df)
        lings = {
            'No':[i for i in range(0,3)],
            'Ubah nama kolom':df.columns,
            'Filter Nilai yang kosong/Null':df.columns
            }
        #,df.columns[0:],[df.columns[-1]]
        xi=pd.DataFrame(lings,index=lings['No'])
        #print(xi)
        
        
        if st.button("Lakukan pencarian"):
            st.success("yahahahahah pal pal e pal pale pal ")
            #if ax[-5:] == '.xlsx':
        #    df = pd.read_excel(ax)  
    except NameError:
        st.warning('Please Upload Any data')
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
    try:
        ax= st.file_uploader('Input your File...') 
        if ax is not None:  
            st.success("File berhasil diunggah...")
        df = pd.read_excel(ax)
        list_prompt = {
            "No":[i for i in range(0,5)],
            "Ubah nama kolom":df.columns,
            "Filter Nilai yang kosong/Null":df.columns
        }
        xi=pd.DataFrame(list_prompt,index=list_prompt['No'])
        
        nama_provinsi =st.multiselect('Pilih perintah yang diinginkan...',xi[1:])
        
        if nama_provinsi:
            if nama_provinsi=='Ubah nama kolom':
                nama_kolom_lama = st.multiselect('Masukkan nama kolom',xi['Ubah nama kolom'])
                nama_kolom_baru = st.text_input('Masukkan nama kolom baru...')

                if st.button('Submit'):
                        df.rename(columns={nama_kolom_lama[0]:nama_kolom_baru})           
                        st.write(df.columns) 
                        print('Changed')
            if nama_provinsi=='Filter Nilai yang kosong/Null':
                nama_kolom_lama = st.multiselect('Masukkan nama kolom',xi['Ubah nama kolom'])
                x = [i for i in nama_kolom_lama]
                st.write(x)

 
    except ValueError:
        st.warning("Type Data belum tersedia..")
if program == 'Crypto Prices':
    pass
    #with st.form('Bitcoin'):r
       # st.write("Price: ${1000}")

if program =='Chat-Ai':
    
# Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    pairs = [
        ['hi','hai','hallo','hello'],
        ['nama kamu siapa','kamu siapa'],
        ['apa itu hipotesis statistik','hipotesis statistik','hipotesis statistik adalah'],
        ['sebutkan bagian hipotesis statistik','sebutkan hipotesis statistik','bagian bagian hipotesis statistik','bagian-bagian hipotesis statistik'],
        ['agi','agi adalah','apa itu agi']
    ]
    reflec = [
        ['hello','hallo','hai','hi'],
        ['nama saya Galdyn','nama saya effraine'],
        ['hipotesis statistik adalah pernyataan atau asumsiyang diajukan dalam analisis statistik untuk diuji melalui pengumpulan dam analisis data'],
        ["""\n-Hipotesis nol(H0):ini adalah hipotesis yang menyatakan bahwa tidak ada perbedaan,tidak ada hubungan ata tidak ada efek yang
        signifikan dalam data.Ini sering kali menggambarkan keadaan dasar atau status quo yang akan diuji.\n
        -hipotesis alternatif(H1):ini adalah hipotesis yang berlawanan dengan hipotesis nol.Ini menyatakan bahwa ada perbedaan,ada hubungan atau efek yang signifikan dalam data.
        """],
        ['Artificial General Intelegence']
    ]
    def response():
        xt = False
        for i in range(0,len(pairs)):
            if prompt.lower() in pairs[i]:
                #rint(reflec[i][random.randrange(0,len(reflec[i]))])
                x= st.chat_message("ai")
                x.write(str(reflec[i][random.randrange(0,len(reflec[i]))]))
                st.session_state.messages.append({"role": "ai", "content": (str(reflec[i][random.randrange(0,len(reflec[i]))]))})
                xt=True
        if xt==False:
            w=st.chat_message('ai')
            w.write(f'Maaf yang anda maksudkan ~{prompt}~ belum dapat saya pahami...')
            st.session_state.messages.append({"role": "ai", "content": 'Maaf yang anda maksudkan ~{prompt}~ belum dapat saya pahami...'})
            
    prompt = st.chat_input("Say something")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        if 'hitunglah' in prompt.lower():
            prompt = prompt.split(" ")
            w=st.chat_message('ai')
            w.write(eval(prompt[-1]))
            st.session_state.messages.append({"role": "ai", "content": eval(prompt[-1])})
        else:
            response()
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
        if nama_daerah:
            minimum = st.number_input('Masukkan Harga Minimum...',min_value=100_000,placeholder='Rp.100.0000',value=None)
            maximum = st.number_input('Masukkan Harga Minimum...',value=None)
            if minimum and maximum:
                if st.button("Lakukan pencarian"):
        
                    asyncio = __import__('asyncio')
                    async def gets():
                        st.write('Sedang Mengumpulkan data...')
                        global requests
                        sert = st.progress(0)
                        requests = __import__('requests')
                        sup = __import__('bs4').BeautifulSoup
                        st.write('Hasil Yang Ditemukan')
                        for percentage in range(100):
                            download.progress(percentage+1)
                            dat = requests.get('https://lelang.go.id')
                            if dat:
                                break
                            await asyncio.sleep(0.1)
                    asyncio.run(gets())
                        
                    #st.success("yahahahahah pal pal e pal pale pal ")
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
    from streamlit_elements import dashboard,elements,mui,html
    def show_image():
        with elements("image"):
            with dashboard.Grid(layout):
                mui.cardMedia(component='img',src=f"data:iamge/png,{st.session_state['img']}")
    with elements("new_element"):
        mui.Typography("Hello world")
    layout = [
        dashboard.Item('first item',0,0,2,2),
        dashboard.Item('second item',2,0,2,2,isDraggable=False,moved=False),
        dashboard.Item('three item',2,0,2,2,isResizable=True)
        ]
    with elements('image_grid'):    
        with dashboard.Grid(layout):
            mui.Paper("First item",key='first item')
            mui.Paper('Second item',isDraggable=False,moved=False)
            mui.Paper('three item',isResizable=True)


    
