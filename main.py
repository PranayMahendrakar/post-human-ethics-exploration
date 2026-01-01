#!/usr/bin/env python3
"""
Post-Human Ethics Exploration System
Author: Pranay M.

Framework that explores ethical frameworks for advanced technological
civilizations.
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
import json
import sys

console = Console()

BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║            🔮 POST-HUMAN ETHICS EXPLORATION SYSTEM 🔮                          ║
║                    Advanced Civilization Ethics Framework                      ║
║                           Author: Pranay M.                                    ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

MODULES = {
    "1": ("Enhanced Being Ethics", "enhanced", "Ethics for enhanced beings"),
    "2": ("Digital Consciousness Ethics", "digital", "Ethics for digital minds"),
    "3": ("Multi-Substrate Ethics", "substrate", "Ethics across substrates"),
    "4": ("Temporal Ethics Explorer", "temporal", "Ethics across time scales"),
    "5": ("Cosmic Ethics Framework", "cosmic", "Ethics at cosmic scale"),
    "6": ("Value Evolution Modeler", "value_evolution", "Model value evolution"),
    "7": ("Identity Ethics Analyzer", "identity", "Ethics of fluid identity"),
    "8": ("Collective Ethics Designer", "collective", "Ethics for collective minds"),
    "9": ("Existence Ethics Explorer", "existence", "Ethics of existence types"),
    "10": ("Ethics Dashboard", "dashboard", "View post-human ethics dashboard")
}

SYSTEM_PROMPTS = {
    "enhanced": """You are an expert in transhumanist ethics and enhancement philosophy.

For each enhanced being ethics exploration, examine:

1. **Enhancement Types**: Cognitive, physical, emotional, moral
2. **Enhancement Ethics**: Is enhancement permissible/obligatory?
3. **Distribution Justice**: Who gets enhanced?
4. **Identity Continuity**: Does enhancement change who we are?
5. **Social Implications**: Effects on unenhanced
6. **Limits Question**: Are there enhancements we shouldn't pursue?

Explore ethical frameworks for enhanced beings.""",

    "digital": """You are an expert in philosophy of mind and digital ethics.

For each digital consciousness ethics question, analyze:

1. **Moral Status**: Do digital minds have moral standing?
2. **Rights Framework**: What rights should they have?
3. **Suffering Capacity**: Can digital minds suffer?
4. **Creation Ethics**: Ethics of creating digital minds
5. **Termination Ethics**: Ethics of ending digital minds
6. **Simulation Ethics**: Obligations to simulated beings

Explore ethics for digital consciousness.""",

    "substrate": """You are an expert in substrate-independent ethics.

For each multi-substrate ethics question, examine:

1. **Substrate Neutrality**: Does substrate matter morally?
2. **Transfer Ethics**: Ethics of mind uploading/transfer
3. **Multiple Instantiation**: Ethics of copying minds
4. **Hybrid Beings**: Ethics of biological-digital hybrids
5. **Substrate Rights**: Rights regardless of medium
6. **Integration Ethics**: Ethics of substrate mixing

Explore ethics across different substrates of mind.""",

    "temporal": """You are an expert in long-term ethics and temporal philosophy.

For each temporal ethics exploration, analyze:

1. **Long-term Obligations**: Duties to distant future
2. **Intergenerational Justice**: Fairness across generations
3. **Deep Time Ethics**: Very long-term considerations
4. **Temporal Discounting**: Should we discount future?
5. **Reversibility Ethics**: Ethics of irreversible actions
6. **Legacy Obligations**: What do we owe the future?

Explore ethics across extended time scales.""",

    "cosmic": """You are an expert in cosmic ethics and existential philosophy.

For each cosmic ethics framework, develop:

1. **Universal Values**: Values that transcend Earth
2. **Cosmic Responsibilities**: Obligations at cosmic scale
3. **Extraterrestrial Ethics**: Ethics toward alien life
4. **Cosmic Resource Ethics**: Space resource use
5. **Existential Risk Ethics**: Preventing extinction
6. **Cosmic Meaning**: Ethics in vast universe

