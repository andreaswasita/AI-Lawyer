---
template_id: surat-gugatan-cerai
version: "1.0"
language: id
---

# SURAT GUGATAN CERAI

**Perihal: Gugatan Perceraian**

Kepada Yth.
Ketua {{pengadilan_agama}}
di tempat

Assalamu'alaikum Wr. Wb.

Yang bertanda tangan di bawah ini:

**Nama** : {{nama_penggugat}}
**NIK** : {{nik_penggugat}}
**Tempat/Tgl Lahir** : {{tempat_lahir_penggugat}}, {{tanggal_lahir_penggugat}}
**Agama** : {{agama_penggugat}}
**Pekerjaan** : {{pekerjaan_penggugat}}
**Alamat** : {{alamat_penggugat}}

Selanjutnya disebut sebagai **PENGGUGAT**;

Dengan ini mengajukan Gugatan Cerai terhadap:

**Nama** : {{nama_tergugat}}
**NIK** : {{nik_tergugat}}
**Tempat/Tgl Lahir** : {{tempat_lahir_tergugat}}, {{tanggal_lahir_tergugat}}
**Agama** : {{agama_tergugat}}
**Pekerjaan** : {{pekerjaan_tergugat}}
**Alamat** : {{alamat_tergugat}}

Selanjutnya disebut sebagai **TERGUGAT**;

---

## POSITA (Alasan Gugatan)

1. Bahwa pada tanggal {{tanggal_nikah}}, Penggugat dan Tergugat telah melangsungkan pernikahan yang dicatat oleh Pegawai Pencatat Nikah {{tempat_nikah}}, sebagaimana ternyata dari Kutipan Akta Nikah Nomor: {{nomor_akta_nikah}};

2. Bahwa setelah pernikahan tersebut, Penggugat dan Tergugat bertempat tinggal di {{alamat_penggugat}};

{{#if jumlah_anak > 0}}
3. Bahwa dalam perkawinan tersebut Penggugat dan Tergugat telah dikaruniai {{jumlah_anak}} ({{jumlah_anak_terbilang}}) orang anak, yaitu:
{{data_anak}}
{{/if}}

4. Bahwa pada mulanya kehidupan rumah tangga Penggugat dan Tergugat berjalan rukun dan harmonis, namun sejak {{kronologi}};

5. Bahwa akibat permasalahan tersebut, antara Penggugat dan Tergugat terus menerus terjadi perselisihan dan pertengkaran dan tidak ada harapan akan hidup rukun lagi dalam rumah tangga;

{{#if pisah_sejak}}
6. Bahwa sejak tanggal {{pisah_sejak}}, antara Penggugat dan Tergugat telah berpisah tempat tinggal;
{{/if}}

7. Bahwa berdasarkan alasan-alasan tersebut di atas, gugatan perceraian Penggugat telah memenuhi ketentuan sebagaimana diatur dalam:
   - Pasal 39 ayat (2) Undang-Undang Nomor 1 Tahun 1974 tentang Perkawinan;
   - Pasal 19 Peraturan Pemerintah Nomor 9 Tahun 1975;
   - Pasal 116 Kompilasi Hukum Islam;

---

## PETITUM (Tuntutan)

Berdasarkan alasan-alasan tersebut di atas, Penggugat mohon kepada Ketua {{pengadilan_agama}} cq. Majelis Hakim yang memeriksa perkara ini berkenan menjatuhkan putusan sebagai berikut:

### PRIMER:

1. Mengabulkan gugatan Penggugat seluruhnya;
2. Menjatuhkan talak satu bain sughra Tergugat ({{nama_tergugat}}) terhadap Penggugat ({{nama_penggugat}});

{{#if tuntutan_hak_asuh}}
3. Menetapkan hak asuh anak (hadhanah) atas anak yang bernama {{data_anak}} kepada Penggugat selaku ibu kandungnya;
{{/if}}

{{#if tuntutan_nafkah}}
4. Menghukum Tergugat untuk membayar nafkah anak sebesar {{jumlah_nafkah}} ({{jumlah_nafkah_terbilang}}) setiap bulan sampai anak tersebut dewasa/mandiri;
{{/if}}

{{#if tuntutan_harta}}
5. Menetapkan harta bersama (gono-gini) sebagai berikut:
{{daftar_harta}}
   Dan membagi harta bersama tersebut masing-masing ½ (seperdua) bagian untuk Penggugat dan ½ (seperdua) bagian untuk Tergugat;
{{/if}}

6. Membebankan biaya perkara menurut hukum;

### SUBSIDAIR:

Apabila Majelis Hakim berpendapat lain, mohon putusan yang seadil-adilnya *(ex aequo et bono)*.

Wassalamu'alaikum Wr. Wb.

{{kota}}, {{tanggal_pengajuan}}

Hormat Penggugat,

&nbsp;

**{{nama_penggugat}}**

---

## Lampiran yang Diperlukan:
1. Fotokopi Kartu Tanda Penduduk (KTP) Penggugat
2. Fotokopi Kutipan Akta Nikah
3. Fotokopi Kartu Keluarga
4. Fotokopi Akta Kelahiran Anak (jika ada)
5. Surat Keterangan dari RT/RW/Kelurahan
6. Bukti-bukti pendukung lainnya (foto, rekaman, visum, dll)
