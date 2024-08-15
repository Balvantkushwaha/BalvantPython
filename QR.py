import qrcode
my_qr = qrcode.QRCode(
    version =1,
    box_size =10 ,
    border =5
  )
my_qr.add_data("https://www.youtube.com/channel/UC9FxWc-PcEOGT6GhIe_idIg ")
image = my_qr.make_image(
    fill_color ="green",
    black_color ="white",
)
image.save("ramkishan channel .png")