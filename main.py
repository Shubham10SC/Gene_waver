from src.modules.evolution_ai import evolve
from src.modules.xna_core import XNAFirewall
import sys

def run_project():
    print("💎 GENE-WEAVER: MASTER DEPLOYMENT")
    print("64 Steps of Biological Engineering\n")
    
    fw = XNAFirewall()
    print("   [1] Firewall initialized.")
    encrypted = fw.encrypt_to_xna("SENSITIVE_GENOME")
    print(f"   [2] Payload Encrypted: {encrypted}")
    
    print("\nProject initialized. Ready for GitHub push.")

if __name__ == "__main__":
    run_project()
