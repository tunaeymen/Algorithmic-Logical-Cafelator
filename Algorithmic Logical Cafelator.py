C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_RED = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE = "\033[34m"
C_MAGENTA = "\033[35m"
C_CYAN = "\033[36m"
C_WHITE = "\033[37m"

def show_welcome_screen():

    print(C_YELLOW + """
@@@@ @  @@@@@@@@@@@@            @       @@@@@@@@@@@@@@@@@
  @@@ @  @@@@@@@               @      @@@@@@@@@@@@@@@@@@@
     @@@    @@                       @   @@@@@@@@@@@@@@@@
      @ @@@                    @@@@        @@@@@@@@@@@@@@
        @@@                    @  @ @       @@@@@@@@@@@@@
                             @@@      @      @@@@@@@@@@@@
@@@          @              @@                 @@@@@@@@@@
@@@         @@@ @@@  @ @@@@@             @    @ @@@@@@@@@
@@  @@@         @@@@                           @@@@@@@@@@
@@ @@@                                          @@@@@@@@@
@  @@@                        @                 @ @@@@@@@
  @@@           @         @    @@                 @@@@@@@
 @@@@           @@              @@@  @@          @ @@@@@@
 @@@@  @        @@@              @@@               @@@@@@
@@@@@  @        @@@@@                    @        @ @@@@@
@@@@   @        @@   @@@        @@@@@@@  @          @@@@@
@@@@@             @     @   @    @@@@@@@             @@@@
@@@ @   @        @@ @@@@@@   @ @     @@@             @@@@
@@@ @   @       @@@@@ @@@@ @    @@    @@@ @          @@@@
@@@ @            @@@@@@@@@ @@@    @ @            @    @@@
@@@ @    @        @@@@@@@@@@@@@@@          @    @@@    @@
@@@@               @@@@@@@@@@@@@@@@                    @@
@@@@                 @@@@@@@@@@@@@@@@                    
@@           @         @@@@@@@@@@@@ @                    
@@           @               @@@   @@               @@@  
@@ @          @ @         @@@   @@@@@@@                  
@ @                   @@@@  @@@@@@@@@ @@@@            @@ 
@@          @@@  @ @@@@@@@ @@@@@@@@@@ @@@@@@ @@          
           @@@@  @@ @@@@@@@  @@@@@@   @@@@@@ @  @      @ 
@        @@@@@@@  @ @@@@@@@ @      @ @@@@@@ @@  @@@@@@   
         @@@@@ @  @ @@@@@@@  @@@@@@ @@@@@@@ @      @@ @  
""" + C_RESET)

    print(f"{C_BLUE}{C_BOLD}        [ALGORITHMIC LOGICAL CAFELATOR v1.0 ]        {C_RESET}\n")
    input(f"{C_WHITE}Kahveyi demlemeye başlamak için Enter'a basın...{C_RESET}")
    
    print(f"{C_CYAN}" + "=" * 65 + f"{C_RESET}")
    print(f"{C_MAGENTA}{C_BOLD}               MANHATTAN CAFE'NIN KAHVE LABORATUVARI          {C_RESET}")
    print(f"{C_CYAN}" + "=" * 65 + f"{C_RESET}")
    print(f"{C_RED}  [!] İşlemci Tipi    : 8-Bit Kafe ALU (Arithmetic Logic Unit){C_RESET}")
    print(f"{C_BLUE}  [+] Operasyon Seti  : Aritmetik, Mantıksal ve Demleme Komutları{C_RESET}")
    print(f"{C_GREEN}  [✓] Durum Bayrakları  : E (Empty), S (Spill), O (Overbrew), D (Debt){C_RESET}")
    print(f"{C_BLUE}  [i] Sürüm Durumu    : Demleniyor...{C_RESET}")
    print(f"{C_CYAN}" + "=" * 65 + f"{C_RESET}")
    
    input(f"\n{C_WHITE}Kafe menüsüne geçmek için Enter'a basın...{C_RESET}")