Explore ethics at cosmic scales.""",

    "value_evolution": """You are an expert in moral philosophy and value dynamics.

For each value evolution model, analyze:

1. **Value Change Mechanisms**: How values evolve
2. **Value Lock-in Risks**: Risks of fixed values
3. **Value Drift**: How to handle changing values
4. **Meta-level Values**: Values about values
5. **Reflective Equilibrium**: Stable value sets
6. **Future Values**: What values should we want to have?

Model how values might evolve in advanced civilizations.""",

    "identity": """You are an expert in personal identity and ethics.

For each identity ethics analysis, examine:

1. **Identity Continuity**: What makes you the same person?
2. **Fluid Identity**: Ethics when identity is malleable
3. **Merged Identities**: Ethics of mind merging
4. **Distributed Identity**: Ethics of distributed selves
5. **Identity Creation**: Ethics of creating new identities
6. **Identity Rights**: Rights related to identity

Explore ethics of fluid and malleable identity.""",

    "collective": """You are an expert in collective intelligence ethics.

For each collective ethics design, develop:

1. **Collective Moral Status**: Are collectives moral agents?
2. **Emergence Ethics**: Ethics of emergent collective minds
3. **Individual-Collective Balance**: Rights of parts vs whole
4. **Collective Decision Making**: How collectives choose
5. **Collective Responsibility**: Who's responsible?
6. **Hive Mind Ethics**: Ethics of merged consciousness

Design ethics for collective minds.""",

    "existence": """You are an expert in existential philosophy and ethics.

For each existence ethics exploration, examine:

1. **Creation Ethics**: When is creating beings ethical?
2. **Non-existence Comparison**: Is non-existence better/worse?
3. **Existence Types**: Different modes of being
4. **Termination Ethics**: When is ending existence ethical?
5. **Suffering and Existence**: Relationship to quality
6. **Existence Rights**: Rights to exist or not exist

Explore fundamental ethics of existence.""",

    "dashboard": """You are an expert in ethical theory synthesis.

For each dashboard, generate:

1. **Key Questions**: Active ethical questions
2. **Framework Status**: Ethical frameworks developed
3. **Open Problems**: Unresolved dilemmas
4. **Convergence Areas**: Where frameworks agree
5. **Divergence Areas**: Where frameworks conflict
6. **Research Priorities**: Where to focus

View post-human ethics exploration dashboard."""
}

def get_multiline_input(prompt_text):
    console.print(f"\n[cyan]{prompt_text}[/cyan]")
    console.print("[dim](Type 'END' on a new line when finished)[/dim]\n")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def query_llama(system_prompt, user_input):
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure Ollama is running."

def display_menu():
    console.print(BANNER, style="bold blue")
    table = Table(title="🔮 Post-Human Ethics Modules", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=8)
    table.add_column("Module", style="green", width=28)
    table.add_column("Description", style="white", width=42)
    for key, (name, _, desc) in MODULES.items():
        table.add_row(key, name, desc)
    table.add_row("0", "Exit", "Exit the application")
    console.print(table)

def run_module(module_key):
    name, key, desc = MODULES[module_key]
    console.print(Panel(f"🔮 {name}", style="bold green"))
    user_input = get_multiline_input(f"Describe your {name.lower()} request:")
    with console.status(f"[bold green]Processing {name}..."):
        response = query_llama(SYSTEM_PROMPTS[key], user_input)
    console.print(Panel(Markdown(response), title=f"🔮 {name} Results", border_style="green"))

def main():
    while True:
        display_menu()
        choice = Prompt.ask("\nSelect a module", choices=["0","1","2","3","4","5","6","7","8","9","10"])
        if choice == "0":
            console.print("\n[yellow]Thank you for using the Post-Human Ethics Exploration System![/yellow]")
            console.print("[dim]Author: Pranay M.[/dim]\n")
            break
        try:
            run_module(choice)
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled.[/yellow]")
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
