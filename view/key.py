import keyboard, time

def key(*listkey):
    """
    Menunggu dan mengembalikan nama tombol yang ditekan.

    Fungsi ini akan terus berjalan dalam loop tak terbatas sampai mendeteksi
    sebuah tombol ditekan (event `KEY_DOWN`). Setelah mendeteksi tombol ditekan,
    fungsi akan mengembalikan nama tombol tersebut.

    Returns:
        str: Nama tombol yang ditekan.

    Catatan:
        Fungsi ini menggunakan modul `keyboard` untuk membaca event keyboard.
        Pastikan modul `keyboard` sudah terinstal dan memiliki izin yang diperlukan
        untuk membaca input keyboard.
    """
    keyboard.unhook_all()
    while True:
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN and key.name in listkey:
            return key.name
