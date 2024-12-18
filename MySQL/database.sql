-- Membuat Database tokokelontong;
CREATE DATABASE IF NOT EXISTS tokokelontong;

-- Use DB tokokelontong
USE tokokelontong;

-- Drop tabel jika ada
DROP TABLE IF EXISTS transaksisupplier;
DROP TABLE IF EXISTS detailtransaksi;
DROP TABLE IF EXISTS barang;
DROP TABLE IF EXISTS transaksi;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS kategori;


-- Membuat tabel Kategori
CREATE TABLE
    `tokokelontong`.`kategori` (
        `idkategori` INT NOT NULL AUTO_INCREMENT,
        `namaKategori` VARCHAR(25) NOT NULL,
        PRIMARY KEY (`idkategori`)
    );

-- Membuat tabel transaksi
CREATE TABLE
    `tokokelontong`.`transaksi` (
        `idtransaksi` INT NOT NULL AUTO_INCREMENT,
        `waktuTransaksi` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `totalBayar` DECIMAL(10, 2) NOT NULL,
        PRIMARY KEY (`idtransaksi`)
    );

-- Membuat tabel supplier
CREATE TABLE
    `tokokelontong`.`supplier` (
        `idSupplier` INT NOT NULL AUTO_INCREMENT,
        `namaSupplier` VARCHAR(255) NOT NULL,
        `alamat` VARCHAR(255) NULL,
        `noTelepon` VARCHAR(20) NOT NULL,
        `email` VARCHAR(255) NULL,
        PRIMARY KEY (`idSupplier`)
    );

-- Mebuat tabel barang
CREATE TABLE
    `tokokelontong`.`barang` (
        `idBarang` INT NOT NULL AUTO_INCREMENT,
        `idKategori` INT NULL,
        `idSupplier` INT NULL,
        `namaBarang` VARCHAR(255) NOT NULL,
        `hargaJual` DECIMAL(10, 2) NOT NULL,
        `hargaPack` DECIMAL(10, 2) NULL DEFAULT NULL,
        PRIMARY KEY (`idBarang`),
        INDEX `idKategori_idx` (`idKategori` ASC) VISIBLE,
        INDEX `idSupplier_idx` (`idSupplier` ASC) VISIBLE,
        CONSTRAINT `idKategori` FOREIGN KEY (`idKategori`) REFERENCES `tokokelontong`.`kategori` (`idkategori`) ON DELETE SET NULL ON UPDATE SET NULL,
        CONSTRAINT `idSupplier` FOREIGN KEY (`idSupplier`) REFERENCES `tokokelontong`.`supplier` (`idSupplier`) ON DELETE SET NULL ON UPDATE SET NULL
    );