class ALU8Bit:
    def __init__(self):
        self.flags = {"E": 0, "D": 0, "S": 0, "O": 0}

    def execute(self, opcode, a, b):
        res = 0
        if opcode == 0:
            res = a + b
        elif opcode == 1:
            res = a - b
        elif opcode == 2:
            res = a & b
        elif opcode == 3:
            res = a | b
        elif opcode == 4:
            res = a ^ b
        elif opcode == 5:
            res = ~a & 0xFF
        elif opcode == 6:
            res = a << 1
        elif opcode == 7:
            res = a >> 1
            
        final_res = res & 0xFF
        
        self.flags["E"] = 1 if final_res == 0 else 0
        self.flags["D"] = 1 if res < 0 else 0
        self.flags["S"] = 1 if res > 255 or res < 0 else 0
        self.flags["O"] = 1 if (opcode == 0 and ((a ^ res) & (b ^ res) & 0x80)) or (opcode == 1 and ((a ^ b) & (a ^ res) & 0x80)) else 0
        
        return final_res

    def get_flags(self):
        return self.flags

def main():
    show_welcome_screen()
    
    alu = ALU8Bit()
    
    islem_isimleri = {
        "0": "ADD (Kahve Ekleme)",
        "1": "SUB (Kahve Eksiltme)",
        "2": "AND (Aroma Kesişimi)",
        "3": "OR (Harmanlama)",
        "4": "XOR (Özel Harman)",
        "5": "NOT (Ters Demleme)",
        "6": "SHL (Sola Süzme)",
        "7": "SHR (Sağa Süzme)"
    }

    while True:
        print(f"{C_CYAN}=" * 65 + f"{C_RESET}")
        print(f"{C_BLUE}{C_BOLD}           MANHATTAN CAFE - 8-BIT KAHVE KONTROL PANELİ        {C_RESET}")
        print(f"{C_CYAN}=" * 65 + f"{C_RESET}")
        
        print(f"{C_WHITE}Lütfen yapmak istediğiniz demleme işlemini seçin:{C_RESET}")
        for k, v in islem_isimleri.items():
            print(f"  {C_YELLOW}{k}{C_RESET} = {v}")
        print(f"  {C_RED}q{C_RESET} = Kafeden Ayrıl\n")
        
        secim = input(f"{C_CYAN}Seçiminiz: {C_RESET}").strip()
        
        if secim.lower() == 'q':
            print(f"\n{C_MAGENTA}Kahve dükkanı kapatılıyor... Görüşürüz. <3{C_RESET}")
            break
            
        if secim not in islem_isimleri:
            print(f"\n{C_RED}[!] Geçersiz Demleme Kodu! Devam etmek için Enter'a basın...{C_RESET}")
            input()
            continue

        try:
            print(f"{C_CYAN}-" * 65 + f"{C_RESET}")
            val_a = int(input(f"{C_YELLOW}A Kahve Dozunu Girin (0-255): {C_RESET}"))
            
            val_b = 0
            if secim in ["0", "1", "2", "3", "4"]:
                val_b = int(input(f"{C_YELLOW}B Kahve Dozunu Girin (0-255): {C_RESET}"))
            
            res = alu.execute(int(secim), val_a, val_b)
            flags = alu.get_flags()
            
            signed_res = res if res < 128 else res - 256
            
            print(f"\n{C_GREEN}[SONUÇ] İşlem: {islem_isimleri[secim]}{C_RESET}")
            print(f"{C_WHITE}Demleme Sonucu (Decimal): {res} | İşaretli (Signed): {signed_res}{C_RESET}")
            print(f"{C_WHITE}Hex: {hex(res)} | Binary: {bin(res)}{C_RESET}")
            print(f"{C_YELLOW}Bayraklar (Flags): E: {flags['E']} (Bardak Boşaldı!), S: {flags['S']} (Kahve Taştı!), D: {flags['D']} (Borçlu/Eksi Hesap), O: {flags['O']} (Aşırı demlendi){C_RESET}")
            
            print("\n" + f"{C_CYAN}=" * 65 + f"{C_RESET}")
            input(f"{C_WHITE}Yeni bir kahve demlemek için ENTER'a basın...{C_RESET}")
            
        except ValueError:
            print(f"\n{C_RED}[!] Hata: Lütfen sadece sayı girin! Devam etmek için Enter'a basın...{C_RESET}")
            input()

if __name__ == "__main__":
    main()