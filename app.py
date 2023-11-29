import streamlit as st

# Streamlit app
def main():
    st.title('Olist E-Commerce Analysis')

    # Add sections for different parts of your analysis
    st.sidebar.header('Navigation')
    selected_page = st.sidebar.radio(
        'Go to',
        ['Geographical Distribution', 'Transaksi dan Pembayaran', 'Delivery Analysis', 'Sales Analysis', 'Customer Segmentation']
    )

    if selected_page == 'Geographical Distribution':
        st.header('Geographical Distribution')
        st.image('dashboard/map.png', caption='Geographical Distribution Rop Sellers Map', use_column_width=True)
        st.markdown('Berdasarkan peta folium di atas, dapat dilihat bahwa titik koordinat penjual cenderung tersebar merata ke wilayah Tenggara Brasil.')
        st.image('dashboard/map2.png', caption='Geographical Distribution Rop Customers Map', use_column_width=True)
        st.markdown('Berdasarkan peta folium di atas, dapat dilihat bahwa titik koordinat pelanggan cenderung tersebar merata di seluruh Wilayah Brasil.')
        st.image('dashboard/perkembanganwilayah.png', caption='Perkembangan Wilayah', use_column_width=True)
        st.markdown('Terlihat dari kedua plot di atas, dapat dilihat bahwa rata-rata harga terbesar berdasarkan negara bagian pelanggan adalah Paraiba dengan 215 Real Brazil, tetapi jumlah harga cenderung rendah dengan hanya 113.40K Real Brazil. Sebaliknya, proporsional terbalik dengan Sao Paulo di mana harga rata-ratanya terendah, tetapi memiliki jumlah harga terbesar dibandingkan dengan negara bagian lainnya, yaitu 5172.26K Real Brazil. Hal ini menunjukkan bahwa aktivitas transaksi online pembelian dan penjualan terbanyak terjadi di negara bagian ini.')
        


    elif selected_page == 'Transaksi dan Pembayaran':
        st.header('Transaksi dan Pembayaran')
        st.image('dashboard/jumlahtransaksi.png', caption='Transaksi dan Pembayaran', use_column_width=True)
        st.markdown('- Berdasarkan ketiga grafik di atas, terlihat bahwa kartu kredit adalah pilihan pembayaran yang paling disukai oleh pelanggan, mencapai 73.99% dari total. Perkembangan jenis pembayaran dengan kartu kredit juga meningkat pesat dari Januari 2017 hingga Mei 2018. Banyak pelanggan juga lebih memilih untuk membayar dengan cicilan selama 1 bulan. Hal ini menunjukkan bahwa dengan pembayaran menggunakan kartu kredit, pelanggan tidak perlu membayar sekaligus untuk produk yang mereka beli. Mereka dapat membayarnya dengan cicilan sesuai yang mereka inginkan dan dapat dilakukan pada akhir periode.')
        st.markdown('- Pembayaran cicilan terbanyak yang dipilih oleh pelanggan adalah 1. Ini menunjukkan bahwa banyak pelanggan membeli produk yang tidak terlalu mahal dan masih dapat dibayar pada akhir bulan pertama.')

    elif selected_page == 'Delivery Analysis':
        st.header('Delivery Analysis')
        st.image('dashboard/kinerjapengiriman.png', caption='Kinerja Pengiriman', use_column_width=True)
        st.markdown('- Nilai rata-rata biaya pengiriman adalah 22,77 Real Brazil. Namun, masih banyak provinsi yang harus membayar lebih dari R$40 untuk biaya pengiriman. Lima teratas adalah Paraiba, Roraima, Rondonia, Acre, dan Maranhao.')
        st.markdown('- Meskipun Provinsi Roraima juga berada di posisi kedua dari lima provinsi dengan waktu pengiriman rata-rata tertinggi, hal ini perlu didiskusikan lebih lanjut oleh tim Olist. Sehingga, nilai biaya pengiriman dapat disesuaikan dan setiap pelanggan mendapatkan layanan pengiriman terbaik dengan harga yang tepat.')
        

    elif selected_page == 'Sales Analysis':
        st.header('Sales Analysis')
        st.image('dashboard/totalpesanan.png', caption='Total Pesanan antara 2017 dan 2018', use_column_width=True)
        st.markdown('Berdasarkan plot perbandingan di atas, dapat dilihat bahwa terjadi peningkatan pesanan sebesar 136.52% antara bulan Januari hingga Agustus tahun 2017 dengan bulan Januari hingga Agustus tahun 2018. Hal ini mungkin terjadi karena banyak pelanggan baru yang melakukan transaksi di Olist pada tahun 2018. Oleh karena itu, kasus ini sebaiknya diselidiki lebih lanjut dalam pemodelan.')
        st.image('dashboard/totalpesananhari.png', caption='Total Pesanan Hari Waktu dan per Bulan', use_column_width=True)
        st.markdown('- Tidak ada catatan pada November 2016 dan catatan yang tidak lengkap pada September 2018. Jumlah pesanan tertinggi diterima dalam satu bulan adalah pada November 2017.')
        st.markdown('- Berdasarkan total pesanan per hari dalam seminggu, Senin dan Selasa adalah hari dengan transaksi paling banyak dalam seminggu dengan masing-masing 16,29% dan 16,04% dari total.')
        st.markdown('- Dalam total pesanan berdasarkan waktu dalam sehari, dapat dilihat bahwa sore adalah waktu dengan transaksi paling banyak dalam sehari dengan 38,29% dari total. Ini mungkin terjadi karena lebih banyak pelanggan memiliki waktu luang selama istirahat makan siang. Yang kedua paling banyak adalah selama malam saat pelanggan memiliki lebih banyak waktu luang setelah sehari penuh bekerja.')
        st.image('dashboard/totalcuy.png', caption='Total Analysis', use_column_width=True)
        st.markdown('Dari plot Perkembangan Pesanan E-Commerce di Wilayah Brasil, dapat dilihat bahwa Brasil dibagi menjadi 5 wilayah utama, di mana wilayah Sudeste adalah wilayah dengan perkembangan pesanan e-commerce yang paling cepat dari Januari 2017 hingga Agustus 2018. Sementara itu, Sao Paulo dan Rio de Janeiro dari wilayah Sudeste juga menempati peringkat 1 dan 2 untuk pesanan teratas di setiap negara bagian dan kota.')



    elif selected_page == 'Customer Segmentation':
        st.header('Customer Segmentation')
        st.image('dashboard/segment.png', caption='Customer Segment', use_column_width=True)
        st.markdown('Dari Grid Segmentasi Pelanggan di atas, terlihat bahwa Loyal Customer adalah segmen terkecil dibandingkan dengan segmen lainnya, sementara segmen terbesar adalah Gold dan Goners Customers. Olist harus merencanakan strategi tentang bagaimana menjaga Pelanggan Gold dan bagaimana membuat Pelanggan Goners untuk kembali dan berbelanja lagi di Olist.')
        st.markdown('Sementara itu, untuk Pelanggan Fresher, Olist harus merencanakan sesuatu seperti menyediakan promosi menarik bagi mereka agar tetap menggunakan layanan Olist dan dapat menjadi Pelanggan Gold.')


if __name__ == '__main__':
    main()
