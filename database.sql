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

-- Menambahkan data contoh ke tabel kategori
INSERT INTO `tokokelontong`.`kategori` (`namaKategori`) VALUES
('Makanan'),
('Minuman'),
('Kebutuhan Rumah Tangga'),
('Elektronik'),
('Kosmetik'),
('Peralatan Tulis'),
('Mainan Anak');

-- Menambahkan data contoh ke tabel supplier
INSERT INTO `tokokelontong`.`supplier` (`namaSupplier`, `alamat`, `noTelepon`, `email`) VALUES
('Supplier A', 'Jl. Mawar No. 1', '81234567890', 'suppliera@email.com'),
('Supplier B', 'Jl. Melati No. 2', '81345678901', 'supplierb@email.com'),
('Supplier C', 'Jl. Anggrek No. 3', '81456789012', 'supplierc@email.com'),
('Supplier D', 'Jl. Sakura No. 4', '81567890123', 'supplierd@email.com'),
('Supplier E', 'Jl. Kenanga No. 5', '81678901234', 'suppliere@email.com');

-- Menambahkan data contoh ke tabel transaksi
INSERT INTO `tokokelontong`.`transaksi` (`waktuTransaksi`, `totalBayar`) VALUES
('2024-12-01 10:00:00', 72000.00),
('2024-12-02 15:30:00', 50000.00),
('2024-12-03 18:00:00', 40000.00),
('2024-12-04 12:45:00', 120000.00),
('2024-12-05 17:20:00', 75000.00);

-- Menambahkan data contoh ke tabel barang
INSERT INTO `tokokelontong`.`barang` (`idKategori`, `idSupplier`, `namaBarang`, `hargaJual`, `hargaPack`) VALUES
(1, 1, 'Beras', 12000.00, 60000.00),
(1, 2, 'Gula', 15000.00, 75000.00),
(2, 2, 'Air Mineral', 5000.00, 30000.00),
(3, 3, 'Sabun Cuci', 7000.00, 35000.00),
(4, 3, 'Lampu LED', 25000.00, 120000.00),
(5, 4, 'Lipstik', 30000.00, 150000.00),
(6, 4, 'Pulpen', 2000.00, 10000.00),
(7, 5, 'Mobil Mainan', 50000.00, 250000.00);

-- Menambahkan data contoh ke tabel detailTransaksi
INSERT INTO `tokokelontong`.`detailtransaksi` (`idTransaksi`, `idBarang`, `banyakBarang`) VALUES
(1, 1, 3),
(1, 2, 2),
(2, 3, 5),
(3, 4, 2),
(4, 5, 4),
(5, 6, 10);

-- Menambahkan data contoh ke tabel transaksisupplier
INSERT INTO `tokokelontong`.`transaksisupplier` (`idBarang`, `hargaBeli`, `waktuTransaksi`, `kuantitas`) VALUES
(1, 11000.00, '2024-11-28 08:00:00', 100),
(2, 14000.00, '2024-11-29 09:30:00', 50),
(3, 4500.00, '2024-11-30 11:15:00', 120),
(4, 6800.00, '2024-11-30 14:00:00', 200),
(5, 24000.00, '2024-12-01 16:45:00', 80),
(6, 29000.00, '2024-12-02 10:00:00', 60),
(7, 1800.00, '2024-12-03 09:45:00', 300);