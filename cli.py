import argparse
from engine.brain import MonFontsBrain
from engine.compiler import FontCompiler
import json

def main():
    parser = argparse.ArgumentParser(description="MonFonts Engine - Terminal Synthesis")
    parser.add_argument("--prompt", type=str, required=True, help="Description of the font")
    parser.add_argument("--output", type=str, default="./output", help="Output directory")
    
    args = parser.parse_args()
    
    print(f"[*] Initializing Brain with prompt: '{args.prompt}'")
    brain = MonFontsBrain()
    params = brain.conceptualize_font(args.prompt)
    
    print(f"[*] Parameters locked for: {params.font_name}")
    
    print("[*] Loading base topology and compiling binary...")
    compiler = FontCompiler(args.output)
    
    # Load the base skeleton mappings
    with open("data/topology.json", "r") as f:
        topology = json.load(f)
        
    output_file = compiler.compile(params, topology)
    print(f"[+] Synthesis complete! Font saved to: {output_file}")

if __name__ == "__main__":
    main()