-- Membuat tabel detailTransaksi
CREATE TABLE
    `tokokelontong`.`detailtransaksi` (
        `idDetailTransaksi` INT NOT NULL AUTO_INCREMENT,
        `idTransaksi` INT,
        `idBarang` INT,
        `banyakBarang` INT NOT NULL,
        PRIMARY KEY (`idDetailTransaksi`),
        INDEX `idTransaksi_idx` (`idTransaksi` ASC) VISIBLE,
        INDEX `idBarang_idx` (`idBarang` ASC) VISIBLE,
        CONSTRAINT `idTransaksi` FOREIGN KEY (`idTransaksi`) REFERENCES `tokokelontong`.`transaksi` (`idtransaksi`) ON DELETE SET NULL ON UPDATE SET NULL,
        CONSTRAINT `idBarang` FOREIGN KEY (`idBarang`) REFERENCES `tokokelontong`.`barang` (`idBarang`) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

-- Membuat tabel transaksisupplier
CREATE TABLE
    `tokokelontong`.`transaksisupplier` (
        `idTransaksiSupplier` INT NOT NULL AUTO_INCREMENT,
        `idBarang` INT NOT NULL,
        `hargaBeli` DECIMAL(10, 2) NOT NULL,
        `waktuTransaksi` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `kuantitas` INT NOT NULL,
        PRIMARY KEY (`idTransaksiSupplier`),
        INDEX `idBarang_idx` (`idBarang` ASC) VISIBLE,
        CONSTRAINT `idBarangDetail` FOREIGN KEY (`idBarang`) REFERENCES `tokokelontong`.`barang` (`idBarang`) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

-- Data contoh untuk tabel kategori
INSERT INTO `tokokelontong`.`kategori` (`namaKategori`) VALUES
('Makanan'),
('Minuman'),
('Alat Tulis'),
('Bumbu Dapur'),
('Peralatan Rumah Tangga'),
('Rokok');

-- Data contoh untuk tabel supplier
INSERT INTO `tokokelontong`.`supplier` (`namaSupplier`, `alamat`, `noTelepon`, `email`) VALUES
('PT. Sumber Rezeki', 'Jl. Sudirman No. 1', '081234567890', 'sumberrezeki@gmail.com'),
('CV. Cahaya Abadi', 'Jl. Thamrin No. 15', '081987654321', 'cahaya.abadi@mail.com'),
('Toko Maju Jaya', 'Jl. Ahmad Yani No. 20', '085612345678', NULL),
('UD. Makmur Sentosa', 'Jl. Kebon Jeruk No. 3', '081223344556', 'makmur.sentosa@mail.com'),
('PT. Indo Sukses', 'Jl. Pahlawan No. 50', '081998877665', 'info@indosukses.co.id'),
('CV. Global Abadi', 'Jl. Veteran No. 21', '085677889900', 'contact@globalabadi.co.id'),
('PT. Mitra Sejahtera', NULL, '082334455667', 'mitra.sejahtera@mail.com'),
('CV. Karya Bersama', 'Jl. Perintis No. 10', '083223344556', NULL);

-- Data contoh untuk tabel transaksi
INSERT INTO `tokokelontong`.`transaksi` (`waktuTransaksi`, `totalBayar`) VALUES
('2024-12-01 10:15:00', 75000.00),
('2024-12-01 12:30:00', 95000.00),
('2024-12-02 09:00:00', 60000.00);

-- Data contoh untuk tabel barang
INSERT INTO `tokokelontong`.`barang` (`idKategori`, `idSupplier`, `namaBarang`, `hargaJual`, `hargaPack`) VALUES
(1, 1, 'Biskuit Kaleng', 45000.00, 40000.00),
(2, 2, 'Air Mineral 1L', 3000.00, 2800.00),
(3, 3, 'Pulpen Biru', 2000.00, NULL),
(4, 1, 'Garam Dapur', 5000.00, NULL),
(5, 2, 'Sapu Lidi', 15000.00, NULL),
(6, 4, 'Rokok Djarum', 20000.00, NULL),
(6, 5, 'Rokok Gudang Garam', 21000.00, NULL),
(6, 6, 'Rokok Sampoerna', 22000.00, NULL),
(6, 4, 'Rokok Surya', 23000.00, NULL),
(1, 1, 'Kerupuk Udang', 12000.00, 11000.00),
(2, 2, 'Teh Botol', 6000.00, 5800.00),
(3, 3, 'Spidol Merah', 2500.00, NULL),
(3, 3, 'Pensil 2B', 1500.00, NULL),
(4, 1, 'Kecap Manis', 8000.00, 7500.00),
(4, 2, 'Saus Sambal', 7000.00, 6800.00),
(5, 3, 'Lap Piring', 5000.00, NULL),
(5, 4, 'Ember Plastik', 25000.00, NULL),
(1, 5, 'Snack Cokelat', 10000.00, 9500.00),
(2, 6, 'Susu Kotak', 12000.00, 11500.00),
(6, 7, 'Rokok Marlboro', 25000.00, NULL);

-- Data contoh untuk tabel detailTransaksi
INSERT INTO `tokokelontong`.`detailtransaksi` (`idTransaksi`, `idBarang`, `banyakBarang`) VALUES
(1, 1, 2),
(1, 2, 5),
(2, 3, 10),
(3, 4, 6);

-- Data contoh untuk tabel transaksisupplier
INSERT INTO `tokokelontong`.`transaksisupplier` (`idBarang`, `hargaBeli`, `waktuTransaksi`, `kuantitas`) VALUES
(1, 40000.00, '2024-12-01 08:00:00', 10),
(2, 2500.00, '2024-12-01 09:00:00', 20),
(3, 1800.00, '2024-12-02 07:00:00', 50),
(4, 4500.00, '2024-12-02 08:00:00', 15),
(5, 14000.00, '2024-12-03 10:00:00', 30),
(6, 18500.00, '2024-12-03 11:00:00', 25),
(7, 19000.00, '2024-12-03 12:00:00', 20),
(8, 20000.00, '2024-12-03 13:00:00', 15),
(9, 11500.00, '2024-12-04 08:00:00', 40),
(10, 2700.00, '2024-12-04 09:00:00', 60),
(11, 1700.00, '2024-12-05 07:00:00', 70),
(12, 4500.00, '2024-12-05 08:00:00', 35),
(13, 6500.00, '2024-12-05 10:00:00', 20),
(14, 6200.00, '2024-12-05 11:00:00', 15),
(15, 4900.00, '2024-12-06 08:00:00', 50),
(16, 23000.00, '2024-12-06 09:00:00', 10),
(17, 8900.00, '2024-12-06 10:00:00', 25),
(18, 11200.00, '2024-12-06 11:00:00', 30),
(19, 8700.00, '2024-12-07 08:00:00', 20),
(20, 15000.00, '2024-12-07 09:00:00', 40);
