import sys
from src.modules.xna_core import XNAFirewall
from src.modules.evolution_ai import simulate_evolutionary_escape
from src.utils.biocad import generate_plasmid_map
from src.utils.dossier import generate_lab_report

def main_menu():
    print("\n" + "="*50)
    print("🛰️  GENE-WEAVER: GLOBAL OPERATING TERMINAL")
    print("="*50)
    print("1. [SHIELD]  Run XNA Genetic Firewall")
    print("2. [EVOLVE]  Run Darwin-X Evolution Engine")
    print("3. [DESIGN]  Generate Bio-CAD Plasmid Map")
    print("4. [REPORT]  Generate Clinical Trial Dossier")
    print("5. [EXIT]    Terminate Session")
    print("="*50)

    choice = input("\nSELECT PROTOCOL: ")
    
    if choice == '1':
        fw = XNAFirewall()
        data = input("Enter data to encrypt: ")
        print(f"XNA ENCRYPTED: {fw.encrypt_to_xna(data)}")
    elif choice == '2':
        simulate_evolutionary_escape("AGAGGTTTGATAACCCTGTC", 500)
    elif choice == '3':
        generate_plasmid_map("AGAGGTTTGATAACCCTGTC")
    elif choice == '4':
        generate_lab_report({'id': 'SEQ_001'}, {'hour': 24})
    elif choice == '5':
        print("System Standby.")
        sys.exit()

if __name__ == "__main__":
    while True:
        main_menu()
