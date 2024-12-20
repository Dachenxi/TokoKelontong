SELECT namabarang,
    banyakBarang
FROM detailtransaksi
INNER JOIN barang Using(idbarang)
WHERE idtransaksi = 1