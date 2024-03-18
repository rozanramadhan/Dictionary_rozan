meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "WKWKWK": "suatu kata untuk mengekspresikan saat kita tertawa",
            "YTTA": "yang tau tau aja",
            "OMG": "sesutu yang mengekspresikan kaget disertai dengan singkatan oh my god",
            }
    
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("makna kata",word,"adalah",meme_dict[word])
else:
    print("ada kesalahan dari admin sehingga tidak dapat menemukan kata")
